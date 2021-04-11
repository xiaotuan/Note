### 51.2　System V IPC与POSIX IPC比较

下面几个章节将分别对各种POSIX IPC机制进行介绍，同时还会将它们与其在System V中的对应机制进行对比。下面考虑这两种IPC之间的一些常规比较。

与System V IPC相比，POSIX IPC拥有下列常规优势。

+ POSIX IPC的接口比System V IPC接口简单。
+ POSIX IPC模型——使用名字替代键、使用open、close以及unlink函数——与传统的UNIX文件模型更加一致。
+ POSIX IPC对象是引用计数的。这就简化了对象删除，因为可以断开一个POSIX IPC对象的链接，并且知道当所有进程都关闭该对象之后对象就会被销毁。

然而System V IPC具备一个显著的优势：可移植性。POSIX IPC在下列方面的移植性不如System V IPC。

+ System V IPC在SUSv3中进行了规定，并且几乎所有的UNIX实现都支持System V IPC。而与之相反的是，POSIX IPC机制在SUSv3中则是一个可选的组件。一些UNIX实现并不支持（所有）POSIX IPC机制。这种情况可以通过Linux上的微观世界反映出来：POSIX共享内存从内核2.4开始得到支持；完整的POSIX信号量实现从内核2.6开始得到支持；POSIX消息队列从内核2.6.6开始得到支持。
+ 尽管SUSv3对POSIX IPC对象名字进行了规定，但各种实现仍然采用不同的规则来命名IPC对象。这些差异使得程序员在编写可移植应用程序时需要做一些（很少）额外的工作。
+ POSIX IPC的各种细节并没有在SUSv3中进行规定。特别是没有规定使用哪些命令来显示和删除系统上的IPC对象。（在很多实现上使用的是标准的文件系统命令，但用来标识IPC对象的路径名的细节信息则因实现而异。）

