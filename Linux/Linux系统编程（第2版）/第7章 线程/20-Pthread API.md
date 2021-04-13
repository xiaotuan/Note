### 7.7.2　Pthread API

Pthread API定义了构建一个多线程程序需要的方方面面——虽然是在很底层做的。Pthread API提供了100多个接口，因此还是很庞大的。由于Pthread API过于庞大和丑陋，Pthreads也有不少骂声。但是，它依然是UNIX系统上核心的线程库，即使使用不同的线程机制，Pthreads还是值得一学的，因为很多都是构建在Pthreads上的。

Pthread API在文件<pthread.h>中定义。API中的每个函数前缀都是pthread_。举个例子，创建线程的函数称为pthread_create()（我们将很快学到，在7.7.4节）。Pthread函数可以划分成两个大的分组：

线程管理

完成创建、销毁、连接和datach线程的函数。我们将在本章探讨这些。

同步

管理线程的同步的函数，包括互斥、条件变量和障碍。我们将在本节探讨互斥。

