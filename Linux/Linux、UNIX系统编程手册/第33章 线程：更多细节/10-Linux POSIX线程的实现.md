### 33.5　Linux POSIX线程的实现

针对Pthreads API：Linux下有两种实现。

+ LinuxThreads：这是最初的Linux线程实现，由Xavier Leroy开发。
+ NPTL（Native POSIX Threads Library）：这是Linux线程实现的现代版，由Ulrich Drepper和Ingo Molnar开发，以取代LinuxThreads。NPTL的性能优于LinuxThreads，也更符合SUSv3的Pthreads标准。对NPTL的支持需要修改内核，这始于Linux 2.6。

> 一度，人们曾将由 IBM 开发的另一线程实现——NGPT（Next Generation POSIX Threads）视为 LinuxThreads 的继任者。NGPT采用M:N模型设计，性能明显优于LinuxThreads。不过，NPTL的开发者决意推出新的实现。NPTL的设计方法有所调整，采用1:1模型，性能也优于 NGPT。随着NPTL的发布，对NGPT的开发也随之终止。

后续各节将讨论这两种实现的更多细节，并将二者对SUSv3 Pthreads标准的背离之处一一指处。

此处值得强调的是：LinuxThreads实现已经过时，并且glibc从2.4版本开始也已不再支持它，所有新的线程库开发都基于NPTL。

