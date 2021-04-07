### 9.1.3　使用Google Geocoding API实现地理编码的管道

每个房产信息都有地区名称，因此我们想对其进行地理编码，也就是说找到它们对应的坐标（经度、纬度）。我们可以使用这些坐标将房产信息放到地图上，或是根据它们到某个位置的距离对搜索结果进行排序。开发这种功能需要复杂的数据库、文本匹配以及空间计算。而使用Google的Geocoding API，可以避免上面提到的几个问题。可以通过浏览器或 `curl` 打开下述URL以获取数据。

```python
$ curl "https://maps.googleapis.com/maps/api/geocode/json?sensor=false&ad
dress=london"
{
　 "results" : [
　　　　 ...
　　　　 "formatted_address" : "London, UK",
　　　　 "geometry" : {
　　　　　　...
　　　　　　"location" : {
　　　　　　　 "lat" : 51.5073509,
　　　　　　　 "lng" : -0.1277583
　　　　　　},
　　　　　　"location_type" : "APPROXIMATE",
　　　　　　...
　 ],
　 "status" : "OK"
}

```

我们可以看到一个JSON对象，当搜索"location"时，可以很快发现Google提供的是伦敦中心坐标。如果继续搜索，会发现同一文档中还包含其他位置。其中，第一个坐标位置是最相关的。因此，如果存在 `results[0].geometry.location` 的话，它就是我们所需要的信息。

Google的Geocoding API可以使用之前用过的技术（ `treq` ）进行访问。只需几行，就可以找出一个地址的坐标位置（查看 `pipeline` 目录的 `geo.py` 文件），其代码如下。

```python
@defer.inlineCallbacks
def geocode(self, address):
　 endpoint = 'http://web:9312/maps/api/geocode/json'
　 parms = [('address', address), ('sensor', 'false')]
　 response = yield treq.get(endpoint, params=parms)
　 content = yield response.json()
　 geo = content['results'][0]["geometry"]["location"]
　 defer.returnValue({"lat": geo["lat"], "lon": geo["lng"]})
```

该函数使用了一个和前面用过的URL相似的URL，不过在这里将其指向到一个假的实现，以使其执行速度更快，侵入性更小，可离线使用并且更加可预测。可以使用 `endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'` 来访问Google的服务器，不过需要记住的是Google对请求有严格的限制。 `address` 和 `sensor` 的值都通过 `treq` 的 `get()` 方法的 `params` 参数进行了自动URL编码。 `treq.get()` 方法返回了一个延迟操作，我们对其执行 `yield` 操作，以便在响应可用时恢复它。对 `response.json()` 的第二个 `yield` 操作，用于等待响应体加载完成并解析为Python对象。此时，我们可以得到第一个结果的位置信息，将其格式化为字典后，使用 `defer.returnValue()` 返回，该方法是从使用 `inlineCallbacks` 的方法返回值的最适当的方式。如果任何地方存在问题，该方法会抛出异常，并通过Scrapy报告给我们。

通过使用 `geocode()` ， `process_item()` 可以变为一行代码，如下所示。

```python
item["location"] = yield self.geocode(item["address"][0])
```

我们可以在 `ITEM_PIPELINES` 设置中添加并启用该管道，其优先级数值应当小于ES的优先级数值，以便ES获取坐标位置的值。

```python
ITEM_PIPELINES = {
　　...
　　'properties.pipelines.geo.GeoPipeline': 400,
```

我们启用调试数据，运行一个快速的爬虫。

```python
$ scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=90 -L DEBUG
...
{'address': [u'Greenwich, London'],
...
 'image_urls': [u'http://web:9312/images/i06.jpg'],
 'location': {'lat': 51.482577, 'lon': -0.007659},
 'price': [1030.0],
...

```

现在，可以看到Item中包含了 `location` 字段。太好了！不过当使用真实的Google API的URL临时运行它时，很快就会得到类似下面的异常。

```python
File "pipelines/geo.py" in geocode (content['status'], address))
Exception: Unexpected status="OVER_QUERY_LIMIT" for
address="*London"
```

这是我们在完整代码中放入的一个检查，用于确保Geocoding API的响应中 `status` 字段的值是 `OK` 。如果该值非真，则说明我们得到的返回数据不是期望的格式，无法被安全使用。在本例中，我们得到了 `OVER_QUERY_LIMIT` 状态，可以清楚地说明在什么地方发生了错误。这可能是我们在许多案例中都会面临的一个重要问题。由于Scrapy的引擎具备较高的性能，缓存和资源请求的限流成为了必须考虑的问题。

