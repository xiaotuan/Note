# 附录A　安全客户端与daemon的通信

附录A中的内容本应放在第3章或者第5章。但是因为内容实在是太长了，所以只好放在附录当中。

Docker使用了客户端—服务端模型。客户端使用CLI，同时服务端（daemon）实现功能，并对外提供REST API。

客户端叫作 `docker` （在Windows上是 `docker.exe` ），daemon叫作 `dockerd` （在Windows上是 `dockerd.exe` ）。默认安装方式将客户端和服务端安装在同一台主机上，并且配置通过本地安全PIC Socket进行通信。

+ Linux： `/var/run/docker.sock` 。
+ Windows： `//./pipe/docker_engine` 。

不过，也可以配置客户端和服务端通过网络进行通信。但是daemon默认网络配置使用不安全的HTTP Socket，端口是2375/tcp，如图A.1所示。

![144.png](./images/144.png)
<center class="my_markdown"><b class="my_markdown">图A.1　配置客户端和服务端通过网络进行通信</b></center>

注：

> 默认使用 `2375` 作为客户端和服务端之间未加密通信方式的端口，而 `2376` 则用于加密通信。

在实验室这样还可以，但是生产环境却是不能接受的。

TLS就是解决之道！

Docker允许用户配置客户端和daemon间只接收安全的TLS方式连接。生产环境中推荐这种配置，即使在可信内部网络中，也建议如此配置！

Docker为客户端—daemon间使用基于TLS的安全通信提供了两种模式。

+ **daemon**  **模式** ：Docker daemon只接收认证客户端的链接。
+ **客户端模式** ：Docker客户端只接收拥有证书的Docker daemon发起的链接，其中证书需要由可信CA签发。

同时使用两种模式能提供最高的安全等级。

下面会使用简单的实验环境来完成Docker的 **daemon**  **模式** 和 **客户端模式** TLS的配置过程。

