### 7.7.1　Linux线程实现

Pthreads标准是一堆文字描述。在Linux中，该标准的实现是通过glibc提供的，即Linux的C库。随着时间推移，glibc提供了两个不同的Pthreads实现机制：LinuxThreads和NPTL。

LinuxThreads是Linux原始的Pthread实现，提供1:1的线程机制。它的第一版被包含在glibc的2.0版本中，虽然只是作为外部库提供。LinuxThreads在设计上是为了内核设计的，它提供非常少的线程支持：和创建一个新的线程的clone()系统调用不同。LinuxThreads通过已有的UNIX接口实现了POSIX线程机制。举个例子，LinuxThreads通过信号实现线程到线程的通信机制（参见第10章）。由于缺乏对Pthreads的内核支持，LinuxThreads需要“管理员”线程来协调各种操作，当线程数很大时会导致可扩展性很差，而且对于POSIX标准的兼容也不太完善。

本地POSIX线程库（NPTL）比LinuxThreads要优越，依然是标准的LinuxPthread实现机制。NPTL是在Linux 2.6和glibc2.3中引入的。类似于LinuxThreads，NPTL基于clone()系统调用和内核模型提供了1:1的线程模式，线程和其他任何进程没有太大区别，除了它们共享特性资源。和LinuxThreads不同，NPTL突出了内核2.6新增的额外内核接口，包括用于线程同步的futex()系统调用，以及exit_group()系统调用，用于终止进程中的所有线程，内核支持线程本地存储（TLS）模式。NPTL解决了LinuxThreads的非一致性问题，极大提升了线程的兼容性，支持在单个进程中创建几千个线程，而且不会变慢。

> <img class="my_markdown" src="../images/1.png" style="width:62px;  height: 63px; "/> **NGPT**
> 和NPTL对立的是下一代POSIX线程（NGPT）。类似于NPTL，NGPT也是期望解决LinuxThreads的局限性，并提升可扩展性。但是，不同于NPTL和LinuxThreads，NGPT实现的是N:M的线程模式。正如在Linux中，总是采纳更简单的解决方案，因此NGPT只是在历史上留下一笔而已。

虽然基于LinuxThreads的系统开始成长起来，而且现在还有。由于NPTL是LinuxThreads的一个很大改进，强烈建议把系统更新到NPTL（抛弃一个很古老的系统其实不需要理由），如果没有更新到NPTL的话，那就还是采用单线程编程吧。

