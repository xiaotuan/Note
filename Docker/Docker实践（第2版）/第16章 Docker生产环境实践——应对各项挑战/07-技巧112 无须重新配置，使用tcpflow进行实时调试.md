### 技巧112　无须重新配置，使用tcpflow进行实时调试

tcpdump是网络诊断的事实标准，如果需要深入调试网络问题，它可能是大多数人首选的工具。

但tcpdump通常用于显示分组摘要以及检查分组首部和协议信息——它对于两个程序之间应用层数据流的展示并不是很完善。但是这些信息在调查两个应用程序间的通信问题时可能非常重要。

#### 问题

需要监控容器化应用程序的通信数据。

#### 解决方案

使用tcpflow捕获通过接口的流量。

tcpflow类似于tcpdump（接受相同的模式匹配表达式），但是它的目的是更好地了解应用程序的数据流。可以通过系统包管理工具安装tcpflow，但是，如果系统包中没有，我们也为此准备了一个可用的Docker镜像，它在功能上与通过包管理工具安装的效果一样：

```c
$ IMG=dockerinpractice/tcpflow
$ docker pull $IMG
$ alias tcpflow="docker run --rm --net host $IMG"
```

这里有两种方式通过Docker使用tcpflow，一是将其指向docker0接口，并使用分组过滤表达式只检索想要的分组，或者使用技巧111的方法来找到感兴趣的容器的veth接口，并捕获该接口。



**提示**

可能需要查看第10章中的图10-2来回忆Docker中的网络流量是如何流动的，看一下为何捕获docker0可以捕获容器流量。



表达式过滤是tcpflow的很强大的特性，可以在附加接口之后使用，它可以让用户深入了解感兴趣的流量。我们将展示一个简单的示例以便读者可以快速上手：

```c
$ docker run -d --name tcpflowtest alpine:3.2 sleep 30d
fa95f9763ab56e24b3a8f0d9f86204704b770ffb0fd55d4fd37c59dc1601ed11
$ docker inspect -f '{{ .NetworkSettings.IPAddress }}' tcpflowtest
172.17.0.1
$ tcpflow -c -J -i docker0 'host 172.17.0.1 and port 80'
tcpflow: listening on docker0
```

在上面的示例中，我们要求tcpflow以彩色的方式打印容器中通过80端口（通常用于HTTP流量）的流入或流出流量。现在，读者可以通过在新终端的容器中访问网页来体验上述命令的效果：

```c
$ docker exec tcpflowtest wget -O /dev/null http://www.example.com/
Connecting to www.example.com (93.184.216.34:80)
null            100% |*******************************|  1270   0:00:00 ETA
```

读者将可以看到在tcpflow终端中的彩色输出。到目前为止，命令的累积输出看上去会是这样：

```c
$ tcpflow -J -c -i docker0 'host 172.17.0.1 and (src or dst port 80)'
tcpflow: listening on docker0
172.017.000.001.36042-093.184.216.034.00080: >
GET / HTTP/1.1　　⇽---　蓝色开始
 Host: www.example.com
User-Agent: Wget
Connection: close
093.184.216.034.00080-172.017.000.001.36042: >
HTTP/1.0 200 OK　　⇽---　红色开始
 Accept-Ranges: bytes
Cache-Control: max-age=604800
Content-Type: text/html
Date: Mon, 17 Aug 2015 12:22:21 GMT
[...]
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
[...]
```

#### 讨论

tcpflow 是工具箱的一个很好补充，尽管它并不引人注目。用户可以对长时间运行的容器执行tcpflow，以便了解其现在正在传送的内容，或者与tcpdump（见技巧111）一起使用，来获得更详细的应用程序发送的请求以及传输的信息。

如同tcpdump一样，技巧111也讲述了用nsenter来监控一个容器而不是所有容器的流量（这正是监控docker0将会做到的）。

