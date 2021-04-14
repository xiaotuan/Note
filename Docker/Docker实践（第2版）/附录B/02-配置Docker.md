### B.1　配置Docker

大多数主流发行版的配置文件的位置列在表B-1中。

<center class="my_markdown"><b class="my_markdown">表B-1　Docker配置文件位置</b></center>

| 发 行 版 | 配 置 文 件 |
| :-----  | :-----  | :-----  | :-----  |
| Ubuntu/Debian/Gentoo | /etc/default/docker |
| OpenSuse/CentOS/Red Hat | /etc/sysconfg/docker |

注意，有一些发行版把配置作为单个文件，而另外一些发行版使用一个目录或者多个文件。例如，在Red Hat企业版证书中，有一个叫/etc/sysconfig/docker/docker-storage的文件，习惯上它包含与Docker守护进程的存储选项有关的配置。

如果读者所用的发行版没有和表B-1中的名字匹配的任何文件，那么值得检查一下/etc/docker文件夹，因为那里可能有相关的文件。

在这些文件中，管理着传递给Docker守护进程启动命令的相关参数。例如，编辑的时候，下面这样的命令允许为宿主机上的Docker守护进程设置启动参数：

```c
DOCKER_OPTS=""
```

例如，如果想把Docker根目录从默认的位置（/var/lib/docker）改到别的地方，用户可能会把之前的那条改成：

```c
DOCKER_OPTS="-g /mnt/bigdisk/docker"
```

如果所用的发行版使用systemd配置文件（和/etc不同），那么还可以查找systemd文件夹下的docker文件中的 `ExecStart` 这一行，想要修改的话也可以修改。这个文件可能位于/usr/lib/systemd/system/service/docker或者/lib/systemd/system/docker.service。下面是一个示例文件：

```c
[Unit]
Description=Docker Application Container Engine
Documentation=http://docs.docker.io
After=network.target
[Service]
Type=notify
EnvironmentFile=-/etc/sysconfig/docker
ExecStart=/usr/bin/docker -d --selinux-enabled
Restart=on-failure
LimitNOFILE=1048576
LimitNPROC=1048576
[Install]
WantedBy=multi-user.target
```

`EnvironmentFile` 这一行把启动脚本指向了我们之前讨论过的有 `DOCKER_OPTS` 这项的文件。如果直接修改systemctl文件，需要执行 `systemctl daemon-reload` 命令，以便确保systemd守护进程采用了这个修改。

