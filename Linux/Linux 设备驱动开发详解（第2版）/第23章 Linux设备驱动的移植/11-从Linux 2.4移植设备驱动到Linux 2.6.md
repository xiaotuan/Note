### 23.3 从Linux 2.4移植设备驱动到Linux 2.6

从Linux 2.4内核到Linux 2.6内核，Linux在可装载模块机制、设备模型、一些核心API等方面发生了较大改变，随着公司产品的过渡，驱动工程师会面临着将驱动从Linux 2.4内核移植到Linux 2.6内核，或是让驱动能同时支持Linux 2.4内核与Linux 2.6内核的任务。

下面分析Linux 2.4内核和Linux 2.6内核在设备驱动方面的几个主要的不同点。

#### 1．内核模块的Makefile

Linux 2.4内核中，模块的编译只需内核源码头文件，并在包括linux/modules.h头文件之前定义MODULE，且其编译、连接后生成的内核模块后缀为.o。而在Linux 2.6内核中，模块的编译需要依赖配置过的内核源码，编译过程首先会到内核源码目录下，读取顶层的Makefile文件，然后再返回模块源码所在目录，且编译、连接后生成的内核模块后缀为.ko。

Linux 2.4中内核模块的Makefile模板如代码清单23.4所示。

代码清单23.4 Linux 2.4中内核模块的Makefile模板

1 #Makefile2.4 
 
 2 KVER=$(shell uname -r) 
 
 3 KDIR=/lib/modules/$(KVER)/build 
 
 4 OBJS=mymodule.o 
 
 5 CFLAGS=-D_ _KERNEL_ _ -I$(KDIR)/include -DMODULE -D_ _KERNEL_SYSCALLS_ _ 
 
 6 -DEXPORT_SYMTAB -O2 -fomit-frame-pointer -Wall -DMODVERSIONS



7 -include $(KDIR)/include/linux/modversions.h 
 
 8 all: $(OBJS) 
 
 9 mymodule.o: file1.o file2.o 
 
 10 ld -r -o $@ $^ 
 
 11 clean: 
 
 12 rm -f *.o

而Linux 2.6中内核模块的Makefile模板如代码清单23.5所示。

代码清单23.5 Linux 2.6中内核模块的Makefile模板

1 # Mcakefile2.6 
 
 2 ifneq ($(KERNELRELEASE),) 
 
 3 #dependency relationshsip of files and target modules 
 
 4 #mymodule-objs := file1.o file2.o 
 
 5 #obj-m := mymodule.o 
 
 6 obj-m := second.o 
 
 7 else 
 
 8 PWD := $(shell pwd) 
 
 9 KVER ?= $(shell uname -r) 
 
 10 KDIR := /lib/modules/$(KVER)/build 
 
 11 all: 
 
 12 $(MAKE) -C $(KDIR) M=$(PWD) 
 
 13 clean: 
 
 14 rm -rf .*.cmd *.o *.mod.c *.ko .tmp_versions 
 
 15 endif

Linux 2.6内核模板Makefile中的KERNELRELEASE是在内核源码的顶层Makefile中定义的一个变量，在第一次读取执行此Makefile时，KERNELRELEASE没有被定义，所以make将读取执行else之后的内容。如果make的目标是clean，将直接执行clean操作，然后结束；当make的目标为all时，-C $(KDIR)指明跳转到内核源码目录下读取那里的Makefile，M=$(PWD)表明之后要返回到当前目录继续读入、执行当前的Makefile。当从内核源码目录返回时，KERNELRELEASE已被定义，kbuild也被启动去解析kbuild语法的语句，make将继续读取else之前的内容。else之前的内容为kbuild语法的语句，指明模块源码中各文件的依赖关系，以及要生成的目标模块名。"mymodule-objs := file1.o file2.o"表示mymoudule.o由file1.o与file2.o连接生成，"obj-m := mymodule.o"表示编译连接后将生成mymodule模块。

“$(MAKE) -C $(KDIR) M=$(PWD)”与“$(MAKE) -C $(KDIR) SUBDIRS =$(PWD)”的作用是等效的，后者是较老的使用方法。

