### 7.7 增加并发控制后的globalmem驱动

在globalmem()的读写函数中，由于要调用copy_from_user()、copy_to_user()这些可能导致阻塞的函数，因此不能使用自旋锁，宜使用信号量。

驱动工程师习惯将某设备所使用的自旋锁、信号量等辅助手段也放在设备结构中，因此，可如代码清单7.4那样修改globalmem_dev结构体的定义，并在模块初始化函数中初始化这个信号量，如代码清单7.5所示。

代码清单7.4 增加并发控制后的globalmem设备结构体

1 struct globalmem_dev { 
 
 2 struct cdev cdev; /*cdev结构体*/ 
 
 3 unsigned char mem[GLOBALMEM_SIZE]; /*全局内存*/ 
 
 
 4 struct semaphore sem; /* 
 并发控制用的信号量 
 */ 
 
 5 };

代码清单7.5 增加并发控制后的globalmem设备驱动模块加载函数

1 int globalmem_init(void) 
 
 2 { 
 
 3 int result; 
 
 4 dev_t devno = MKDEV(globalmem_major, 0); 
 
 5 
 
 6 /* 申请设备号*/ 
 
 7 if (globalmem_major) 
 
 8 result = register_chrdev_region(devno, 1, "globalmem"); 
 
 9 else { /* 动态申请设备号 */ 
 
 10 result = alloc_chrdev_region(&devno, 0, 1, "globalmem"); 
 
 11 globalmem_major = MAJOR(devno); 
 
 12 } 
 
 13 if (result < 0) 
 
 14 return result; 
 
 15 
 
 16 /* 动态申请设备结构体的内存*/ 
 
 17 globalmem_devp = kmalloc(sizeof(struct globalmem_dev), GFP_KERNEL); 
 
 18 if (!globalmem_devp) { /*申请失败*/ 
 
 19 result = - ENOMEM; 
 
 20 goto fail_malloc; 
 
 21 } 
 
 22 memset(globalmem_devp, 0, sizeof(struct globalmem_dev)); 
 
 23 
 
 24 globalmem_setup_cdev(globalmem_devp, 0); 
 
 
 25 init_MUTEX(&globalmem_devp->sem); /* 
 初始化信号量 
 */



26 return 0; 
 
 27 
 
 28 fail_malloc: unregister_chrdev_region(devno, 1); 
 
 29 return result; 
 
 30 }

在访问globalmem_dev中的共享资源时，需先获取这个信号量，访问完成后，随即释放这个信号量。驱动中新的globalmem读、写操作如代码清单7.6所示。

代码清单7.6 增加并发控制后的globalmem读写操作

1 /*增加并发控制后的globalmem读函数*/ 
 
 2 static ssize_t globalmem_read(struct file *filp, char _ _user *buf, size_t size, 
 
 3 loff_t *ppos) 
 
 4 { 
 
 5 unsigned long p = *ppos; 
 
 6 unsigned int count = size; 
 
 7 int ret = 0; 
 
 8 struct globalmem_dev *dev = filp->private_data; /*获得设备结构体指针*/ 
 
 9 
 
 10 /*分析和获取有效的写长度*/ 
 
 11 if (p >= GLOBALMEM_SIZE) 
 
 12 return 0; 
 
 13 if (count > GLOBALMEM_SIZE - p) 
 
 14 count = GLOBALMEM_SIZE - p; 
 
 15 
 
 
 16 if (down_interruptible(&dev->sem)) /* 
 获得信号量 
 */ 
 
 17 return - ERESTARTSYS; 
 
 18 
 
 19 /*内核空间→用户空间*/ 
 
 20 if (copy_to_user(buf, (void*)(dev->mem + p), count)) { 
 
 21 ret = - EFAULT; 
 
 22 } else { 
 
 23 *ppos += count; 
 
 24 ret = count; 
 
 25 
 
 26 printk(KERN_INFO "read %d bytes(s) from %d\n", count, p); 
 
 27 } 
 
 
 28 up(&dev->sem); /* 
 释放信号量 
 */ 
 
 29 
 
 30 return ret; 
 
 31 } 
 
 32 
 
 33 /*增加并发控制后的globalmem写函数*/ 
 
 34 static ssize_t globalmem_write(struct file *filp, const char _ _user *buf, 
 
 35 size_t size, loff_t *ppos) 
 
 36 { 
 
 37 unsigned long p = *ppos; 
 
 38 unsigned int count = size; 
 
 39 int ret = 0; 
 
 40 struct globalmem_dev *dev = filp->private_data; /*获得设备结构体指针*/ 
 
 41 
 
 42 /*分析和获取有效的写长度*/ 
 
 43 if (p >= GLOBALMEM_SIZE) 
 
 44 return 0;



45 if (count > GLOBALMEM_SIZE - p) 
 
 46 count = GLOBALMEM_SIZE - p; 
 
 47 
 
 
 48 if (down_interruptible(&dev->sem)) /* 获得信号量 */ 
 
 49 return - ERESTARTSYS; 
 
 50 
 
 51 /*用户空间→内核空间*/ 
 
 52 if (copy_from_user(dev->mem + p, buf, count)) 
 
 53 ret = - EFAULT; 
 
 54 else { 
 
 55 *ppos += count; 
 
 56 ret = count; 
 
 57 
 
 58 printk(KERN_INFO "written %d bytes(s) from %d\n", count, p); 
 
 59 } 
 
 
 60 up(&dev->sem); /* 
 释放信号量 
 */ 
 
 61 return ret; 
 
 62 }

代码第16～17行和第49～50行用于获取信号量，如果down_interruptible()返回值非0，则意味着其在获得信号量之前已被打断，这时写函数返回-ERESTARTSYS。代码第28和60行用于在对临界资源访问结束后释放信号量。

除了globalmem的读写操作之外，如果在读写的同时，另一执行单元执行MEM_CLEAR IO控制命令，也会导致全局内存的混乱，因此，globalmem_ioctl()函数也需被重写，如代码清单7.7所示。

代码清单7.7 增加并发控制后的globalmem设备驱动ioctl()函数

1 static int globalmem_ioctl(struct inode *inodep, struct file *filp, unsigned 
 
 2 int cmd, unsigned long arg) 
 
 3 { 
 
 4 struct globalmem_dev *dev = filp->private_data; /*获得设备结构体指针*/ 
 
 5 
 
 6 switch (cmd) { 
 
 7 case MEM_CLEAR: 
 
 
 8 if (down_interruptible(&dev->sem)) /* 
 获得信号量 
 */ 
 
 9 return - ERESTARTSYS; 
 
 10 
 
 11 memset(dev->mem, 0, GLOBALMEM_SIZE); 
 
 
 12 up(&dev->sem); /* 
 释放信号量*/ 
 
 13 
 
 14 printk(KERN_INFO "globalmem is set to zero\n"); 
 
 15 break; 
 
 16 
 
 17 default: 
 
 18 return - EINVAL; 
 
 19 } 
 
 20 return 0; 
 
 21 }

增加并发控制后globalmem的完整驱动位于虚拟机的/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/drivers/globalmem/ch7目录，其使用方法与6.4节globalmem驱动在用户空间的验证一致。



