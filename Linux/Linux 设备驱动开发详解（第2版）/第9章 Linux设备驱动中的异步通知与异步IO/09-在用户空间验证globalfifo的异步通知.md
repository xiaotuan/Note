### 9.3.2 在用户空间验证globalfifo的异步通知

现在，我们可以采用与代码清单9.2类似的方法，编写一个在用户空间验证globalfifo异步通知的程序，这个程序在接收到由globalfifo发出的信号后将输出信号值，如代码清单9.11所示。

代码清单9.11 监控globalfifo异步通知信号的应用程序

1 #include ... 
 
 2 
 
 3 /*接收到异步读信号后的动作*/ 
 
 4 void input_handler(int signum) 
 
 5 { 
 
 6 printf("receive a signal from globalfifo,signalnum:%d\n",signum); 
 
 7 } 
 
 8 
 
 9 main() 
 
 10 { 
 
 11 int fd, oflags; 
 
 12 fd = open("/dev/globalfifo", O_RDWR, S_IRUSR | S_IWUSR); 
 
 13 if (fd != - 1) { 
 
 14 /* 启动信号驱动机制 */ 
 
 15 signal(SIGIO, input_handler); /* 让input_handler()处理SIGIO信号 */ 
 
 16 fcntl(fd, F_SETOWN, getpid()); 
 
 17 oflags = fcntl(fd, F_GETFL); 
 
 18 fcntl(fd, F_SETFL, oflags | FASYNC); 
 
 19 while(1) { 
 
 20 sleep(100); 
 
 21 } 
 
 22 } else {



23 printf("device open failure\n"); 
 
 24 } 
 
 25 }

/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/drivers/globalfifo/ch9包含了支持异步通知的globalfifo驱动以及代码清单9.11对应的globalfifo_test.c测试程序，在该目录运行make将得到globalfifo.ko和globalfifo_test：

lihacker@lihacker-laptop:～/develop/svn/ldd6410-read-only/training/kernel/drivers/ 
 
 globalfifo/ch9$ make 
 
 make -C /lib/modules/2.6.28-11-generic/build M=/home/lihacker/develop/svn/ldd6410- 
 
 read-only/training/kernel/drivers/globalfifo/ch9 modules 
 
 make[1]: Entering directory `/usr/src/linux-headers-2.6.28-11-generic' 
 
 CC [M] /home/lihacker/develop/svn/ldd6410-read-only/training/kernel/drivers/globalfifo/ 
 
 ch9/globalfifo.o 
 
 Building modules, stage 2. 
 
 MODPOST 1 modules 
 
 CC /home/lihacker/develop/svn/ldd6410-read-only/training/kernel/drivers/globalfifo/ 
 
 ch9/globalfifo.mod.o 
 
 LD [M] /home/lihacker/develop/svn/ldd6410-read-only/training/kernel/drivers/globalfifo/ 
 
 ch9/globalfifo.ko 
 
 make[1]: Leaving directory '/usr/src/linux-headers-2.6.28-11-generic' 
 
 gcc -o globalfifo_test globalfifo_test.c

按照与8.3.2节相同的方法加载新的globalfifo设备驱动并创建设备文件节点，运行上述程序，每当通过echo向/dev/globalfifo写入新的数据时，input_handler()将会被调用：

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalfifo/ch9# ./globalfifo_test& 
 
 [1] 25251

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalfifo/ch9# 
 echo 1 > /dev/globalfifo 
 
 
 receive a signal from globalfifo,signalnum:29 
 
 root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/d 
 
 rivers/globalfifo/ch9# 
 echo hello > /dev/globalfifo 
 
 
 receive a signal from globalfifo,signalnum:29

