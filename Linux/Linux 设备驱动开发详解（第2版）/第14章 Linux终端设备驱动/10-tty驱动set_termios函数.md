### 14.5.2 tty驱动set_termios函数

大部分 termios 用户空间函数被库转换为对驱动节点的 ioctl()调用，而tty ioctl中的大部分命令会被tty核心转换为对tty驱动的set_termios()函数的调用。set_termios()函数需要根据用户对termios的设置（termios设置包括字长、奇偶校验位、停止位、波特率等）完成实际的硬件设置。

tty_operations中的set_termios()函数原型为：

void(*set_termios)(struct tty_struct *tty, struct termios *old);

新的设置被保存在tty_struct中，旧的设置被保存在old参数中，若新旧参数相同，则什么都不需要做，对于被改变的设置，需完成硬件上的设置，代码清单14.9给出了set_termios()函数的例子。

代码清单14.9 tty驱动程序set.termios()函数范例

1 static void xxx_set_termios(struct tty_struct *tty, struct termios *old_termios) 
 
 2 { 
 
 3 struct xxx_tty *info = (struct cyclades_port*)tty->driver_data; 
 
 4 /* 新设置等同于老设置，什么也不做 */ 
 
 5 if (tty->termios->c_cflag == old_termios->c_cflag) 
 
 6 return ; 
 
 7 ... 
 
 8 
 
 9 /* 关闭CRTSCTS硬件流控制 */ 
 
 10 if ((old_termios->c_cflag &CRTSCTS) && !(cflag &CRTSCTS)) { 
 
 11 ...



12 } 
 
 13 
 
 14 /* 打开CRTSCTS硬件流控制 */ 
 
 15 if (!(old_termios->c_cflag &CRTSCTS) && (cflag &CRTSCTS)) { 
 
 16 ... 
 
 17 } 
 
 18 
 
 19 /* 设置字节大小 */ 
 
 20 switch (tty->termios->c_cflag &CSIZE) { 
 
 21 case CS5: 
 
 22 ... 
 
 23 case CS6: 
 
 24 ... 
 
 25 case CS7: 
 
 26 ... 
 
 27 case CS8: 
 
 28 ... 
 
 29 } 
 
 30 
 
 31 /* 设置奇偶校验 */ 
 
 32 if (tty->termios->c_cflag &PARENB) 
 
 33 if (tty->termios->c_cflag &PARODD) /* 奇校验 */ 
 
 34 ... 
 
 35 else /* 偶校验*/ 
 
 36 ... 
 
 37 else /* 无校验*/ 
 
 38 ... 
 
 39 }

