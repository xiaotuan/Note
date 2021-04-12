## 7.1　Docker容器——简介

容器是镜像的运行时实例。正如从虚拟机模板上启动VM一样，用户也同样可以从单个镜像上启动一个或多个容器。虚拟机和容器最大的区别是容器更快并且更轻量级——与虚拟机运行在完整的操作系统之上相比，容器会共享其所在主机的操作系统/内核。

图7.1为使用单个Docker镜像启动多个容器的示意图。

![32.png](./images/32.png)
<center class="my_markdown"><b class="my_markdown">图7.1　使用单个Docker镜像启动多个容器</b></center>

启动容器的简便方式是使用 `docker container run` 命令。该命令可以携带很多参数，在其基础的格式 `docker container run <image> <app>` 中，指定了启动所需的镜像以及要运行的应用。 `docker container run -it ubuntu /bin/bash` 则会启动某个Ubuntu Linux容器，并运行Bash Shell作为其应用；如果想启动PowerShell并运行一个应用，则可以使用命令 `docker container run -it microsoft- /powershell:nanoserver pwsh.exe` 。

`-it` 参数可以将当前终端连接到容器的Shell终端之上。

容器随着其中运行应用的退出而终止。在上面两个示例中，Linux容器会在Bash Shell退出后终止，而Windows容器会在PowerShell进程终止后退出。

一个简单的验证方法就是启动新的容器，并运行 `sleep` 命令休眠10s。容器会启动，然后运行休眠命令，在10s后退出。如果读者在Linux主机（或者在Linux容器模式下的Windows主机上）运行 `docker container run alpine:latest sleep 10` 命令，Shell会连接到容器Shell 10s的时间，然后退出；读者可以在Windows容器上运行 `docker container run microsoft/powershell:nanoserver Start-Sleep -s 10` 来验证这一点。

读者可以使用 `docker container stop` 命令手动停止容器运行，并且使用 `docker container start` 再次启动该容器。如果再也不需要该容器，则使用 `docker container rm` 命令来删除容器。

以上仅仅是“电梯游说”！接下来一起了解更多细节。

