### 8.1.3 在用户空间验证globalfifo的读写

/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/drivers/globalfifo/ch8包含了globalfifo的驱动，运行“make”命令编译得到globalfifo.ko。接着insmod模块：

lihacker@lihacker-laptop:~/develop/svn/ldd6410-read-only/training/kernel/drivers/gl 
 
 obalfifo/ch8$ 
 sudo su

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/ 
 
 drivers/globalfifo/ch8# 
 insmod globalfifo.ko

创建设备文件节点“/dev/globalfifo”：

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/ 
 
 drivers/globalfifo/ch8# mknod /dev/globalfifo c 249 0

启动两个进程，一个进程“cat /dev/globalfifo&”在后台执行，一个进程“echo字符串 /dev/globalfifo”在前台执行：

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/ 
 
 drivers/globalfifo/ch8# 
 cat /dev/globalfifo & 
 
 [1] 20910

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/ 
 
 drivers/globalfifo/ch8# 
 echo 'I want to be' > /dev/globalfifo 
 
 
 I want to be

root@lihacker-laptop:/home/lihacker/develop/svn/ldd6410-read-only/training/kernel/ 
 
 drivers/globalfifo/ch8# echo 'a great Chinese Linux driver Engineer' > /dev/globalfifo 
 
 
 a great Chinese Linux driver Engineer

每当echo进程向/dev/globalfifo写入一串数据，cat进程就立即将该串数据显现出来，好的，让我们抱着这个信念“I want to be a great Chinese Linux driver Engineer”继续前行吧！



