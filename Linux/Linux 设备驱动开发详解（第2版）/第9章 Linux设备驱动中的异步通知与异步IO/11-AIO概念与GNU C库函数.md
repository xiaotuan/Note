### 9.4.1 AIO概念与GNU C库函数

Linux中最常用的输入/输出（I/O）模型是同步I/O。在这个模型中，当请求发出之后，应用程序就会阻塞，直到请求满足为止。这是很好的一种解决方案，因为调用应用程序在等待I/O请求完成时不需要占用CPU。但是在某些情况中，I/O请求可能需要与其他进程产生交叠。可移植操作系统接口（POSIX）异步I/O（AIO）应用程序接口（API）就提供了这种功能。

Linux异步I/O是2.6版本内核的一个标准特性，但是我们在2.4版本内核的补丁中也可以找到它。AIO基本思想是允许进程发起很多I/O操作，而不用阻塞或等待任何操作完成。稍后或在接收到I/O操作完成的通知时，进程再检索I/O操作的结果。

select()函数所提供的功能（异步阻塞 I/O）与AIO类似，它对通知事件进行阻塞，而不是对I/O调用进行阻塞。

在异步非阻塞I/O中，我们可以同时发起多个传输操作。这需要每个传输操作都有惟一的上下文，这样才能在它们完成时区分到底是哪个传输操作完成了。在AIO中，通过aiocb（AIO I/O Control Block）结构体进行区分。这个结构体包含了有关传输的所有信息，以及为数据准备的用户缓冲区。在产生I/O通知（称为完成）时，aiocb结构就被用来惟一标识所完成的I/O操作。

AIO系列API被GNU C库函数所包含，它被POSIX.1b所要求，主要包括如下函数。

#### 1．aio_read

aio_read()函数请求对一个有效的文件描述符进行异步读操作。这个文件描述符可以表示一个文件、套接字甚至管道。aio_read函数的原型如下：

int aio_read( struct aiocb *aiocbp );

aio_read()函数在请求进行排队之后会立即返回。如果执行成功，返回值就为0；如果出现错误，返回值就为−1，并设置errno的值。

#### 2．aio_write

aio_write()函数用来请求一个异步写操作。其函数原型如下：

int aio_write( struct aiocb *aiocbp );

aio_write()函数会立即返回，说明请求已经进行排队（成功时返回值为0，失败时返回值为−1，并相应地设置errno。

#### 3．aio_error

aio_error()函数被用来确定请求的状态。其原型如下：

int aio_error( struct aiocb *aiocbp );

这个函数可以返回以下内容。

EINPROGRESS：说明请求尚未完成。

ECANCELLED：说明请求被应用程序取消了。

−1：说明发生了错误，具体错误原因由errno记录。

#### 4．aio_return

异步I/O和标准I/O方式之间的另外一个区别是不能立即访问这个函数的返回状态，因为异步I/O并没有阻塞在read()调用上。在标准的read()调用中，返回状态是在该函数返回时提供的。但是在异步I/O中，我们要使用aio_return()函数。这个函数的原型如下：

ssize_t aio_return( struct aiocb *aiocbp );

只有在aio_error()调用确定请求已经完成（可能成功，也可能发生了错误）之后，才会调用这个函数。aio_return()的返回值就等价于同步情况中read或write系统调用的返回值（所传输的字节数，如果发生错误，返回值为负数）。

代码清单9.12给出了用户空间应用程序进行异步读操作的一个例程，它首先打开文件，然后准备aiocb结构体，之后调用aio_read(&my_aiocb)进行提出异步读请求，当aio_error(&my_aiocb) == EINPROGRESS即操作还在进行中时，一直等待，结束后通过aio_return(&my_aiocb)获得返回值。

代码清单9.12 用户空间异步读例程

1 #include <aio.h> 
 
 2 ...



3 int fd, ret; 
 
 4 struct aiocb my_aiocb; 
 
 5 
 
 6 fd = open("file.txt", O_RDONLY); 
 
 7 if (fd < 0) 
 
 8 perror("open"); 
 
 9 
 
 10 /* 清零aiocb结构体 */ 
 
 11 bzero((char*) &my_aiocb, sizeof(struct aiocb)); 
 
 12 
 
 13 /* 为aiocb请求分配数据缓冲区 */ 
 
 14 my_aiocb.aio_buf = malloc(BUFSIZE + 1); 
 
 15 if (!my_aiocb.aio_buf) 
 
 16 perror("malloc"); 
 
 17 
 
 18 /* 初始化aiocb的成员 */ 
 
 19 my_aiocb.aio_fildes = fd; 
 
 20 my_aiocb.aio_nbytes = BUFSIZE; 
 
 21 my_aiocb.aio_offset = 0; 
 
 22 
 
 23 ret = aio_read(&my_aiocb); 
 
 24 if (ret < 0) 
 
 25 perror("aio_read"); 
 
 26 
 
 27 while (aio_error(&my_aiocb) == EINPROGRESS) 
 
 28 continue; 
 
 29 
 
 30 if ((ret = aio_return(&my_iocb)) > 0) { 
 
 31 /* 获得异步读的返回值 */ 
 
 32 } else { 
 
 33 /* 读失败，分析errorno */ 
 
 34 }

