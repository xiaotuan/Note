### 9.4　为CPU密集型、阻塞或遗留功能建立接口

本章最后一节讨论的是访问大多数非Twisted的工作。尽管有高效的异步代码所带来的巨大收益，但为Twisted和Scrapy重写每个库，既不现实也不可行。使用Twisted的线程池和 `reactor.spawnProcess()` 方法，我们可以使用任何Python库甚至其他语言编写的二进制包。

