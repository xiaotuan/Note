### 14.5.4 tty驱动ioctl函数

当用户在tty设备节点上进行ioctl()调用时，tty_operations中的ioctl()函数会被tty核心调用。如果tty驱动不知道如何处理传递给它的IOCTL值，它返回–ENOIOCTLCMD，之后tty核心会执行一个通用的操作。

驱动中常见的需处理的I/O控制命令包括TIOCSERGETLSR（获得这个tty设备的线路状态寄存器LSR的值）、TIOCGSERIAL（获得串口线信息）、TIOCMIWAIT（等待MSR改变）、TIOCGICOUNT（获得中断计数）等。代码清单14.12给出了tty驱动程序ioctl()函数的范例。

代码清单14.12 tty驱动程序ioctl()函数范例

1 static int xxx_ioctl(struct tty_struct *tty, struct file *filp, unsigned int 
 
 2 cmd, unsigned long arg) 
 
 3 { 
 
 4 struct xxx_tty *info = tty->driver_data; 
 
 5 ... 
 
 6 /* 处理各种命令 */ 
 
 7 switch (cmd){ 
 
 8 case TIOCGSERIAL: 
 
 9 ... 
 
 10 case TIOCSSERIAL: 
 
 11 ... 
 
 12 case TIOCSERCONFIG: 
 
 13 ... 
 
 14 case TIOCMIWAIT: 
 
 15 ... 
 
 16 case TIOCGICOUNT:



17 ... 
 
 18 case TIOCSERGETLSR: 
 
 19 ... 
 
 20 } 
 
 21 ... 
 
 22 }

