### 9.4.4 AIO与设备驱动

在内核中，每个I/O请求都对应于一个kiocb结构体，其ki_filp成员指向对应的file指针，通过is_sync_kiocb()可以判断某kiocb是否为同步I/O请求，如果返回非真，表示为异步I/O请求。

块设备和网络设备本身是异步的，只有字符设备必须明确表明应支持AIO。AIO对于大多数字符设备而言都不是必须的，只有极少数设备需要。比如，对于磁带机，由于I/O操作很慢，这时候使用异步I/O将可改善性能。

字符设备驱动程序中，file_operations包含3个与AIO相关的成员函数：

ssize_t (*aio_read) (struct kiocb *iocb, char *buffer, 
 
 size_t count, loff_t offset); 
 
 ssize_t (*aio_write) (struct kiocb *iocb, const char *buffer, 
 
 size_t count, loff_t offset); 
 
 int (*aio_fsync) (struct kiocb *iocb, int datasync);

aio_read()和aio_write()与file_operations中的read()和write()中的offset参数不同，它直接传递值，而后者传递的是指针，这是因为AIO从来不需要改变文件的位置。

aio_read()和aio_write()函数本身不一定完成了读和写操作，它只是发起、初始化读和写操作，代码清单9.17给出了驱动程序中aio_read()和aio_write()函数的实现例子。

代码清单9.17 设备驱动中的异步I/O函数

1 struct async_work { 
 
 2 struct kiocb *iocb; /* kiocb结构体指针*/ 
 
 3 int result; /*执行结果 */ 
 
 4 struct work_struct work; /* 工作结构体 */ 
 
 5 }; 
 
 6 ... 
 
 7 /*异步读*/ 
 
 8 static ssize_t xxx_aio_read(struct kiocb *iocb, char *buf, size_t count, loff_t 
 
 9 pos) 
 
 10 { 
 
 11 return xxx_defer_op(0, iocb, buf, count, pos); 
 
 12 } 
 
 13 
 
 14 /*异步写*/ 
 
 15 static ssize_t xxx_aio_write(struct kiocb *iocb, const char *buf, size_t count, 
 
 16 loff_t pos) 
 
 17 { 
 
 18 return xxx_defer_op(1, iocb, (char*)buf, count, pos); 
 
 19 } 
 
 20 
 
 21 /*初始化异步I/O*/ 
 
 22 static int xxx_defer_op(int write, struct kiocb *iocb, char *buf, size_t count, 
 
 23 loff_t pos) 
 
 24 { 
 
 25 struct async_work *async_wk; 
 
 26 int result; 
 
 27 /* 当我们能访问buffer时进行copy */ 
 
 28 if (write) 
 
 29 result = xxx_write(iocb->ki_filp, buf, count, &pos); 
 
 30 else 
 
 31 result = xxx_read(iocb->ki_filp, buf, count, &pos); 
 
 32 /* 如果是同步IOCB，立即返回状态 */ 
 
 33 if (is_sync_kiocb(iocb)) 
 
 34 return result; 
 
 35 
 
 36 /* 否则，推后几微秒执行 */



37 async_wk = kmalloc(sizeof(*async_wk), GFP_KERNEL); 
 
 38 if (async_wk == NULL) 
 
 39 return result; 
 
 40 /*调度延迟的工作*/ 
 
 41 async_wk->iocb = iocb; 
 
 42 async_wk->result = result; 
 
 
 43 INIT_WORK(&async_wk->work, xxx_do_deferred_op, async_wk); 
 
 
 44 schedule_delayed_work(&async_wk->work, Hz / 100); 
 
 45 return - EIOCBQUEUED; /*控制权返回用户空间*/ 
 
 46 } 
 
 47 
 
 48 /*延迟后执行*/ 
 
 49 static void xxx_do_deferred_op(void *p) 
 
 50 { 
 
 51 struct async_work *async_wk = (struct async_work*)p; 
 
 52 ... /* 执行I/O操作 */ 
 
 
 53 aio_complete(async_wk->iocb, async_wk->result, 0); 
 
 54 kfree(async_wk); 
 
 55 }

上述代码中最核心的是使用work_struct机制通过schedule_delayed_work()函数将I/O操作延后执行，而在具体的I/O操作执行完成后，53行调用aio_complete()通知内核驱动程序已经完成了I/O操作。

通常而言，具体的字符设备驱动一般不需要实现AIO支持，而内核中仅有fs/direct-io.c，drivers/usb/gadget/inode.c、fs/nfs/direct.c等少量地方使用了AIO。

