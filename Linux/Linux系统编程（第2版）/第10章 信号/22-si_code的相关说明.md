### 10.6.2　si_code的相关说明

si_code字段说明信号发生的原因。对于用户发送的信号，该字段说明信号是如何被发送的。对于内核发送的信号，该字段说明信号发送的原因。

以下si_code值对任何信号都是有效的。它们说明了信号如何发送以及为何发送。

SI_ASYNCIO

由于完成异步I/O而发送该信号（见第5章）。

SI_KERNEL

信号由内核产生。

SI_MESGQ

由于一个POSIX消息队列的状态改变而发送该信号（不在本书的范围内）。

SI_QUEUE

信号由sigqueue()发送（见下一节）。

SI_TIMER

由于POSIX定时器超时而发送该信号（见第11章）。

SI_TKILL

信号由tkill()或tgkill()发送。这些系统调用是线程库使用的，不在本书的讨论范围内。

SI_SIGIO

由于SIGIO排队而发送该信号。

SI_USER

信号由kill()或raise()发送。

以下的si_code值只对SIGBUS有效。它们说明了发生硬件错误的类型：

BUS_ADRALN

进程发生了对齐错误（见第9章对对齐的讨论）。

BUS_ADRERR

进程访问无效的物理地址。

BUS_OBJERR

进程造成了其他类型的硬件错误。

对于SIGCHLD，以下值表示子进程给父进程发送信号时的行为：

CLD_CONTINUED

子进程被停止，但已经继续执行。

CLD_DUMPED

子进程非正常终止。

CLD_EXITED

子进程通过exit()正常终止。

CLD_KILLED

子进程被杀死了。

CLD_STOPPED

子进程被停止了。

CLD_TRAPPED

子进程进入一个陷阱。

以下值只对SIGFPE有效。它们说明了发生算术错误的类型：

FPE_FLTDIV

进程执行了一个除以0的浮点数运算。

FPE_FLTOVF

进程执行了一个会溢出的浮点数运算。

FPE_FLTINV

进程执行了一个无效的浮点数运算。

FPE_FLTRES

进程执行了一个不精确或无效结果的浮点数运算。

FPE_FLTSUB

进程执行了一个造成下标超出范围的浮点数运算。

FPE_FLTUND

进程执行了一个造成下溢的浮点数运算。

FPE_INTDIV

进程执行了一个除以0的整数运算。

FPE_INTOVF

进程执行了一个溢出的整数运算。

以下si_code值只对SIGILL有效。它们说明了执行非法指令的性质：

ILL_ILLADR

进程试图进入非法的寻址模式。

ILL_ILLOPC

进程试图执行一个非法的操作码。

ILL_ILLOPN

进程试图执行一个非法的操作数。

ILL_PRVOPC

进程试图执行特权操作码。

ILL_PRVREG

进程试图在特权寄存器上运行。

ILL_ILLTRP

进程试图进入一个非法的陷阱。

对于所有这些值，si_addr都指向非法操作的地址。

对于SIGPOLL，以下值表示形成信号的I/O事件：

POLL_ERR

发生了I/O错误。

POLL_HUP

设备挂起或套接字断开。

POLL_IN

文件有可读数据。

POLL_MSG

有个消息。

POLL_OUT

文件能够被写入。

POLL_PRI

文件有可读的高优先级数据。

以下的代码对SIGSEGV有效，描述了两种非法访问内存的类型：

SEGV_ACCERR

进程以无效的方式访问有效的内存区域，也就是说进程违反了内存访问的权限。

SEGV_MAPERR

进程访问无效的内存区域。

对于这两个值，si_addr包含了非法操作地址。

对于SIGTRAP，这两个si_code值表示陷阱的类型：

TRAP_BRKPT

进程“踩到”了一个断点。

TRAP_TRACE

进程“踩到”了一个追踪陷阱。

注意，si_code字段是个数值，而不是位。

