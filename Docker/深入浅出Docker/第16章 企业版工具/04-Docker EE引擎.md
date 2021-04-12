### 16.2.1　Docker EE引擎

Docker引擎提供Docker全部核心功能。核心功能包括镜像、容器管理、网络、卷、集群、安全等。在本书编写之时，包括两个版本：社区版（CE）和企业版（EE）。

两个版本最大的不同，也是用户最关心的，就是发布周期和相应支持了。

Docker EE是按季度发布，采用基于时间版本的方案。例如，2018年6月发布的Docker EE叫作 `18.06.x-ee` 。Docker公司提供持续一年的支持，并且为每个版本打补丁。

##### 安装Docker EE

安装Docker EE很简单。但是，不同平台的安装方式略有不同。本书会介绍在Ubuntu 16.04的安装过程，但其他平台的安装也非常简单。

Docker EE是基于订阅模式的服务，所以用户需要一个Docker ID并且激活订阅。然后就可以获得专享Docker EE仓库，在接下来的步骤中会用到。试用许可证通常也是可行的。

注：

> 在Windows服务器上的Docker通常都安装Docker EE。参考第3章内容可以了解如何在Windows Server 2016上安装Docker EE。

下面的命令可能需要sudo前缀。

（1）检查是否拥有最新包列表

```rust
$ apt-get update
```

（2）安装过程需要通过HTTPS访问Docker EE。

```rust
$ apt-get install -y \
          apt-transport-https \
          curl \
          software-properties-common
```

（3）登录Docker存储，复制Docker EE仓库URL。

使用浏览器访问 Docker Store。单击右上方的用户名并选择 `My Content` 。选择某个已经订阅的Docker EE，单击 `Setup` ，如图16.2所示。

![110.png](./images/110.png)
<center class="my_markdown"><b class="my_markdown">图16.2　选择已订阅的Docker EE，单击 `Setup`</b></center>

复制 `Resources` 面板下面的仓库URL。

下载许可证，如图16.3所示。

![111.png](./images/111.png)
<center class="my_markdown"><b class="my_markdown">图16.3　下载许可证</b></center>

本书演示了如何设置Ubuntu的仓库。但是，当前Docker存储页面还包括其他Linux发行版的设置教程。

（4）在环境变量中设置专享的Docker EE仓库URL。

```rust
$ DOCKER_EE_REPO=<paste-in-your-unique-ee-url>
```

（5）将官方Docker GPG密钥加入全部密钥环（keyring）。

```rust
$ curl -fsSL "${DOCKER_EE_REPO}/ubuntu/gpg" | sudo apt-key add -
```

（6）设置最新的稳定版仓库。可能要用最新的稳定版本替换最后一行的值。

```rust
$ add-apt-repository \
   "deb [arch=amd64] $DOCKER_EE_REPO/ubuntu \
   $(lsb_release -cs) \
   stable-17.06"
```

（7）运行 `apt-get update` ，从刚设置的Docker EE仓库中拉取最新包列表。

```rust
$ apt-get update
```

（8）卸载之前的Docker。

```rust
$ apt-get remove docker docker-engine docker-ce docker.io
```

（9）安装Docker EE。

```rust
$ apt-get install docker-ee -y
```

（10）检查安装是否成功。

```rust
$ docker --version
Docker version 17.06.2-ee-6, build e75fdb8
```

安装完成，可以启动Docker EE引擎了。

接下来安装UCP。

