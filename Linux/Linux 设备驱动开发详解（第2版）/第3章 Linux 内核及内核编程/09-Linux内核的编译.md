### 3.4.1 Linux内核的编译

Linux驱动工程师需要牢固地掌握Linux内核的编译方法以为嵌入式系统构建可运行的Linux操作系统映像。在编译LDD6410的内核时，需要配置内核，可以使用下面命令中的一个：

#make config（基于文本的最为传统的配置界面，不推荐使用） 
 
 #make menuconfig（基于文本菜单的配置界面） 
 
 #make xconfig（要求QT被安装） 
 
 #make gconfig（要求GTK+被安装）

在配置Linux 2.6内核所使用的make config、make menuconfig、make xconfig和make gconfig 这4种方式中，最值得推荐的是make menuconfig，它不依赖于QT或GTK+，且非常直观，对LDD6410的Linux 2.6.28内核运行make menuconfig后的界面如图3.6。



![P80_39483.jpg](../images/P80_39483.jpg)
内核配置包含的项目相当多，arch/arm/configs/ldd6410lcd_defconfig文件包含了LDD6410的默认配置，因此，只需要运行make ldd6410lcd_defconfig就可以为LDD6410开发板配置内核。

编译内核和模块的方法是：

make zImage 
 
 make modules

执行完上述命令后，在源代码的根目录下会得到未压缩的内核映像vmlinux和内核符号表文件System.map，在arch/arm/boot/目录会得到压缩的内核映像zImage，在内核各对应目录得到选中的内核模块。

Linux 2.6内核的配置系统由以下3个部分组成。

● Makefile：分布在Linux内核源代码中的Makefile，定义Linux内核的编译规则。

● 配置文件（Kconfig）：给用户提供配置选择的功能。

● 配置工具：包括配置命令解释器（对配置脚本中使用的配置命令进行解释）和配置用户界面（提供基于字符界面和图形界面）。这些配置工具都是使用脚本语言，如Tcl/TK、Perl等编写。

使用make config、make menuconfig等命令后，会生成一个.config配置文件，记录哪些部分被编译入内核、哪些部分被编译为内核模块。

运行make menuconfig等时，配置工具首先分析与体系结构对应的/arch/xxx/Kconfig文件（xxx即为传入的ARCH参数），/arch/xxx/Kconfig文件中除本身包含一些与体系结构相关的配置项和配置菜单以外，还通过source语句引入了一系列Kconfig文件，而这些Kconfig又可能再次通过source引入下一层的Kconfig，配置工具依据这些Kconfig包含的菜单和项目即可描绘出一个如图3.6所示的分层结构。例如，/arch/arm/Kconfig文件的结构如下：

mainmenu "Linux Kernel Configuration" 
 
 config ARM 
 
 bool 
 
 default y 
 
 select HAVE_AOUT



select HAVE_IDE 
 
 select RTC_LIB 
 
 select SYS_SUPPORTS_APM_EMULATION 
 
 select HAVE_OPROFILE 
 
 select HAVE_ARCH_KGDB 
 
 select HAVE_KPROBES if (!XIP_KERNEL) 
 
 select HAVE_KRETPROBES if (HAVE_KPROBES) 
 
 select HAVE_FUNCTION_TRACER if (!XIP_KERNEL) 
 
 select HAVE_GENERIC_DMA_COHERENT 
 
 help 
 
 The ARM series is a line of low-power-consumption RISC chip designs 
 
 licensed by ARM Ltd and targeted at embedded applications and 
 
 handhelds such as the Compaq IPAQ. ARM-based PCs are no longer 
 
 manufactured, but legacy ARM-based PC hardware remains popular in 
 
 Europe. There is an ARM Linux project with a web page at 
 
 <http://www.arm.linux.org.uk/>.

... 
 
 config MMU 
 
 bool 
 
 default y

... 
 
 config ARCH_S3C64XX 
 
 bool "Samsung S3C64XX" 
 
 select GENERIC_GPIO 
 
 select HAVE_CLK 
 
 help 
 
 Samsung S3C64XX series based systems 
 
 ... 
 
 if ARCH_S3C64XX 
 
 source "arch/arm/mach-s3c6400/Kconfig" 
 
 source "arch/arm/mach-s3c6410/Kconfig" 
 
 endif

...

