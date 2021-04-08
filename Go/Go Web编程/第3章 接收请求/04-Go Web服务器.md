### 3.2.1　Go Web服务器

跟其他编程语言里面的绝大多数标准库不一样，Go提供了一系列用于创建Web服务器的标准库。正如代码清单3-1所示，创建一个服务器的步骤非常简单，只要调用 `ListenAndServe` 并传入网络地址以及负责处理请求的处理器（handler）作为参数就可以了。如果网络地址参数为空字符串，那么服务器默认使用80端口进行网络连接；如果处理器参数为 `nil` ，那么服务器将使用默认的多路复用器 `DefaultServeMux` 。

代码清单3-1　最简单的Web服务器

```go
package main
import (
　　 "net/http"
)
func main() {
　　 http.ListenAndServe("", nil)
}
```

用户除了可以通过 `ListenAndServe` 的参数对服务器的网络地址和处理器进行配置之外，还可以通过 `Server` 结构对服务器进行更详细的配置，其中包括为请求读取操作设置超时时间、为响应写入操作设置超时时间以及为 `Server` 结构设置错误日志记录器等。

代码清单3-2和代码清单3-1的作用基本上是相同的，它们之间的唯一区别在于代码清单3-2可以通过 `Server` 结构对服务器进行更多的配置。

代码清单3-2　带有附加配置的Web服务器

```go
package main
import (
　　"net/http"
)
func main() {
　　server := http.Server{
　　　　Addr:　　"127.0.0.1:8080",
　　　　Handler: nil,
　　}
　　server.ListenAndServe()
}
```

代码清单3-3展示了 `Server` 结构所有可选的配置选项。

代码清单3-3　 `Server` 结构的配置选项

```go
type Server struct {
　　Addr　　　　　 string
　　Handler　　　　Handler
　　ReadTimeout　　time.Duration
　　WriteTimeout　 time.Duration
　　MaxHeaderBytes int
　　TLSConfig　　　*tls.Config
　　TLSNextProto　 map[string]func(*Server, *tls.Conn, Handler)
　　ConnState　　　func(net.Conn, ConnState)
　　ErrorLog　　　 *log.Logger
}
```

