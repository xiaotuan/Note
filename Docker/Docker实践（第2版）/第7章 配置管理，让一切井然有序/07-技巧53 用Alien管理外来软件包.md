### 技巧53　用Alien管理外来软件包

本书里（还有互联网上）绝大部分Dockerfile示例使用的都是基于Debian的镜像，而软件开发的现实决定了许多人不会专门做这些打包的事情。

好在有现成的工具可以帮助用户实现这一点。

#### 问题

想要安装一个外来的发行版的软件包。

#### 解决方案

使用一个名为Alien的工具来转换软件包。Alien已经被内置到了一个Docker镜像里，我们将使用该镜像作为本技巧的一部分。

Alien是一款命令行工具，是专为转换不同格式的软件包文件设计的，如表7-1所示。我们不止一次遇到过需要让外来软件包管理系统下的软件包正常工作的情况，例如，.deb用在CentOs中，.rpm文件用在非Red Hat系的系统中。

<center class="my_markdown"><b class="my_markdown">表7-1　Alien支持的包格式</b></center>

| 扩 展 名 | 描 述 |
| :-----  | :-----  | :-----  | :-----  |
| .deb | Debian包 |
| .rpm | Red Hat包管理 |
| .tgz | Slackware gzip压缩的TAR文件 |
| .pkg | Solaris PKG包 |
| .slp | Stampede包 |



**注意**

出于本技巧的初衷，没有完全覆盖到Solaris包和Stampede包。Solaris要求安装Solaris特有的软件，而Stampede则是一个已经废弃的项目。



在本书的研究过程中我们发现，在非Debian系的发行版上安装Alien可能会有些费劲儿。这是一本Docker书，我们自然决定以Docker镜像的形式提供一个转换工具。作为一个小福利，这一工具用到了技巧49中介绍的 `ENTRYPOINT` 命令，让用户可以更加便利地使用它。

举个例子，让我们下载然后（使用Alien）转换eatmydata这个软件包，在技巧62里会用到它：

```c
$ mkdir tmp && cd tmp　　⇽---　创建一个空的工作目录
$ wget \
http://mirrors.kernel.org/ubuntu/pool/main/libe/libeatmydata
➥/eatmydata_26-2_i386.deb　　⇽---　检索想要转换的包文件
$ docker run -v $(pwd):/io dockerinpractice/alienate　　⇽---　运行dockerinpractice/ alienate镜像，将当前目录挂载到容器的/io路径下。容器会检查该目录，尝试转换找到的任意有效文件
Examining eatmydata_26-2_i386.deb from /io
eatmydata_26-2_i386.deb appears to be a Debian package　　⇽---　容器通知用户它运行Alien包装脚本时的行为
eatmydata-26-3.i386.rpm generated
eatmydata-26.slp generated
eatmydata-26.tgz generated
================================================
/io now contains:
eatmydata-26-3.i386.rpm
eatmydata-26.slp
eatmydata-26.tgz
eatmydata_26-2_i386.deb
================================================
$ ls -1　　⇽---　文件已经被转换为RPM、Slackware TGZ和Stampede文件
eatmydata_26-2_i386.deb
eatmydata-26-3.i386.rpm
eatmydata-26.slp
eatmydata-26.tgz
```

或者，也可以直接将想要下载并转换的软件包的URL直接传给 `docker run` 命令：

```c
$ mkdir tmp && cd tmp
$ docker run -v $(pwd):/io dockerinpractice/alienate \
http://mirrors.kernel.org/ubuntu/pool/main/libe/libeatmydata
➥/eatmydata_26-2_i386.deb
wgetting http://mirrors.kernel.org/ubuntu/pool/main/libe/libeatmydata
➥/eatmydata_26-2_i386.deb
--2015-02-26 10:57:28-- http://mirrors.kernel.org/ubuntu/pool/main/libe
➥/libeatmydata/eatmydata_26-2_i386.deb
Resolving mirrors.kernel.org (mirrors.kernel.org)... 198.145.20.143,
➥149.20.37.36, 2001:4f8:4:6f:0:1994:3:14, ...
Connecting to mirrors.kernel.org (mirrors.kernel.org)|198.145.20.143|:80...
➥connected.
HTTP request sent, awaiting response... 200 OK
Length: 7782 (7.6K) [application/octet-stream]
Saving to: 'eatmydata_26-2_i386.deb'
     0K .......                         100% 2.58M=0.003s
2015-02-26 10:57:28 (2.58 MB/s) - 'eatmydata_26-2_i386.deb' saved
➥[7782/7782]
Examining eatmydata_26-2_i386.deb from /io
eatmydata_26-2_i386.deb appears to be a Debian package
eatmydata-26-3.i386.rpm generated
eatmydata-26.slp generated
eatmydata-26.tgz generated
=========================================================
/io now contains:
eatmydata-26-3.i386.rpm
eatmydata-26.slp
eatmydata-26.tgz
eatmydata_26-2_i386.deb
=========================================================
$ ls -1
eatmydata_26-2_i386.deb
eatmydata-26-3.i386.rpm
eatmydata-26.slp
eatmydata-26.tgz
```

如果想在自己的容器里运行Alien，可以通过这个命令启动容器：

```c
docker run -ti --entrypoint /bin/bash dockerinpractice/alienate
```



**警告**

Alien这款工具的定位是“尽力而为”，它并不保证一定能够将提供的包转换成功。



#### 讨论

Docker的使用引起了人们又一次地关注起已经停息了一段时间的“发行版战争”。在此之前大多数组织已经选择简单地使用Red Hat或Debian的应用商店，并不需要关注其他包管理系统。而现在，在一个组织内收到要求引入基于“外来“发行版的Docker镜像的请求并不罕见。

这就是本技巧可以发挥作用的地方，因为“外来“的软件包可以被转换成一个更友好的格式。我们会在第14章讨论安全的时候回顾这一主题。

