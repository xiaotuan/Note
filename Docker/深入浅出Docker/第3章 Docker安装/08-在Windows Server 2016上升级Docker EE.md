### 3.5.2　在Windows Server 2016上升级Docker EE

在本节中，会向读者一步一步介绍如何在Windows上将Docker 1.12.2版本升级到最新版本的Docker EE。

假设读者已经完成了全部的准备工作，比如为容器配置了正确的重启策略，如果运行有Swarm服务，则需要将待升级Swarm节点设置为drain状态。

本例中全部命令都应当通过PowerShell终端执行。

（1）检查当前Docker版本。

```rust
> docker version
Client:
 Version:     1.12.2-cs2-ws-beta
<Snip>
Server:
 Version:     1.12.2-cs2-ws-beta
```

（2）卸载本机上可能存在的由微软公司提供的旧版本Docker，并从Docker官方获取最新版本进行安装。

```rust
> Uninstall-Module DockerMsftProvider -Force
> Install-Module DockerProvider -Force
```

（3）更新Docker包。

下面的命令会强制更新（无须卸载操作）Docker，并设置为开机自启动。

```rust
> Install-Package -Name docker -ProviderName DockerProvider -Update -Force
Name      Version          Source       Summary
----      -------          ------       -------
Docker    17.06.2-ee-6     Docker       Docker for Windows Server 2016
```

现在读者可能想重启自己的节点，以确保刚安装的Docker不会对系统开机有任何的影响。

（4）检查并确保每一个容器和服务都已经重启成功。

