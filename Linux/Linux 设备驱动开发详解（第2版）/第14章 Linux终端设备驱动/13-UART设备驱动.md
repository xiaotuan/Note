### 14.6 UART设备驱动

尽管一个特定的UART设备驱动完全可以遵循第14.2～14.5节的方法来设计，即定义tty_driver并实现tty_operations其中的成员函数，但是Linux已经在文件serial_core.c中实现了UART设备的通用tty驱动层（姑且称其为串口核心层），这样，UART驱动的主要任务演变成实现serial-core.c中定义的一组uart_xxx接口而非tty_xxx接口，如图14.4所示。

![P339_46948.jpg](../images/P339_46948.jpg)
serial_core.c串口核心层完全可以被当作14.2～14.5节tty设备驱动的实例，它实现了UART设备的tty驱动。回过头来再看12.2节“设备驱动的分层思想”，是否更加豁然开朗？

串口核心层为串口设备驱动提供了如下3个结构体。

#### 1．uart_driver

uart_driver包含串口设备的驱动名、设备名、设备号等信息，它封装了tty_driver，使得底层的UART驱动无需关心tty_driver，其定义如代码清单14.13所示。

代码清单14.13 uart_driver结构体

1 struct uart_driver { 
 
 2 struct module *owner; 
 
 3 const char *driver_name; /* 驱动名 */ 
 
 4 const char *dev_name; /* 设备名 */ 
 
 5 int major; /* 主设备号 */ 
 
 6 int minor; /* 次设备号 */



7 int nr; 
 
 8 struct console *cons; 
 
 9 
 
 10 /* 私有的，底层驱动不应该访问这些成员，应该被初始化为NULL */ 
 
 11 struct uart_state *state; 
 
 12 struct tty_driver *tty_driver; 
 
 13 };

一个tty驱动必须注册/注销tty_driver，而一个UART驱动则演变为注册/注销uart_driver，使用如下接口：

int uart_register_driver(struct uart_driver *drv); 
 
 void uart_unregister_driver(struct uart_driver *drv);

实际上，uart_register_driver()和uart_unregister_driver()中分别包含了tty_register_driver()和tty_unregister_driver()的操作，如代码清单14.14所示。

代码清单14.14 uart_register_driver()和uart_unregister_driver()函数

1 int uart_register_driver(struct uart_driver *drv) 
 
 2 { 
 
 3 struct tty_driver *normal = NULL; 
 
 4 int i, retval; 
 
 5 
 
 6 BUG_ON(drv->state); 
 
 7 
 
 8 drv->state = kzalloc(sizeof(struct uart_state) * drv->nr, GFP_KERNEL); 
 
 9 retval = -ENOMEM; 
 
 10 if (!drv->state) 
 
 11 goto out; 
 
 12 
 
 13 normal = alloc_tty_driver(drv->nr); 
 
 14 if (!normal) 
 
 15 goto out; 
 
 16 
 
 17 drv->tty_driver = normal; 
 
 18 /* 初始化tty_driver */ 
 
 19 normal->owner = drv->owner; 
 
 20 normal->driver_name = drv->driver_name; 
 
 21 normal->name = drv->dev_name; 
 
 22 normal->major = drv->major; 
 
 23 normal->minor_start = drv->minor; 
 
 24 normal->type = TTY_DRIVER_TYPE_SERIAL; 
 
 25 normal->subtype = SERIAL_TYPE_NORMAL; 
 
 26 normal->init_termios = tty_std_termios; 
 
 27 normal->init_termios.c_cflag = B9600 | CS8 | CREAD | HUPCL | CLOCAL; 
 
 28 normal->init_termios.c_ispeed = normal->init_termios.c_ospeed = 9600; 
 
 29 normal->flags = TTY_DRIVER_REAL_RAW | TTY_DRIVER_DYNAMIC_DEV; 
 
 30 normal->driver_state = drv; 
 
 31 tty_set_operations(normal, &uart_ops); 
 
 32 
 
 33 /* 初始化UART状态 */ 
 
 34 for (i = 0; i < drv->nr; i++) { 
 
 35 struct uart_state *state = drv->state + i; 
 
 36 
 
 37 state->close_delay = 500; /* .5 seconds */ 
 
 38 state->closing_wait = 30000; /* 30 seconds */



39 
 
 40 mutex_init(&state->mutex); 
 
 41 } 
 
 42 
 
 43 retval = tty_register_driver(normal); 
 
 44 out: 
 
 45 if (retval < 0) { 
 
 46 put_tty_driver(normal); 
 
 47 kfree(drv->state); 
 
 48 } 
 
 49 return retval; 
 
 50 } 
 
 51 
 
 52 void uart_unregister_driver(struct uart_driver *drv) 
 
 53 { 
 
 54 struct tty_driver *p = drv->tty_driver; 
 
 55 tty_unregister_driver(p); 
 
 56 put_tty_driver(p); 
 
 57 kfree(drv->state); 
 
 58 drv->tty_driver = NULL; 
 
 59 }

