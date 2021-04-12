### 3.5.1　在Ubuntu 16.04上升级Docker CE

本书假设读者已经完成了全部的升级前置步骤并且Docker处于可以升级的状态，同时还可以用root用户身份运行升级命令。以root用户运行升级命令是 **不推荐** 的，但是可以简化本书中的示例。如果读者不采用root用户运行升级命令，那最好不过了！那么需要通过 `sudo` 来执行下列指令。

（1）更新APT包列表。

```rust
$ apt-get update
```

（2）卸载当前Docker。

```rust
$ apt-get remove docker docker-engine docker-ce docker.io -y
```

在之前的版本中，Docker引擎的包名可能有多个。这条命令能够确保已经安装的Docker包全部被删除。

（3）安装新版本Docker。

有不同版本的Docker可供选择，并且有多种方式可以安装Docker。无论是Docker CE还是Docker EE，都有不止一种安装方式。例如，Docker CE可以通过apt或者deb包管理方式进行安装，也可以使用Docker官网上的脚本。

接下来的命令会使用get.docker.com的脚本完成最新版本Docker CE的安装和配置。

```rust
$ wget -qO- https://get.docker.com/ | sh
```

（4）将Docker配置为开机自启动。

```rust
$ systemctl enable docker
Synchronizing state of docker.service...
Executing /lib/systemd/systemd-sysv-install enable docker
$ systemctl is-enabled docker
enabled
```

此时读者可能想重启自己的节点。这样可以确保刚安装的Docker不会对系统开机有任何的影响。

（5）检查并确保每一个容器和服务都已经重启成功。

```rust
$ docker container ls
CONTAINER ID    IMAGE     COMMAND       CREATED           STATUS
97e599aca9f5    alpine    "sleep 1d"    14 minutes ago    Up 1 minute
$ docker service ls
ID              NAME          MODE         REPLICAS     IMAGE
ibyotlt1ehjy    prod-equus1   replicated   1/1          alpine:latest
```

请注意，更新Docker还有其他的方法。本书只是介绍了基于Ubuntu Linux 16.04 版本的方式。

