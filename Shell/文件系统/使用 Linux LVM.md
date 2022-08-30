[toc]

### 1. 定义物理卷

创建过程的第一步就是将硬盘上的物理分区转换成 Linux LVM 使用的物理卷区段。可以使用 `fdisk` 命令在创建了基本的 Linux 分区之后，通过 `t` 命令改变分区类型。

```
[...] 
Command (m for help): t 
Selected partition 1 
Hex code (type L to list codes): 8e 
Changed system type of partition 1 to 8e (Linux LVM) 

Command (m for help): p 

Disk /dev/sdb: 5368 MB, 5368709120 bytes 
255 heads, 63 sectors/track, 652 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes 
Sector size (logical/physical): 512 bytes / 512 bytes 
I/O size (minimum/optimal): 512 bytes / 512 
bytes Disk identifier: 0xa8661341 

Device Boot 	Start 	End 	Blocks 		Id 	System 
/dev/sdb1 			1 	262 	2104483+	8e 	Linux LVM 

Command (m for help): w 
The partition table has been altered! 

Calling ioctl() to re- read partition table. 
Syncing disks. 
$
```

> 说明：如果下一步中的 `pvcreate` 命令不能正常工作，很可能是因为 LVM2 软件包没有默认安装。可以安装软件包名 lvm2 的软件。

下一步是用分区来创建实际的物理卷。这可以通过 `pvcreate` 命令来完成。`pvcreate` 定义了用于物理卷的物理分区。它只是简单地将分区标记成 Linux LVM 系统中的分区而已。

```shell
$ sudo pvcreate /dev/sdb1
dev_is_mpath: failed to get device for 8:17
Physical volume "/dev/sdb1" successfully created
```

> 说明：别被吓人的消息 `dev_is_mpath: failed to get device for 8:17` 或类似的消息唬住。只要看到了 successfully created 就没问题。`pvcreate` 命令会检查分区是否为多路设备。如果不是的话，就会发出上面那段消息。

如果你想查看创建进度的话，可以使用 `pvdisplay` 命令来显示已创建的物理卷列表：

```shell
$ sudo pvdisplay /dev/sdb1 
"/dev/sdb1" is a new physical volume of "2. 01 GiB"
--- NEW Physical volume ---
PV Name 		/dev/sdb1 
VG Name 
PV Size 		2. 01 GiB
Allocatable 	NO
PE Size 		0
Total PE 		0
Free PE 		0
Allocated PE 	0
PV UUID 		0FIuq2- LBod- IOWt- 8VeN- tglm- Q2ik- rGU2w7 
```

### 2. 创建卷组

要从命令行创建卷组，需要使用 `vgcreate` 命令。`vgcreate` 命令需要一些命令行参数来定义卷组名以及你用来创建卷组的物理卷名。

```shell
$ sudo vgcreate Vol1 /dev/sdb1
Volume group "Vol1" successfully created 
$
```

如果你想看看新创建的卷组的细节，可用 `vgdisplay` 命令：

```shell
$ sudo vgdisplay Vol1
--- Volume group ---
VG Name 				Vol1
System ID
Format 					lvm2
Metadata Areas 			1
Metadata Sequence No 	1
VG Access 				read/write
VG Status 				resizable
MAX LV 					0
Cur LV 					0
Open LV					0
Max PV 					0
Cur PV 					1
Act PV 					1
VG Size 				2.00 GiB
PE Size 				4.00 MiB
Total PE 				513
Alloc PE / Size 		0 / 0
Free PE / Size 			513 / 2.00 GiB
VG UUID 				oe4I7e-5RA9-G9ti-ANoI-QKLz-qkX4-58Wj6e
```

### 3. 创建逻辑卷

要创建逻辑卷，使用 `lvcreate` 命令。虽然你通常不需要在其他 Linux LVM 命令中使用命令行选项，但 `lvcreate` 命令要求至少输入一些选项。

<center><b>lvcreate 的选项</b></center>

