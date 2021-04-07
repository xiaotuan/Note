### 9.3　使用Twisted专用客户端建立服务接口

到目前为止，我们看到了如何通过 `treq` 使用类REST API。Scrapy还可以和许多其他使用Twisted专用客户端的服务建立接口。比如，我们想要与MongoDB建立接口，当搜索"MongoDB Python"时，将会得到 `PyMongo` ，该库是阻塞/同步的，不能和Twisted一起使用，除非使用后续小节中的方法，在管道中描述线程，处理阻塞操作。如果搜索"MongoDB Twisted Python"，将会得到 `txmongo` ，该库可以在Twisted和Scrapy中完美运行。通常情况下，Twisted客户端背后的社区都很小，但相比自行编写客户端，这仍然是一个更好的选择。我们将使用一个类似的Twisted专用客户端作为接口，处理Redis键值对存储。

