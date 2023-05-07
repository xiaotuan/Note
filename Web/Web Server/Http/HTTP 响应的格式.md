[toc]

和 HTTP 请求相似，HTTP 响应也由 3 部分构成，分别是：

+ HTTP 的版本、状态代码和描述。
+ 响应头（Response Header）。
+ 响应正文（Response Content）。

下面的代码是一个 HTTP/1.1 响应的例子：

```
HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Content-type: text/html; charset=GBK
Content-length: 102

<html>
    <head>
        <title>HelloWorld</title>
    </head>
   	<body>
   	    <h1>hello</h1>
   	</body>
</html>
```

### 1. HTTP 的版本、状态代码和描述

HTTP 响应的第一行包括服务器使用的 HTTP 的版本、状态代码，以及对状态代码的描述，这 3 项内容之间以空格分隔。

```
HTTP/1.1 200 OK
```

状态代码是一个 3 位整数，以 1、2、3、4 或 5 开头：

+ 1xx：信息提示，表示临时的响应。
+ 2xx：响应成功，表明服务器成功地接收了客户端请求。
+ 3xx：重定向。
+ 4xx：客户端错误，表明客户端可能有问题。
+ 5xx：服务器错误，表明服务器由于遇到某种错误而不能响应客户请求。

以下是一些常见的状态代码：

+ 200：响应成功。
+ 400：错误的请求。客户发送的 HTTP 请求不正确。
+ 404：文件不存在。在服务器上没有客户要求访问的文档。
+ 405：服务器不支持客户的请求方式。
+ 500：服务器内部错误。

### 2. 响应头（Response Header）

响应头也和请求头一样包含许多有用的信息，例如服务器类型、正文类型和正文长度等，如下所示：

```
Server: Apache-Coyote/1.1	// 服务器类型
Content-type: text/html; charset=GBK	// 正文类型
Content-length: 102	// 正文长度
```

### 3. 响应正文（Response Content）

响应正文就是服务器返回的具体数据，它是浏览器真正请求访问的信息，最常见的是 HTML 文档，如下所示：

```
<html>
    <head>
        <title>HelloWorld</title>
    </head>
   	<body>
   	    <h1>hello</h1>
   	</body>
</html>
```

HTTP 请求头与请求正文之间必须用空行分隔，同样，HTTP 响应头与响应正文之间也必须用空行分隔。

