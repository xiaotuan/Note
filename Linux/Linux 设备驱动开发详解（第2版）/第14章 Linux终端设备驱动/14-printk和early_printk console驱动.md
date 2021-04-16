### 14.7 printk和early_printk console驱动

在Linux内核中，printk()函数是最常用的调试手段。printk()的打印消息会放入一个环形缓冲区，而/proc/kmsg文件用于描述这个缓冲区。通过dmesg命令或klogd可以读取该缓冲区。如果用户空间的klogd守护进程在运行，它将获取内核消息并分发给 syslogd，syslogd接着检查/etc/syslog.conf来找出如何处理它们。

内核printk信息支持8个级别，从高到低分别是：KERN_EMERG、KERNEL_ALERT、KERN_CRIT、KERN_ERR、KERN_WARNING、KERN_NOTICE、KERN_INFO、KERN_DEBUG。当调用printk()函数时指定的优先级小于指定的控制台优先级console_loglevel时，调试消息就显示在控制台终端。缺省的console_loglevel值是DEFAULT_CONSOLE_LOGLEVEL，用户可以使用系统调用sys_syslog或klogd-c来修改console_loglevel值，也可以直接echo值到/proc/sys/kernel/printk。/proc/sys/kernel/printk文档包含4个整数值，前两个表示系统当前的优先级和缺省优先级。

在Linux中，用于printk输出的是内核console，专门用console结构体来描述，如代码清单14.19所示。

代码清单14.19 用于printk的console结构体

1 struct console { 
 
 2 char name[16]; 
 
 3 void (*write)(struct console *, const char *, unsigned); 
 
 4 int (*read)(struct console *, char *, unsigned); 
 
 5 struct tty_driver *(*device)(struct console *, int *);



6 void (*unblank)(void); 
 
 7 int (*setup)(struct console *, char *); 
 
 8 int (*early_setup)(void); 
 
 9 short flags; 
 
 10 short index; 
 
 11 int cflag; 
 
 12 void *data; 
 
 13 struct console *next; 
 
 14 };

其中，较关键的是write()和setup()成员函数，前者用于将打印消息写入console，后者用于设置console的特性，如波特率、停止位等。

printk()函数经过重重调用，经过_ _call_console_drivers()函数，最终调用console的write()成员函数将控制台消息打印出去，如代码清单14.20所示。

代码清单14.20 printk()最终调用到console的write()成员函数

1 static void _ _call_console_drivers(unsigned start, unsigned end) 
 
 2 { 
 
 3 struct console *con; 
 
 4 
 
 5 for (con = console_drivers; con; con = con->next) { 
 
 6 if ((con->flags & CON_ENABLED) && con->write && 
 
 7 (cpu_online(smp_processor_id()) || 
 
 8 (con->flags & CON_ANYTIME))) 
 
 9 con->write(con, &LOG_BUF(start), end - start); 
 
 10 } 
 
 11}

内核提供如下API用于注册和注销console：

void register_console(struct console *); 
 
 int unregister_console(struct console *);

在内核init/main.c文件中的start_kernel()函数中，会调用console_init()函数，该函数会调用位于内核存放console初始化函数的代码段，调用其中的每一个初始化console的函数，如代码清单14.21。

代码清单14.21 console_init()函数

1 void _ _init console_init(void) 
 
 2 { 
 
 3 initcall_t *call; 
 
 4 
 
 5 tty_ldisc_begin(); 
 
 6 
 
 7 call = _ _con_initcall_start; 
 
 8 while (call < _ _con_initcall_end) { 
 
 9 (*call)(); 
 
 10 call++; 
 
 11 } 
 
 12}

实际上，对于任何一个初始化console的函数而言，只需要通过console_initcall()进行包装，即可把它放入.con_initcall.init节（开始地址为_ _con_initcall_start），典型地，如最常用的8250对应的console结构体以及初始化代码如清单14.22。

代码清单14.22 8250的console及console_initcall

1 static struct console serial8250_console = { 
 
 2 .name = "ttyS",



3 .write = serial8250_console_write, 
 
 4 .device = uart_console_device, 
 
 5 .setup = serial8250_console_setup, 
 
 6 .early_setup = serial8250_console_early_setup, 
 
 7 .flags = CON_PRINTBUFFER, 
 
 8 .index = -1, 
 
 9 .data = &serial8250_reg, 
 
 10 }; 
 
 11 
 
 12 static int _ _init serial8250_console_init(void) 
 
 13 { 
 
 14 if (nr_uarts > UART_NR) 
 
 15 nr_uarts = UART_NR; 
 
 16 
 
 17 serial8250_isa_init_ports(); 
 
 18 register_console(&serial8250_console); 
 
 19 return 0; 
 
 20 } 
 
 21 console_initcall(serial8250_console_init);

