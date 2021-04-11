### 3.3　标准C语言函数库；GNU C语言函数库（glibc）

标准C语言函数库的实现随UNIX的实现而异。GNU C语言函数库（glibc, http://www.gnu.org /software/libc/）是Linux上最常用的实现。

> 最初，Roland McGrath是GNU C语言函数库的主要开发者和维护者。如今，Ulrich Drepper挑起了这副重担。
> Linux同样支持各种其他C语言函数库，其中包括应用于嵌入式设备领域、受限内存条件下的C语言函数库。uClibc（http://www.uclibc.org/）和dietlibc（http://www.fefe.de/dietlibc/）便是其中的两个例子。本书的讨论范围仅限于glibc，因为为Linux开发的大多数应用程序都使用该函数库。

