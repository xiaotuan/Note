## 3.1　Windows版Docker（DfW）

在了解Windows版Docker之前，读者首先要知道这是由Docker公司提供的一个产品。这意味着它易于下载，并且有一个很灵活的安装器（installer）。Windows版Docker需要运行在一个安装了64位Windows 10操作系统的计算机上，通过启动一个独立的引擎来提供Docker环境。

其次，读者需要知晓Windows版Docker是一个社区版本（Community Edition，CE）的应用，并不是为生产环境设计的。

最后，读者还需要知道Windows版Docker在某些版本特性上可能是延后支持的。这是因为Docker公司对该产品的定位是稳定性第一，新特性其次。

以上3点被添加到Windows版Docker这个安装快捷简单，但并不支持生产环境部署的产品当中。

闲话少说，接下来请读者跟随本书一起了解一下如何安装Windows版Docker。

在安装之前，Windows版Docker的环境有以下要求。

+ Windows 10 Pro / Enterprise / Education（1607 Anniversary Update、Build 14393或者更新的版本）。
+ Windows必须是64位的版本。
+ 需要启用Windows操作系统中的Hyper-V和容器特性。

接下来的步骤会假设读者的计算机已经开启了BIOS设置中的硬件虚拟化支持。如果没有开启，读者需要在机器上执行下面的步骤。

首先，读者需要确认在Windows 10操作系统中， **Hyper-V** 和 **容器** 特性已安装并且开启。

（1）右键单击Windows开始按钮并选择“应用和功能”页面。

（2）单击“程序和功能”链接。

（3）单击“启用或关闭Windows功能”。

（4）确认Hyper-V和容器复选框已经被勾选，并单击确定按钮。

按上述步骤操作完成后，会安装并开启Hyper-V和容器特性，如图3.1所示。读者需要重启操作系统。

<center class="my_markdown"><b class="my_markdown">图3.1　开启Hyper-V和容器特性</b></center>

其中，容器特性只有在summer 2016 Windows 10 Anniversary Update（build 14393）版本或更高版本上才能开启。

当读者完成Hyper-V和容器特性的安装并重启机器之后，就可以安装Windows版Docker了。

（1）访问Docker的下载页面，并单击其中的 `Download for Windows` 按钮。

（2）单击后会跳转到Docker商店，需要读者使用自己的Docker ID进行登录。

（3）单击任意 `Get Docker` 下载链接。Docker for Windows分为稳定版（Stable）和抢鲜版（Edge）。抢鲜版当中包含一些新特性，但是可能不够稳定。单击下载链接后，会将名为 `Docker for Windows Installer.exe` 的安装包下载到默认下载目录。

（4）找到上一步下载的安装包并运行即可。

以管理员身份运行安装向导，并按照提示一步一步完成整个安装过程。安装完成后Docker会作为系统服务自动启动，并且在Windows的通知栏看到Docker的大鲸鱼图标。

恭喜！到目前为止已经成功完成Windows版Docker的安装。

打开命令行或者PowerShell界面，并尝试执行下面的命令。

```rust
Client:
 Version:       18.01.0-ce
 API version:   1.35
 Go version:    go1.9.2
 Git commit:    03596f5
 Built: Wed Jan 10 20:05:55 2018
 OS/Arch:       windows/amd64
 Experimental:  false
 Orchestrator:  swarm
Server:
 Engine:
  Version:      18.01.0-ce
  API version:  1.35 (minimum version 1.12)
  Go version:   go1.9.2
  Git commit:   03596f5
  Built:        Wed Jan 10 20:13:12 2018
  OS/Arch:      linux/amd64
  Experimental: false
```

注意观察命令输出内容，其中 **Server** 部分中的 `OS/Arch` 属性展示了当前的操作系统是 `linux/amd64` 。这是因为在默认安装方式中，Docker daemon是运行在Hyper-V虚拟机中的一个轻量级Linux上的。这种情况下，读者只能在Windows版Docker上运行Linux容器。

如果读者想要运行原生Windows容器（Native Windows Container），可以右击Windows通知栏中的Docker鲸鱼图标，并选择“切换到Windows容器”。使用下面的命令也可以完成切换（进入 `\Program Files\Docker\Docker` 目录下执行）。

```rust
C:\Program Files\Docker\Docker> .\dockercli -SwitchDaemon
```

如果没有开启Windows容器特性，则会看到图3.2的提示。

![15.png](./images/15.png)
<center class="my_markdown"><b class="my_markdown">图3.2　没有开启Windows容器特性的提示</b></center>

如果已经开启了Windows容器特性，则只需要花费数秒就能完成切换。一旦切换完成，在命令行中执行 `docker version` 指令的输出内容如下。

```rust
C:\> docker version
Client:
 <Snip>
Server:
 Engine:
  Version:      18.01.0-ce
  API version:  1.35 (minimum version 1.24)
  Go version:   go1.9.2
  Git commit:   03596f5
  Built:        Wed Jan 10 20:20:36 2018
  OS/Arch:      windows/amd64
  Experimental: true
```

可以看到，现在Server版本信息变成了 `windows/amd64` 。这意味着Docker daemon运行在原生Windows内核上，并且只能运行Windows容器了。

同时也可以发现， `Experimental` 这个属性的值为 `true` 。这表示当前运行的Docker版本是实验版本。本章前面提到，Docker for Windows有两个版本：稳定版和抢鲜版。在本书编写的过程中，Windows容器是抢鲜版中的一个实验特性。

读者可以通过运行 `dockercli -Version` 命令来查看当前的Docker版本。 `dockercli` 命令在 `C:\Program Files\Docker\Docker` 目录下。

```rust
PS C:\Program Files\Docker\Docker> .\dockercli -Version
Docker for Windows
Version: 18.01.0-ce-win48 (15285)
Channel: edge
Sha1: ee2282129dec07b8c67890bd26865c8eccdea88e
OS Name: Windows 10 Pro
Windows Edition: Professional
Windows Build Number: 16299
```

下面展示了一些常用的能够正常执行的Docker命令。

```rust
> docker image ls
REPOSITORY    TAG      IMAGE ID     CREATED       SIZE
> docker container ls
CONTAINER ID   IMAGE   COMMAND   CREATED    STATUS   PORTS   NAMES
> docker system info
Containers: 1
 Running: 0
 Paused: 0
 Stopped: 1
Images: 6
Server Version: 17.12.0-ce
Storage Driver: windowsfilter
<Snip>
```

Windows版Docker包括Docker引擎（客户端和daemon）、Docker Compose、Docker Machine以及Docker Notary命令行。通过下列命令确认各个模块已经成功安装。

```rust
C:\> docker --version
Docker version 18.01.0-ce, build 03596f5
C:\> docker-compose --version
docker-compose version 1.18.0, build 8dd22a96
C:\> docker-machine --version
docker-machine.exe version 0.13.0, build 9ba6da9
C:\> notary version
notary
 Version:    0.4.3
 Git commit: 9211198
```