实际上，console_initcall()是一个宏，其定义于include/linux/init.h文件，它可以展开成：

#define console_initcall(fn) \ 
 
 static initcall_t _ _initcall_##fn \ 
 
 _ _used _ _section(.con_initcall.init) = fn

留意其中的__section(.con_initcall.init)，实际上是一个链接阶段的指示，表明将指定的函数放入.con_initcall.init节。

console_init()是由init/main.c文件中的start_kernel()函数调用的，而在console_init ()被调用前，还执行了一系列的操作。为了在console_init()被调用前就能使用printk()，可以使用内核的“early printk”支持，该选项位于内核配置菜单“Linux Kernel Configuration”下的“ Kernel hacking”菜单之下。

对于early printk的console的注册往往通过解析内核的early_param完成，如对于8250而言，定义了“earlycon”这样一个内核参数，当解析此内核参数时，相应地被early_param ()绑定的函数setup_early_serial8250_console()被调用，此函数将注册一个用于early printk的console。

代码清单14.23 8250的early printk console

1 static struct console early_serial8250_console __initdata = { 
 
 2 .name = "uart", 
 
 3 .write = early_serial8250_write, 
 
 4 .flags = CON_PRINTBUFFER | CON_BOOT, 
 
 5 .index = -1, 
 
 6 }; 
 
 7 
 
 8 int _ _init setup_early_serial8250_console(char *cmdline) 
 
 9 { 
 
 10 char *options; 
 
 11 int err; 
 
 12 
 
 13 options = strstr(cmdline, "uart8250,"); 
 
 14 if (!options) { 
 
 15 options = strstr(cmdline, "uart,"); 
 
 16 if (!options) 
 
 17 return 0; 
 
 18 } 
 
 19 
 
 20 options = strchr(cmdline, ',') + 1; 
 
 21 err = early_serial8250_setup(options);



22 if (err < 0) 
 
 23 return err; 
 
 24 
 
 25 register_console(&early_serial8250_console); 
 
 26 
 
 27 return 0; 
 
 28 } 
 
 29 
 
 
 30 early_ 
 param("earlycon", setup_ 
 early_ 
 serial8250_ 
 console);

例如，在Linux启动的command line中设置如下参数，将使能8250作为early printk的console。

earlycon=uart8250,mmio,0xff5e0000,115200n8 
 
 earlycon=uart8250,io,0x3f8,9600n8

留意一下，代码清单14.22第7行的flags和代码清单14.23第4行的flags的区别，会发现后者多出了一个CON_BOOT属性。实例上，所有的具有CON_BOOT属性的console都会在内核初始化至late initcall阶段的时候被注销，注销它们的函数是disable_boot_consoles()，其定义如代码清单14.24。

代码清单14.24 disable_boot_consoles()函数

1 static int _ _init disable_boot_consoles(void) 
 
 2 { 
 
 3 if (console_drivers != NULL) { 
 
 4 if (console_drivers->flags & CON_BOOT) { 
 
 5 printk(KERN_INFO "turn off boot console %s%d\n", 
 
 6 console_drivers->name, console_drivers->index); 
 
 7 return unregister_console(console_drivers); 
 
 8 } 
 
 9 } 
 
 10 return 0; 
 
 11 } 
 
 
 12 late_ 
 initcall(disable_ 
 boot_ 
 consoles);

这里再补充一个知识，内核的initcall分成了8级，对应的节分别为.initcall0.init、.initcall1.init、.initcall2.init、.initcall3.init、.initcall4.init、.initcall5.init、.initcall6.init、.initcall7.init，分别通过pure_ initcall(fn)、core_initcall(fn) 、postcore_initcall(fn) 、arch_initcall(fn)、subsys_initcall(fn)、fs_initcall(fn)、device_initcall(fn)、late_initcall(fn)可将指定的函数放入对应的节。对于pure_initcall()而言，它指定的initcall不依赖于任何其他部分，因此，其指定函数只能built-in，不能在模块中。对于1～7级而言，还存在对应的sync版本，分别通过core_initcall_sync(fn)、postcore_initcall_sync(fn)、arch_ initcall_sync(fn)、subsys_initcall_sync(fn)、fs_initcall_sync(fn)、device_initcall_sync(fn)、late_ initcall_sync(fn)修饰。

通过代码清单14.24的第12行可以看出，disable_boot_consoles()被late_initcall()修饰，因此被放入了.initcall7.init这个节。

