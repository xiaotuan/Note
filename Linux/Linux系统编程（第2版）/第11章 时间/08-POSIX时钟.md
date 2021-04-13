### 11.2　POSIX时钟

本章讨论的一些系统调用使用了POSIX时钟，它是一种实现和表示时间源的标准。clockid_t类型表示了特定的POSIX时钟，Linux支持其中五种：

CLOCK_REALTIME

系统级的真实时间（墙钟时间）。设置该时钟需要特殊权限。

CLOCK_MONOTONIC

任何进程都无法更改的单调递增的时钟。它表示自某个非特定起始点以来所经过的时间，比如从系统启动到现在的时间。

CLOCK_MONOTONIC_RAW

和CLOCK_MONOTONIC类似，差别在于该时钟不能调整（对误差进行微调）。也就是说，如果硬件时钟运行比运行时钟快或慢，该时钟不会进行调整。该时钟是Linux特有的。

CLOCK_PROCESS_CPUTIME_ID

处理器提供给每个进程的高精度时钟。例如，在i386体系结构上，这个时钟采用时间戳计数（TSC）寄存器。

CLOCK_THREAD_CPUTIME_ID

和每个进程的时钟类似，但是进程中每个线程的该时钟是独立的。

在POSIX标准中，只有CLOCK_REALTIME是必须实现的。因此，虽然Linux提供了所有五个时钟，但如果希望代码可移植，就应该只使用CLOCK_REALTIME。

