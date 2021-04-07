### 8.1.2　理解Twisted和非阻塞I/O——一个Python故事

既然我们已经掌握了原语，接下来让我告诉你一个Python的小故事。该故事中所有人物均为虚构，如有雷同纯属巧合。

```python
# ~*~ Twisted - A Python tale ~*~
from time import sleep
# Hello, I'm a developer and I mainly setup Wordpress.
def install_wordpress(customer):
　　# Our hosting company Threads Ltd. is bad. I start installation and...
　　print "Start installation for", customer
　　# ...then wait till the installation finishes successfully. It is
　　# boring and I'm spending most of my time waiting while consuming
　　# resources (memory and some CPU cycles). It's because the process
　　# is *blocking*.
　　sleep(3)
　　print "All done for", customer
# I do this all day long for our customers
def developer_day(customers):
　　for customer in customers:
　　　　install_wordpress(customer)
developer_day(["Bill", "Elon", "Steve", "Mark"])
```

运行该代码。

```python
$ ./deferreds.py 1
------ Running example 1 ------
Start installation for Bill
All done for Bill
Start installation
...
* Elapsed time: 12.03 seconds
```

我们得到的是顺序的执行。4位客户，每人执行3秒，意味着总共需要12秒的时间。这种方式的扩展性不是很好，因此我们将在第二个例子中添加多线程。

```python
import threading
# The company grew. We now have many customers and I can't handle
the
# workload. We are now 5 developers doing exactly the same thing.
def developers_day(customers):
　　# But we now have to synchronize... a.k.a. bureaucracy
　　lock = threading.Lock()
　　#
　　def dev_day(id):
　　　　print "Goodmorning from developer", id
　　　　# Yuck - I hate locks...
　　　　lock.acquire()
　　　　while customers:
　　　　　　customer = customers.pop(0)
　　　　　　lock.release()
　　　　　　# My Python is less readable
　　　　　　install_wordpress(customer)
　　　　　　lock.acquire()
　　　　lock.release()
　　　　print "Bye from developer", id
　　# We go to work in the morning
　　devs = [threading.Thread(target=dev_day, args=(i,)) for i in
range(5)]
　　[dev.start() for dev in devs]
　　# We leave for the evening
　　[dev.join() for dev in devs]
# We now get more done in the same time but our dev process got more
# complex. As we grew we spend more time managing queues than doing dev
# work. We even had occasional deadlocks when processes got extremely
# complex. The fact is that we are still mostly pressing buttons and
# waiting but now we also spend some time in meetings.
developers_day(["Customer %d" % i for i in xrange(15)])
```

按照下述方式运行这段代码。

```python
$ ./deferreds.py 2
------ Running example 2 ------
Goodmorning from developer 0Goodmorning from developer
1Start installation forGoodmorning from developer 2
Goodmorning from developer 3Customer 0
...
from developerCustomer 13 3Bye from developer 2
* Elapsed time: 9.02 seconds

```

在这段代码中，使用了5个线程并行执行。15个客户，每人3秒，总共需要执行45秒，而当使用5个并行的线程时，最终只花费了9秒钟。不过代码有些难看。现在代码的一部分只用于管理并发性，而不是专注于算法或业务逻辑。另外，输出也变得混乱并且可读性很差。即使是让很简单的多线程代码正确运行，也有很大难度，因此我们将转为使用Twisted。

```python
# For years we thought this was all there was... We kept hiring more
# developers, more managers and buying servers. We were trying harder
# optimising processes and fire-fighting while getting mediocre
# performance in return. Till luckily one day our hosting
# company decided to increase their fees and we decided to
# switch to Twisted Ltd.!
from twisted.internet import reactor
from twisted.internet import defer
from twisted.internet import task
# Twisted has a slightly different approach
def schedule_install(customer):
　　# They are calling us back when a Wordpress installation completes.
　　# They connected the caller recognition system with our CRM and
　　# we know exactly what a call is about and what has to be done
　　# next.
　　#
　　# We now design processes of what has to happen on certain events.
　　def schedule_install_wordpress():
　　　　def on_done():
　　　　　　print "Callback: Finished installation for", customer
　　　　print "Scheduling: Installation for", customer
　　　　return task.deferLater(reactor, 3, on_done)
　　#
　　def all_done(_):
　　　　print "All done for", customer
　　#
　　# For each customer, we schedule these processes on the CRM
　　# and that
　　# is all our chief-Twisted developer has to do
　　d = schedule_install_wordpress()
　　d.addCallback(all_done)
　　#
　　return d
# Yes, we don't need many developers anymore or any synchronization.
# ~~ Super-powered Twisted developer ~~
def twisted_developer_day(customers):
　　print "Goodmorning from Twisted developer"
　　#
　　# Here's what has to be done today
　　work = [schedule_install(customer) for customer in customers]
　　# Turn off the lights when done
　　join = defer.DeferredList(work)
　　join.addCallback(lambda _: reactor.stop())
　　#
　　print "Bye from Twisted developer!"
# Even his day is particularly short!
twisted_developer_day(["Customer %d" % i for i in xrange(15)])
# Reactor, our secretary uses the CRM and follows-up on events!
reactor.run()
```

现在运行该代码。

