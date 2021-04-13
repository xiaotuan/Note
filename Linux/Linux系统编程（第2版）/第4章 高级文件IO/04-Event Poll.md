### 4.2　Event Poll

由于poll()和select()的局限，Linux 2.6内核<a class="my_markdown" href="['#anchor43']"><sup class="my_markdown">[3]</sup></a>引入了event poll(epoll)机制。虽然epoll的实现比poll()和select()要复杂得多，epoll解决了前两个都存在的基本性能问题，并增加了一些新的特性。

对于poll()和select()（见第2章），每次调用时都需要所有被监听的文件描述符列表。内核必须遍历所有被监视的文件描述符。当这个文件描述符列表变得很大时——包含几百个甚至几千个文件描述符时——每次调用都要遍历列表就变成规模上的瓶颈。

epoll把监听注册从实际监听中分离出来，从而解决了这个问题。一个系统调用会初始化epoll上下文，另一个从上下文中加入或删除监视的文件描述符，第三个执行真正的事件等待（event wait）。

