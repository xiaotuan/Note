## 3.2　Mac版Docker（DfM）

Mac版Docker也是由Docker公司提供的一个产品。读者大可以放心使用Docker，而无须先成为一个内核工程师，也不必通过很极客的方法将Docker安装到Mac。DfM的安装方式特别简单。

Mac版Docker是由Docker公司基于社区版的Docker提供的一个产品。这意味着在笔记本上安装单引擎版本的Docker是非常简单的。但是同时，这也意味着Mac版Docker并不是为生产环境而设计的。如果读者听说过 **boot2docker** ，那么Mac版Docker就是一个流畅、简单并且稳定版的boot2docker。

对于Mac版Docker来说，提供基于Mac原生操作系统中Darwin内核的Docker引擎没有什么意义。所以在Mac版Docker当中，Docker daemon是运行在一个轻量级的Linux VM之上的。Mac版Docker通过对外提供daemon和API的方式与Mac环境实现无缝集成。这意味着读者可以在Mac上打开终端并直接使用Docker命令。

尽管在Mac上实现了无缝集成，还是要谨记Mac版Docker底层是基于Linux VM运行的，所以说Mac版Docker只能运行基于Linux的Docker容器。不过这样已经很好了，因为大部分容器实际上都是基于Linux的。

图3.3展示了Mac版Docker的抽象架构。

![16.png](./images/16.png)
<center class="my_markdown"><b class="my_markdown">图3.3　Mac版Docker的抽象架构</b></center>

注：

> Mac版Docker采用HyperKit9实现了一个极其轻量级的Hypervisor。HyperKit是基于Xhyve Hypervisor的。Mac版Docker也利用了DataKit的某些特性，并运行了一个高度优化后的Linux发行版Moby（基于Alpine Linux）。

接下来开始安装Mac版Docker。

（1）打开浏览器，访问Docker的下载页面，然后单击 `Download for Mac` 按钮。

（2）页面会跳转到Docker商店，需要读者使用自己的Docker ID和密码进行登录。

（3）单击下载链接 `Get Docker CE` 。

Mac版Docker分为两个版本：稳定版（Stable）和抢鲜版（Edge）。抢鲜版包含一些新特性，但是并不保证稳定运行。

单击链接后，会下载 **Docker.dmg** 安装包。

（4）运行上一步中下载的Docker.dmg文件。将代表Docker的鲸鱼图标拖拽到应用文件夹（Application folder）中。

（5）打开应用文件夹（可能会自动打开）并且双击Docker应用图标来启动Docker。读者可能需要确认是否运行，因为这是从互联网下载的应用程序。

（6）输入Mac用户密码，这样安装程序可以获取到创建组件所需的权限。

（7）Docker daemon进程启动。

一个活动的鲸鱼图标会在屏幕上方状态栏中出现。一旦Docker成功运行，鲸鱼图标就静止了。读者可以单击鲸鱼图标来管理DfM。

DfM现在已经安装完成，读者可以打开一个终端，并运行一些常用的Docker指令。尝试运行下面的命令。

```rust
$ docker version
Client:
 Version:      17.05.0-ce
 API version:  1.29
 Go version:   go1.7.5
 Git commit:   89658be
 Built:        Thu May 4 21:43:09 2017
 OS/Arch:      darwin/amd64
Server:
 Version:      17.05.0-ce
 API version:  1.29 (minimum version 1.12)
 Go version:   go1.7.5
 Git commit:   89658be
 Built:        Thu May 4 21:43:09 2017
 OS/Arch:      linux/amd64
 Experimental: true
```

注意， **Server** 的 `OS/Arch` 属性中显示的值是 `linux/amd64` 。这是因为daemon是基于前文提到过的Linux VM运行的。

**Client** 组件是原生的Mac应用，运行在Mac操作系统Darwin内核之上（ `OS/Arch: darwin/amd64` ）。

除此之外，还需要注意当前Docker版本是一个实验性质的版本（ `Experimental: true` ）。这是因为它是抢鲜版，抢鲜版中开启了一些实验特性。

运行其他Docker命令。

```rust
$ docker --version
Docker version 17.05.0-ce, build 89658be
$ docker image ls
REPOSITORY    TAG      IMAGE ID      CREATED      SIZE
$ docker container ls
CONTAINER ID   IMAGE   COMMAND   CREATED    STATUS    PORTS    NAMES
```

Mac版Docker安装了Docker引擎（客户端以及服务端守护程序）、Docker Compose、Docker machine以及Notary命令行。下面的3条命令向读者展示了如何确认这些组件是否成功安装，以及组件的版本信息。

```rust
$  docker --version
Docker version 17.05.0-ce, build 89658be
$  docker-compose --version
docker-compose version 1.13.0, build 1719ceb
$  docker-machine --version
docker-machine version 0.11.0, build 5b27455
$ notary version
notary
  Version:    0.4.3
  Git commit: 9211198
```

