### 10.4.3　Docker的概念与组件

如图10-6所示，Docker引擎（简称Docker）包含多个组件。刚才在测试Docker安装是否成功时，我们就用到了第一个组件Docker客户端，它就是用户在与Docker守护进程交互时所使用的命令行接口。

![66.png](../images/66.png)
<center class="my_markdown"><b class="my_markdown">图10-6　Docker引擎由Docker客户端、Docker 守护进程以及不同的Docker容器组成，这些容器为Docker镜像的实例。Docker镜像可以通过Dockerfile创建，并且镜像还能够存储在Docker注册中心（registy）中</b></center>

Docker守护进程运行在宿主操作系统（host OS）之上，该进程会对客户端发送的服务请求进行应答，并对容器进行管理。

Docker容器（简称容器）是对运行特定应用所需的全部程序（包括操作系统在内）的一种轻量级虚拟化。轻量级容器会让应用以及与之相关联的其他程序认为自己独占了整个操作系统以及所有硬件，但是实际上并非如此，多个应用共享同一宿主操作系统。

Docker容器都基于Docker镜像构建，后者是辅助容器进行启动的只读模板，所有容器都需要通过镜像启动。有好几种不同的方法可以创建Docker镜像，其中一种就是在一个名为Dockerfile的文件里包含一系列指令。

Docker镜像既可以以本地形式存储在运行着Docker守护进程的机器上（也就是Docker的宿主机之上），也可以被托管至名为Docker注册中心的Docker镜像资源库里面。用户既可以使用自己的私有Docker注册中心，也可以使用Docker Hub（https://hub.docker.com/）作为自己的registy。Docker Hub同时提供公开和私有的Docker镜像，但私有的Docker镜像需要付费才能使用。

如果用户是在类似Ubuntu这样的Linux系统上安装Docker，那么Docker守护进程和Docker客户端将被安装到同一机器里面。但如果用户是在OS X和Windows这样的系统上安装Docker，那么Docker只会把客户端安装在操作系统里面，而守护进程则会被安装到其他地方，通常会是一个运行在该系统之上的虚拟机里面。这种情况的一个例子是，在OS X上安装Docker时，Docker客户端将被安装到OS X里面，而Docker守护进程则会被安装到VirtualBox（一款基于x86架构的虚拟机监视器）的一个虚拟机里面。

在此之后，用户只需要通过Docker镜像来运行Docker容器，并将其运行在Docker宿主之上就可以了。

在对Docker有了一个大体的了解之后，我们是时候来学习如何将Web应用部署到Docker里面了。接下来的一节将继续使用前面展示过的简单Web服务作为例子，演示如何将Web应用部署到Docker容器。

