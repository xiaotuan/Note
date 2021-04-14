### 技巧57　通过BusyBox和Alpine精简Docker镜像

自Linux诞生起就出现了一些小而可用的操作系统，它们可以嵌到低功耗或廉价的计算机上。幸运的是，这些项目的努力成果已经被重新用于生产小型Docker镜像，它们可以用于镜像大小非常重要的场合。

#### 问题

想要得到一个小而功能俱全的镜像。

#### 解决方案

在构建自己的镜像时，使用一个小的基础镜像，如BusyBox或Alpine。

这是另外一个领域，其中现有技术的更迭非常迅速。两种流行的选择是BusyBox和Alpine，而每种都有不同的特点。

如果用户的目标是小而精，那么BusyBox可能会是首选。倘若用户以如下命令启动一个BusyBox镜像，那么可能会发生一些意外情况：

```c
$ docker run -ti busybox /bin/bash
exec: "/bin/bash": stat /bin/bash: no such file or directory2015/02/23 >
09:55:38 Error response from daemon: Cannot start container >
73f45e34145647cd1996ae29d8028e7b06d514d0d32dec9a68ce9428446faa19: exec: >
"/bin/bash": stat /bin/bash: no such file or directory
```

BusyBox甚至已经精简到了没有bash的程度！取而代之的是它使用ash，这是一个兼容posix的shell——实际上它是像bash和ksh这样更高级的shell的一个受限版本：

```c
$ docker run -ti busybox /bin/ash
/ #
```

而许多类似这样的决策的结果便是，BusyBox镜像的大小竟然精简到了小于2.5 MB！



**警告**

BusyBox还有一些其他出人意料的行为。举个例子，该镜像下 `tar` 命令的版本将很难从GNU标准的 `tar` 包中解压出TAR文件。



如果用户想要只依赖一些简单工具来编写一个小脚本，这样做会很赞，但是如果想要在其他任何必须自行安装它的地方运行，这就不太好了。BusyBox没有自带的包管理。

其他维护人员已经给BusyBox加上了包管理的功能。举个例子，progrium/busybox可能不是最小的BusyBox容器（它现在小于5 MB），但是它有opkg，这意味着用户可以轻松地安装其他常用软件包，同时将镜像的大小保持为绝对最小。举个例子，如果缺少bash，可以像下面这样安装它：

```c
$ docker run -ti progrium/busybox /bin/ash
/ # opkg-install bash > /dev/null
/ # bash
bash-4.3#
```

在提交时，这会生成一个6 MB的镜像。

有一个很有意思的Docker镜像（它已经成为精简Docker镜像的标准）便是gliderlabs/ alpine。它和BusyBox很像，但是有更广泛的软件包。

这些软件包均被设计为精简安装。作为一个具体示例，代码清单7-17展示了一个Dockerfile，它产生的镜像大小为1/4 GB。

代码清单7-17　Ubuntu加mysql-client

```c
FROM ubuntu:14.04
RUN apt-get update -q \
&& DEBIAN_FRONTEND=noninteractive apt-get install -qy mysql-client \
&& apt-get clean && rm -rf /var/lib/apt
ENTRYPOINT ["mysql"]
```



**提示**

在 `apt-get install` 之前加上 `DEBIAN_FRONTEND = noninteractive` 可以确保在安装时不会在安装过程中提示任何输入。由于用户不能在执行命令时轻松地响应问题，因此这一点往往在Dockerfile里非常有用。



对比之下，这次会产出一个略大于36 MB的镜像，如代码清单7-18所示。

代码清单7-18　Alphine加mysql-client

```c
FROM gliderlabs/alpine:3.6
RUN apk-install mysql-client
ENTRYPOINT ["mysql"]
```

#### 讨论

在过去的几年里，这一领域发展得非常迅速。在Docker公司的一些帮助下，Alphine的基础镜像已经超越了BusyBox，成为了Docker标准的一部分。

此外，其他的标准基础镜像也在不断瘦身。例如Debian镜像在我们准备本书第2版时已经快瘦身到100MB了——远比它之前要小。

还有一个值得一提的是，有许多关于减小镜像体积或者使用更小的基础镜像的讨论。但是有时候这些问题并不需要去解决。记住，通常把时间和精力花在克服现有的瓶颈上是最佳策略，而不是取得理论上有好处，但是实际上并不值得你的努力的成果。

