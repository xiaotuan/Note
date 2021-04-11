### 59.14　UNIX与Internet domain socket比较

当编写通过网络进行通信的应用程序时必须要使用Internet domain socket，但当位于同一系统上的应用程序使用socket进行通信时则可以选择使用Internet或UNIX domain socket。在这种情况下该使用哪个domain？为何使用这个domain呢？

编写只使用Internet domain socket的应用程序通常是最简单的做法，因为这种应用程序既能运行于同一个主机上，也能运行在网络中的不同主机上。但之所以要选择使用UNIX domain socket是存在几个原因的。

+ 在一些实现上，UNIX domain socket的速度比Internet domain socket的速度快。
+ 可以使用目录（在Linux上是文件）权限来控制对UNIX domain socket的访问，这样只有运行于指定的用户或组ID下的应用程序才能够连接到一个监听流socket或向一个数据报socket发送一个数据报，同时为如何验证客户端提供了一个简单的方法。使用Internet domain socket时如果需要验证客户端的话就需要做更多的工作了。
+ 使用UNIX domain socket可以像61.13.3节中总结的那样传递打开的文件描述符和发送者的验证信息。

