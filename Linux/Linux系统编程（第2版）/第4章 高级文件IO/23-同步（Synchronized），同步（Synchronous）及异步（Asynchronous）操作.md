### 4.5　同步（Synchronized），同步（Synchronous）及异步（Asynchronous）操作

UNIX操作系统在使用术语同步（synchronized），非同步（nonsynchronized），同步（synchronous），异步（asynchronous）时很随意，基本没有考虑这几个词所引起的困惑（在英语中，synchronized和synchronous之间的区别很小）。<a class="my_markdown" href="['#anchor45']"><sup class="my_markdown">[5]</sup></a>

synchronous写操作在数据全部写到内核缓冲区之前是不会返回的。synchronous读操作在数据写到应用程序在用户空间的缓冲区之前是不会返回的。相反地，异步写操作在用户空间还有数据时可能就返回了，异步读操作在数据准备好之前可能就返回了。也就是说，异步操作在请求时并没有被放入操作队列中来执行，而只是在后期查询。当然，在这种情况下，必须存在一定的机制来确认操作是否已经完成以及完成的程度。

synchronized操作要比synchronous操作更严格，也更安全。synchronized写操作把数据写回硬盘，确保硬盘上的数据和内核缓冲区中的是同步的。synchronized读操作总是返回最新的数据，一般是从硬盘中读取。

总的来说，同步（synchronous）和异步（asynchronous）是指I/O操作在返回前是否等待某些事件（如数据存储）返回。而术语同步（synchronized）和异步（asynchronized）则明确指定了某个事件必须发生（如把数据写回硬盘）。

通常，UNIX的写操作是synchronous但nonsynchronized，读操作是synchronous且synchronized。<a class="my_markdown" href="['#anchor46']"><sup class="my_markdown">[6]</sup></a>对于写操作，上述特性的任意组合都是可能的，如表4-1所示。

<center class="my_markdown"><b class="my_markdown">表4-1　写操作的同步性（synchronicity）</b></center>

| 同步（synchronized） | 非同步（nonsynchronized） |
| :-----  | :-----  | :-----  | :-----  |
| 同步（synchronous） | 写操作在数据写入磁盘后才返回。当打开文件时指定O_SYNC时才按照这种方式执行 | 写操作在数据保存入内核缓冲区后返回。这是常见执行行为 |
| 异步 | 写操作在请求被加入队列后返回。一旦该操作被执行，会确保数据写入磁盘 | 写操作在请求被加入队列后返回。一旦该操作被执行，会确保数据写入内核缓冲区 |

由于读取旧数据没有意义，读操作通常是同步的（synchronized）。读操作既可以是同步（synchronous）的，也可以是异步（asynchronous）的，如表4-2所示。

<center class="my_markdown"><b class="my_markdown">表4-2　读操作的同步性</b></center>

| 同步的（synchronized） |
| :-----  | :-----  | :-----  |
| 同步（synchronous） | 读操作直到最新数据保存到提供的缓冲区后才返回。（这是常见的执行方式） |
| 异步 | 读操作在请求被加入队列后返回。一旦该操作被执行，返回最新数据 |

在第2章，我们讨论如何使写操作同步（synchronized）（设置O_SYNC标志），以及如何确保所有I/O操作是同步的（synchronized）（通过fsync()及其友元函数）。现在，我们来看看如何使读写操作异步完成。

