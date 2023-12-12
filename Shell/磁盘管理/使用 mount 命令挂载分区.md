磁盘挂载命令为 `mount`，命令格式如下：

```shell
mount [参数] -t [类型] [设备名称] [目的文件夹]
```

主要参数如下：

+ `-V`：显示程序版本。
+ `-h`：显示辅助信息。
+ `-v`：显示执行过程详细信息。
+ `-o ro`：只读模式挂载。
+ `-o rw`：读写模式挂载
+ `-s-r`：等于 `-o ro`。
+ `-w`: 等于 `-o rw`。

挂载点是一个文件夹，因此在挂载之前先要创建一个文件夹，一般我们把挂载点放到 `/mnt` 目录下，在 `/mnt` 下创建一个 `tmp` 文件夹，然后将 U 盘的 `/dev/sdb1` 分区挂载到 `/mnt/tmp` 文件夹里面：

```shell
xiaotuan@xiaotuan:~$ ls /mnt
xiaotuan@xiaotuan:~$ sudo mkdir /mnt/tmp
[sudo] xiaotuan 的密码： 
xiaotuan@xiaotuan:~$ ls /mnt
tmp
xiaotuan@xiaotuan:~$ sudo mount -t vfat /dev/sdb1 /mnt/tmp
```

