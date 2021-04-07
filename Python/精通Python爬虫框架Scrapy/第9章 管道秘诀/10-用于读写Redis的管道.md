### 9.3.1　用于读写Redis的管道

Google Geocoding API是按照IP进行限制的。我们可以利用多个IP（例如使用多台服务器）进行缓解，此时需要避免重复请求其他机器上已经完成地理编码的地址。这种情况也适用于之前运行中曾见到过的地址。我们不想浪费宝贵的限额。

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 请与API供应商沟通，确保在他们的策略下这种做法是可行的。比如，你可能必须每隔几分钟/小时就要丢弃掉缓存记录，或者根本不允许缓存。

我们可以使用Redis的键值对缓存，从本质上说，它是一个分布式的字典。我们已经在vagrant环境中运行了一个Redis实例，可以使用 `redis-cli` 命令，从开发机连接它并执行基本操作。

```python
$ redis-cli -h redis
redis:6379> info keyspace
# Keyspace
redis:6379> set key value
OK
redis:6379> info keyspace
# Keyspace
db0:keys=1,expires=0,avg_ttl=0
redis:6379> FLUSHALL
OK
redis:6379> info keyspace
# Keyspace
redis:6379> exit

```

通过Google搜索"Redis Twisted"，我们找到了 `txredisapi` 库。其本质区别是它不再是同步Python库的包装，而是适用于Twisted的库，它使用 `reactor.connectTCP()` 连接Redis、实现Twisted协议等。使用该库的方式与其他库类似，不过在Twisted应用中使用它时，其效率肯定会更高一些。我们在安装它时可以再附带一个工具库—— `dj_redis_url` ，该工具库用于解析Redis配置URL，我们可以使用 `pip` 进行安装（ `sudo pip install txredisapi dj_redis_url` ），和往常一样，在我们的开发机中也已经预先安装好了这些库。

可以按如下代码初始化 `RedisCache` 。

```python
from txredisapi import lazyConnectionPool
class RedisCache(object):
...
　　def __init__(self, crawler, redis_url, redis_nm):
　　　　self.redis_url = redis_url
　　　　self.redis_nm = redis_nm
　　　　args = RedisCache.parse_redis_url(redis_url)
　　　　self.connection = lazyConnectionPool(connectTimeout=5,
　　　　　　　　　　　　　　　　　　　　　　 replyTimeout=5,
　　　　　　　　　　　　　　　　　　　　　　 **args)
　　　　crawler.signals.connect(
　　　　　　　　self.item_scraped,signal=signals.item_scraped)
```

该管道非常简单。为了连接Redis服务器，我们需要主机地址、端口等参数，由于这些参数是以URL格式存储的，因此需要使用 `parse_redis_url()` 方法解析该格式（为简洁起见已经省略）。为键设置前缀作为命名空间的行为非常常见，在本例中，我们将其存储在 `redis_nm` 中。然后，使用 `txredisapi` 的 `lazyConnectionPool()` ，打开到服务器的连接。

最后一行使用了一个很有意思的函数。我们的目的是将地理编码管道与该管道包装起来。如果在Redis中没有某个值，我们将不会设置该值，我们的地理编码管道将像之前那样使用API对地址进行地理编码。在该操作完成之后，需要有一种方式在Redis中缓存这些键值对，在这里是通过连接到 `signals.item_scraped` 信号的方式实现的。我们定义的回调（ `item_scraped()` 方法，将很快看到）在非常靠后的位置被调用，此时坐标位置将会被设置。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 本示例的完整代码位于  `ch09/properties/properties/pipelines/redis.py` 。

我们通过查找和记录每个 `Item` 的地址和位置，保持了缓存的简单性。这对Redis来说是很有意义的，因为它经常运行在同一个服务器当中，这使得它运行速度非常快。如果不是这种情况，那么可能需要添加一个基于字典的缓存，与我们在地理编码管道中的实现类似。下面是处理传入的Item的方法。

