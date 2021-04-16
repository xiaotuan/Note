### 19.6.2 CramFS

在嵌入式Linux环境中，许多人会采用RAMDISK来储存文件系统的内容，RAMDISK的含义是在启动时，把一部份内存虚拟成磁盘，并且把之前准备好的文件系统映像文件解压缩到该RAMDISK环境中。假设压缩后的文件系统映像为8MB，存放于Flash，解压缩后为16MB，如果采用RAMDISK，将需要8MB的Flash和16MB的RAM空间，而采用CramFS后，就不再需要消耗16MB的RAM空间。

CramFS是Linus Torvalds参与开发的文件系统，在linux/fs/cramfs中可以找到CramFS的源代码。CramFS是一种压缩的只读文件系统，当浏览Flash中的目录或读取文件时，CramFS文件系统会动态地计算出压缩后的数据所储存的位置，并实时地解压缩到内存中，对于用户来说，使用CramFS与RAMDISK感觉不出使用上的差异性。

CramFS工具的下载地址为http://sourceforge.net/projects/cramfs/，通过如下命令可以创建CramFS文件系统映像：

mkcramfs my_cramfs/ cramfs.img （my_cramfs是我们要创建映像的目录）

如下命令将生成的cramfs.img映像复制到Flash的第一个分区并mount到/mnt/nor目录：

cp cramfs.img /dev/mtd1 
 
 mount -cramfs /dev/mtdblock1 /mnt/nor

很多时候，工程中需要基于已有的文件系统映像添加、删除一些文件后建立新的文件系统映像，这时候并不需要完全重新操作，可用如下的方法。

（1）将映像以loop方式挂载到某目录。

mkdir tmpdir 
 
 mount rootfs.cramfs tmpdir -o loop 
 
 cd tmpdir

（2）压缩被挂载的文件系统。

tar -cvf ../rootfs.tar ./ 将tmpdir中的内容打包放在其父目录下 
 
 umount tmpdir

（3）解压缩文件系统到新目录。

mkdir rootfs 
 
 tar -xvf rootfs.tar -C rootfs

（4）修改新目录（这里是rootfs）中的内容，以符合新的需要。

（5）重新创建映像文件。

mkcramfs rootfs rootfs.cramfs

