### 22.4 内核打印信息——printk()

在Linux中，内核打印语句printk()会将内核信息输出到内核信息缓冲区中。内核信息缓冲区是一个环形缓冲区（ring buffer），因此，如果塞入的消息过多，就会将之前的消息冲刷掉。

Linux的klogd进程（一个系统守护进程，它截获并且记录下Linux内核日志信息）会通过/proc/kmsg文件读取缓冲区，一旦读取完成，内核信息便从缓冲区中被删除。之后，klogd守护进程会将读取的内核信息派发给syslogd守护进程（syslogd记录下系统里所有提供日志记录的程序给出的日志和信息内容，每一个被记录的消息至少包含时间戳和主机名），syslogd这个守护进程会根据/etc/syslog.conf将不同的服务产生的日志记录到不同的文件中。例如在/etc/syslog.conf中增加“kern.* /tmp/kernel_debug.txt”一行，则内核信息也会被放置到/tmp/kernel_debug.txt文件中。执行“insmod hello.ko”，我们看到/tmp/kernel_debug.txt文件中多出如下一行：

Jul 6 00:40:51 localhost kernel: Hello World enter

用户也可以直接使用“cat /proc/kmsg”命令来显示内核信息，但是，由于/proc/kmsg是一个“永无休止的文件”，因此，“cat /proc/kmsg”的进程只能通过“Ctrl+C”或kill终止。另外，使用dmesg命令也可以直接读取ring buffer中的信息。

printk()定义了8个消息级别，分为级别0～7，越低级别（数值越大）的消息越不重要，第0级是紧急事件级，第7级是调试级，代码清单22.3所示为printk()的级别定义。

代码清单22.3 printk()的级别定义

1 #define KERN_EMERG "<0>" /*紧急事件，一般是系统崩溃之前提示的消息 */ 
 
 2 #define KERN_ALERT "<1>" /* 必须立即采取行动 */ 
 
 3 #define KERN_CRIT "<2>"/*临界状态，通常涉及严重的硬件或软件操作失败 */ 
 
 4 #define KERN_ERR "<3>" /*用于报告错误状态，设备驱动程序会 
 
 5 经常使用KERN_ERR来报告来自硬件的问题 */ 
 
 6 #define KERN_WARNING "<4>" /*对可能出现问题的情况进行警告， 
 
 7 这类情况通常不会对系统造成严重问题 */ 
 
 8 #define KERN_NOTICE "<5>" /*有必要进行提示的正常情形， 
 
 9 许多与安全相关的状况用这个级别进行汇报*/ 
 
 10 #define KERN_INFO "<6>" /*内核提示性信息，很多驱动程序 
 
 11 在启动的时候，以这个级别打印出它们找到的硬件信息*/ 
 
 12 #define KERN_DEBUG "<7>" /* 用于调试信息 */

通过/proc/sys/kernel/printk文件可以调节printk的输出等级，该文件有4个数字值，如下所示。

● 控制台日志级别：优先级高于该值的消息将被打印至控制台。

● 默认的消息日志级别：将用该优先级来打印没有优先级的消息。

● 最低的控制台日志级别：控制台日志级别可被设置的最小值（最高优先级）。l 默认的控制台日志级别：控制台日志级别的默认值。

上述4个值的默认设置为6、4、1、7。

通过如下命令可以使得Linux内核的任何printk都被输出：

# echo 8 > /proc/sys/kernel/printk

在设备驱动中，我们经常需要输出调试或系统信息，尽管可以直接采用printk("<7>debug info …\n")方式的printk()语句输出，但是通常可以使用封装了printk()的更高级的宏，如pr_debug()、dev_debug()等。代码清单22.4所示为pr_debug()和pr_info()的定义，代码清单22.5所示为dev_dbg()、dev_err()、dev_info()等的定义，前一组的输出中不包含设备信息，后一组包含。

代码清单22.4 替代printk()的宏

1 #ifdef DEBUG 
 
 2 #define pr_debug(fmt,arg...) \ 
 
 3 printk(KERN_DEBUG fmt,##arg) 
 
 4 #else 
 
 5 static inline int _ _attribute_ _ ((format (printf, 1, 2))) pr_debug(const char * fmt, ...) 
 
 6 { 
 
 7 return 0; 
 
 8 } 
 
 9 #endif 
 
 10 
 
 11 #define pr_info(fmt,arg...) \ 
 
 12 printk(KERN_INFO fmt,##arg)

代码清单22.5 包含设备信息的替代printk()的宏

1 #define dev_printk(level, dev, format, arg...) \ 
 
 2 printk(level "%s %s: " format , dev_driver_string(dev) , (dev)→bus_id , ## arg) 
 
 3 
 
 4 #ifdef DEBUG 
 
 5 #define dev_dbg(dev, format, arg...) \ 
 
 6 dev_printk(KERN_DEBUG , dev , format , ## arg) 
 
 7 #else 
 
 8 #define dev_dbg(dev, format, arg...) do { (void)(dev); } while (0) 
 
 9 #endif 
 
 10 
 
 11 #define dev_err(dev, format, arg...) \ 
 
 12 dev_printk(KERN_ERR , dev , format , ## arg) 
 
 13 #define dev_info(dev, format, arg...) \ 
 
 14 dev_printk(KERN_INFO , dev , format , ## arg) 
 
 15 #define dev_warn(dev, format, arg...) \ 
 
 16 dev_printk(KERN_WARNING , dev , format , ## arg) 
 
 17 #define dev_notice(dev, format, arg...) \ 
 
 18 dev_printk(KERN_NOTICE , dev , format , ## arg)

在打印信息时，如果想输出其所在的函数，可以使用_ _FUNCTION_ _，如：

printk("%s: Incorrect IRQ %d from %s\n", _ _FUNCTION_ _, irq, devname);

C99标准已经提供了_ _func_ _来指定函数名，因此目前_ _FUNCTION_ _实际定义为：

#define _ _FUNCTION_ _ (_ _func_ _)