通过以上比较可以看到，从Makefile编写角度来看，在Linux 2.6内核下，内核模块编译不必定义复杂的CFLAGS，而且模块中各文件依赖关系的表示更加简洁清晰。

在分析清楚Linux 2.4和Linux 2.6的内核模块Makefile的差异之后，可以给出同时支持Linux 2.4内核和Linux 2.6内核的内核模块Makefile文件，如代码清单23.6所示。这个模板中实际上根据内核版本，去读取不同的Makefile。

代码清单23.6 同时支持Linux 2.4/2.6的内核模块的Makefile模板

1 #Makefile for 2.4 & 2.6 
 
 2 VERS26=$(findstring 2.6,$(shell uname -r)) 
 
 3 MAKEDIR?=$(shell pwd) 
 
 4 ifeq ($(VERS26),2.6) 
 
 5 include $(MAKEDIR)/Makefile2.6



6 else 
 
 7 include $(MAKEDIR)/Makefile2.4 
 
 8 endif

#### 2．内核模块加载时的版本检查

Linux 2.4内核下，执行“cat /proc/ksyms”，将会看到内核符号，而且在名字后还会跟随着一串校验字符串，此校验字符串与内核版本有关。在内核源码头文件linux/modules目录下存在许多*.ver文件，这些文件起着为内核符号添加校验后缀的作用，如ksyms.ver文件里有一行"#define printk _set_ver(printk)"，linux/modversions.h文件会包含所有的.ver文件。

所以当模块包含linux/modversions.h文件后，编译时，模块里使用的内核符号实质上成为带有校验后缀的内核符号。在加载模块时，如果模块使用的内核符号的校验字符串与当前运行内核所导出的相应的内核符号的校验字符串不一致，即当前内核空间并不存在模块所使用的内核符号，就会出现“Invalid module format”的错误。

Linux内核所采用的在内核符号添加校验字符串来验证模块的版本与内核的版本是否匹配的方法很复杂且会浪费内核空间，而且随着SMP、PREEMPT等机制在Linux 2.6内核的引入和完善，模块运行时对内核的依赖不再仅仅取决于内核版本，还取决于内核的配置，此时内核符号的校验码是否一致不能成为判断模块可否被加载的充分条件。

在Linux 2.6内核的linux/vermagic.h头文件中定义了“版本魔术字符串”—VERMAGIC_ STRING（如代码清单23.7所示），VERMAGIC_STRING不仅包含内核版本号，还包含内核编译所使用的GCC版本、SMP与PREEMPT等配置信息。在编译模块时，我们可以看到屏幕上会显示“MODPOST”（模块后续处理），在内核源码目录下scripts/mod/modpost.c文件中可以看到模块后续处理部分的代码。

就是在这个阶段，VERMAGIC_STRING会被添加到模块的modinfo段中，模块编译生成后，通过“modinfo mymodule.ko”命令可以查看此模块的vermagic等信息。

Linux 2.6内核下的模块装载器里保存有内核的版本信息，在装载模块时，装载器会比较所保存的内核vermagic与此模块的modinfo段里保存的vermagic信息是否一致，两者一致时，模块才能被装载。

代码清单23.7 VERMAGIC_STRING的定义

1 #ifdef CONFIG_SMP /* 配置了SMP */ 
 
 2 #define MODULE_VERMAGIC_SMP "SMP " 
 
 3 #else 
 
 4 #define MODULE_VERMAGIC_SMP "" 
 
 5 #endif 
 
 6 
 
 7 #ifdef CONFIG_PREEMPT /* 配置了PREEMPT */ 
 
 8 #define MODULE_VERMAGIC_PREEMPT "preempt " 
 
 9 #else 
 
 10 #define MODULE_VERMAGIC_PREEMPT "" 
 
 11 #endif 
 
 12 
 
 13 #ifdef CONFIG_MODULE_UNLOAD /* 支持module卸载 */ 
 
 14 #define MODULE_VERMAGIC_MODULE_UNLOAD "mod_unload " 
 
 15 #else 
 
 16 #define MODULE_VERMAGIC_MODULE_UNLOAD ""



