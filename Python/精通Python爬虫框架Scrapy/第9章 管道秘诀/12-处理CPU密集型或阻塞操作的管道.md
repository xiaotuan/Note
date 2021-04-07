### 9.4.1　处理CPU密集型或阻塞操作的管道

第8章讲到，reactor对于简短、非阻塞的任务非常理想。如果必须要执行一些更复杂或是涉及阻塞的事情，该怎么做呢？Twisted提供了线程池，可以使用 `reactor.callInThread()`  API调用，在一些线程中执行慢操作，而不是在主线程中执行（Twisted的reactor）。这就意味着reactor会持续运行其处理过程，并在计算发生时响应事件。请注意，在线程池中的处理不是线程安全的。这就是说当你使用全局状态时，又会出现多线程编程中所有的传统同步问题。让我们从该管道的一个简单版本起步，逐渐编写出完整的代码。

```python
class UsingBlocking(object):
　　@defer.inlineCallbacks
　　def process_item(self, item, spider):
　　　　price = item["price"][0]
　　　　out = defer.Deferred()
　　　　reactor.callInThread(self._do_calculation, price, out)
　　　　item["price"][0] = yield out
　　　　defer.returnValue(item)
　　def _do_calculation(self, price, out):
　　　　new_price = price + 1
　　　　time.sleep(0.10)
　　　　reactor.callFromThread(out.callback, new_price)
```

在前面的管道中，我们看到了实际运行的基本原语。对于每个 `Item` ，我们抽取其价格，并希望使用 `_do_calculation()` 方法处理它。该方法使用了一个阻塞操作 `time.sleep()` 。我们将使用 `reactor.callInThread()` 调用把它放到另一个线程中运行。其中，被调用的函数以及传给该函数的任意数量的参数将会作为参数。显然，我们不只传递了 `price` ，还创建并传递了一个名为 `out` 的延迟操作。当 `_do_ calculation()` 完成计算时，我们将使用out回调返回值。在下一步中，我们对这个延迟操作执行了yield处理，并为价格设置了新值，最后返回 `Item` 。

在 `_do_ calculation()` 中，注意到有一个简单的计算——价格自增1，然后是100毫秒的睡眠。这是非常多的时间，如果在reactor线程中调用，它将使我们每秒处理的页数无法超过10页。通过使其在其他线程中运行，就不再有这个问题了。任务将会在线程池中排队，等待出现可用的线程，一旦进入线程执行，该线程就将睡眠100毫秒。最后一步是触发 `out` 回调。正常情况下，可以使用 `out.callback(new_price)` ，不过由于现在处于另一个线程中，这种方法不再安全。如果这样做，会导致延迟操作的代码和Scrapy的功能会从另一个线程调用，迟早会出现错误的数据。替代方案是使用 `reactor.callFromThread()` ，同样，也是将函数作为参数，并将任意数量的额外参数传到函数中。该函数将会排队，由reactor线程调用；而另一方面，会解除 `process_item()` 对象 `yield` 操作的阻塞，为该 `Item` 恢复Scrapy操作。

如果有全局状态（比如计数器、移动平均值等）的话，那么在 `_do_calculation()` 中使用它们会发生什么呢？例如，我们添加两个变量—— `beta` 和 `delta` ，如下所示。

```python
class UsingBlocking(object):
　　def __init__(self):
　　　　self.beta, self.delta = 0, 0
　　...
　　def _do_calculation(self, price, out):
　　　　self.beta += 1
　　　　time.sleep(0.001)
　　　　self.delta += 1
　　　　new_price = price + self.beta - self.delta + 1
　　　　assert abs(new_price-price-1) < 0.01
　　　　time.sleep(0.10)...
```

上面的代码存在问题，我们会得到断言错误。这是因为如果一个线程在 `self.beta` 和 `self.delta` 之间切换，而另一个线程使用这些 `beta/delta` 的值恢复计算价格，那么会发现它们处于不一致的状态（ `beta` 比 `delta` 大），因此，会计算出错误的结果。短暂的睡眠使该问题更容易产生，不过即便没有它，竞态条件也将很快出现。为了避免此类问题发生，必须使用锁，比如使用Python的 `threading.RLock()` 递归锁。当使用锁时，我们可以确信不会存在两个线程同时执行其保护的临界区的情况。

```python
class UsingBlocking(object):
　　def __init__(self):
　　　　...
　　　　self.lock = threading.RLock()
　　...
　　def _do_calculation(self, price, out):
　　　　with self.lock:
　　　　　　self.beta += 1
　　　　　　...
　　　　　　new_price = price + self.beta - self.delta + 1
　　　　assert abs(new_price-price-1) < 0.01 ...
```

前面的代码现在是正确的。请记住我们并不需要保护整段代码，只需覆盖全局状态的使用就够了。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 本示例的完整代码位于 `ch09/properties/p``roperties/pipelines/computation.py` 文件中。

要想使用该管道，只需在 `settings.py` 文件中将其添加到 `ITEM_PIPELINES` 设置即可，如下所示。

```python
ITEM_PIPELINES = { ...
　　'properties.pipelines.computation.UsingBlocking': 500,
```

可以按照平时那样运行该爬虫。按照预期，管道延时显著增长了100毫秒，不过我们惊喜地发现吞吐量几乎保持不变，即每秒25个item左右。