#### 2．uart_port

uart_port用于描述一个UART端口（直接对应于一个串口）的I/O端口或I/O内存地址、FIFO大小、端口类型等信息，其定义如代码清单14.15。

代码清单14.15 uart_port结构体

1 struct uart_port { 
 
 2 spinlock_t lock; /* 端口锁 */ 
 
 3 unsigned int iobase; /* I/O端口基地址 */ 
 
 4 unsigned char __iomem *membase; /* I/O内存基地址 */ 
 
 5 unsigned int irq; /* 终端号 */ 
 
 6 unsigned int uartclk; /* UART时钟 */ 
 
 7 unsigned char fifosize; /* 传输fifo大小 */ 
 
 8 unsigned char x_char; /* xon/xoff字符 */ 
 
 9 unsigned char regshift; /* 寄存器位移 */ 
 
 10 unsigned char iotype; /* I/O存取类型 */ 
 
 11 unsigned char unused1; 
 
 12 
 
 13 unsigned int read_status_mask; /* 驱动相关的 */ 
 
 14 unsigned int ignore_status_mask; /* 驱动相关的 */ 
 
 15 struct uart_info *info; /* 指向parent信息 */ 
 
 16 struct uart_icount icount; /* 计数 */ 
 
 17 
 
 18 struct console *cons; /* console结构体 */ 
 
 19 #ifdef CONFIG_SERIAL_CORE_CONSOLE 
 
 20 unsigned long sysrq; /* sysrq超时 */ 
 
 21 #endif 
 
 22 
 
 23 upf_t flags; 
 
 24 unsigned int mctrl; /* 目前modem控制设置 */ 
 
 25 unsigned int timeout; /* 基于字符的超时 */ 
 
 26 unsigned int type; /* 端口类型 */ 
 
 27 const struct uart_ops *ops; /* UART操作集 */



28 unsigned int custom_divisor; 
 
 29 unsigned int line; /* 端口索引 */ 
 
 30 unsigned long mapbase; /* ioremap后基地址 */ 
 
 31 struct device *dev; /* parent设备 */ 
 
 32 unsigned char hub6; 
 
 33 unsigned char suspended; 
 
 34 unsigned char unused[2]; 
 
 35 void *private_data; 
 
 36 };

串口核心层提供如下函数来添加一个端口：

int uart_add_one_port(struct uart_driver *drv, struct uart_port *port);

对上述函数的调用应该发生在uart_register_driver()之后，uart_add_one_port()的一个最重要作用是封装了tty_register_device()。

uart_add_one_port()的“反函数”是uart_remove_one_port()，其中会调用tty_unregister_device()，原型为：

int uart_remove_one_port(struct uart_driver *drv, struct uart_port *port);

#### 3．uart_ops

uart_ops定义了针对UART的一系列操作，包括发送、接收及线路设置等，如果说tty_driver中的tty_operations对于串口还较为抽象，那么uart_ops则直接面向了串口的UART，其定义如代码清单14.16。Linux驱动的这种层次非常类似于面向对象编程中基类、派生类的关系，派生类针对特定的事物会更加具体，而基类则站在更高的抽象层次上。

代码清单14.16 uart_ops结构体

1 struct uart_ops { 
 
 2 unsigned int (*tx_empty)(struct uart_port *); 
 
 3 void (*set_mctrl)(struct uart_port *, unsigned int mctrl); 
 
 4 unsigned int (*get_mctrl)(struct uart_port *); 
 
 5 void (*stop_tx)(struct uart_port *); 
 
 6 void (*start_tx)(struct uart_port *); 
 
 7 void (*send_xchar)(struct uart_port *, char ch); 
 
 8 void (*stop_rx)(struct uart_port *); 
 
 9 void (*enable_ms)(struct uart_port *); 
 
 10 void (*break_ctl)(struct uart_port *, int ctl); 
 
 11 int (*startup)(struct uart_port *); 
 
 12 void (*shutdown)(struct uart_port *); 
 
 13 void (*flush_buffer)(struct uart_port *); 
 
 14 void (*set_termios)(struct uart_port *, struct ktermios *new, 
 
 15 struct ktermios *old); 
 
 16 void (*set_ldisc)(struct uart_port *); 
 
 17 void (*pm)(struct uart_port *, unsigned int state, 
 
 18 unsigned int oldstate); 
 
 19 int (*set_wake)(struct uart_port *, unsigned int state); 
 
 20 
 
 21 const char *(*type)(struct uart_port *); /*一个描述端口类型的字符串 */ 
 
 22 /* 释放该端口使用的I/O和memory资源 */ 
 
 23 void (*release_port)(struct uart_port *); 
 
 24 
 
 25 /* 申请该端口使用的I/O和memory资源 */ 
 
 26 int (*request_port)(struct uart_port *); 
 
 27 void (*config_port)(struct uart_port *, int);



28 int (*verify_port)(struct uart_port *, struct serial_struct *); 
 
 29 int (*ioctl)(struct uart_port *, unsigned int, unsigned long); 
 
 30 #ifdef CONFIG_CONSOLE_POLL 
 
 31 void (*poll_put_char)(struct uart_port *, unsigned char); 
 
 32 int (*poll_get_char)(struct uart_port *); 
 
 33 #endif 
 
 34 };

