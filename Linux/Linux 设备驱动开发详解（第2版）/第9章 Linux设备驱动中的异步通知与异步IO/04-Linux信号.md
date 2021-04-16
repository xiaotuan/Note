### 9.2.1 Linux信号

使用信号进行进程间通信（IPC）是UNIX中的一种传统机制，Linux也支持这种机制。在Linux中，异步通知使用信号来实现，Linux中可用的信号及其定义如表9-1所示。



**表9-1 Linux信号**

| 信 号 | 值 | 含 义 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| SIGHUP | 1 | 挂起 |
| SIGINT | 2 | 终端中断 |
| SIGQUIT | 3 | 终端退出 |
| SIGILL | 4 | 无效命令 |
| SIGTRAP | 5 | 跟踪陷阱 |
| SIGIOT | 6 | IOT陷阱 |
| SIGBUS | 7 | BUS错误 |
| SIGFPE | 8 | 浮点异常 |
| SIGKILL | 9 | 强行终止（不能被捕获或忽略） |
| SIGUSR1 | 10 | 用户定义的信号1 |
| SIGSEGV | 11 | 无效的内存段处理 |
| SIGUSR2 | 12 | 用户定义的信号2 |
| SIGPIPE | 13 | 半关闭管道得写操作已经发生 |
| SIGALRM | 14 | 计时器到期 |
| SIGTERM | 15 | 终止 |
| SIGSTKFLT | 16 | 堆栈错误 |
| SIGCHLD | 17 | 子进程已经停止或退出 |
| SIGCONT | 18 | 如果停止了，继续执行 |
| SIGSTOP | 19 | 停止执行（不能被捕获或忽略） |
| SIGTSTP | 20 | 终端停止信号 |
| SIGTTIN | 21 | 后台进程需要从终端读取输入 |
| SIGTTOU | 22 | 后台进程需要向从终端写出 |
| SIGURG | 23 | 紧急的套接字事件 |
| SIGXCPU | 24 | 超额使用CPU分配的时间 |
| SIGXFSZ | 25 | 文件尺寸超额 |
| SIGVTALRM | 26 | 虚拟时钟信号 |
| SIGPROF | 27 | 时钟信号描述 |
| SIGWINCH | 28 | 窗口尺寸变化 |
| SIGIO | 29 | I/O |
| SIGPWR | 30 | 断电重启 |

除了SIGSTOP和SIGKILL两个信号外，进程能够忽略或捕获其他的全部信号。一个信号被捕获的意思是当一个信号到达时有相应的代码处理它。如果一个信号没有被这个进程所捕获，内核将采用默认行为处理。



