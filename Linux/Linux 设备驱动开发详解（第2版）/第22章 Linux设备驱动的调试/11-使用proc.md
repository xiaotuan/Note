### 22.5 使用/proc

在Linux系统中，/proc文件系统十分有用，它被用于内核向用户导出信息。/proc文件系统是一个虚拟文件系统，通过它可以使用一种新的方法在Linux内核空间和用户空间之间进行通信。在/proc文件系统中，我们可以将对虚拟文件的读写作为与内核中实体进行通信的一种手段，与普通文件不同的是，这些虚拟文件的内容都是动态创建的。/proc下的文件并非完全是只读的，若节点可写，还可用于一定的控制或配置目的，例如前面介绍的写/proc/sys/kernel/printk可以改变printk的打印级别。

Linux系统的许多命令本身都是通过分析/proc下的文件来完成，如ps、top、uptime和free等。例如，free命令通过分析/proc/meminfo文件得到可用内存信息，下面显示了对应的meminfo文件和free命令的结果。

● meminfo文件：

[root@localhost proc]# cat meminfo 
 
 MemTotal: 29516 kB 
 
 MemFree: 1472 kB 
 
 Buffers: 4096 kB 
 
 Cached: 12648 kB 
 
 SwapCached: 0 kB 
 
 Active: 14208 kB 
 
 Inactive: 8844 kB 
 
 HighTotal: 0 kB 
 
 HighFree: 0 kB 
 
 LowTotal: 29516 kB 
 
 LowFree: 1472 kB 
 
 SwapTotal: 265064 kB 
 
 SwapFree: 265064 kB 
 
 Dirty: 20 kB 
 
 Writeback: 0 kB 
 
 Mapped: 10052 kB 
 
 Slab: 3864 kB 
 
 CommitLimit: 279820 kB 
 
 Committed_AS: 13760 kB 
 
 PageTables: 444 kB 
 
 VmallocTotal: 999416 kB 
 
 VmallocUsed: 560 kB 
 
 VmallocChunk: 998580 kB

● free命令：

[root@localhost proc]# free 
 
 total used free shared buffers cached 
 
 Mem: 29516 28104 1412 0 4100 12700 
 
 -/+ buffers/cache: 11304 18212 
 
 Swap: 265064 0 265064

Linux的USB、PCI等内核代码本身都会创建/proc节点导出内核信息，虽然不值得鼓励，但在Linux设备驱动程序中，驱动工程师自定义/proc节点以向外界传递信息的方法仍然是可行的。

在Linux系统中，可用如下函数创建/proc节点：

struct proc_dir_entry *create_proc_entry(const char *name, mode_t mode, 
 
 struct proc_dir_entry *parent);

struct proc_dir_entry *create_proc_read_entry(const char *name, mode_t mode, 
 
 struct proc_dir_entry *base, read_proc_t *read_proc, void * data);

create_proc_entry()函数用于创建/proc节点，而create_proc_read_entry()调用create_proc_entry()创建只读的/proc节点。参数name为/proc节点的名称，parent/base为父目录的节点，如果为NULL，则指/proc目录，read_proc是/proc节点的读函数指针。当read()系统调用在/proc文件系统中执行时，它映像到一个数据产生函数，而不是一个数据获取函数。

下列函数用于创建/proc目录：

struct proc_dir_entry *proc_mkdir(const char *name, struct proc_dir_entry *parent);

结合create_proc_entry()和proc_mkdir()，代码清单22.6中的程序可用于先在/proc下创建一个目录，而后在该目录下创建一个文件。

代码清单22.6 proc_mkdir()和create_proc_entry()函数使用范例

1 /* 创建/proc下的目录 */ 
 
 2 example_dir = proc_mkdir("procfs_example", NULL); 
 
 3 if (example_dir == NULL) { 
 
 4 rv = - ENOMEM; 
 
 5 goto out; 
 
 6 } 
 
 7 
 
 8 example_dir→owner = THIS_MODULE; 
 
 9 
 
 10 /* 创建一个例子/proc文件 */ 
 
 11 example_file = create_proc_entry("example_file", 0666, example_dir); 
 
 12 if (example_file == NULL) { 
 
 13 rv = - ENOMEM; 
 
 14 goto out; 
 
 15 } 
 
 16 
 
 17 example_file→owner = THIS_MODULE; 
 
 18 example_file→read_proc = example_file_read; 
 
 19 example_file→write_proc = example_file_write;

作为上述函数各返回值的proc_dir_entry结构体中包含了/proc节点的读函数指针（read_proc_t *read_proc）、写函数指针（write_proc_t *write_proc）以及父节点、子节点信息等。

/proc节点的读写函数的类型分别为：

typedef int (read_proc_t)(char *page, char **start, off_t off, 
 
 int count, int *eof, void *data); 
 
 typedef int (write_proc_t)(struct file *file, const char __user *buffer, 
 
 unsigned long count, void *data);

读函数中page指针指向用于写入数据的缓冲区，start用于返回实际的数据写到内存页的位置，eof是用于返回读结束标志，offset是读的偏移，count是要读的数据长度。

