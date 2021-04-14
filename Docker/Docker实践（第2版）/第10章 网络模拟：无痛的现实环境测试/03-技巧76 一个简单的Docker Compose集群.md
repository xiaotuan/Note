### 技巧76　一个简单的Docker Compose集群

Docker Compose的前身名为fig，fig是一个现已弃用的独立项目，旨在减轻启动多个容器时指定正确的链接、卷及端口参数的痛苦。Docker 公司对其情有独钟，直接将其收购、重制，并使用新的名字进行了发布。

本技巧使用一个简单的Docker容器编排示例来介绍Docker Compose。

#### 问题

想要让宿主机上连接的容器协同工作。

#### 解决方案

使用Docker Compose—— 一个用于定义和运行多容器的Docker应用程序的工具，其核心思想是声明应用程序的启动配置，然后使用一条简单的命令来启动该应用程序，而无须使用复杂的shell脚本或Makefile来组装容器启动命令。



**注意**

本书假定读者已安装好Docker Compose（参照官方说明文档以获取最新信息）。



为尽可能保持简单，本技巧将使用一个回响（echo）服务器和客户端。客户端每5秒发送一个常见的“Hello world!”消息给回响服务器，然后接收返回的信息。



**提示**

本技巧的源代码可从https://github.com/docker-in-practice/docker-compose-echo获取。



下面的命令将创建一个工作目录，用于创建服务器镜像：

```c
$ mkdir server
$ cd server
```

使用代码清单10-1 所示代码创建服务器Dockerfile。

代码清单10-1　Dockerfile——简单的回响服务器

```c
.FROM debian
RUN apt-get update && apt-get install -y nmap　　⇽---　安装nmap包，它提供了这里所使用的ncat程序
CMD ncat -l 2000 -k --exec /bin/cat　　⇽---　在启动该镜像时默认运行ncat程序
```

参数-l 2000指示ncat监听端口2000，参数-k让它同时接受多个客户端连接，并在客户端关闭连接后继续运行，以便更多客户端可以接入。最后一个参数--exec /bin/cat是让ncat为所有接入的连接运行/bin/cat，把来自该连接的数据转发给该运行中的程序。

接下来，使用以下命令构建这个Dockerfile：

```c
$ docker build -t server .
```

现在可以创建客户端镜像，用于向服务器发送消息。创建一个新目录，并将 client.py 文件及Dockerfile放置于此：

```c
$ cd ..
$ mkdir client
$ cd client
```

代码清单10-2给出的是一个简单的Python程序，作为回响服务器的客户端。

代码清单10-2　client.py—— 一个简单的回响客户端

```c
import socket, time, sys　　⇽---　导入所需的Python包
 while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 　　⇽---　创建一个套接字对象
     s.connect(('talkto',2000)) 　　⇽---　使用该套接字连接talkto服务器的2000端口
     s.send('Hello, world\n') 　　⇽---　发送一个带换行符的字符串到该套接字上
     data = s.recv(1024) 　　⇽---　创建一个1024字节的缓冲用于接收数据，并在收到消息时将数据放置到data变量中
     print 'Received:', data　　⇽---　将接收到的数据打印到标准输出中
     sys.stdout.flush()　　⇽---　刷新标准输出缓冲区以便在消息进入时将其显示出来
     s.close()　　⇽---　关闭该套接字对象
     time.sleep(5) 　　⇽---　等待5秒然后重复上述步骤
```

客户端的Dockerfile很简单。它安装Python，添加client.py文件，然后将其指定为启动时的默认运行项，如代码清单10-3所示。

代码清单10-3　Dockerfile—— 一个简单的回响客户端

```c
FROM debian
RUN apt-get update && apt-get install -y python
ADD client.py /client.py
CMD ["/usr/bin/python","/client.py"]
```

使用以下命令构建客户端：

```c
docker build -t client .
```

为了展示Docker Compose的价值，首先手动地运行这些容器：

```c
docker run --name echo-server -d server
docker run --name client --link echo-server:talkto client
```