17 #endif 
 
 18 
 
 19 #ifndef MODULE_ARCH_VERMAGIC /* 体系结构VERMAGIC */ 
 
 20 #define MODULE_ARCH_VERMAGIC "" 
 
 21 #endif 
 
 22 
 
 23 /* 拼接内核版本、上述VERMAGIC以及GCC版本 */ 
 
 24 #define VERMAGIC_STRING \ 
 
 25 UTS_RELEASE " " \ 
 
 26 MODULE_VERMAGIC_SMP MODULE_VERMAGIC_PREEMPT \ 
 
 27 MODULE_VERMAGIC_MODULE_UNLOAD MODULE_ARCH_VERMAGIC \ 
 
 28 "gcc-" _ _stringify(_ _GNUC_ _) "." _ _stringify(_ _GNUC_MINOR_ _)

在通过make menuconfig对内核进行新的配置后，再基于Linux 2.6.15.5内核编译生成的hello.ko模块（见第4章），这个模块的modinfo结果如下：

[root@localhost driver_study]# modinfo hello.ko 
 
 filename: hello.ko 
 
 license: Dual BSD/GPL 
 
 author: Song Baohua 
 
 description: A simple Hello World Module 
 
 alias: a simplest module 
 
 vermagic: 2.6.15.5 SMP preempt PENTIUM4 gcc-3.2 
 
 depends:

从中可以看出，其vermagic为“2.6.15.5 SMP preempt PENTIUM4 gcc-3.2”，运行“insmod hello.ko”命令，得到如下错误：

insmod: error inserting 'hello.ko': -1 Invalid module format 
 
 hello: version magic '2.6.15.5 SMP preempt PENTIUM4 gcc-3.2' should be '2.6.15.5 686 gcc-3.2'

原因在于加载该hello.ko时候所使用的内核虽然还是Linux 2.6.15.5，但是和编译hello.ko时的内核的关键部分配置不一样，导致vermagic不一致，发生冲突，从而加载失败。

#### 3．内核模块的加载与卸载函数

在Linux 2.6内核中，内核模块必须调用宏module_init 与module_exit()去注册初始化与退出函数。在Linux 2.4内核中，如果加载函数命名为init_module()，卸载函数命名为cleanup_module()，可以不必使用module_init与module_exit宏。因此，若使用module_init 与module_exit宏，代码在Linux 2.4内核与Linux 2.6内核中都能工作，如代码清单23.8所示。

代码清单23.8 同时支持Linux 2.4/2.6的内核模块加载/卸载函数

1 static int mod_init_func(void) 
 
 2 { 
 
 3 ... 
 
 4 return 0; 
 
 5 } 
 
 6 
 
 7 static void mod_exit_func(void) 
 
 8 { 
 
 9 ... 
 
 10 } 
 
 11 
 
 12 module_init(mod_init_func); 
 
 13 module_exit(mod_exit_func);



#### 4．内核模块使用计数

不管是在Linux 2.4内核还是在Linux 2.6内核中，当内核模块正在被使用时，是不允许被卸载的，内核模板使用计数用来反映模块的使用情况。Linux 2.4内核中，模块自身会通过MOD_INC_USE_COUNT、MOD_DEC_USE_COUNT宏来管理自己被使用的计数。Linux 2.6内核提供了更健壮、灵活的模块计数管理接口try_module_get(&module)及module_put (&module)取代Linux 2.4中的模块使用计数管理宏。而且，Linux 2.6内核下，对于为具体设备写驱动的开发人员而言，基本无须使用try_module_get()与module_put()，设备驱动框架结构中的驱动核心往往已经承担了此项工作。

#### 5．内核模块导出符号

