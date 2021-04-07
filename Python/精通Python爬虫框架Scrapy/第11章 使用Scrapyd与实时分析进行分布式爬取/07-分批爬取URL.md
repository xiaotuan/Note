### 11.4.2　分批爬取URL

现在，我们准备开发处理详情页URL的基础架构，目的是对其进行垂直爬取、分批并分发到多台Scrapyd节点中，而不是在本地爬取。

如果查看第8章中的Scrapy架构，就可以很容易地得出结论，这是爬虫中间件的任务，因为它实现了 `process_spider_output()` ，在到达下载器之前，在此处处理请求，并能够中止它们。我们在实现中限制只支持基于 `CrawlSpider` 的爬虫，另外还只支持简单的GET请求。如果需要更加复杂，比如POST或有权限验证的请求，那么需要开发更复杂的功能来扩展参数、请求头，甚至可能在每次批量运行后重新登录。

在开始之前，先来快速浏览一下Scrapy的GitHub。我们将回顾 `SPIDER_MIDDLEWARES_BASE` 设置，以查看Scrapy提供的参考实现，以便尽最大可能复用它。Scrapy 1.0包含如下爬虫中间件： `HttpErrorMiddleware` 、 `OffsiteMiddleware` 、 `RefererMiddleware` 、 `UrlLengthMiddleware` 以及 `DepthMiddleware` 。在快速了解它们的实现之后，我们发现 `OffsiteMiddleware` （只有60行代码）与想要实现的功能很相似。它根据爬虫的 `allowed_domains` 属性，把URL限制在某些特定域名中。我们可以使用相似的模式吗？和 `OffsiteMiddleware` 实现中丢弃URL不同，我们将对这些URL进行分批并发送到Scrapyd节点中。事实证明这是可以的。下面是实现的部分代码。

```python
def __init__(self, crawler):
　　settings = crawler.settings
　　self._target = settings.getint('DISTRIBUTED_TARGET_RULE', -1)
　　self._seen = set()
　　self._urls = []
　　self._batch_size = settings.getint('DISTRIBUTED_BATCH_SIZE', 1000)
　　...
def process_spider_output(self, response, result, spider):
　　for x in result:
　　　　if not isinstance(x, Request):
　　　　　　yield x
　　　　else:
　　　　　　rule = x.meta.get('rule')
　　　　　　if rule == self._target:
　　　　　　　　self._add_to_batch(spider, x)
　　　　　　else:
　　　　　　　　yield x
def _add_to_batch(self, spider, request):
　　url = request.url
　　if not url in self._seen:
　　　　self._seen.add(url)
　　　　self._urls.append(url)
　　　　if len(self._urls) >= self._batch_size:
　　　　　　self._flush_urls(spider)
```

`process_spider_output()` 既处理 `Item` 也处理 `Request` 。我们只想处理 `Request` ，因此我们对其他所有内容执行 `yield` 操作。如果查看 `CrawlSpider` 的源代码，就会注意到将 `Request / Response` 映射到 `Rule` 的方式是通过其 `meta` 字典的名为 `'rule'` 的整型字段。我们检查该数值，如果它指向目标的 `Rule（DISTRIBUTED_TARGET_RULE` 设置），则会调用 `_add_to_batch()` 添加URL到当前批次。然后，丢弃该 `Request` 。对其他所有 `Request` 执行 `yield` 操作，比如下一页链接、无变化的链接。 `_add_to_batch()` 方法实现了一个去重机制。不过很遗憾的是，由于前一节中描述的分片流程，我们可能对少数URL抽取两次。我们使用 `_seen` 集合检测并丢弃重复值。然后，把这些URL添加到 `_urls` 列表中，如果其大小超过 `_batch_size` （ `DISTRIBUTED_BATCH_SIZE` 设置），就会触发调用 `_flush_urls()` 。该方法提供了如下的关键功能。

```python
def __init__(self, crawler):
　　...
　　self._targets = settings.get("DISTRIBUTED_TARGET_HOSTS")
　　self._batch = 1
　　self._project = settings.get('BOT_NAME')
　　self._feed_uri = settings.get('DISTRIBUTED_TARGET_FEED_URL', None)
　　self._scrapyd_submits_to_wait = []
def _flush_urls(self, spider):
　　if not self._urls:
　　　　return
　　target = self._targets[(self._batch-1) % len(self._targets)]
　　data = [
　　　　 ("project", self._project),
　　　　 ("spider", spider.name),
　　　　 ("setting", "FEED_URI=%s" % self._feed_uri),
　　　　 ("batch", str(self._batch)),
　　]
　　json_urls = json.dumps(self._urls)
　　data.append(("setting", "DISTRIBUTED_START_URLS=%s" % json_urls))
　　d = treq.post("http://%s/schedule.json" % target,
　　　　　　　　　data=data, timeout=5, persistent=False)
　　self._scrapyd_submits_to_wait.append(d)
　　self._urls = []
　　self._batch += 1
```

