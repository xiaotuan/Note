### 6.1.3 file_operations结构体

file_operations结构体中的成员函数是字符设备驱动程序设计的主体内容，这些函数实际会在应用程序进行Linux的open()、write()、read()、close()等系统调用时最终被调用。file_operations结构体目前已经比较庞大，它的定义如代码清单6.4所示。

代码清单6.4 file_operations结构体

1 struct file_operations { 
 
 2 struct module *owner; 
 
 3 /* 拥有该结构的模块的指针，一般为THIS_MODULES */ 
 
 4 loff_t(*llseek)(struct file *, loff_t, int); 
 
 5 /* 用来修改文件当前的读写位置 */ 
 
 6 ssize_t(*read)(struct file *, char _ _user *, size_t, loff_t*); 
 
 7 /* 从设备中同步读取数据 */ 
 
 8 ssize_t(*write)(struct file *, const char _ _user *, size_t, loff_t*); 
 
 9 /* 向设备发送数据*/ 
 
 10 ssize_t(*aio_read)(struct kiocb *, char _ _user *, size_t, loff_t); 
 
 11 /* 初始化一个异步的读取操作*/ 
 
 12 ssize_t(*aio_write)(struct kiocb *, const char _ _user *, size_t, loff_t); 
 
 13 /* 初始化一个异步的写入操作*/ 
 
 14 int(*readdir)(struct file *, void *, filldir_t); 
 
 15 /* 仅用于读取目录，对于设备文件，该字段为 NULL */



16 unsigned int(*poll)(struct file *, struct poll_table_struct*); 
 
 17 /* 轮询函数，判断目前是否可以进行非阻塞的读取或写入*/ 
 
 18 int(*ioctl)(struct inode *, struct file *, unsigned int, unsigned long); 
 
 19 /* 执行设备I/O控制命令*/ 
 
 20 long(*unlocked_ioctl)(struct file *, unsigned int, unsigned long); 
 
 21 /* 不使用BLK的文件系统，将使用此种函数指针代替ioctl */ 
 
 22 long(*compat_ioctl)(struct file *, unsigned int, unsigned long); 
 
 23 /* 在64位系统上，32位的ioctl调用，将使用此函数指针代替*/ 
 
 24 int(*mmap)(struct file *, struct vm_area_struct*); 
 
 25 /* 用于请求将设备内存映射到进程地址空间*/ 
 
 26 int(*open)(struct inode *, struct file*); 
 
 27 /* 打开 */ 
 
 28 int(*flush)(struct file*); 
 
 29 int(*release)(struct inode *, struct file*); 
 
 30 /* 关闭*/ 
 
 31 int (*fsync) (struct file *, struct dentry *, int datasync); 
 
 32 /* 刷新待处理的数据*/ 
 
 33 int(*aio_fsync)(struct kiocb *, int datasync); 
 
 34 /* 异步fsync */ 
 
 35 int(*fasync)(int, struct file *, int); 
 
 36 /* 通知设备FASYNC标志发生变化*/ 
 
 37 int(*lock)(struct file *, int, struct file_lock*); 
 
 38 ssize_t(*sendpage)(struct file *, struct page *, int, size_t, loff_t *, int); 
 
 39 /* 通常为NULL */ 
 
 40 unsigned long(*get_unmapped_area)(struct file *,unsigned long, unsigned long, 
 
 41 unsigned long, unsigned long); 
 
 42 /* 在当前进程地址空间找到一个未映射的内存段 */ 
 
 43 int(*check_flags)(int); 
 
 44 /* 允许模块检查传递给fcntl(F_SETEL...)调用的标志 */ 
 
 45 int(*dir_notify)(struct file *filp, unsigned long arg); 
 
 46 /* 对文件系统有效，驱动程序不必实现*/ 
 
 47 int(*flock)(struct file *, int, struct file_lock*); 
 
 48 ssize_t (*splice_write)(struct pipe_inode_info *, struct file *, loff_t *, size_t, 
 
 49 unsigned int); /* 由VFS调用，将管道数据粘接到文件 */ 
 
 50 ssize_t (*splice_read)(struct file *, loff_t *, struct pipe_inode_info *, size_t, 
 
 51 unsigned int); /* 由VFS调用，将文件数据粘接到管道 */ 
 
 52 int (*setlease)(struct file *, long, struct file_lock **); 
 
 53 };

下面我们对file_operations结构体中的主要成员进行分析。

llseek()函数用来修改一个文件的当前读写位置，并将新位置返回，在出错时，这个函数返回一个负值。

read()函数用来从设备中读取数据，成功时函数返回读取的字节数，出错时返回一个负值。

write()函数向设备发送数据，成功时该函数返回写入的字节数。如果此函数未被实现，当用户进行write()系统调用时，将得到-EINVAL返回值。

readdir()函数仅用于目录，设备节点不需要实现它。

ioctl()提供设备相关控制命令的实现（既不是读操作也不是写操作），当调用成功时，返回给调用程序一个非负值。

mmap()函数将设备内存映射到进程内存中，如果设备驱动未实现此函数，用户进行mmap()系统调用时将获得-ENODEV返回值。这个函数对于帧缓冲等设备特别有意义。

当用户空间调用Linux API函数open()打开设备文件时，设备驱动的open()函数最终被调用。驱动程序可以不实现这个函数，在这种情况下，设备的打开操作永远成功。与open()函数对应的是release()函数。

poll()函数一般用于询问设备是否可被非阻塞地立即读写。当询问的条件未触发时，用户空间进行select()和poll()系统调用将引起进程的阻塞。

aio_read()和aio_write()函数分别对与文件描述符对应的设备进行异步读、写操作。设备实现这两个函数后，用户空间可以对该设备文件描述符调用aio_read()、aio_write()等系统调用进行读写。

