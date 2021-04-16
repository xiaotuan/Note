### 13.5 块设备驱动的ioctl函数

与字符设备驱动一样，块设备可以包含一个ioctl()函数以提供对设备的I/O控制能力。实际上，高层的块设备层代码处理了绝大多数I/O控制，如BLKFLSBUF、BLKROSET、BLKDISCARD、HDIO_GETGEO、BLKROGET、BLKSECTGET等，因此，具体的块设备驱动中通常只需要实现设备相关的ioctl命令。例如，源代码文件为drivers/block/floppy.c中实现了与软驱相关的命令如FDEJECT、FDSETPRM、FDFMTTRK等。



