### 57.5　创建互联socket对：socketpair()

有时候让单个进程创建一对socket并将它们连接起来是比较有用的。这可以通过使用两个socket()调用和一个bind()调用以及对listen()、connect()、accept()（用于流socket）的调用或对connect()（用于数据报socket）的调用来完成。socketpair()系统调用则为这个操作提供了一个快捷方式。



![1463.png](../images/1463.png)
socketpair()系统调用只能用在UNIX domain中，即domain参数必须被指定为AF_UNIX。（这个约束适用于大多数实现，但却是合理的，因为这一对socket是创建于单个主机系统上的。）socket的type可以被指定为SOCK_DGRAM或SOCK_STREAM。protocol参数必须为0。sockfd数组返回了引用这两个相互连接的socket的文件描述符。

将type指定为SOCK_STREAM相当于创建一个双向管道（也被称为流管道）。每个socket都可以用来读取和写入，并且这两个socket之间每个方向上的数据信道是分开的。（在从BSD演化来的实现中，pipe()被实现成了一个对socketpair()的调用。）

一般来讲，socket对的使用方式与管道的使用方式类似。在调用完socketpair()之后，进程会使用fork()创建一个子进程。子进程会继承父进程的文件描述符的副本，包括引用socket对的描述符。因此父进程和子进程就可以使用这一对socket来进行IPC了。

使用socketpair()创建一对socket与手工创建一对相互连接的socket这两种做法之间的一个差别在于前一对socket不会被绑定到任意地址上。这样就能够避免一类安全问题了，因为这一对socket对其他进程是不可见的。

> 从内核2.6.27开始，Linux为type参数提供了第二种用途，即允许将两个非标准的标记与socket type取OR。SOCK_CLOEXEC标记会导致内核为两个新文件描述符启用close-on-exec标记（FD_CLOEXEC）。这个标记之所以有用的原因与4.3.1节中描述的open() O_CLOEXEC标记有用的原因是一样的。SOCK_NONBLOCK标记会导致内核在两个底层打开着的文件描述符上设置O_NONBLOCK标记，这样在该socket上发生的后续I/O操作就不会阻塞了，从而就无需通过调用fcntl()来取得同样的结果了。

