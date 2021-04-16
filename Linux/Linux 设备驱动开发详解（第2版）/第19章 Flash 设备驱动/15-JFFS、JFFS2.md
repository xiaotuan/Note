### 19.6.3 JFFS/JFFS2

JFFS是由瑞典Axis Communications AB公司开发的，于1999年末基于GNU GPL发布的文件系统。最初的发布版本基于Linux 2.0，后来Red Hat将它移植到Linux 2.2，在使用的过程中，JFFS设计中的局限被不断地暴露出来。于是在2001年初，Red Hat决定实现一个新的JFFS2 （http:/*www.infradead.org）。

JFFS2是一个日志结构（log-structured）的文件系统，它在闪存上顺序地存储包含数据和原数据（meta-data）的节点。JFFS2的日志结构存储方式使得它能对闪存进行out-of-place更新，而不是磁盘所采用的in-place更新方式。它提供的垃圾回收机制，使得我们不需要马上对擦写越界的块进行擦写，而只需要对其设置一个标志，标明为“脏”块。当可用的块数不足时，垃圾回收机制才开始回收这些节点。同时，由于JFFS2基于日志结构，在意外掉电后仍然可以保持数据的完整性，而不会丢失数据。因此，JFFS2成为了目前Flash上应用最广泛的文件系统。

然而，JFFS2挂载时需要扫描整块Flash以确定节点的合法性以及建立必要的数据结构，这使得JFFS2挂载时间比较长。又由于JFFS2将节点信息保存在内存中，使得它所占用的内存量和节点数目成正比。再者，由于JFFS2通过随机方式来实现磨损平衡，它不能保证磨损平衡的确定性。因此，人们提出了JFFS3，它就是为解决JFFS2的这些缺陷而设计的。

和CramFS一样，也存在一个制作JFFS2文件系统的工具mkfs.jffs2（包含在mtd-utils中），执行如下命令即可生成所要的映象：

./mkfs.jffs2 -d my_jffs2/ -o jffs2.img （my_jffs2是我们要制作映像的目录）

使用mkfs.jffs2制作映像的时候，要注意指定正确的擦除块大小和页面大小，对于NAND Flash，应使用“-n”去掉生成映像中的clean marker。

接下来将jffs2.img复制到Flash第1个分区（复制到MTD字符设备），如下所示：

cp jffs2.img /dev/mtd1

之后，就可以将对应的块设备mount到Linux的目录了，如下所示：

mount -t jffs2 /dev/mtdblock1 /mnt/nor

对于NAND Flash，应使用mtd-utils中的nandwrite工具进行jffs2映像向NAND Flash的烧录，在烧录前可以使用flash_eraseall擦除Flash，并在OOB区域加上JFFS2需要的clean marker。

LDD6410开发板的文件系统中已包含mtd-utils系列工具。mtd-utils的当前最新版本为1.3.1，其下载地址为：ftp:/*ftp.infradead.org/pub/mtd-utils/mtd-utils-1.3.1.tar.bz2。

