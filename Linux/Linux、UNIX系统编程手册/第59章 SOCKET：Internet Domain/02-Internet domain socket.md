### 59.1　Internet domain socket

Internet domain流socket是基于TCP之上的，它们提供了可靠的双向字节流通信信道。

Internet domain数据报socket是基于UDP之上的。UDP socket与之在UNIX domain中的对应实体类似，但需要注意下列差别。

+ UNIX domain数据报socket是可靠的，但UDP socket则是不可靠的——数据报可能会丢失、重复或到达的顺序与它们被发送的顺序不同。
+ 在一个UNIX domain数据报socket上发送数据会在接收socket的数据队列为满时阻塞。与之不同的是，使用UDP时如果进入的数据报会使接收者的队列溢出，那么数据报就会静默地被丢弃。