命令执行完成后，按组合键Ctrl+C退出客户端，并删除这些容器：

```c
docker rm -f client echo-server
```

即便在这个简单的示例中，还是会有很多东西出错：先启动客户端将造成应用程序启动失败，忘记删除容器将在重启时造成问题，错误命名容器也将造成失败。当容器及其架构变得越来越复杂时，这类编排问题将随之增多。

Compose对此提供了解决之道，它把容器的启动和配置的编排封装在一个简单的文本文件中，并为用户管理启动与关闭命令的细节。

Compose需要一个YAML文件。请在一个新目录中创建该文件：

```c
cd ..
mkdir docker-compose
cd docker-compose
```

YAML文件的内容如代码清单10-4所示。

代码清单10-4　docker-compose.yml——Docker Compose回响服务器与客户端YAML文件

```c
version: "3"　　⇽---　这个Docker Compose文件遵循第3版规范
 services:
  echo-server: 　　⇽---　运行中的服务的引用名称是它们的标识：本示例中是echo-server和client
     image: server　　⇽---　每个小节都必须定义所使用的镜像：本示例中是客户端与服务器镜像
     expose: 　　⇽---　将echo-server的2000端口对其他服务公开
     - "2000"
  client: 　　⇽---　运行中的服务的引用名称是它们的标识：本示例中是echo-server和client
               image: client　　⇽---　每个小节都必须定义所使用的镜像：本示例中是客户端与服务器镜像
               links: 　　⇽---　定义一个指向echo-server的链接。客户端内对talkto的引用将被发送给回响服务器。其映射是通过在运行的容器中动态设置/etc/hosts文件完成的
- echo-server:talkto
```

docker-compose.yml的语法非常容易理解： `services` 键下的是命名的服务，配置声明在下方缩进的小节中。每个配置项名称后面都有一个冒号，这些项目的属性要么声明在同一行，要么声明在后续以相同缩进层次破折号开始的几行中。

这里需要理解的关键配置项是客户端定义中的 `links` 。这个链接的创建方式与 `docker run` 命令创建链接的方式一致，不同的是Compose会处理好启动顺序。实际上，大部分Docker命令行参数在docker-compose.yml语法中都有直接的对应关系。

这个示例中使用 `image:` 语句来定义每个服务所使用的镜像，不过也可以在 `build:` 语句中定义Dockerfile的路径，让docker-compose动态地重新构建所需镜像。Docker Compose会自动进行构建。



**提示**

YAML文件是使用简单语法的一个文本配置文件。更多信息可从其官方网站获得。



现在所有的基础设施都创建好了，运行该应用程序很简单：

```c
$ docker-compose up
Creating dockercompose_server_1...
Creating dockercompose_client_1...
Attaching to dockercompose_server_1, dockercompose_client_1
client_1 | Received: Hello, world
client_1 |
client_1 | Received: Hello, world
client_1 |
```



**提示**

如果在启动docker-compose时出现类似“Couldn’t connect to Docker daemon athttp+unix:// var/run/docker.sock--is it running?”这样的错误，其问题可能是需要使用sudo运行。



确认结果无误后，按多次组合键Ctrl+C退出应用程序。使用相同的命令即可重新运行该应用程序，而无须考虑删除容器的问题。需要注意的是，在重新运行时输出的是“Recreating”（重新创建）而不是“Creating”（创建）。

#### 讨论

上面的小节中提到了一个可能需要使用sudo的地方——如果这适用于你，请重新阅读一下技巧41，因为它将让使用与Docker守护进程交互的工具变得异常简单。

Docker公司宣称Docker Compose可以在生产中使用， 既可以像这里所展示的用在单台机器上，也可以在swarm模式中部署在多台机器上——你将在技巧87中看到如何实现这一点。

我们已经对Docker Compose有所了解，接下来讨论一个更复杂的docker-compose现实场景：使用socat、卷及替代链接为运行在宿主机上的一个SQLite实例添加类似服务器的功能。