| 选项 | 长选项名     | 描述                                                       |
| ---- | ------------ | ---------------------------------------------------------- |
| -c   | --chunksize  | 指定快照逻辑卷的单位大小                                   |
| -C   | --contiguous | 设置或重置连续分配策略                                     |
| -i   | --stripes    | 指定条带数                                                 |
| `-I` | --stripesize | 指定每个条带的大小                                         |
| -l   | --extents    | 指定分配给新逻辑卷的逻辑区段数，或者要用的逻辑区段的百分比 |
| -L   | --size       | 指定分配给新逻辑卷的硬盘大小                               |
|      | --minor      | 指定设备的次设备号                                         |
| -m   | --mirrors    | 创建逻辑卷镜像                                             |
| -M   | --persistent | 让次设备号一直有效                                         |
| -n   | --name       | 指定新逻辑卷的名称                                         |
| -p   | --permission | 为逻辑卷设置读/写权限                                      |
| -r   | --readahead  | 设置预读扇区数                                             |
| -R   | --regionsize | 指定将镜像分成多大的区                                     |
| -s   | --snapshot   | 创建快照逻辑卷                                             |
| -Z   | --zero       | 将新逻辑卷的前 1 KB 数据设置为零                           |

例如：

```shell
$ sudo lvcreate -l 100%FREE -n lvtest Vol1
Logical volume "lvtest" created
```

如果想查看你创建的逻辑卷的详细情况，可用 `lvdisplay` 命令。

```shell
$ sudo lvdisplay Vol1 
--- Logical volume --- 
LV Path 					/dev/Vol1/lvtest
LV Name 					lvtest
VG Name 					Vol1
LV UUID 					4W2369-pLXy-jWmb-lIFN-SMNX-xZnN-3KN208
LV Write Access 			read/write
LV Creation host, time ... 	-0400
LV Status 					available
# open 						0
LV Size 					2.00 GiB
Current LE 					513
Segments 					1
Allocation 					inherit
Read ahead sectors 			auto
- currently set to 			256
Block device 				253:2
```

你可以用 `-l` 选项来按可用空间的百分比来指定这个大小，或者用 `-L` 选项以字节、千字节（KB）、兆字节（MB）或吉字节（GB）为单位来指定实际的大小。`-n` 选项允许你为逻辑卷指定一个名称。

### 4. 创建文件系统

运行完 `lvcreate` 命令之后，逻辑卷就已经产生了，但它还没有文件系统。你必须使用相应的命令行程序来创建所需要的文件系统：

```shell
$ sudo mkfs. ext4 /dev/Vol1/lvtest
mke2fs 1.41.12 (17-May-2010)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
131376 inodes, 525312 blocks
26265 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=541065216
17 block groups
32768 blocks per group, 32768 fragments per group
7728 inodes per group

Superblock backups stored on blocks: 
		32768, 98304, 163840, 229376, 294912 

Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done

This filesystem will be automatically checked every 28 mounts or 180 days, whichever comes first. Use tune2fs -c or -i to override.
```

在创建了新的文件系统之后，可以用标准 Linux mount 命令将这个卷挂载到虚拟目录中，就跟它是物理分区一样。唯一的不同是你需要用特殊的路径来标识逻辑卷。

```shell
$ sudo mount /dev/Vol1/lvtest /mnt/my_ partition
$
$ mount /dev/mapper/vg_server01-lv_root on /type ext4 (rw)
[...]
/dev/mapper/Vol1-lvtest on /mnt/my_partition type ext4 (rw)
$
$ cd /mnt/my_ partition
$
$ ls -al
total 24
drwxr-xr-x. 	3 	root 	root 	4096 	Jun 12 10:22 	.
drwxr-xr-x. 	3 	root 	root 	4096 	Jun 11 09:58	..
drwx------. 	2 	root 	root 	16384 	Jun 12 10:22 lost+ found
```

### 5. 修改 LVM

Linux LVM 的好处在于能够动态修改文件系统，因此最好有工具能够让你实现这些操作。

<center><b>Linux LVM 命令</b></center>

| 命令     | 功能               |
| -------- | ------------------ |
| vgchange | 激活和禁用卷组     |
| vgremove | 删除卷组           |
| vgextend | 将物理卷加到卷组中 |
| vgreduce | 从卷组中删除物理卷 |
| lvextend | 增加逻辑卷的大小   |
| lvreduce | 减小逻辑卷的大小   |

> 提示：在手动增加或减小逻辑卷的大小时，要特别小心。逻辑卷中的文件系统需要手动修整来处理大小上的改变。大多数文件系统都包含了能够重新格式化文件系统的命令行程序，比如用于 ext2、ext3 和 ext4 文件系统的 resize2fs 程序。