首先，它使用一个批次计数器（ `_batch` ）来决定要将该批次发送到哪个Scrapyd服务器中。我们在 `_targets` （ `DISTRIBUTED_TARGET_HOSTS` 设置）中保持更新可用的服务器。然后，构造POST请求到Scrapyd的 `schedule.json` 。这比之前通过 `curl` 执行的更加高级，因为它传递了一些精心挑选的参数。基于这些参数，Scrapyd可以有效地计划运行任务，类似如下所示。

```python
scrapy crawl distr \
-s DISTRIBUTED_START_URLS='[".../property_000000.html", ... ]' \
-s FEED_URI='ftp://anonymous@spark/%(batch)s_%(name)s_%(time)s.jl' \
-a batch=1
```

除了项目和爬虫名外，我们还向爬虫传递了一个FEED_URI设置。我们可以从DISTRIBUTED_TARGET_FEED_URL设置中获取该值。

由于Scrapy支持FTP，我们可以让Scrapyd通过匿名FTP的方式将爬取到的 `Item` 文件上传到Spark服务器中。格式包含爬虫名（ `%(name)s` ）和时间（ `%(time)s` ）。如果只使用这些，那么当两个文件的创建时间相同时，最终会产生冲突。为了避免意外覆盖，我们还添加了一个 `%(batch)s` 参数。默认情况下，Scrapy不知道任何关于批次的事情，因此我们需要找到一种方式来设置该值。Scrapyd中 `schedule.json` 这个API的一个有趣特性是，如果参数不是设置或少数几个已知参数的话，它将会被作为参数传给爬虫。默认情况下，爬虫参数将会成为爬虫属性，未知的 `FEED_URI` 参数将会去查阅爬虫的属性。因此，通过传递 `batch` 参数给 `schedule.json` ，我们可以在 `FEED_URI` 中使用它以避免冲突。

最后一步是使用编码为JSON的该批次详情页URL编译为 `DISTRIBUTED_ START_URLS` 设置。除了熟悉和简单之外，使用该格式并没有什么特殊的理由。任何文本格式都可以做到。

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 通过命令行向Scrapy传输大量数据丝毫也不优雅。在一些时候，你想要将参数存储到数据存储中（比如Redis），并且只向Scrapy传输ID。如果想要这样做，则需要在 `_flush_urls()` 和 `process_start_requests()` 中做一些小的改变。

我们使用 `treq.post()` 处理POST请求。Scrapyd对持久化连接处理得不是很好，因此使用 `persistent=False` 禁用该功能。为了安全起见，我们还设置了一个5秒的超时时间。有趣的是，我们为该请求在 `_scrapyd_submits_to_wait` 列表中存储了延迟函数，后续内容中将会进行讲解。关闭该函数时，我们将重置 `_urls` 列表，并增加当前的 `_batch` 值。

出人意料的是，我们在关闭操作处理器中发现了如下所示的诸多功能。

```python
def __init__(self, crawler):
　　...
　　crawler.signals.connect(self._closed, signal=signals.spider_
closed)
@defer.inlineCallbacks
def _closed(self, spider, reason, signal, sender):
　　# Submit any remaining URLs
　　self._flush_urls(spider)
　　yield defer.DeferredList(self._scrapyd_submits_to_wait)
```

`_close()` 将会在我们按下Ctrl + C或爬取完成时被调用。无论哪种情况，我们都不希望丢失属于最后一个批次的任何URL，因为它们还没有被发送出去。这就是为什么我们在 `_close()` 方法中首先要做的是调用 `_flush_urls(spider)` 清空最后的批次的原因。第二个问题是，作为非阻塞代码，任何 `treq.post()` 在停止爬取时都可能完成或没有完成。为了避免丢失任何批次，我们将使用之前提及的 `scrapyd_submits_to_wait` 列表，来包含所有的 `treq.post()` 的延迟函数。我们使用 `defer.DeferredList()` 进行等待，直到全部完成。由于 `_close()` 使用了 `@defer.inlineCallbacks` ，我们只需对其执行 `yield` 操作，并在所有请求完成之后进行恢复即可。

总结来说，在 `DISTRIBUTED_START_URLS` 设置中包含批量URL的任务将被送往Scrapyd服务器，并在这些Scrapyd服务器中运行相同的爬虫。很明显，我们需要某种方式以使用该设置初始化 `start_urls` 。

