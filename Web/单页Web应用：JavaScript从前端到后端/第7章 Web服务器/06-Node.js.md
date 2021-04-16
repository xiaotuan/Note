

### 
  7.2 Node.js


Node.js是一个平台，它使用的语言是JavaScript。当把它作为HTTP服务器的时候，它的哲学思想和Twisted、Tornado或者 mod_perl是类似的。相比之下，许多其他的流行Web服务器平台会分成两个组件：HTTP服务器和应用处理容器。例子包括，Apache/PHP、Passenger/Ruby或者是Tomcat/Java。

HTTP服务器和应用一起编写，能够很容易地完成一些在HTTP服务器和应用组件分离的平台上面难以完成的任务。比如，如果想把日志写入内存数据库，不需要担心HTTP服务器停止和应用服务器启动的情形，就可以直接写入。

