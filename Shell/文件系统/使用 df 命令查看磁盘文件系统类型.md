在终端中输入如下命令来查询当前磁盘挂载的是那个文件系统：

```shell
$ df -T -h
```

例如：

```shell
$ df -T -h
文件系统       类型      容量  已用  可用 已用% 挂载点
udev           devtmpfs  1.9G     0  1.9G    0% /dev
tmpfs          tmpfs     395M  6.1M  389M    2% /run
/dev/sda1      ext4       78G   17G   58G   23% /
tmpfs          tmpfs     2.0G  800K  2.0G    1% /dev/shm
tmpfs          tmpfs     5.0M  4.0K  5.0M    1% /run/lock
tmpfs          tmpfs     2.0G     0  2.0G    0% /sys/fs/cgroup
WorkSpaces     vboxsf    932G  425G  508G   46% /media/sf_WorkSpaces
tmpfs          tmpfs     395M  112K  395M    1% /run/user/1000
```

从上面的输出中，我们可以看出 `/dev/sda1` 磁盘的文件系统是 `ext4`。