serial_core.c中定义了tty_operations的实例，包含uart_open()、uart_close()、uart_write()、uart_send_xchar()等成员函数（如代码清单14.17），这些函数会借助uart_ops结构体中的成员函数来完成具体的操作，代码清单14.18所示为tty_operations的uart_send_xchar()成员函数利用uart_ops 中start_tx()、send_xchar()成员函数的例子。

代码清单14.17 串口核心层的tty_operations实例

1 static const struct tty_operations uart_ops = { 
 
 2 .open = uart_open, 
 
 3 .close = uart_close, 
 
 4 .write = uart_write, 
 
 5 .put_char = uart_put_char, 
 
 6 .flush_chars = uart_flush_chars, 
 
 7 .write_room = uart_write_room, 
 
 8 .chars_in_buffer= uart_chars_in_buffer, 
 
 9 .flush_buffer = uart_flush_buffer, 
 
 10 .ioctl = uart_ioctl, 
 
 11 .throttle = uart_throttle, 
 
 12 .unthrottle = uart_unthrottle, 
 
 13 .send_xchar = uart_send_xchar, 
 
 14 .set_termios = uart_set_termios, 
 
 15 .set_ldisc = uart_set_ldisc, 
 
 16 .stop = uart_stop, 
 
 17 .start = uart_start, 
 
 18 .hangup = uart_hangup, 
 
 19 .break_ctl = uart_break_ctl, 
 
 20 .wait_until_sent= uart_wait_until_sent, 
 
 21 #ifdef CONFIG_PROC_FS 
 
 22 .read_proc = uart_read_proc, 
 
 23 #endif 
 
 24 .tiocmget = uart_tiocmget, 
 
 25 .tiocmset = uart_tiocmset, 
 
 26 #ifdef CONFIG_CONSOLE_POLL 
 
 27 .poll_init = uart_poll_init, 
 
 28 .poll_get_char = uart_poll_get_char, 
 
 29 .poll_put_char = uart_poll_put_char, 
 
 30 #endif 
 
 31 };

代码清单14.18 串口核心层的tty_operations与uart_ops关系

1 static void uart_send_xchar(struct tty_struct *tty, char ch) 
 
 2 { 
 
 3 struct uart_state *state = tty->driver_data; 
 
 4 struct uart_port *port = state->port; 
 
 5 unsigned long flags; 
 
 6 /* 如果uart_ops中实现了send_xchar成员函数 */ 
 
 7 if (port->ops->send_xchar)



8 port->ops->send_xchar(port, ch); 
 
 9 else { /* uart_ops中未实现send_xchar成员函数 */ 
 
 10 port->x_char = ch; 
 
 11 if (ch) { 
 
 12 spin_lock_irqsave(&port->lock, flags); 
 
 13 port->ops->start_tx(port); /* 发送xchar */ 
 
 14 spin_unlock_irqrestore(&port->lock, flags); 
 
 15 } 
 
 16 } 
 
 17 }

在使用串口核心层这个通用串口tty驱动层的接口后，一个串口驱动要完成的主要工作如下。

（1）定义uart_driver、uart_ops、uart_port等结构体的实例并在适当的地方根据具体硬件和驱动的情况初始化它们，当然具体设备xxx的驱动可以将这些结构套在新定义的xxx_uart_driver、xxx_uart_ops、xxx_uart_port之内。

（2）在模块初始化时调用uart_register_driver()和uart_add_one_port()以注册UART驱动并添加端口，在模块卸载时调用uart_unregister_driver()和uart_remove_one_port()以注销UART驱动并移除端口。

（3）根据具体硬件的datasheet实现uart_ops中的成员函数，这些函数的实现成为UART驱动的主体工作。

