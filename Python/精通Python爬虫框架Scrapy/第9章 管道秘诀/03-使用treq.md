### 9.1.1　使用treq

`treq` 是一个Python包，相当于基于Twisted应用编写的Python  `requests` 包。它可以让我们轻松执行GET、POST以及其他HTTP请求。想要安装该包，可以使用 `pip install treq` ，不过它已经在我们的开发机中预先安装好了。

我们更倾向于选择 `treq` 而不是Scrapy的 `Request/crawler.engine.download()` 的原因是，虽然它们都很简单，但是在性能上 `treq` 更有优势，我们将会在第10章中看到更详细的介绍。

