### 35.2.3　SCHED_BATCH和SCHED_IDLE策略

Linux 2.6系列的内核添加了两个非标准调度策略：SCHED_BATCH和SCHED_IDLE。尽管这些策略是通过POSIX实时调度API来设置的，但实际上它们并不是实时策略。

SCHED_BATCH策略是在版本为2.6.16的内核中加入的，它与默认的SCHED_OTHER策略类似，两个之间的差别在于SCHED_BATCH策略会导致频繁被唤醒的任务被调度的次数较少。这种策略用于进程的批量式执行。

SCHED_IDLE策略是在版本为2.6.23的内核中加入的，它也与SCHED_OTHER类似，但提供的功能等价于一个非常低的nice值（即低于+19）。在这个策略中，进程的nice值毫无意义。它用于运行低优先级的任务，这些任务在系统中没有其他任务需要使用CPU时才会大量使用CPU。