在Linux 2.4内核下，默认情况下模块中的非静态全局变量及函数在模块加载后会输出到内核空间。而在Linux 2.6内核下，默认情况时模块中的非静态全局变量及函数在模块加载后不会输出到内核空间，需要显式调用宏EXPORT_SYMBOL才能输出。所以在Linux 2.6内核的模块下，EXPORT_NO_SYMBOLS宏的调用没有意义，是空操作。在同时支持Linux 2.4内核与Linux 2.6内核的设备驱动中，可以通过代码清单23.9来导出模块的内核符号。

代码清单23.9 同时支持Linux 2.4/2.6内核的导出内核符号代码段

1 #include <linux/module.h> 
 
 2 #ifndef LINUX26 
 
 3 EXPORT_NO_SYMBOLS; 
 
 4 #endif 
 
 5 EXPORT_SYMBOL(var); 
 
 6 EXPORT_SYMBOL(func);

另外，如果需要在Linux 2.4内核下使用EXPORT_SYMBOL，必须在CFLAGS中定义EXPORT_SYMTAB，否则编译将会失败。

从良好的代码风格角度出发，模块中不需要输出到内核空间且不需为模块中其他文件所用的全局变量及函数最好显式申明为static类型，需要输出的内核符号最好以模块名为前缀。模块加载后，Linux 2.4内核下可通过/proc/ksyms，Linux 2.6内核下可通过/proc/kallsyms查看模块输出的内核符号。

#### 6．内核模块输入参数

在Linux 2.4内核下，通过MODULE_PARM(var,type)宏来向模块传递命令行参数。var为接受参数值的变量名，type为采取如下格式的字符串[min[-max]]{b,h,i,l,s}。min及max 用于表示当参数为数组类型时，允许输入的数组元素的个数范围；b指byte，h指short，i指int，l指long，s指string。

在Linux 2.6内核下，宏MODULE_PARM(var,type)不再被支持，而是使用module_param(name, type, perm)和module_param_array(name, type, nump, perm)宏。

同样地，为了使驱动能根据内核的版本分别调用不同的宏导出内核符号，可以使用类似代码清单23.10所示的方法。

代码清单23.10 同时支持Linux 2.4/2.6的模块输入参数范例

1 #include <linux/module.h> 
 
 2 #ifdef LINUX26



3 #include <linux/moduleparam.h> 
 
 4 #endif 
 
 5 int int_param = 0; 
 
 6 char *string_param = "I love Linux"; 
 
 7 int array_param[4] = 
 
 8 { 
 
 9 1, 1, 1, 1 
 
 10 }; 
 
 11 #ifdef LINUX26 
 
 12 int len = 1; 
 
 13 #endif 
 
 14 #ifdef LINUX26 
 
 15 MODULE_PARM(int_param, "i"); 
 
 16 MODULE_PARM(string_param, "s"); 
 
 17 MODULE_PARM(array_param, "1-4i"); 
 
 18 #else 
 
 19 module_param(int_param, int, 0644); 
 
 20 module_param(string_param, charp, 0644); 
 
 21 #if LINUX_VERSION_CODE >= 
 
 22 KERNEL_VERSION(2, 6, 10) 
 
 23 module_param_array(array_param, int, 
 
 24 &len, 0644); 
 
 25 #else 
 
 26 module_param_array(array_param, int, len, 0644); 
 
 27 #endif 
 
 28 #endif

#### 7．内核模块别名、加载接口

Linux 2.6内核在linux/module.h中提供了MODULE_ALIAS(alias)宏，模块可以通过调用此宏为自己定义一个或若干个别名。而在Linux 2.4内核下，用户只能在/etc/modules.conf中为模块定义别名。

加载内核模块的接口request_module()在Linux 2.4内核下为request_module(const char * module_name)，在Linux 2.6内核下则为request_module(const char *fmt, ...)。在Linux 2.6内核下，驱动开发人员可以通过调用以下的方法来加载内核模块。

request_module("xxx"); 
 
 request_module("char-major-%d-%d", MAJOR(dev), MINOR(dev))；

#### 8．结构体初始化

在Linux 2.4内核中，习惯以代码清单23.11所示的方法来初始化结构体，即“成员:值”的方式。