可以访问Geocoder API的文档来了解其限制：“免费用户API：每24小时允许2500个请求，每秒允许5个请求”。即使使用了Google Geocoding API的付费版本，仍然会有每秒10个请求的限流，这就意味着该讨论仍然是有意义的。

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 下面的实现看起来可能会比较复杂，但是它们必须在上下文中进行判断。而在典型的多线程环境中创建此类组件需要线程池和同步，这样就会产生更加复杂的代码。

下面是使用Twisted技术实现的一个简单而又足够好用的限流引擎。

```python
class Throttler(object):
　　def __init__(self, rate):
　　　　self.queue = []
　　　　self.looping_call = task.LoopingCall(self._allow_one)
　　　　self.looping_call.start(1. / float(rate))
　　def stop(self):
　　　　self.looping_call.stop()
　　def throttle(self):
　　　　d = defer.Deferred()
　　　　self.queue.append(d)
　　　　return d
　　def _allow_one(self):
　　　　if self.queue:
　　　　　　self.queue.pop(0).callback(None)
```

该代码中，延迟操作排队进入列表中，每次调用 `_allow_one()` 时依次触发它们； `_allow_one()` 检查队列是否为空，如果不是，则调用最旧的延迟操作的 `callback()` （先入先出，FIFO）。我们使用Twisted的 `task.LoopingCall()`  API周期性调用 `_allow_one()` 。使用 `Throttler` 非常简单。我们可以在管道的 `__init__` 中对其进行初始化，并在爬虫结束时对其进行清理。

```python
class GeoPipeline(object):
　　def __init__(self, stats):
　　　　self.throttler = Throttler(5) # 5 Requests per second
　　def close_spider(self, spider):
　　　　self.throttler.stop()
```

在使用想要限流的资源之前（在本例中为在 `process_item()` 中调用 `geocode()` ），需要对限流器的 `throttle()` 方法执行 `yield` 操作。

```python
yield self.throttler.throttle()
item["location"] = yield self.geocode(item["address"][0])
```

在第一个 `yield` 时，代码将会暂停，等待足够的时间过去之后再恢复。比如，某个时刻共有11个延迟操作在队列中，我们的速率限制是每秒5个请求，我们的代码将会在队列清空时恢复，大约为11/5=2.2秒。

使用 `Throttler` 后，我们不再会发生错误，但是爬虫速度会变得非常慢。通过观察发现，示例的房产信息中只有有限的几个不同位置。这是使用缓存的一个非常好的机会。我们可以使用一个简单的Python字典来实现缓存，不过这种情况下将会产生竞态条件，导致不正确的API调用。下面是一个没有该问题的缓存，此外还演示了一些Python和Twisted的有趣特性。

```python
class DeferredCache(object):
　　def __init__(self, key_not_found_callback):
　　　　self.records = {}
　　　　self.deferreds_waiting = {}
　　　　self.key_not_found_callback = key_not_found_callback
　　@defer.inlineCallbacks
　　def find(self, key):
　　　　rv = defer.Deferred()
　　　　if key in self.deferreds_waiting:
　　　　　　self.deferreds_waiting[key].append(rv)
　　　　else:
　　　　　　self.deferreds_waiting[key] = [rv]
　　　　　　if not key in self.records:
　　　　　　　　try:
　　　　　　　　　　value = yield self.key_not_found_callback(key)
　　　　　　　　　　self.records[key] = lambda d: d.callback(value)
　　　　　　　　except Exception as e:
　　　　　　　　　　self.records[key] = lambda d: d.errback(e)
　　　　　　action = self.records[key]
　　　　　　for d in self.deferreds_waiting.pop(key):
　　　　　　　　reactor.callFromThread(action, d)
　　　　value = yield rv
　　　　defer.returnValue(value)
```

该缓存看起来和人们通常期望的有些不同。它包含两个组成部分。

+ `self.deferreds_waiting` ：这是一个延迟操作的队列，等待指定键的值。
+ `self.records` ：这是已经出现的键-操作对的字典。

