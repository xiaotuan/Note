### 11.4.3　从设置中获取初始URL

当你注意到爬虫中间件提供的用于处理爬虫给我们的 `start_requests` 的 `process_start_requests()` 方法时，就会感受到爬虫中间件是怎样满足我们的需求的。我们检测 `DISTRIBUTED_START_URLS` 设置是否已被设定，如果是的话，则解码JSON并使用其中的URL对相关的 `Request` 进行 `yield` 操作。对于这些请求，我们设置 `CrawlSpider` 的 `_response_download()` 方法作为回调，并设置 `meta['rule']` 参数，以便其 `Response` 能够被适当的 `Rule` 处理。坦白来说，我们查阅了Scrapy的源代码，发现 `CrawlSpider` 创建 `Request` 的方式使用了相同的方法。在本例中，代码如下所示。

```python
def __init__(self, crawler):
　　...
　　self._start_urls = settings.get('DISTRIBUTED_START_URLS', None)
　　self.is_worker = self._start_urls is not None
def process_start_requests(self, start_requests, spider):
　　if not self.is_worker:
　　　　for x in start_requests:
　　　　　　yield x
　　else:
　　　　for url in json.loads(self._start_urls):
　　　　　　yield Request(url, spider._response_downloaded,
　　　　　　　　　　　　　meta={'rule': self._target})
```

我们的中间件已经准备好了。可以在 `settings.py` 中启用它并进行设置。

```python
SPIDER_MIDDLEWARES = {
　　'properties.middlewares.Distributed': 100,
}
DISTRIBUTED_TARGET_RULE = 1
DISTRIBUTED_BATCH_SIZE = 2000
DISTRIBUTED_TARGET_FEED_URL = ("ftp://anonymous@spark/"
　　　　　　　　　　　　　　　 "%(batch)s_%(name)s_%(time)s.jl")
DISTRIBUTED_TARGET_HOSTS = [
　　"scrapyd1:6800",
　　"scrapyd2:6800",
　　"scrapyd3:6800",
]
```

一些人可能会认为 `DISTRIBUTED_TARGET_RULE` 不应该作为设置，因为不同爬虫之间可能是不一样的。你可以将其认为是默认值，并且可以在爬虫中使用 `custom_settings` 属性进行覆写，比如：

```python
custom_settings = {
　　'DISTRIBUTED_TARGET_RULE': 3
}
```

不过在我们的例子中并不需要这么做。我们可以做一个测试运行，爬取作为设置提供的单个页面。

```python
$ scrapy crawl distr -s \
DISTRIBUTED_START_URLS='["http://web:9312/properties/property_000000.html"]'

```

当爬取成功后，可以尝试更进一步，爬取页面后使用FTP传输给Spark服务器。

```python
scrapy crawl distr -s \
DISTRIBUTED_START_URLS='["http://web:9312/properties/property_000000. html"]' \
-s FEED_URI='ftp://anonymous@spark/%(batch)s_%(name)s_%(time)s.jl' -a batch=12

```

如果你通过ssh登录到Spark服务器中（稍后会有更多介绍），将会看到一个文件位于 `/root/items` 目录中，比如 `12_distr_date_time.jl` 。

上述是使用Scrapyd实现分布式爬取的中间件的示例实现。你可以使用它作为起点，实现满足自己特殊需求的版本。你可能需要适配的事情包括如下内容。

+ 支持的爬虫类型。比如，一个不局限于 `CrawlSpider` 的替代方案可能需要你的爬虫通过适当的 `meta` 以及采用回调命名约定的方式来标记分布式请求。
+ 向Scrapyd传输URL的方式。你可能希望使用特定域名信息来减少传输的信息量。比如，在本例中，我们只传输了房产的ID。
+ 你可以使用更优雅的分布式队列解决方案，使爬虫能够从失败中恢复，并允许Scrapyd将更多的URL提交到批处理。
+ 你可以动态填充目标服务器列表，以支持按需扩展。

