### 28.4　exec()和fork()对进程属性的影响

进程有多种属性，其中一部分已经在前面几章有所说明，后续章节将讨论其他一些属性。关于这些属性，存在两个问题。

+ 当进程执行exec()时，这些属性将发生怎样的变化？
+ 当执行fork()时，子进程会继承哪些属性？

表28-4是对这些问题的回答。exec()列注明，调用exec()期间哪些属性得以保存。fork()列则表明调用fork()之后子进程继承，或（有时是）共享了哪些属性。除了标注为Linux特有的属性之外，列出的所有属性均获得了标准UNIX实现的支持，调用exec()和fork()期间对它们的处理也都符合SUSv3规范。

<center class="my_markdown"><b class="my_markdown">表28-4：exec()和fork()对进程属性的影响</b></center>

| 进 程 属 性 | exec() | fork() | 影响属性的接口；额外说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 进程地址空间 |
| 文本段 | 否 | 共享 | 子进程与父进程共享文本段 |
| 栈段 | 否 | 是 | 函数入口/出口；alloca()、longjmp()、siglongjmp() |
| 数据段和堆段 | 否 | 是 | brk()、sbrk() |
| 环境变量 | 见注释 | 是 | putenv()、setenv()；直接修改environ。execle()和execve()会对其改写，其他exec()调用则会加以保护 |
| 内存映射 | 否 | 是；见注释 | mmap()、munmap()。跨越fork()进程，映射的MAP_NORES ERVE标志得以继承。带有madvise（MADV_DONTFORK）标志的映射则不会跨fork()继承 |
| 内存锁 | 否 | 否 | mlock()、munlock() |
| 进程标识符和凭证 |
| 进程ID | 是 | 否 |
| 父进程ID | 是 | 否 |
| 进程组ID | 是 | 是 | setpgid() |
| 会话ID | 是 | 是 | setsid() |
| 实际ID | 是 | 是 | setuid()、setgid()，以及相关调用 |
| 有效和保存设置（saved set）ID | 见注释 | 是 | setuid()、setgid()，以及相关调用。第9章解释了exec()是如何影响这些ID的 |
| 补充组ID | 是 | 是 | setgroups()、initgroups() |
| 文件、文件IO和目录 |
| 打开文件描述符 | 见注释 | 是 | open()、close()、dup()、pipe()、socket()等。文件描述符在跨越exec()调用的过程中得以保存，除非对其设置了执行时关闭（close-on-exec）标志。父、子进程中的描述符指向相同的打开文件描述，参考5.4节 |
| 执行时关闭（close-on- exec）标志 | 是（如果关闭） | 是 | fcntl（F_SETFD） |
| 文件偏移 | 是 | 共用 | lseek()、read()、write()、readv()、writev()。父、子进程共享文件偏移 |
| 打开文件状态标志 | 是 | 共用 | open()、fcntl(F_SETFL)。父、子进程共享打开文件状态标志 |
| 异步I/O操作 | 见注释 | 否 | aio_read()、aio_write()以及相关调用。调用exec()期间，会取消尚未完成的操作 |
| 目录流 | 否 | 是：见注释 | opendir()、readdir()。SUSv3规定，子进程获得父进程目录流的一份副本，不过这些副本可以（也可以不）共享目录流的位置。Linux系统不共享目录流的位置 |
| 文件系统 |
| 当前工作目录 | 是 | 是 | chdir() |
| 根目录 | 是 | 是 | chroot() |
| 文件模式创建掩码 | 是 | 是 | umask() |
| 信号 |
| 信号处置 | 见注释 | 是 | signal()、sigaction()。将处置设置成默认或忽略的信号在执行 exec()期间保持不变；已捕获的信号会恢复为默认处置。参考27.5节 |
| 信号掩码 | 是 | 是 | 信号传递；sigprocmask()、sigaction() |
| 挂起（pending）信号集合 | 是 | 否 | 信号传递；raise()、kill()、sigqueue() |
| 备选信号栈 | 否 | 是 | sigaltstack() |
| 定时器 |
| 间隔定时器 | 是 | 否 | setitimer() |
| 由alarm()设置的定时器 | 是 | 否 | alarm() |
| POSIX定时器 | 否 | 否 | timer_create()及其相关调用 |
| POSIX线程 |
| 线程 | 否 | 见注释 | fork()调用期间，子进程只会复制调用线程 |
| 线程可撤销状态与类型 | 否 | 是 | exec()之后，将可撤销类型和状态分别重置为 PTHREAD_CANCEL_ENABLE和PTHREAD_CANCEL_DEFERRED |
| 互斥量与条件变量 | 否 | 是 | 关于调用 fork()期间对互斥量以及其他线程资源的处理细节可参考33.3节 |
| 优先级与调度 |
| nice值 | 是 | 是 | nice()、setpriority() |
| 调度策略及优先级 | 是 | 是 | sched_setscheduler()、sched_setparam() |
| 资源与CPU时间 |
| 资源限制 | 是 | 是 | setrlimit() |
| 进程和子进程的 CPU时间 | 是 | 否 | 由times()返回 |
| 资源使用量 | 是 | 否 | 由getrusage()返回 |
| 进程间通信 |
| System V共享内存段 | 否 | 是 | shmat()、shmdt() |
| POSIX共享内存 | 否 | 是 | shm_open()及其相关调用 |
| POSIX消息队列 | 否 | 是 | mq_open()及其相关调用。父、子进程的描述符都指向同一打开消息队列描述。子进程并不继承父进程的消息通知注册信息 |
| POSIX命名信号量 | 否 | 共用 | sem_open()及其相关调用。子进程与父进程共享对相同信号量的引用 |
| POSIX未命名信号量 | 否 | 见注释 | sem_init()及其相关调用。如果信号量位于共享内存区域，那么子进程与父进程共享信号量；否则，子进程拥有属于自己的信号量拷贝 |
| System V信号量调整 | 是 | 否 | 参考47.8节 |
| 文件锁 | 是 | 见注释 | flock()。子进程自父进程处继承对同一锁的引用 |
| 记录锁 | 见注释 | 否 | fcntl(F_SETLK)。除非将指代文件的文件描述符标记为执行时关闭，否则会跨越exec()对锁加以保护 |
| 杂项 |
| 地区设置 | 否 | 是 | setlocale()。作为C运行时初始化的一部分，执行新程序后会调用setlocale(LC_ALL，"C")的等效函数 |
| 浮点环境 | 否 | 是 | 运行新程序时，将浮点环境状态重置为默认值，参考fenv(3) |
| 控制终端 | 是 | 是 |
| 退出处理器程序 | 否 | 是 | atexit()、on_exit() |
| Linux特有 |
| 文件系统ID | 见注释 | 是 | setfsuid()、setfsgid()。一旦相应的有效ID发生变化，那么这些ID也会随之改变 |
| timeerfd定时器 | 是 | 见注释 | timerfd_create()，子进程继承的文件描述符与父进程指向相同的定时器 |
| 能力 | 见注释 | 是 | capset()。执行exec()期间对能力的处理一如39.5节所述 |
| 功能外延集合 | 是 | 是 |
| 能力安全位（securebits）标志 | 见注释 | 是 | 执行exec()期间，会保全所有的安全位标志， SECBIT_ KEEP_CAPS除外，总是会清除该标志 |
| CPU黏性（affinity） | 是 | 是 | sched_setaffinity() |
| SCHED_RESET_ON_FORK | 是 | 否 | 参考35.3.2节 |
| 允许的CPU | 是 | 是 | 参考cpuset(7)手册页 |
| 允许的内存节点 | 是 | 是 | 参考cpuset(7)手册页 |
| 内存策略 | 是 | 是 | 参考set_mempolicy(2)手册页 |
| 文件租约 | 是 | 见注释 | fcntl（F_SETLEASE）。子进程从父进程处继承对相同租约的引用 |
| 目录变更通知 | 是 | 否 | dnotify API，通过fcntl（F_NOTIFY）来实现支持 |
| prctl（PR_SET_DUMP ABLE） | 见注释 | 是 | exec()执行期间会设置PR_SET_DUMPABLE标志，执行设置用户或组ID程序的情况除外，此时将清除该标志 |
| prctl（PR_SET_PDEAT HSIG） | 是 | 否 |
| prctl（PR_SET_NAME） | 否 | 是 |
| oom_adj | 是 | 是 | 参考49.9节 |
| coredump_filter | 是 | 是 | 参考22.1节 |

