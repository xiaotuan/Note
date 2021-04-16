### 9.3.1 在globalfifo驱动中增加异步通知

首先，参照代码清单9.2，应该将异步结构体指针添加到globalfifo_dev设备结构体内，如代码清单9.7所示。

代码清单9.7 增加异步通知后的globalfifo设备结构体

1 struct globalfifo_dev { 
 
 2 struct cdev cdev; /*cdev结构体*/ 
 
 3 unsigned int current_len; /*fifo有效数据长度*/ 
 
 4 unsigned char mem[GLOBALFIFO_SIZE]; /*全局内存*/ 
 
 5 struct semaphore sem; /*并发控制用的信号量*/ 
 
 6 wait_queue_head_t r_wait; /*阻塞读用的等待队列头*/ 
 
 7 wait_queue_head_t w_wait; /*阻塞写用的等待队列头*/ 
 
 
 8 struct fasync_struct *async_queue; /* 异步结构体指针，用于读 
 */ 
 
 9 };

参考代码清单9.3的fasync()函数模板，globalfifo的这个函数如代码清单9.8。

代码清单9.8 支持异步通知的globalfifo设备驱动fasync()函数

1 static int globalfifo_fasync(int fd, struct file *filp, int mode) 
 
 2 { 
 
 3 struct globalfifo_dev *dev = filp->private_data; 
 
 
 4 return fasync_helper(fd, filp, mode, &dev->async_queue); 
 
 5 }

在globalfifo设备被正确写入之后，它变得可读，这个时候驱动应释放SIGIO信号以便应用程序捕获，代码清单9.9给出了支持异步通知的globalfifo设备驱动的写函数。

代码清单9.9 支持异步通知的globalfifo设备驱动写函数

1 static ssize_t globalfifo_write(struct file *filp, const char __user *buf, 
 
 2 size_t count, loff_t *ppos) 
 
 3 { 
 
 4 struct globalfifo_dev *dev = filp->private_data; /* 获得设备结构体指针 */ 
 
 5 int ret; 
 
 6 DECLARE_WAITQUEUE(wait, current); /*定义等待队列*/ 
 
 7 
 
 8 down(&dev->sem); /*获取信号量*/ 
 
 9 add_wait_queue(&dev->w_wait, &wait); /*进入写等待队列头*/ 
 
 10 
 
 11 /* 等待FIFO非满 */ 
 
 12 if (dev->current_len == GLOBALFIFO_SIZE) { 
 
 13 if (filp->f_flags &O_NONBLOCK) { /* 如果是非阻塞访问 */ 
 
 14 ret = - EAGAIN; 
 
 15 goto out; 
 
 16 } 
 
 17 _ _set_current_state(TASK_INTERRUPTIBLE); /*改变进程状态为睡眠*/ 
 
 18 up(&dev->sem); 
 
 19 
 
 20 schedule(); /*调度其他进程执行*/ 
 
 21 if (signal_pending(current)) { /* 如果是因为信号唤醒 */ 
 
 22 ret = - ERESTARTSYS; 
 
 23 goto out2; 
 
 24 } 
 
 25 
 
 26 down(&dev->sem); /*获得信号量*/ 
 
 27 } 
 
 28 
 
 29 /*从用户空间拷贝到内核空间*/ 
 
 30 if (count > GLOBALFIFO_SIZE - dev->current_len) 
 
 31 count = GLOBALFIFO_SIZE - dev->current_len; 
 
 32 
 
 33 if (copy_from_user(dev->mem + dev->current_len, buf, count)) { 
 
 34 ret = - EFAULT; 
 
 35 goto out; 
 
 36 } else { 
 
 37 dev->current_len += count; 
 
 38 printk(KERN_INFO "written %d bytes(s),current_len:%d\n", count, dev 
 
 39 ->current_len); 
 
 40 
 
 41 wake_up_interruptible(&dev->r_wait); /*唤醒读等待队列*/



42 /* 产生异步读信号 */ 
 
 43 if (dev->async_queue) 
 
 
 44 kill_fasync(&dev->async_queue, SIGIO, POLL_IN); 
 
 45 
 
 46 ret = count; 
 
 47 } 
 
 48 
 
 49 out: up(&dev->sem); /* 释放信号量 */ 
 
 50 out2:remove_wait_queue(&dev->w_wait, &wait); 
 
 51 set_current_state(TASK_RUNNING); 
 
 52 return ret; 
 
 53 }

参考代码清单9.6，增加异步通知后的globalfifo设备驱动的release()函数中需调用globalfifo_fasync()函数将文件从异步通知列表中删除，代码清单9.10给出了支持异步通知的globalfifo_release()函数。

代码清单9.10 增加异步通知后的globalfifo设备驱动release()函数

1 int globalfifo_release(struct inode *inode, struct file *filp) 
 
 2 { 
 
 
 3 /* 
 将文件从异步通知列表中删除 
 */ 
 
 
 4 globalfifo_fasync( - 1, filp, 0); 
 
 5 return 0; 
 
 6 }

