### 8.7.1　初始化inotify

在使用inotify之前，首先进程必须对它初始化。系统调用inotify_init()用于初始化inotify，并返回一个文件描述符，指向初始化的实例：



![388.png](../images/388.png)
参数flags通常是0，但也可能是下列标志位的位或运算值：

IN_CLOEXEC

对新文件描述符设置执行后关闭（close-on-exec）。

IN_NONBLOCK

对新文件描述符设置O_NONBLOCK。

出错时，inotify_init1()会返回-1，并相应设置errno值为下列值之一：

EMFILE inotify达到用户最大的实例数上限。

ENFILE 文件描述符数达到系统的最大上限。

ENOMEM 剩余内存不足，无法完成请求。

下面，我们对inotify进行初始化，以便后续使用：



![389.png](../images/389.png)
