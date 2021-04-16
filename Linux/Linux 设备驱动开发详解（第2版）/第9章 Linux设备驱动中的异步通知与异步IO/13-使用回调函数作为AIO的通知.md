### 9.4.3 使用回调函数作为AIO的通知

除了信号之外，应用程序还可提供一个回调（Callback）函数给内核，以便AIO的请求完成后内核调用这个函数。

代码清单9.16给出了使用回调函数作为AIO异步I/O请求完成的通知机制的例子。

代码清单9.16 使用回调函数作为AIO异步I/O通知机制例程

1 /*设置异步I/O请求*/ 
 
 2 void setup_io(...) 
 
 3 { 
 
 4 int fd; 
 
 5 struct aiocb my_aiocb; 
 
 6 ... 
 
 7 /* 设置AIO请求 */ 
 
 8 bzero((char*) &my_aiocb, sizeof(struct aiocb)); 
 
 9 my_aiocb.aio_fildes = fd; 
 
 10 my_aiocb.aio_buf = malloc(BUF_SIZE + 1); 
 
 11 my_aiocb.aio_nbytes = BUF_SIZE; 
 
 12 my_aiocb.aio_offset = next_offset; 
 
 13 
 
 14 /* 连接AIO请求和线程回调函数 */ 
 
 15 my_aiocb.aio_sigevent.sigev_notify = SIGEV_THREAD; 
 
 16 my_aiocb.aio_sigevent.notify_function = aio_completion_handler; 
 
 17 /*设置回调函数*/ 
 
 18 my_aiocb.aio_sigevent.notify_attributes = NULL; 
 
 19 my_aiocb.aio_sigevent.sigev_value.sival_ptr = &my_aiocb; 
 
 20 ... 
 
 21 ret = aio_read(&my_aiocb); /* 发起AIO请求*/ 
 
 22 } 
 
 23 
 
 24 /* 异步I/O完成回调函数 */ 
 
 25 void aio_completion_handler(sigval_t sigval) 
 
 26 { 
 
 27 struct aiocb *req; 
 
 28 req = (struct aiocb*)sigval.sival_ptr; 
 
 29 
 
 30 /* AIO请求完成? */ 
 
 31 if (aio_error(req) == 0) 
 
 32 /* 请求完成，获得返回值 */ 
 
 33 ret = aio_return(req); 
 
 34 }

上述程序在创建aiocb请求之后，使用SIGEV_THREAD请求了一个线程回调函数来作为通知方法。在回调函数中，通过(struct aiocb*)sigval.sival_ptr可以获得对应的aiocb指针，使用AIO函数可验证请求是否已经完成。

proc文件系统包含了两个虚拟文件，它们可以用来对异步I/O的性能进行优化。

（1）/proc/sys/fs/aio-nr文件提供了系统范围异步I/O请求现在的数目。

（2）/proc/sys/fs/aio-max-nr文件是所允许的并发请求的最大个数，最大个数通常是64KB，这对于大部分应用程序来说都已经足够了。

