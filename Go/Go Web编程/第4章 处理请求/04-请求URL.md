### 4.1.2　请求URL

`Request` 结构中的 `URL` 字段用于表示请求行中包含的URL（请求行也就是HTTP请求报文的第一行），这个字段是一个指向 `url.URL` 结构的指针，代码清单4-1展示了这个结构的定义。

代码清单4-1　 `URL` 结构

```go
type URL struct {
　　Scheme　 string
　　Opaque　 string
　　User　　 *Userinfo
　　Host　　 string
　　Path　　 string
　　RawQuery string
　　Fragment string
}
```

URL的一般格式为：

```go
scheme://[userinfo@]host/path[?query][#fragment]
```

那些在 `scheme` 之后不带斜线的URL则会被解释为：

```go
scheme:opaque[?query][#fragment]
```

在开发Web应用的时候，我们常常会让客户端通过URL的查询参数向服务器传递信息，而URL结构的 `RawQuery` 字段记录的就是客户端向服务器传递的查询参数字符串。举个例子，如果客户端向地址<a class="my_markdown" href="['http://www.example.com/post?id=123&thread_id=456']">http://www.example.com/post?id=123&thread_id=456</a>发送一个请求，那么 `RawQuery` 字段的值就会被设置为 `id=123&thread_id=456` 。虽然通过对 `RawQuery` 字段的值进行语法分析可以获取到键值对格式的查询参数，但直接使用 `Request` 结构的 `Form` 字段来获取这些键值对会更方便一些。本章稍后就会对 `Request` 结构的 `Form` 字段、 `PostForm` 字段和 `MultipartForm` 字段进行介绍。

另外需要注意的一点是，如果请求报文是由浏览器发送的，那么程序将无法通过 `URL` 结构的 `Fragment` 字段获取URL的片段部分。本书在第1章中就提到过，浏览器在向服务器发送请求之前，会将URL中的片段部分剔除掉——因为服务器接收到的都是不包含片段部分的URL，所以程序自然也无法通过 `Fragment` 字段去获取URL的片段部分了，造成这个问题的原因在于浏览器，与我们正在使用的 `net/http` 库无关。 `URL` 结构的 `Fragment` 字段之所以会存在，是因为并非所有请求都来自浏览器：除了浏览器发送的请求之外，服务器还可能会接收到HTTP客户端库、Angular这样的客户端框架或者某些其他工具发送的请求；此外别忘了，不仅服务器程序可以使用 `Request` 结构，客户端库也同样可以把 `Request` 结构用作自己的一部分。

