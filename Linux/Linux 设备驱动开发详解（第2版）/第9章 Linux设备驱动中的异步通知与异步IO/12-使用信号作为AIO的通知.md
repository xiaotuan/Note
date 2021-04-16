### 9.4.2 使用信号作为AIO的通知

9.1～9.3节讲述的信号作为异步通知的机制在AIO中仍然是适用的，为使用信号，使用AIO的应用程序同样需要定义信号处理程序，在指定的信号被产生时会触发调用这个处理程序。作为信号上下文的一部分，特定的aiocb请求被提供给信号处理函数用来区分AIO请求。

代码清单9.15给出了使用信号作为AIO异步I/O通知机制的例子。



代码清单9.15 使用信号作为AIO异步I/O通知机制例程

1 /*设置异步I/O请求*/ 
 
 2 void setup_io(...) 
 
 3 { 
 
 4 int fd; 
 
 5 struct sigaction sig_act; 
 
 6 struct aiocb my_aiocb; 
 
 7 ... 
 
 8 /* 设置信号处理函数 */ 
 
 9 sigemptyset(&sig_act.sa_mask); 
 
 10 sig_act.sa_flags = SA_SIGINFO; 
 
 11 sig_act.sa_sigaction = aio_completion_handler; 
 
 12 
 
 13 /* 设置AIO请求 */ 
 
 14 bzero((char*) &my_aiocb, sizeof(struct aiocb)); 
 
 15 my_aiocb.aio_fildes = fd; 
 
 16 my_aiocb.aio_buf = malloc(BUF_SIZE + 1); 
 
 17 my_aiocb.aio_nbytes = BUF_SIZE; 
 
 18 my_aiocb.aio_offset = next_offset; 
 
 19 
 
 20 /* 连接AIO请求和信号处理函数 */ 
 
 21 my_aiocb.aio_sigevent.sigev_notify = SIGEV_SIGNAL; 
 
 22 my_aiocb.aio_sigevent.sigev_signo = SIGIO; 
 
 23 my_aiocb.aio_sigevent.sigev_value.sival_ptr = &my_aiocb; 
 
 24 
 
 25 /* 将信号与信号处理函数绑定 */ 
 
 26 ret = sigaction(SIGIO, &sig_act, NULL); 
 
 27 ... 
 
 28 ret = aio_read(&my_aiocb); /*发出异步读请求*/ 
 
 29 } 
 
 30 
 
 31 /*信号处理函数*/ 
 
 32 void aio_completion_handler(int signo, siginfo_t *info, void *context) 
 
 33 { 
 
 34 struct aiocb *req; 
 
 35 
 
 36 /* 确定是我们需要的信号*/ 
 
 37 if (info->si_signo == SIGIO) { 
 
 38 req = (struct aiocb*)info->si_value.sival_ptr; /*获得aiocb*/ 
 
 39 
 
 40 /* 请求的操作完成了吗? */ 
 
 41 if (aio_error(req) == 0) { 
 
 42 /* 请求的操作完成，获取返回值 */ 
 
 43 ret = aio_return(req); 
 
 44 } 
 
 45 } 
 
 46 }

特别要注意上述代码的第38行通过(struct aiocb*)info->si_value.sival_ptr获得了信号对应的aiocb。