```python
$ ./deferreds.py 3
------ Running example 3 ------
Goodmorning from Twisted developer
Scheduling: Installation for Customer 0
....
Scheduling: Installation for Customer 14
Bye from Twisted developer!
Callback: Finished installation for Customer 0
All done for Customer 0
Callback: Finished installation for Customer 1
All done for Customer 1
...
All done for Customer 14
* Elapsed time: 3.18 seconds

```

此时，我们在没有使用多线程的情况下，就获得了良好运行的代码，以及漂亮的输出结果。我们并行处理了所有的15位客户，也就是说，应当执行45秒的计算只花费了3秒钟！技巧就是将所有阻塞调用的 `sleep()` 替换为Twisted对应的 `task.deferLater()` 以及回调函数。由于处理现在发生在其他地方，因此可以毫不费力地同时为15位客户服务。

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 刚才提到前面的处理此时是在其他地方执行的。这是在作弊吗？答案当然不是。算法计算仍然在CPU中处理，不过与磁盘和网络操作相比，CPU操作速度很快。因此，将数据传给CPU、从一个CPU发送或存储数据到另一个CPU中，占据了大部分时间。我们使用非阻塞的I/O操作，为CPU节省了这些时间。这些操作，尤其是像 `task.deferLater()` 这样的操作，会在数据传输完成后触发回调函数。

另一个需要非常注意的地方是 `Goodmorning from Twisted developer` 以及 `Bye from Twisted developer!` 消息。在代码启动时，它们就都被立即打印了出来。如果代码过早地到达该点，那么应用实际是什么时候运行的呢？答案是Twisted应用（包括Scrapy）完全运行在 `reactor.run()` 上！当调用该方法时，必须拥有应用程序预期使用的所有可能的延迟链（相当于前面故事中建立CRM系统的步骤和流程）。你的 `reactor.run()` （故事中的秘书）执行事件监控以及触发回调。

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> reactor的主要规则是：只要是快速的非阻塞操作就可以做任何事。

非常好！不过虽然代码没有了多线程时的混乱输出，但是这里的回调函数还是有一些难看！因此，我们将引入下一个例子。

```python
# Twisted gave us utilities that make our code way more readable!
@defer.inlineCallbacks
def inline_install(customer):
　　print "Scheduling: Installation for", customer
　　yield task.deferLater(reactor, 3, lambda: None)
　　print "Callback: Finished installation for", customer
　　print "All done for", customer
def twisted_developer_day(customers):
　 ... same as previously but using inline_install()
　　　 instead of schedule_install()
twisted_developer_day(["Customer %d" % i for i in xrange(15)])
reactor.run()
```

以如下方式运行该代码。

```python
$ ./deferreds.py 4
... exactly the same as before

```

上述代码和之前那个版本的代码看起来基本一样，不过更加优雅。 `inlineCallbacks` 生成器使用了一些Python机制让 `inline_install()` 的代码能够暂停和恢复。 `inline_install()` 变为延迟函数，并且为每位客户并行执行。每当执行 `yield` 时，执行会在当前的 `inline_install()` 实例上暂停，当yield的延迟函数触发时再恢复。

现在唯一的问题是，如果不是只有15个客户，而是10000个，该代码会无耻地同时启动10000个处理序列（调用HTTP请求、数据库写操作等）。这样可能会正常运行，也可能造成各种各样的失败。在大规模并发应用中，比如Scrapy，一般需要将并发量限制到可接受的水平。在本例中，可以使用 `task.Cooperator()` 实现该限制。Scrapy使用了同样的机制在item处理管道中限制并发量（ `CONCURRENT_ITEMS` 设置）。

```python
@defer.inlineCallbacks
def inline_install(customer):
　 ... same as above
# The new "problem" is that we have to manage all this concurrency to
# avoid causing problems to others, but this is a nice problem to have.
def twisted_developer_day(customers):
　　print "Goodmorning from Twisted developer"
　　work = (inline_install(customer) for customer in customers)
　　#
　　# We use the Cooperator mechanism to make the secretary not
　　# service more than 5 customers simultaneously.
　　coop = task.Cooperator()
　　join = defer.DeferredList([coop.coiterate(work) for i in xrange(5)])
　　#
　　join.addCallback(lambda _: reactor.stop())
　　print "Bye from Twisted developer!"
twisted_developer_day(["Customer %d" % i for i in xrange(15)])
reactor.run()
# We are now more lean than ever, our customers happy, our hosting
# bills ridiculously low and our performance stellar.
# ~*~ THE END ~*~
```

运行该代码。

```python
$ ./deferreds.py 5
------ Running example 5 ------
Goodmorning from Twisted developer
Bye from Twisted developer!
Scheduling: Installation for Customer 0
...
Callback: Finished installation for Customer 4
All done for Customer 4
Scheduling: Installation for Customer 5
...
Callback: Finished installation for Customer 14
All done for Customer 14
* Elapsed time: 9.19 seconds

```

可以看到，现在有类似于5个客户的处理槽。如果想要处理一个新的客户，只有在存在空槽时才可以开始，实际上，在这个例子中客户处理的时间总是相同的（3秒），因此会造成5位客户会在同一时间被批量处理的情况。最后，我们得到了和多线程示例中相同的性能，不过现在只使用了一个线程，代码更加简单并且更容易正确编写。

祝贺你，坦白地说，现在你得到了对于Twisted和非阻塞I/O编程的一份非常严谨的介绍。

