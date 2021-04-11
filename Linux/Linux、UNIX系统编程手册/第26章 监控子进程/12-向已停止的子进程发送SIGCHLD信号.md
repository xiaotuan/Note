### 26.3.2　向已停止的子进程发送SIGCHLD信号

正如可以使用 waitpid()来监测已停止的子进程一样，当信号导致子进程停止时，父进程也就有可能收到 SIGCHLD 信号。调用 sigaction()设置 SIGCHLD 信号处理程序时，如传入 SA_NOCLDSTOP 标志即可控制这一行为。若未使用该标志，系统会在子进程停止时向父进程发送 SIGCHLD 信号；反之，如果使用了这一标志，那么就不会因子进程的停止而发出SIGCHLD信号。（22.7节中对signal()的实现就未指定SA_NOCLDSTOP。）

> 因为默认情况下会忽略信号SIGCHLD，SA_NOCLDSTOP标志仅在设置SIGCHLD信号处理程序时才有意义。而且，SA_NOCLDSTOP只对SIGCHLD信号起作用。

SUSv3 也允许，当信号SIGCONT导致已停止的子进程恢复执行时，向其父进程发送SIGCHLD信号。（相当于waitpid()的WCONTINUED标志。）始于版本2.6.9，Linux内核实现了这一特性。