代码清单23.11 Linux 2.4内核中结构体初始化习惯

1 static struct file_operations lp_fops = 
 
 2 { 
 
 3 owner: THIS_MODULE, 
 
 4 write: lp_write, 
 
 5 ioctl: lp_ioctl, 
 
 6 open: lp_open, 
 
 7 release: lp_release, 
 
 8 };

但是，在Linux 2.6内核中，为了尽量向标准C靠拢，习惯使用如代码清单23.12所示的方法来初始化结构体，即“成员=值”的方式。

代码清单23.12 Linux 2.6内核中结构体初始化习惯

1 static struct file_operations lp_fops = 
 
 2 { 
 
 3 .owner = THIS_MODULE, 
 
 4 .write = lp_write, 
 
 5 .ioctl = lp_ioctl, 
 
 6 .open = lp_open, 
 
 7 .release = lp_release, 
 
 8 };

#### 9．字符设备驱动

在Linux 2.6内核中，将Linux 2.4内核中都为8位的主次设备号分别扩展为12位和20位。鉴于此，Linux 2.4内核中的kdev_t被废除，Linux 2.6内核中新增的dev_t拓展到了32位。在Linux 2.4内核中，通过inode->i_rdev即可得到设备号，而在Linux 2.6内核中，为了增强代码的可移植性，内核中新增了iminor()和imajor()这两个函数来从inode获得设备号。

在Linux 2.6内核中，对于字符设备驱动，提供了专门用于申请/动态分配设备号的register_ chrdev_region()函数和alloc_chrdev_region()函数，而在Linux 2.4内核中，对设备号的申请和注册字符设备的行为都是在register_chrdev()函数中进行的，没有单独的cdev结构体，因此也不存在cdev_init()、cdev_add()、cdev_del()这些函数。要注意的是，register_chrdev()在Linux 2.6内核中仍然被支持，但是不能访问超过256的设备号。

其次，devfs设备文件系统在Linux 2.6内核中被取消了，因此，最新的驱动中也不宜再调用devfs_register()、devfs_unregister()这样的函数。

● proc操作。

以前的/proc中只能给出字符串，而新增的seq_file操作使得/proc中的文件能导出如long等多种数据，为了支持这一新的特性，需要实现seq_operations结构体中的seq_printf()、seq_putc()、seq_puts()、seq_escape()、seq_path()、seq_open()等成员函数。

● 内存分配。

Linux 2.4和Linux 2.6在内存分配方面发生了一些细微的变化，这些变化主要包括：

＜linux/malloc.h＞头文件被改为＜linux/slab.h＞；

分配标志GFP_BUFFER被GFP_NOIO和GFP_NOFS取代；

新增了__GFP_REPEAT、__GFP_NOFAIL和__GFP_NORETRY分配标志；

页面分配函数alloc_pages()、get_free_page()被包含在＜linux/gfp.h＞中；

对NUMA系统新增了alloc_pages_node()、free_hot_page()、free_cold_page()函数；

新增了内存池；

针对r-cpu变量的DEFINE_PER_CPU()、EXPORT_PER_CPU_SYMBOL()、EXPORT_PER_CPU_ SYMBOL_GPL()、DECLARE_PER_CPU()、DEFINE_PER_CPU()等宏因为抢占调度的出现而变得不安全，被get_cpu_var()、put_cpu_var()、alloc_percpu()、free_percpu()、per_cpu_ptr()、get_cpu_ptr()、put_cpu_ptr()等函数替换。

● 内核时间变化。

在Linux 2.6中，一些平台的节拍（Hz）发生了变化，因此引入了新的64位计数器jiffies_64，新的时间结构体timespec增加了ns成员变量，新增了add_timer_on()定时器函数，新增了ns级延时函数ndelay()。

● 并发/同步。

任务队列（task queue）接口函数都被取消，新增了work queue接口函数。

● 音频设备驱动。

Linux 2.4内核中音频设备驱动的默认框架是OSS，而Linux2.6内核中音频设备驱动的默认框架则是ALSA，这显示ALSA是一种未来的趋势。

