### 3.4　使用HTTP/2

在本章的最后，让我们来了解一下如何使用HTTP/2构建本章介绍的Web服务器。

本书在第1章已经对HTTP/2做过简单的介绍，并且提到过在1.6或以上版本的Go语言中，如果使用HTTPS模式启动服务器，那么服务器将默认使用HTTP/2。但是，在默认情况下，版本低于1.6版本的Go语言将不会安装 `http2` 包，因此用户需要通过手动执行以下命令来获取这个包：

```go
go get "golang.org/x/net/http2"
```

为了让代码清单3-6中构建的Web服务器用上HTTP/2，我们需要给这个服务器导入 `http2` 包，并通过添加一些代码行来让服务器打开对HTTP/2的支持。为了做到这一点，我们需要调用 `http2` 包中的 `ConfigureServer` 方法，并将服务器配置传递给它，修改后的服务器代码如代码清单3-13所示。

代码清单3-13　启用HTTP/2

```go
package main
import (
　　"fmt"
　　"golang.org/x/net/http2"
　　"net/http"
)
type MyHandler struct{}
func (h *MyHandler) ServeHTTP (w http.ResponseWriter, r *http.Request) {
　　fmt.Fprintf(w, "Hello World!")
}
func main() {
　　handler := MyHandler{}
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　　　Handler: &handler,
　　}
　　http2.ConfigureServer(&server, &http2.Server{})
　　server.ListenAndServeTLS("cert.pem", "key.pem")
}
```

现在，我们只要执行以下代码就可以启动这个打开了HTTP/2功能的Web服务器了：

```go
go run server.go
```

为了检查服务器是否运行在HTTP/2模式之下，我们可以使用cURL对服务器进行检查。因为cURL在很多平台上都是可用的，所以本书会经常使用它作为检测工具，因此现在是时候来学习一下如何使用cURL了。

cURL

> cURL是一个命令行工具，它可以获取指定URL上的文件，又或者向指定的URL发送文件。cURL支持数量庞大的常用互联网协议，其中就包括HTTP和HTTPS。cURL默认安装在包括OS X在内的很多Unix变种之上，并且它同样可以在Windows系统上使用。手动下载和安装cURL的方法可以通过页面http://curl.haxx.se/download.html看到。

cURL从7.43.0版本开始支持HTTP/2，用户在发送请求的时候，只需要打开 `--http2` 标志（flag）就可以发送HTTP/2请求了。此外，为了让cURL能够支持HTTP/2，用户还必须将cURL与 `nghttp2` 这个提供HTTP/2支持的C语言库进行链接（link）。在撰写本节的时候，包括OS X平台在内的很多默认的cURL实现都还没有提供对HTTP/2的支持，因此我们可能需要重新编译cURL，将它与 `nghttp2` 库进行链接，然后用编译后的新版cURL代替原有的cURL。

在完成重新编译cURL的工作之后，我们可以使用以下命令去检查代码清单3-13展示的Web应用是否启用了HTTP/2：

```go
curl -I --http2 --insecure https://localhost:8080/
```

在默认情况下，cURL在以HTTP/2形式访问一个Web应用的时候，会对应用的证书进行验证，并在验证无法通过时拒绝访问。因为我们的Web应用使用的是自行创建的证书和密钥，它们默认是无法通过这一验证的，所以上面的命令在调用cURL的时候使用了 `insecure` 标志，这个标志会让cURL强制接受我们创建的证书，从而使访问可以顺利进行。

如果一切顺利，cURL将返回以下输出：

```go
HTTP/2.0 200
content-type:text/plain; charset=utf-8
content-length:12
date:Mon, 15 Feb 2016 05:33:01 GMT
```

本章虽然详细介绍了如何接收HTTP请求，但是并没有具体地说明如何处理接收到的请求，以及如何向客户端返回响应。虽然处理器和处理器函数是使用Go编写Web应用的关键，但如何处理请求以及如何发送响应才是Web应用真正安身立命之所在。在接下来的一章中，我们将深入学习请求和响应的细节，了解如何从请求中提取信息，以及如何通过响应传递信息。

