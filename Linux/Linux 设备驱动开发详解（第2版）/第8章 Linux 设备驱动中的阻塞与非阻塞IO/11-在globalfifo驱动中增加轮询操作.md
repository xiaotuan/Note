### 8.3.1 在globalfifo驱动中增加轮询操作

在globalfifo的poll()函数中，首先将设备结构体中的r_wait和w_wait等待队列头添加到等待列表，然后通过判断dev->current_len是否等于0来获得设备的可读状态，通过判断dev->current_len是否等于GLOBALFIFO_SIZE来获得设备的可写状态，如代码清单8.12所示。

代码清单8.12 globalfifo设备驱动的poll()函数

1 static unsigned int globalfifo_poll(struct file *filp, poll_table *wait) 
 
 2 { 
 
 3 unsigned int mask = 0; 
 
 4 struct globalfifo_dev *dev = filp->private_data; /*获得设备结构体指针*/ 
 
 5



6 down(&dev->sem); 
 
 7 
 
 8 poll_wait(filp, &dev->r_wait, wait); 
 
 9 poll_wait(filp, &dev->w_wait, wait); 
 
 10 /*fifo非空*/ 
 
 11 if (dev->current_len != 0) 
 
 12 mask |= POLLIN | POLLRDNORM; /*标示数据可获得*/ 
 
 13 /*fifo非满*/ 
 
 14 if (dev->current_len != GLOBALFIFO_SIZE) 
 
 15 mask |= POLLOUT | POLLWRNORM; /*标示数据可写入*/ 
 
 16 
 
 17 up(&dev->sem); 
 
 18 return mask; 
 
 19 }

注意，要把globalfifo_poll赋给globalfifo_fops的poll成员：

static const struct file_operations globalfifo_fops = { 
 
 ... 
 
 .poll = globalfifo_poll, 
 
 ... 
 
 };