start参数比较复杂，对于/proc只包含简单数据的情况，通常不需要在读函数中设置*start，意味着内核将认为数据保存在内存页偏移0的地方。如果将*start设置为非0值，意味着内核将认为*start指向的数据是offset偏移处的数据。

写函数与file_operations中的write()成员类似，需要一次从用户缓冲区到内存空间的复制过程。

Linux系统中可用如下函数删除/proc节点：

void remove_proc_entry(const char *name, struct proc_dir_entry *parent);

Linux系统中已经定义好的可使用的/proc节点宏包括：proc_root_fs（/proc）、proc_net （/proc/net）、proc_bus（/proc/bus）、proc_root_driver（/proc/driver）等，proc_root_fs实际就是NULL。

代码清单22.7所示为一个简单的/proc使用范例，这段代码在模块加载函数中创建/proc文件节点，在模块卸载函数中撤销/proc节点，而文件中只保存了一个32位的无符号整形值。



代码清单22.7 /proc文件系统使用模板

1 #include ... 
 
 2 
 
 3 static struct proc_dir_entry *proc_entry; 
 
 4 static unsigned long val = 0x12345678; 
 
 5 
 
 6 /* 读/proc文件接口 */ 
 
 7 ssize_t simple_proc_read(char *page, char **start, off_t off, int count, 
 
 8 int*eof, void *data) 
 
 9 { 
 
 10 int len; 
 
 11 if (off > 0) { /* 不能偏移访问 */ 
 
 12 *eof = 1; 
 
 13 return 0; 
 
 14 } 
 
 15 
 
 16 len = sprintf(page, "%08x\n", val); 
 
 17 
 
 18 return len; 
 
 19 } 
 
 20 
 
 21 /* 写/proc文件接口 */ 
 
 22 ssize_t simple_proc_write(struct file *filp, const char _ _user *buff, unsigned 
 
 23 long len, void *data) 
 
 24 { 
 
 25 #define MAX_UL_LEN 8 
 
 26 char k_buf[MAX_UL_LEN]; 
 
 27 char *endp; 
 
 28 unsigned long new; 
 
 29 int count = min(MAX_UL_LEN, len); 
 
 30 int ret; 
 
 31 
 
 32 if (copy_from_user(k_buf, buff, count)) { 
 
 33 ret = - EFAULT; 
 
 34 goto err; 
 
 35 } else { 
 
 
 36 new = simple_strtoul(k_buf, &endp, 16); /* 
 字符串转化为整数 
 */ 
 
 37 if (endp == k_buf) { /* 无效的输入参数 */ 
 
 38 ret = - EINVAL; 
 
 39 goto err; 
 
 40 } 
 
 41 val = new; 
 
 42 return count; 
 
 43 } 
 
 44 err: 
 
 45 return ret; 
 
 46 } 
 
 47 
 
 48 int __init simple_proc_init(void) 
 
 49 { 
 
 50 proc_entry = create_proc_entry("sim_proc", 0666, NULL); 
 
 51 if (proc_entry == NULL) { 
 
 52 printk(KERN_INFO "Couldn't create proc entry\n");



53 goto err; 
 
 54 } else { 
 
 55 proc_entry→read_proc = simple_proc_read; 
 
 56 proc_entry→write_proc = simple_proc_write; 
 
 57 proc_entry→owner = THIS_MODULE; 
 
 58 } 
 
 59 return 0; 
 
 60 err: 
 
 61 return -ENOMEM; 
 
 62 } 
 
 63 
 
 64 void __exit simple_proc_exit(void) 
 
 65 { 
 
 66 remove_proc_entry("sim_proc", &proc_root); //撤销/proc 
 
 67 } 
 
 68 
 
 69 module_init(simple_proc_init); 
 
 70 module_exit(simple_proc_exit); 
 
 71 
 
 72 MODULE_AUTHOR("Barry Song, author@linuxdriver.cn"); 
 
 73 MODULE_DESCRIPTION("A simple Module for showing proc"); 
 
 74 MODULE_VERSION("V1.0");

上述代码第36行调用的simple_strtoul()用于转换用户输入的字符串为无符号长整数，第3个参数16意味着转化方式是十六进制。

编译上述简单的“sim_proc.c”为“sim_proc.ko”，运行“insmod sim_proc.ko”加载该模块后，/proc目录下将多出一个文件sim_proc，“ls –l”的结果如下：

[root@localhost proc]# ls -1 sim_proc 
 
 -rw-rw-rw- 1 root root 0 Sep 4 20:31 sim_proc

权限与创建/proc/sim_proc时给出的0666参数是一致的，现在读取sim_proc，如下所示：

[root@localhost proc]# cat sim_proc 
 
 12345678

读出来的正好是我们赋的初值0x12345678。

测试写/proc/sim_proc文件，使用echo命令修改它为0x88888888：

[root@localhost driver_study]# echo 88888888 > /proc/sim_proc

再查看新值：

[root@localhost driver_study]# cat /proc/sim_proc 
 
 88888888

说明我们上一步执行的写操作是正确的。

