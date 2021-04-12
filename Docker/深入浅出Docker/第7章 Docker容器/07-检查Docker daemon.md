### 7.2.4　检查Docker daemon

通常登录Docker主机后的第一件事情是检查Docker是否正在运行。

```rust
$ docker version
Client:
 Version: API  17.05.0-ce
 version: Go   1.29
 version: Git  go1.7.5
 commit:       89658be
 Built:        Thu May 4 22:10:54 2017
 OS/Arch:      linux/amd64
Server:
 Version:      17.05.0-ce
 API version:  1.29 (minimum version 1.12)
 Go version:   go1.7.5
 Git commit:   89658be
 Built:        Thu May 4 22:10:54 2017
 OS/Arch:      linux/amd64
 Experimental: false
```

当命令输出中包含 `Client` 和 `Server` 的内容时，可以继续下面的示例。如果在 `Server` 部分中包含了错误码，这表示Docker daemon很可能没有运行，或者当前用户没有权限访问。

如果在Linux中遇到无权限访问的问题，需要确认当前用户是否属于本地Docker UNIX组。如果不是，可以通过 `usermod -aG docker <user>` 来添加，然后退出并重新登录Shell，改动即可生效。

如果当前用户已经属于本地 `docker` 用户组，那么问题可能是Docker daemon没有运行导致。根据Docker主机的操作系统在下面的内容中选择一条合适的命令，来检查Docker daemon的状态。

```rust
//使用Systemd在Linux系统中执行该命令
$ service docker status
docker start/running, process 29393
//使用Systemd在Linux系统中执行该命令
$ systemctl is-active docker
active
//在Windows Server 2016的PowerShell窗口中运行该命令
> Get-Service docker
Status    Name     DisplayName
------    ----     -----------
Running   Docker   docker
```

如果Docker daemon正在运行中，则可以继续下面的步骤。

