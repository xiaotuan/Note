### B.2.1　使用systemctl重启

大多数现代Linux发行版都使用systemd来管理机器上的服务的启动。如果在命令行执行 `systemctl` ，获取好几页输出，那么宿主机就是在运行systemd。如果得到一个“command not found”消息，那么就进入B.2.2节。

如果想要更改配置，可以按如下方式停止和启动Docker：

```c
$ systemctl stop docker
$ systemctl start docker
```

也可以简单地重启：

```c
$ systemctl restart docker
```

通过下面这些命令来检查进度：

```c
$ journalctl -u docker
$ journalctl -u docker -f
```

这里的第一行会输出Docker守护进程的可用的日志，第二行输出任何新条目的日志。

