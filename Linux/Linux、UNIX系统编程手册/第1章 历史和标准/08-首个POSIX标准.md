### 1.3.2　首个POSIX标准

术语“POSIX（可移植操作系统Portable Operating System Interface的缩写）”是指在IEEE（电器及电子工程师协会），确切地说是其下属的可移植应用标准委员会（PASC, http://www.pasc.org/）赞助下所开发的一系列标准。PASC标准的目标是提升应用程序在源码级别的可移植性。

> POSIX之名来自于Richard Stallman的建议。最后一个字母之所以是“X”是因为大多数UNIX变体之名总以“X”结尾。该标准特别注明，POSIX应发音为“pahz-icks”，类似于“positive”。

本书会关注名为POSIX.1的第一个POSIX标准，以及后续的POSIX.2标准。

#### POSIX.1和POSIX.2

POSIX.1于1989年成为IEEE标准，并在稍作修订后于1990年被正式采纳为ISO标准（ISO/ IEC 9945-1:1990）。无法在线获得这一POSIX标准，但能从IEEE（http://www.ieee.org/）购得。

> POSIX.1一开始是基于一个更早期的（1984年）非官方标准，由名为/usr/group的UNIX厂商协会制定。

符合POSIX.1标准的操作系统应向程序提供调用各项服务的API，POSIX.1文档对此作了规范。凡是提供了上述API的操作系统都可被认定为符合POSIX.1标准。

POSIX.1基于UNIX系统调用和C语言库函数，但无需与任何特殊实现相关。这意味着任何操作系统都可以实现该接口，而不一定要是UNIX操作系统。实际上，在不对底层操作系统大加改动的同时，一些厂商通过添加 API 已经使自己的专有操作系统符合了 POSIX.1标准。

对原有POSIX.1标准的若干扩展也同样重要。正式获批于1993年的IEEE POSIX 1003.1b（POSIX.1b，原名POSIX.4或POSIX 1003.4）包含了一系列对基本POSIX标准的实时性扩展。正式获批于1995年的IEEE POSIX 1003.1c（POSIX.1c）对POSIX线程作了定义。1996年，一个经过修订POSIX.1版本诞生，在核心内容保持不变的同时，并入了实时性和线程扩展。IEEE POSIX 1003.1g（POSIX.1g）定义了包括套接字在内的网络API。分别获批于1999年和2000年的IEEE POSIX 1003.1d（POSIX.1d）和POSIX.1j在POSIX基本标准的基础上，定义了附加的实时性扩展。

> POSIX.1b实时性扩展包括文件同步、异步I/O、进程调度、高精度时钟和定时器、采用信号量、共享内存，以及消息队列的进程间通信。这3种进程间通信方法的称谓前通常冠以POSIX，以示其有别于与之类似而又较为古老的System V信号、共享内存以及消息队列。

POSIX.2（1992，ISO/IEC 9945-2:1993）这一与POSIX.1相关的标准，对shell和包括C编译器命令行接口在内的各种UNIX工具进行了标准化。

#### F151-1和FIPS 151-2

FIPS 是Federal Information Processing Standard（联邦信息处理标准）的缩写，这套标准由美国政府为规范其对计算机系统的采购而制定。FIPS 151-1于1989年发布。这份标准基于1988年的IEEE POSIX.1标准和ANSI C语言标准草案。FIPS 151-1和POSIX.1（1988）之间的主要差别在于：某些对后者来说是可选的特性，对于前者来说是必须的。由于美国政府是计算机系统的“大买家”，大多数计算机厂商都会确保其UNIX系统符合FIPS 151-1版本的POSIX.1规范。

FIPS 151-2与POSIX.1的1990 ISO版保持一致，但在其他方面则保持不变。2000年2月，已然过时的FIPS 151-2标准被废止。

