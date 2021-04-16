### 8.3.2 在用户空间验证globalfifo设备的轮询

编写一个应用程序pollmonitor.c用于监控globalfifo的可读写状态，这个程序如代码清单8.13所示。

代码清单8.13 监控globalfifo是否可非阻塞读写的应用程序

1 #include ... 
 
 2 
 
 3 #define FIFO_CLEAR 0x1 
 
 4 #define BUFFER_LEN 20 
 
 5 main() 
 
 6 { 
 
 7 int fd, num; 
 
 8 char rd_ch[BUFFER_LEN]; 
 
 9 fd_set rfds,wfds; /* 读/写文件描述符集 
 
 10 
 
 11 /*以非阻塞方式打开/dev/globalfifo设备文件*/ 
 
 12 fd = open("/dev/globalfifo", O_RDONLY | O_NONBLOCK); 
 
 13 if (fd != - 1) { 
 
 14 /*FIFO清0*/ 
 
 15 if (ioctl(fd, FIFO_CLEAR, 0) < 0) 
 
 16 printf("ioctl command failed\n"); 
 
 17 
 
 18 while (1) { 
 
 19 FD_ZERO(&rfds); 
 
 20 FD_ZERO(&wfds); 
 
 21 FD_SET(fd, &rfds); 
 
 22 FD_SET(fd, &wfds); 
 
 23 
 
 24 select(fd + 1, &rfds, &wfds, NULL, NULL); 
 
 25 /*数据可获得*/ 
 
 26 if (FD_ISSET(fd, &rfds))



27 printf("Poll monitor:can be read\n"); 
 
 28 /*数据可写入*/ 
 
 29 if (FD_ISSET(fd, &wfds)) 
 
 30 printf("Poll monitor:can be written\n"); 
 
 31 } 
 
 32 } else { 
 
 33 printf("Device open failure\n"); 
 
 34 } 
 
 35 }

运行时看到，到没有任何输入，即FIFO为空时，程序不断地输出“Poll monitor:can be written”，当通过echo向/dev/globalfifo写入一些数据后，将输出“Poll monitor:can be read”和“Poll monitor:can be written”，如果不断地通过echo向/dev/globalfifo写入数据直至写满FIFO，发现pollmonitor程序将只输出“Poll monitor:can be read”。对于globalfifo而言，不会出现既不能读、又不能写的情况。

