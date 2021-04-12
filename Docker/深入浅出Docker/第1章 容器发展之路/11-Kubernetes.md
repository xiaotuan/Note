## 1.10　Kubernetes

Kubernetes是谷歌的一个开源项目，并且开源之后迅速成为容器编排领域的领头羊。有一种很流行的说法：Kubernetes是保证容器部署和运行的软件体系中很重要的一部分。

在本书撰写时，Kubernetes已经采用Docker作为其默认容器运行时（container runtime），包括Kubernetes启动和停止容器，以及镜像的拉取等。但是，Kubernetes也提供了一个可插拔的容器运行时接口CRI。CRI能够帮助Kubernetes实现将运行时环境从Docker快速替换为其他容器运行时。在未来，Kubernetes中的默认容器运行时可能由Docker替换为 `containerd` 。关于 `containerd` 在本书后续部分有更详细的介绍。

关于Kubernetes，读者现在需要了解的就是——Kubernetes是Docker之上的一个平台，现在采用Docker实现其底层容器相关的操作。

![8.png](./images/8.png)
可以通过阅读我Kubernetes的图书，以及观看 **Getting Started with Kubernetes** 视频课程来进一步了解Kubernetes的相关内容。

