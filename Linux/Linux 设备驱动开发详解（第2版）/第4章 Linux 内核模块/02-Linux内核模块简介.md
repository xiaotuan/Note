### 4.1 Linux内核模块简介

Linux内核的整体结构已经非常庞大，而其包含的组件也非常多。我们怎样把需要的部分都包含在内核中呢？

一种方法是把所有需要的功能都编译到Linux内核。这会导致两个问题，一是生成的内核会很大，二是如果我们要在现有的内核中新增或删除功能，将不得不重新编译内核。

有没有一种机制使得编译出的内核本身并不需要包含所有功能，而在这些功能需要被使用的时候，其对应的代码被动态地加载到内核中呢？

Linux提供了这样的一种机制，这种机制被称为模块（Module）。模块具有这样的特点。

● 模块本身不被编译入内核映像，从而控制了内核的大小。

● 模块一旦被加载，它就和内核中的其他部分完全一样。

为了使读者建立对模块的初步感性认识，我们先来看一个最简单的内核模块“Hello World”，如代码清单4.1所示。

代码清单4.1 一个最简单的Linux内核模块

1 #include <linux/init.h> 
 
 2 #include <linux/module.h> 
 
 3 
 
 4 static int hello_init(void) 
 
 5 { 
 
 6 printk(KERN_INFO " Hello World enter\n"); 
 
 7 return 0; 
 
 8 } 
 
 9 
 
 10 static void hello_exit(void) 
 
 11 { 
 
 12 printk(KERN_INFO " Hello World exit\n "); 
 
 13 } 
 
 14 
 
 15 module_init(hello_init); 
 
 16 module_exit(hello_exit); 
 
 17 
 
 18 MODULE_AUTHOR("Barry Song <21cnbao@gmail.com>"); 
 
 19 MODULE_LICENSE("Dual BSD/GPL"); 
 
 20 MODULE_DESCRIPTION("A simple Hello World Module"); 
 
 21 MODULE_ALIAS("a simplest module");

这个最简单的内核模块只包含内核模块加载函数、卸载函数和对Dual BSD/GPL许可权限的声明以及一些描述信息，位于本书配套光盘VirtualBox虚拟机映像的/home/lihacker/develop/ svn/ldd6410-read-only/training/kernel/drivers/hello目录。编译它会产生hello.ko目标文件，通过“insmod ./hello.ko”命令可以加载它，通过“rmmod hello”命令可以卸载它，加载时输出“Hello World enter”，卸载时输出“Hello World exit”。

内核模块中用于输出的函数是内核空间的printk()而非用户空间的printf()，printk()的用法和printf()基本相似，但前者可定义输出级别。printk()可作为一种最基本的内核调试手段，在Linux驱动的调试章节中将详细讲解这个函数。

在Linux中，使用lsmod命令可以获得系统中加载了的所有模块以及模块间的依赖关系，例如：

Module Size Used by 
 
 hello 9 472 0 
 
 nls_iso8859_1 12 032 1 
 
 nls_cp437 13 696 1 
 
 vfat 18 816 1 
 
 fat 57 376 1 vfat 
 
 ...

lsmod命令实际上读取并分析“/proc/modules”文件，与上述lsmod命令结果对应的“/proc/modules”文件如下：

lihacker@lihacker-laptop:～/$ cat /proc/modules 
 
 hello 9472 0 - Live 0xf953b000 
 
 nls_iso8859_1 12032 1 - Live 0xf950c000 
 
 nls_cp437 13696 1 - Live 0xf9561000 
 
 vfat 18816 1 - Live 0xf94f3000 
 
 ...

内核中已加载模块的信息也存在于/sys/module目录下，加载hello.ko后，内核中将包含/sys/module/hello目录，该目录下又包含一个refcnt文件和一个sections目录，在/sys/module/hello目录下运行“tree –a”得到如下目录树：

lihacker@lihacker-laptop:/sys/module/hello$ tree -a 
 
 . 
 
 |-- holders 
 
 |-- initstate 
 
 |-- notes 
 
 | '-- .note.gnu.build-id 
 
 |-- refcnt 
 
 |-- sections 
 
 | |-- .bss 
 
 | |-- .data 
 
 | |-- .gnu.linkonce.this_module 
 
 | |-- .note.gnu.build-id 
 
 | |-- .rodata.str1.1 
 
 | |-- .strtab 
 
 | |-- .symtab 
 
 | '-- .text 
 
 '-- srcversion 
 
 3 directories, 12 files

modprobe命令比insmod命令要强大，它在加载某模块时，会同时加载该模块所依赖的其他模块。使用modprobe命令加载的模块若以“modprobe -r filename”的方式卸载将同时卸载其依赖的模块。

使用modinfo <模块名>命令可以获得模块的信息，包括模块作者、模块的说明、模块所支持的参数以及vermagic：

lihacker@lihacker-laptop:～/develop/svn/ldd6410-read-only/training/kernel/drivers/ 
 
 hello$ modinfo hello.ko 
 
 filename: hello.ko 
 
 alias: a simplest module 
 
 description: A simple Hello World Module 
 
 license: Dual BSD/GPL



author: Barry Song <21cnbao@gmail.com> 
 
 srcversion: 3FE9B0FBAFDD565399B9C05 
 
 depends: 
 
 vermagic: 2.6.28-11-generic SMP mod_unload modversions 586

