### 10.2　使用telnet获得组件利用率

想要理解 `Request/Item` 流是如何通过管道的，我们不会真得去测量流量（尽管这可能会是一个很棒的功能），而是使用更容易的方式测量Scrapy的每个处理阶段中存在多少流体，即 `Request/Response/Item` 。

我们可以通过Scrapy运行的Telnet服务获取性能信息。首先，通过使用telnet命令连接到 `6023` 端口。然后，将会在Scrapy中得到一个Python提示符。需要小心的是，如果你在这里执行了某些阻塞操作，例如 `time.sleep()` ，它将会中止爬虫功能。内置的 `est()` 函数可以打印出一些感兴趣的度量。其中一些或者很专用，或者能够从几个核心度量推断出来。在本章剩余部分只会展示后者。让我们从一个示例运行中了解它们。当运行爬虫时，可以在开发机中打开第二个终端，通过telnet命令连接 `6023` 端口，并运行 `est()` 。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 本章代码位于 `ch10` 目录，其中本例位于 `ch10/speed` 目录。

在第一个终端中，运行如下代码。

```python
$ pwd
/root/book/ch10/speed
$ ls
scrapy.cfg speed
$ scrapy crawl speed -s SPEED_PIPELINE_ASYNC_DELAY=1
INFO: Scrapy 1.0.3 started (bot: speed)

```

现在先不用管 `scrapy crawl speed` 是什么，以及其参数表示什么。本章后续部分会详细解释这些。现在，在第二个终端上，运行如下命令：

```python
$ telnet localhost 6023
>>> est()
...
len(engine.downloader.active)　　　 : 16
...
len(engine.slot.scheduler.mqs)　　　: 4475
...
len(engine.scraper.slot.active)　　 : 115
engine.scraper.slot.active_size　　 : 117760
engine.scraper.slot.itemproc_size　 : 105

```

然后在第二个终端按下Ctrl + D退出Telnet，回到第一个终端，按下Ctrl + C停止爬虫。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 我们在这里忽略了 `dqs` 。如果通过 `JOBDIR` 设置启用了持久化支持的话，还会得到非零的 `dqs` （ `len(engine.slot.scheduler.dqs)` ），你需要将其添加到 `mqs` 的大小中，以继续后续分析。

我们来看一下本例中的这些核心度量都表示什么。 `mqs` 表示目前在调度器中还有很多等待（4475个请求）。还可以。 `len(engine.downloader.active)` 表示目前有16个请求正在下载器中被下载。这和我们在爬虫 `CONCURRENT_REQUESTS` 设置中设定的值相同，所以此处非常好。 `len(engine.scraper.slot.active)` 告知我们正在进行抓取处理的响应有115个。通过 `(engine.scraper.slot.active_size)` ，我们知道这些响应大小总计为115kb。在这些响应中，有 105 个Item此时正在通过管道处理，可以从 `(engine.scraper.slot.itemproc_size)` 看出来，这就意味着剩余的10个请求目前正在爬虫中处理。总体来说，我们可以看出瓶颈似乎在下载器中，在其之前的工作队列（ `mqs` ）非常庞大，但下载器已经满负荷利用了；而在其之后，我们有着数量很高但又比较稳定的任务（可以通过多次执行 `est()` 来确认此项）。

我们感兴趣的另一个信息元是 `stats` 对象，即通常在爬取完成后打印的信息。我们可以在Telnet中，通过 `stats.get_stats()` ，以字典的形式在任何时间访问它，并且可以通过 `p()` 函数打印更优雅的格式。

```python
$ p(stats.get_stats())
{'downloader/request_bytes': 558330,
...
 'item_scraped_count': 2485,
...}

```

对我们来说，目前最感兴趣的度量是 `item_scraped_count` ，它可以通过 `stats.get_value('item_scraped_count')` 直接访问。该度量告知我们到目前为止有多少 `item` 已经被抓取，它应当以系统吞吐量（ `Item` /秒）的速率增长。

