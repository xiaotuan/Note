### 56.2　创建一个socket：socket()

socket()系统调用创建一个新socket。



![1439.png](../images/1439.png)
domain参数指定了socket的通信domain。type参数指定了socket类型。这个参数通常在创建流socket时会被指定为SOCK_STREAM，而在创建数据报socket时会被指定为SOCK_DGRAM。

protocol参数在本书描述的socket类型中总会被指定为0。在一些socket类型中会使用非零的protocol值，但本书并没有对这些socket类型进行描述。如在裸socket（SOCK_RAW）中会将protocol指定为IPPROTO_RAW。

socket()在成功时返回一个引用在后续系统调用中会用到的新创建的socket的文件描述符。

> 从内核2.6.27开始，Linux为type参数提供了第二种用途，即允许两个非标准的标记与socket类型取OR。SOCK_CLOEXEC标记会导致内核为新文件描述符启用close-on-exec标记（FD_CLOEXEC）。这个标记之所以有用的原因与4.3.1节中描述的open() O_CLOEXEC标记有用的原因是一样的。SOCK_NONBLOCK标记导致内核在底层打开着的文件描述符上设置O_NONBLOCK标记，这样后面在该socket上发生的I/O操作就变成非阻塞了，从而无需通过调用fcntl()来取得同样的结果。

