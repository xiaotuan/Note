### 13.7.1 vmem_disk的硬件原理

vmem_disk是一种模拟磁盘，其数据实际上存储在RAM中。它使用通过vmalloc()分配出来的内存空间来模拟出一个磁盘，以块设备的方式来访问这片内存。该驱动是对字符设备驱动相应章节globalmem驱动的块方式改造。

在加载vmem_disk.ko后，使用默认模块参数的情况下，系统会增加4个块设备结点：

root@lihacker-laptop:~/develop/svn/ldd6410-read-only/training/kernel/drivers/vmem_d 
 
 isk# ls -l /dev/vmem_disk* 
 
 brw-rw---- 1 root disk 251, 0 2010-04-18 11:53 /dev/vmem_diska 
 
 brw-rw---- 1 root disk 251, 16 2010-04-18 11:52 /dev/vmem_diskb 
 
 brw-rw---- 1 root disk 251, 32 2010-04-18 11:52 /dev/vmem_diskc 
 
 brw-rw---- 1 root disk 251, 48 2010-04-18 11:52 /dev/vmem_diskd

其中，mkfs.ext2 /dev/vmem_diska命令的执行会回馈如下信息：



root@lihacker-laptop:~/develop/svn/ldd6410-read-only/training/kernel/drivers/vmem_d 
 
 isk# mkfs.ext2 /dev/vmem_diska 
 
 mke2fs 1.41.4 (27-Jan-2009) 
 
 Filesystem label= 
 
 OS type: Linux 
 
 Block size=1024 (log=0) 
 
 Fragment size=1024 (log=0) 
 
 64 inodes, 512 blocks 
 
 25 blocks (4.88%) reserved for the super user 
 
 First data block=1 
 
 Maximum filesystem blocks=524288 
 
 1 block group 
 
 8192 blocks per group, 8192 fragments per group 
 
 64 inodes per group

Writing inode tables: done 
 
 Writing superblocks and filesystem accounting information: done

This filesystem will be automatically checked every 36 mounts or 
 
 180 days, whichever comes first. Use tune2fs -c or -i to override.

它将/dev/vmem_diska格式化为EXT2文件系统。之后我们可以mount这个分区并在其中进行文件读写。

