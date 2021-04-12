## 1.8　Windows容器vs Linux容器

运行中的容器共享宿主机的内核，理解这一点是很重要的。这意味着一个基于Windows的容器化应用在Linux主机上是无法运行的。读者也可以简单地理解为Windows容器需要运行在Windows宿主机之上，Linux容器（Linux Container）需要运行在Linux宿主机上。但是，实际场景要比这复杂得多……

在本书撰写过程中，在Windows机器上运行Linux容器已经成为可能。例如，Windows版Docker（由Docker公司提供的为Windows 10设计的产品）可以在Windows容器模式和Linux容器模式之间进行切换。这是一个正在快速发展的领域，如果读者想要了解，需要查阅 Docker 最新文档。

