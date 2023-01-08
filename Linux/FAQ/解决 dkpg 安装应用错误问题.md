[toc]

### 1. 解决安装应用报 dpkg: 错误: 另外一个进程已经为 dpkg frontend 加锁 错误问题

执行下面命令解决 `dpkg: 错误: 另外一个进程已经为 dpkg frontend 加锁` 报错问题：

```shell
$ sudo rm /var/lib/dpkg/lock-frontend
```

### 2. 解决安装应用报 dpkg: 错误: 另外一个进程已经为 dpkg 状态数据库 加锁 错误问题

执行下面命令解决 `dpkg: 错误: 另外一个进程已经为 dpkg 状态数据库 加锁` 报错问题：

```shell
$ sudo rm /var/lib/dpkg/lock
```

