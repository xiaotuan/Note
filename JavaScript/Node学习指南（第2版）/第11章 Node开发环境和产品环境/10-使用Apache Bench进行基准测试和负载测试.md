

## 11.4　使用Apache Bench进行基准测试和负载测试

> <img class="my_markdown" src="../images/113.png" style="zoom:50%;" />
> **Loadtest应用**
> 你还可以使用Loadtest应用来进行负载测试：
> 它相对于ApacheBench的优势在于，你不但可以设置并发用户，还可以设置并发请求：

一个App再怎么稳定，哪怕是满足了用户的所有需求，如果在性能上很差劲，那么它也注定是短命的。我们需要对程序进行性能测试（performance test），特别是当我们为了提升性能而对代码进行修改的时候。总不能随便改改，就放在产品环境中让用户使用，然后让用户来告诉我们程序中的性能问题吧。

性能测试包含基准测试和负载测试。基准测试（benchmark testing），或称为对比测试（comparison test），指的是运行同一个应用的不同版本，然后看哪个性能更好。当你进行性能调优时，性能测试可以有效地帮你提升程序的效率和可扩展性。测试过程就是，先创建一个标准化的测试，让这个测试在不同版本的程序上运行，然后分析结果。

而负载测试（lood testing），其实就是针对程序进行的压力测试。当对资源的需求过高，或者有太多的并发用户时，你就需要观察程序在什么样的情况下开始崩溃。一般我们都会给程序加压，直到它崩溃。崩溃是负载测试成功的标志。

```python
npm install -g loadtest
```

有很多工具同时支持这两种测试，其中比较流行的是ApacheBench。它流行的原因是：在任何安装了Apache的机器上，都自带ApacheBench——而没有安装Apache的机器少之又少。这个工具又小巧，又好用，而且功能强大。当我不知道应该创建一个可复用的静态数据库连接，还是应该每次用的时候创建一个连接且用完就删掉的时候，我就会使用ApacheBench来运行测试。

ApacheBench通常被称为ab，从现在开始我也使用这个缩写。ab是一个命令行工具，它可以让我们指定一个程序被运行多少次，以及有多少并发用户。如果我们想要模拟20个并发用户同时访问一个Web应用100次，可以使用下面的命令：

```python
loadtest [-n requests] [-c concurrency] [-k] URL
```

```python
ab -n 100 -c 20 http://burningbird.net/
```

命令末尾的斜线是必需的，因为ab只认完整的、包含路径的URL。

ab提供了相当丰富的输出信息。下面的例子就是某次测试（隐藏了工具信息）的输出信息：

```python
Benchmarking burningbird.net (be patient).....done
Server Software:        Apache/2.4.7
Server Hostname:        burningbird.net
Server Port:            80
Document Path:          /
Document Length:        36683 bytes
Concurrency Level:      20
Time taken for tests:   5.489 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      3695600 bytes
HTML transferred:       3668300 bytes
Requests per second:    18.22 [#/sec] (mean)
Time per request: 1097.787 [ms] (mean)
Time per request: 54.889 [ms] (mean, across all concurrent requests)
Transfer rate:          657.50 [Kbytes/sec] received
Connection Times (ms)
              min  mean[+/-sd] median max
Connect:        0    1   2.3      0     7
Processing:   555 1049 196.9   1078  1455
Waiting:       53  421 170.8    404   870
Total:        559 1050 197.0   1080  1462
Percentage of the requests served within a certain time (ms)
  50% 1080
  66% 1142
  75% 1198
  80% 1214
  90% 1341
  95% 1392
  98% 1415
  99% 1462
 100% 1462 (longest request)
```

我们最感兴趣的就是每个测试所用时间的信息，以及最后的（基于百分比的）累积分布。根据这些输出信息，每个请求的平均时间（也就是average time per request这个标签第一次出现的地方）是1 097.787ms。这就是一个用户需要等待响应的平均时间。第二行的信息表示的是吞吐量，可能不如第一行那么有用。

累积分布则提供了另外一个视角，让我们可以很好地观察在某一时间区间内的请求所占的百分比。这些数据同样反映出用户的平均数据，从数据中我们看到的是用户获得响应的平均时间：响应时间从1 080ms到1 462ms不等，其中绝大部分对响应的处理时间为1 392ms及以下。

以上数据中最后一个值得关心的数据是每秒请求数——在本例中这个数字是18.22。这个数据在一定程度上帮助我们预测应用的可扩展性，因为它告诉我们这个应用每秒能处理多少请求——也就是，该程序处理能力的上限。但是，一定要在不同时间和不同负载之下运行这个测试，特别是如果你的系统还提供别的服务。

[1]　JavaScript中的相等有3种级别，第一种是普通相等（\==），可以通过转化为bool类型进行比较是否相等；第二种是reference equal（\===），即引用一致，两个对象指向同一块内存区域，即相等；另一种是deep equal，即内容一致，两个对象指向不同的内存区域，但是它们各自包含的属性和属性值完全一致，也算是相等。——译者注



