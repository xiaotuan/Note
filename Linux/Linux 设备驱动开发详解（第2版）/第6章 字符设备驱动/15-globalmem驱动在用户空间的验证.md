### 6.4 globalmem驱动在用户空间的验证

在对应目录通过“make”命令编译globalmem的驱动，得到globalmem.ko文件。运行：

lihacker@lihacker-laptop:～/develop/svn/ldd6410-read-only/training/kernel/drivers/ 
 
 globalmem/ch6$ 
 sudo su

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalmem/ch6# 
 insmod globalmem.ko

命令加载模块，通过“lsmod”命令，发现globalmem模块已被加载。再通过“cat /proc/devices”命令查看，发现多出了主设备号为250的“globalmem”字符设备驱动：

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalmem/ch6# 
 cat /proc/devices 
 
 Character devices: 
 
 1 mem 
 
 4 /dev/vc/0



4 tty 
 
 4 ttyS 
 
 5 /dev/tty 
 
 5 /dev/console 
 
 5 /dev/ptmx 
 
 6 lp 
 
 7 vcs 
 
 10 misc 
 
 13 input 
 
 14 sound 
 
 21 sg 
 
 29 fb 
 
 99 ppdev 
 
 108 ppp 
 
 116 alsa 
 
 128 ptm 
 
 136 pts 
 
 180 usb 
 
 188 ttyUSB 
 
 189 usb_device 
 
 216 rfcomm 
 
 226 drm 
 
 
 250 globalmem

接下来，通过命令：

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalmem/ch6# 
 mknod /dev/globalmem c 250 0

创建“/dev/globalmem”设备节点，并通过“echo 'hello world' > /dev/globalmem”命令和“cat /dev/globalmem”命令分别验证设备的写和读，结果证明“hello world”字符串被正确地写入globalmem字符设备：

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalmem/ch6# 
 echo "hello world" > /dev/globalmem

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalmem/ch6# 
 cat /dev/globalmem 
 
 hello world

如果启用了sysfs文件系统，将发现多出了/sys/module/globalmem目录，该目录下的树型结构为：

|-- refcnt 
 
 '-- sections 
 
 |-- .bss 
 
 |-- .data 
 
 |-- .gnu.linkonce.this_module 
 
 |-- .rodata 
 
 |-- .rodata.str1.1 
 
 |-- .strtab 
 
 |-- .symtab 
 
 |-- .text 
 
 '-- _ _versions

refcnt记录了globalmem模块的引用计数，sections下包含的数个文件则给出了globalmem所包含的BSS、数据段和代码段等的地址及其他信息。

对于代码清单6.18给出的支持两个globalmem设备的驱动，在加载模块后需创建两个设备节点，/dev/globalmem0对应主设备号globalmem_major，次设备号0，/dev/globalmem1对应主设备号globalmem_major，次设备号1。分别读写/dev/globalmem0和/dev/globalmem1，发现都读写到了正确的对应的设备。