#### 5．aio_suspend

用户可以使用aio_suspend()函数来挂起（或阻塞）调用进程，直到异步请求完成为止，此时会产生一个信号，或者发生其他超时操作。调用者提供了一个aiocb引用列表，其中任何一个完成都会导致aio_suspend()返回。aio_suspend的函数原型如下：

int aio_suspend( const struct aiocb *const cblist[], 
 
 int n, const struct timespec *timeout );

代码清单9.13给出了用户空间异步读操作时使用aio_suspend()函数的例子。

代码清单9.13 用户空间异步I/O aio_suspend()函数使用例程

1 struct aioct *cblist[MAX_LIST] 
 
 2 /* 清零aioct结构体链表 */ 
 
 3 bzero( (char *)cblist, sizeof(cblist) ); 
 
 4 /* 将一个或更多的aiocb放入aioct结构体链表 */ 
 
 5 cblist[0] = &my_aiocb; 
 
 6 ret = aio_read( &my_aiocb ); 
 
 7 ret = aio_suspend( cblist, MAX_LIST, NULL );

#### 6．aio_cancel

aio_cancel()函数允许用户取消对某个文件描述符执行的一个或所有I/O请求。其原型如下：

int aio_cancel( int fd, struct aiocb *aiocbp );

要取消一个请求，用户需提供文件描述符和aiocb指针。如果这个请求被成功取消了，那么这个函数就会返回AIO_CANCELED。如果请求完成了，这个函数就会返回 AIO_NOTCANCELED。

要取消对某个给定文件描述符的所有请求，用户需要提供这个文件的描述符，并将aiocbp参数设置为NULL。如果所有的请求都取消了，这个函数就会返回AIO_CANCELED；如果至少有一个请求没有被取消，那么这个函数就会返回 AIO_NOT_CANCELED；如果没有一个请求可以被取消，那么这个函数就会返回AIO_ALLDONE。然后，可以使用aio_error()来验证每个 AIO 请求，如果某请求已经被取消了，那么aio_error()就会返回−1，并且errno会被设置为ECANCELED。

#### 7．lio_listio

lio_listio()函数可用于同时发起多个传输。这个函数非常重要，它使得用户可以在一个系统调用（一次内核上下文切换）中启动大量的I/O操作。lio_listio API函数的原型如下：

int lio_listio( int mode, struct aiocb *list[], int nent, struct sigevent *sig );

mode参数可以是LIO_WAIT或LIO_NOWAIT。LIO_WAIT会阻塞这个调用，直到所有的 I/O都完成为止。在操作进行排队之后，LIO_NOWAIT就会返回。list是一个aiocb引用的列表，最大元素的个数是由nent定义的。如果list的元素为NULL，lio_listio()会将其忽略。

代码清单9.14给出了用户空间异步I/O操作时使用lio_listio()函数的例子。

代码清单9.14 用户空间异步I/O lio_listio()函数使用例程

1 struct aiocb aiocb1, aiocb2; 
 
 2 struct aiocb *list[MAX_LIST]; 
 
 3 ... 
 
 4 /* 准备第一个aiocb */ 
 
 5 aiocb1.aio_fildes = fd; 
 
 6 aiocb1.aio_buf = malloc( BUFSIZE+1 ); 
 
 7 aiocb1.aio_nbytes = BUFSIZE; 
 
 8 aiocb1.aio_offset = next_offset; 
 
 9 aiocb1.aio_lio_opcode = LIO_READ; /*异步读操作*/ 
 
 10 ... /*准备多个aiocb */ 
 
 11 bzero( (char *)list, sizeof(list) ); 
 
 12 
 
 13 /*将aiocb填入链表*/ 
 
 14 list[0] = &aiocb1; 
 
 15 list[1] = &aiocb2; 
 
 16 ... 
 
 17 ret = lio_listio( LIO_WAIT, list, MAX_LIST, NULL );/*发起大量I/O操作*/

上述代码第9行中，因为是进行异步读操作，所以操作码为LIO_READ，对于写操作来说，应该使用LIO_WRITE作为操作码，而LIO_NOP意味着空操作。

网页http://www.gnu.org/software/libc/manual/html_node/Asynchronous-I_002fO.html包含了AIO库函数的详细信息。