如果查看 `find()` 实现的中间部分，就会发现如果没有在 `self.records` 中找到一个键，则会调用一个预定义的 `callback` 函数，取得缺失值（ `yield self.key_not_found_callback(key)` ）。该回调函数可能会抛出一个异常。我们要如何在Python中以紧凑的方式存储这些值或异常呢？由于Python是一种函数式语言，我们可以根据是否出现异常，在 `self.records` 中存储调用延迟操作的 `callback` 或 `errback` 的小函数（ `lambda` ）。在定义时，该值或异常被附加到 `lambda` 函数中。函数中对变量的依赖被称为闭包，这是大多数函数式编程语言最显著和强大的特性之一。

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 缓存异常有些不太常见，不过这意味着如果在第一次查找某个键时， `key_not_found_callback(key)` 抛出了异常，那么接下来对相同键再次查询时仍然会抛出同样的异常，不需要再执行额外的调用。

`find()` 实现的剩余部分提供了避免竞态条件的机制。如果要查询的键已经在进程当中，将会在 `self.deferreds_waiting` 字典中有记录。在这种情况下，我们不再额外调用 `key_not_found_callback()` ，只是添加到延迟操作列表中，等待该键。当 `key_not_found_callback()` 返回，并且该键的值变为可用时，触发每个等待该键的延迟操作。我们可以直接执行 `action(d)` ，而不是使用 `reactor.callFromThread()` ，不过这样就必须处理所有抛出的异常，并且会创建一个不必要的长延迟链。

使用缓存非常简单。只需在 `__init__()` 中对其初始化，并在执行 `API` 调用时设置回调函数即可。在 `process_item()` 中，按照如下代码使用缓存。

```python
def __init__(self, stats):
　　self.cache = DeferredCache(self.cache_key_not_found_callback)
@defer.inlineCallbacks
def cache_key_not_found_callback(self, address):
　　yield self.throttler.enqueue()
　　value = yield self.geocode(address)
　　defer.returnValue(value)
@defer.inlineCallbacks
def process_item(self, item, spider):
　　item["location"] = yield self.cache.find(item["address"][0])
　　defer.returnValue(item)
```

本例的完整代码包含了更多的错误处理代码，能够对限流导致的错误重试调用（一个简单的 `while` 循环），并且还包含了更新爬虫状态的代码。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 本例的完整代码文件地址为： `ch09/properties/properties/pipelines/geo2.py` 。

要想启用该管道，需要禁用（注释掉）之前的实现，并且在 `settings.py` 文件的 `ITEM_PIPELINES` 中添加如下代码。

```python
ITEM_PIPELINES = {
　　'properties.pipelines.tidyup.TidyUp': 100,
　　'properties.pipelines.es.EsWriter': 800,
　　# DISABLE 'properties.pipelines.geo.GeoPipeline': 400,
　　'properties.pipelines.geo2.GeoPipeline': 400,
}
```

然后，可以按照如下代码运行该爬虫。

```python
$ scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=1000
...
Scraped... 15.8 items/s, avg latency: 1.74 s and avg time in pipelines: 
0.94 s
Scraped... 32.2 items/s, avg latency: 1.76 s and avg time in pipelines: 
0.97 s
Scraped... 25.6 items/s, avg latency: 0.76 s and avg time in pipelines: 
0.14 s
...
: Dumping Scrapy stats:...
　 'geo_pipeline/misses': 35,
　 'item_scraped_count': 1019,

```

可以看到，爬取延时最初由于填充缓存的原因非常高，但是很快就回到了之前的值。统计显示总共有35次未命中，这正是我们所用的示例数据集内不同位置的数量。显然，在本例中总共有1019 - 35 = 984次命中缓存。如果使用真实的Google API，并将每秒对API的请求数量稍微增加，比如通过将 `Throttler(5)` 改为 `Throttler(10)` ，把每秒请求数从5增加到10，就会在 `geo_pipeline/retries` 统计中得到重试的记录。如果发生任何错误，比如使用API无法找到一个位置，将会抛出异常，并且会在 `geo_pipeline/errors` 统计中被捕获到。如果某个位置的坐标已经被设置（后面的小节中看到），则会在 `geo_pipeline/already_set` 统计中显示。最后，当访问 `http://localhost:9200/ properties/ property/_search` ，查看房产信息的ES时，可以看到包含坐标位置值的条目，比如 `{..."location": {"lat": 51.5269736, "lon": -0.0667204}...}` ，这和我们所期望的一样（在运行之前清理集合，确保看到的不是旧值）。

