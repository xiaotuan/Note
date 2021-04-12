## 3.4　在Windows Server 2016上安装Docker

本小节主要介绍在Windows Servre 2016上安装Docker的方法。主要包括以下步骤。

（1）安装Windows容器功能（Windows Container Feature）。

（2）安装Docker。

（3）确认安装成功。

在开始安装之前，读者需要确保操作系统已经更新了最新版本的包以及安全补丁。读者可以通过运行 `sconfig` 命令，并选择选项6来快速完成更新的安装。安装更新可能需要重启系统。

接下来本书会在没有安装容器功能（Container Feature）或者已经安装了老版本Docker的Windows Server 2016上进行演示。

确保容器特性已经安装并且启用。

（1）鼠标右击Windows开始按钮，选择“应用和功能”，接下来会打开“应用和功能”面板。

（2）单击“启用或关闭Windows功能”，接下来会打开“服务器管理器”。

（3）确认面板处于选中状态，然后选择“添加角色和功能”。

（4）根据向导提示执行，直到进入“功能”页面。

（5）确保“容器”功能已经勾选，然后单击向导的“完成”按钮。完成之后需要重启操作系统。

现在已经完成Windows容器功能的安装，接下来可以安装Docker了。本书中采用PowerShell完成安装。

（1）以管理员身份运行PowerShell。

（2）运行下面的命令来安装Docker包管理工具。

```rust
> Install-Module DockerProvider -Force
```

如果出现提示，单击允许（Accept）按钮完成NuGet provider的安装。

（3）安装Docker。

```rust
> Install-Package Docker -ProviderName DockerProvider -Force
```

一旦安装完成，读者可以看到下面的内容。

```rust
Name      Version         Source    Summary
----      -------         ------    -------
Docker    17.06.2-ee-6    Docker    Docker for Windows Server 2016
```

现在Docker已经完成安装，并且设置为开机自启动。

（4）读者可能希望重启系统来确认Docker的安装没有对系统启动造成任何影响。此外在重启之后，可以检查Docker是否自动启动。

Docker现在已经安装成功，读者可以开始部署容器了。下面的命令是确认Docker安装成功的方法。

```rust
> docker --version
Docker version 17.06.2-ee-6, build e75fdb8
> docker system info
Containers: 0
 Running: 0
 Paused: 0
 Stopped: 0
Images: 0
Server Version: 17.06.2-ee-6
Storage Driver: windowsfilter
<Snip>
```

Docker现在已经完成安装，读者可以开始运行Windows容器了。

