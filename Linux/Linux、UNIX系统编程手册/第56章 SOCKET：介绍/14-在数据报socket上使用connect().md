### 56.6.2　在数据报socket上使用connect()

尽管数据报socket是无连接的，但在数据报socket上应用connect()系统调用仍然是起作用的。在数据报socket上调用connect()会导致内核记录这个socket的对等socket的地址。术语已连接的数据报socket就是指此种socket。术语非连接的数据报socket是指那些没有调用connect()的数据报socket（即新数据报socket的默认行为）。

当一个数据报socket已连接之后：

+ 数据报的发送可在socket上使用write()（或send()）来完成并且会自动被发送到同样的对等socket上。与sendto()一样，每个write()调用会发送一个独立的数据报；
+ 在这个socket上只能读取由对等socket发送的数据报。

注意connect()的作用对数据报socket是不对称的。上面的论断只适用于调用了connect()数据报socket，并不适用于它连接的远程socket（除非对等应用程序在其socket上也调用了connect()）。

通过再发起一个connect()调用可以修改一个已连接的数据报socket的对等socket。此外，通过指定一个地址族（如UNIX domain中的sun_family字段）为AF_UNSPEC的地址结构还可以解除对等关联关系。但需要注意的是，其他很多UNIX实现并不支持将AF_UNSPEC用于这种用途。

> SUSv3在解除对等关系方面的论断是比较模糊的，它只是声称通过调用一个指定了“空地址”的connect()调用可以重置一个连接，并没有定义那样一个术语。SUSv4则明确规定了需要使用AF_UNSPEC。

为一个数据报socket设置一个对等socket，这种做法的一个明显优势是在该socket上传输数据时可以使用更简单的I/O系统调用，即无需使用指定了dest_addr和addrlen参数的sendto()，而只需要使用write()即可。设置一个对等socket主要对那些需要向单个对等socket（通常是某种数据报客户端）发送多个数据报的应用程序是比较有用的。

> 在一些TCP/IP实践中，将一个数据报socket连接到一个对等socket能够带来性能上的提升（([Stevens et al., 2004])。在Linux上，连接一个数据报socket能对性能产生些许差异。