在内核的更新过程中，大部分驱动源代码也随着内核中的API变更而修改了，如下面的列表分别摘录了linux-2.4.18和linux-2.6.15.5中的并口打印机字符设备驱动drivers/char/lp.c的源代码：

static struct file_operations lp_fops = { 
 
 
 owner: THIS_MODULE, 
 
 
 write: lp_write, 
 
 
 ioctl: lp_ioctl, 
 
 
 open: lp_open, 
 
 
 release: lp_release, 
 
 #ifdef CONFIG_PARPORT_1284 
 
 
 read: lp_read, 
 
 #endif 
 
 };

static struct file_operations lp_fops = { 
 
 
 .owner = THIS_MODULE, 
 
 
 .write = lp_write, 
 
 
 .ioctl = lp_ioctl, 
 
 
 .open = lp_open, 
 
 
 .release = lp_release, 
 
 #ifdef CONFIG_PARPORT_1284 
 
 
 .read = lp_read, 
 
 #endif 
 
 };

MODULE_PARM(parport,"1-"_ _MODULE_ STRING(LP_NO) "s");

MODULE_PARM(reset, "i");

module_param_array(parport, charp, NULL, 0);
 module_param(reset, bool, 0);

static int lp_release(struct inode 
 
 *inode, struct file *file) 
 
 { 
 
 
 unsigned int minor = MINOR(inode 
 
 
 ->i_rdev);

static int lp_release(struct inode 
 
 *inode, struct file *file) 
 
 { 
 
 
 unsigned int minor = iminor(inode);

lp_claim_parport_or_block 
 
 (&lp_table[minor]); 
 
 parport_negotiate(lp_table[minor].dev 
 
 ->port, IEEE1284_MODE_COMPAT); 
 
 lp_table[minor].current_mode = 
 
 IEEE1284_MODE_COMPAT; 
 
 lp_release_parport(&lp_table[minor]); 
 
 lock_kernel(); 
 
 kfree(lp_table[minor].lp_buffer); 
 
 lp_table[minor].lp_buffer = NULL; 
 
 LP_F(minor) &= ~LP_BUSY; 
 
 unlock_kernel(); 
 
 return 0; 
 
 }

lp_claim_parport_or_block 
 
 (&lp_table[minor]); 
 
 parport_negotiate(lp_table[minor].dev 
 
 ->port, IEEE1284_MODE_COMPAT); 
 
 lp_table[minor].current_mode = 
 
 IEEE1284_MODE_COMPAT; 
 
 lp_release_parport(&lp_table[minor]);

kfree(lp_table[minor].lp_buffer); 
 
 lp_table[minor].lp_buffer = NULL; 
 
 LP_F(minor) &= ~LP_BUSY; 
 
 return 0; 
 
 }

如果驱动源代码要同时支持Linux 2.4和Linux 2.6内核，其实也非常简单，因为通过linux/version.h中的LINUX_VERSION_CODE可以获知内核版本，之后便可以针对不同的宏定义实现不同的驱动源代码，如代码清单23.13所示。



代码清单23.13 同时支持Linux 2.4和Linux 2.6内核的驱动编写方法

1 #include <linux/version.h> 
 
 2 #if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 0) 
 
 3 #define LINUX26 
 
 4 #endif 
 
 5 #ifdef LINUX26 
 
 6 /*Linux 2.6内核中的代码*/ 
 
 7 #else 
 
 8 /*Linux 2.4内核中的代码 */ 
 
 9 #endif

![BZ___637_134_449_211_525.png](../images/BZ___637_134_449_211_525.png)
除了Linux 2.4和Linux2.6之间内核的变更较大以外，Linux 2.6的各个小版本向前推进的时候，驱动的架构也可能发生较大的变动，可以这么说，几乎在不断变动中，这是Linux官方内核演进的特点。因此，运行于2.6.x的驱动不一定能运行于2.6.y，这些时候，我们要注意这两个版本之前的差异，并进行相应的修改。

