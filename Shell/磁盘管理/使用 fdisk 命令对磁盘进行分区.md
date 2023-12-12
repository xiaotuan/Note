如果要对某个磁盘进行分区，可以使用命令 `fdisk` 命令，其格式如下：

```shell
fdisk [参数]
```

主要参数如下：

+ `-b <分区大小>`：指定每个分区的大小。
+ `-l`：列出指定设备的分区表。
+ `-s <分区编号>`：将指定的分区大小输出到标准输出上，单位为块。
+ `-u`：搭配 `-l` 参数，会用分区数目取代柱面数目，来表示每个分区的起始地址。

> 警告：千万不要对自己装 Ubuntu 系统进行分区！！

例如：

```shell
xiaotuan@xiaotuan:~$ sudo fdisk /dev/sdb
[sudo] xiaotuan 的密码： 

Welcome to fdisk (util-linux 2.27.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


命令(输入 m 获取帮助)： m

Help:

  Generic
   d   delete a partition
   F   list free unpartitioned space
   l   list known partition types
   n   add a new partition
   p   print the partition table
   t   change a partition type
   v   verify the partition table
   i   print information about a partition

  Misc
   m   print this menu
   x   extra functionality (experts only)

  Script
   I   load disk layout from sfdisk script file
   O   dump disk layout to sfdisk script file

  Save & Exit
   w   write table to disk and exit
   q   quit without saving changes

  Create a new label
   g   create a new empty GPT partition table
   G   create a new empty SGI (IRIX) partition table
   o   create a new empty DOS partition table
   s   create a new empty Sun partition table


命令(输入 m 获取帮助)： 
```

常用的命令如下：

+ `p`：显式现有的分区
+ `n`：建立新分区
+ `t`：更改分区类型
+ `d`：删除现有的分区
+ `a`：更改分区启动标志
+ `w`：对分区的更改写入到硬盘或者存储器中。
+ `q`：不保存退出

