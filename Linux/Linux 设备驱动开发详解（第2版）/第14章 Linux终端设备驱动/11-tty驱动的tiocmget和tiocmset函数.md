### 14.5.3 tty驱动的tiocmget和tiocmset函数

对TIOCMGET、TIOCMSET、TIOCMBIC和TIOCMBIS IO控制命令的调用将被tty核心转换为对tty驱动tiocmget()函数和tiocmset()函数的调用，TIOCMGET对应tiocmget()函数，TIOCMSET、TIOCMBIC和TIOCMBIS对应tiocmset()函数，分别用于读取Modem控制的设置和进行Modem的设置。代码清单14.10所示为tiocmget()函数的范例，代码清单14.11所示为tiocmset()函数的范例。

代码清单14.10 tty驱动程序tiocmget()函数范例

1 static int xxx_tiocmget(struct tty_struct *tty, struct file *file) 
 
 2 { 
 
 3 struct xxx_tty *info = tty->driver_ data; 
 
 4 unsigned int result = 0; 
 
 5 unsigned int msr = info->msr; 
 
 6 unsigned int mcr = info->mcr; 
 
 7 result = ((mcr &MCR_DTR) ? TIOCM_DTR : 0) | /* DTR 被设置 */ 
 
 8 ((mcr &MCR_RTS) ? TIOCM_RTS : 0) | /* RTS 被设置 */ 
 
 9 ((mcr &MCR_LOOP) ? TIOCM_LOOP : 0) | /* LOOP 被设置 */ 
 
 10 ((msr &MSR_CTS) ? TIOCM_CTS : 0) | /* CTS 被设置 */ 
 
 11 ((msr &MSR_CD) ? TIOCM_CAR : 0) | /* CD 被设置*/ 
 
 12 ((msr &MSR_RI) ? TIOCM_RI : 0) | /* 振铃指示被设置 */ 
 
 13 ((msr &MSR_DSR) ? TIOCM_DSR : 0); /* DSR 被设置 */ 
 
 14 return result; 
 
 15 }



代码清单14.11 tty驱动程序tiocmset()函数范例

1 static int xxx_tiocmset(struct tty_struct *tty, struct file *file, unsigned 
 
 2 int set, unsigned int clear) 
 
 3 { 
 
 4 struct xxx_tty *info = tty->driver_data; 
 
 5 unsigned int mcr = info->mcr; 
 
 6 
 
 7 if (set &TIOCM_RTS) /* 设置RTS */ 
 
 8 mcr |= MCR_RTS; 
 
 9 if (set &TIOCM_DTR) /* 设置DTR */ 
 
 10 mcr |= MCR_RTS; 
 
 11 
 
 12 if (clear &TIOCM_RTS) /* 清除RTS */ 
 
 13 mcr &= ~MCR_RTS; 
 
 14 if (clear &TIOCM_DTR) /* 清除DTR */ 
 
 15 mcr &= ~MCR_RTS; 
 
 16 
 
 17 /* 设置设备新的MCR值 */ 
 
 18 tiny->mcr = mcr; 
 
 19 return 0; 
 
 20 }

tiocmget()函数会访问MODEM状态寄存器（MSR），而tiocmset()函数会访问MODEM控制寄存器（MCR）。

