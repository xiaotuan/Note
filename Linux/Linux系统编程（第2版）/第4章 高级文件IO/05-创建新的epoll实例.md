### 4.2.1　创建新的epoll实例

通过epoll_create1()创建epoll上下文：



![142.png](../images/142.png)


![143.png](../images/143.png)
调用成功时，epoll_create1()会创建新的epoll实例，并返回和该实例关联的文件描述符。这个文件描述符和真正的文件没有关系，仅仅是为了后续调用epoll而创建的。参数flags支持修改epoll的行为，当前，只有EPOLL_CLOEXEC是个合法的flag，它表示进程被替换时关闭文件描述符。

出错时，返回-1，并设置errno为下列值之一：

EINVAL

参数flags非法。

EMFILE

用户打开的文件数达到上限。

ENFILE

系统打开的文件数达到上限。

ENOMEN

内存不足，无法完成本次操作。

epoll_create()是老版本的epoll_create1()的实现，现在已经废弃。它不接收任何标志位。相反地，它接收size参数，该参数没有用。size之前是用于表示要监视的文件描述符个数；现在，内核可以动态获取数据结构的大小，只需要size参数大于0即可。如果size值小于0，会返回EINVAL。如果应用所运行的系统其Linux版本低于Linux内核2.6.27以及glibc 2.9，应该使用老的epoll_create()调用。

epoll的标准调用方式如下：



![144.png](../images/144.png)
当完成监视后，epoll_create1()返回的文件描述符需要通过close()调用来关闭。