```python
@defer.inlineCallbacks
def process_item(self, item, spider):
　　address = item["address"][0]
　　key = self.redis_nm + ":" + address
　　value = yield self.connection.get(key)
　　if value:
　　　　item["location"] = json.loads(value)
　　defer.returnValue(item)
```

和大家的期望相同。我们得到了地址，为其添加前缀，然后使用 `txredisapi connection` 的 `get()` 方法在Redis中查询。我们在Redis中存储的值是JSON编码的对象。如果值已经设定，则使用JSON对其进行解码，并将其设为坐标位置。

当一个 `Item` 到达所有管道的结尾时，我们重新捕获它，确保存储到Redis的位置值当中。下面是实现代码。

```python
from txredisapi import ConnectionError
def item_scraped(self, item, spider):
　　try:
　　　　location = item["location"]
　　　　value = json.dumps(location, ensure_ascii=False)
　　except KeyError:
　　　　return
　　address = item["address"][0]
　　key = self.redis_nm + ":" + address
　　quiet = lambda failure: failure.trap(ConnectionError)
　　return self.connection.set(key, value).addErrback(quiet)
```

这里同样没有什么惊喜。如果我们找到一个位置，就可以得到地址，为其添加前缀，并使用它们作为键值对，用于 `txredisapi` 连接的 `set()` 方法。你会发现该函数没有使用 `@defer.inlineCallbacks` ，这是因为在处理 `signals.item_scraped` 时并不支持该装饰器。这就意味着无法再对 `connection.set()` 使用非常便捷的 `yield` 操作，不过我们可以做的工作是返回延迟操作，Scrapy可以用它串联任何未来的信号进行监听。无论何种情况，如果到Redis的连接无法执行 `connection.set()` ，就会抛出一个异常。可以通过添加自定义错误处理到 `connection.set()` 返回的延迟操作中，静默忽略该异常。在该错误处理中，我们将失败作为参数传递，并告知它们对任何 `ConnectionError` 执行 `trap()` 操作。这是Twisted的延迟操作API的一个非常好用的功能。通过在预期的异常中使用 `trap()` ，我们能够以紧凑的方式静默忽略它们。

为了启用该管道，我们所需做的就是将其添加到 `ITEM_PIPELINES` 设置中，并在 `settings.py` 文件中提供一个 `REDIS_PIPELINE_URL` 。为该管道设置一个比地理编码管道更小的优先级值非常重要，否则其运行就会太迟，无法起到作用。

```python
ITEM_PIPELINES = { ...
　　'properties.pipelines.redis.RedisCache': 300,
　　'properties.pipelines.geo.GeoPipeline': 400,
...
REDIS_PIPELINE_URL = 'redis://redis:6379'
```

我们可以像平时那样运行该爬虫。第一次运行将会和之前类似，不过接下来的每次运行都会像下面这样。

```python
$ scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=100
...
INFO: Enabled item pipelines: TidyUp, RedisCache, GeoPipeline, 
MysqlWriter, EsWriter
...
Scraped... 0.0 items/s, avg latency: 0.00 s, time in pipelines: 0.00 s
Scraped... 21.2 items/s, avg latency: 0.78 s, time in pipelines: 0.15 s
Scraped... 24.2 items/s, avg latency: 0.82 s, time in pipelines: 0.16 s
...
INFO: Dumping Scrapy stats: {...
　 'geo_pipeline/already_set': 106,
　 'item_scraped_count': 106,

```

可以看到 `GeoPipeline` 和 `RedisCache` 都已经启用，并且RedisCache会首先进行。另外，还可以注意到 `geo_pipeline/already_set` 统计值是106。这些是GeoPipeline从Redis缓存中找到的预先填充好的item，并且它们都不需要请求Google API调用。如果Redis缓存为空，你会看到一些键依然会使用Google API进行处理。在性能方面，我们注意到GeoPipeline引发的初始行为现在没有了。实际上，由于目前使用了缓存，因此绕过了每秒5个请求的API限制。当使用Redis时，还应当考虑使用过期键，使系统可以周期性地刷新缓存数据。

