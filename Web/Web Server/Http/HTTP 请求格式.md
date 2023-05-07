[toc]

HTTP 规定，HTTP 请求由如下 3 部分构成：

+ 请求方法，URI 和 HTTP 的版本。
+ 请求头（Request Header）。
+ 请求正文（Request Content）。

下面的代码是一个 HTTP/1.1 请求的例子：

```
POST /hello.jsp HTTP/1.1
Accept: image/gif, image/jpeg, */*
Referer: http://localhost/login.html
Accept-Language: en,zh-cn;q=0.5
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64;
		Trident/7.0; rv:11.0) like Gecko
Host: localhost
Content-Length: 40
Connection: Keep-Alive
Cache-Control: no-cache

username=Tom&password=1234&submit=submit
```

### 1. 请求方式、URI 和 HTTP 的版本

HTTP 请求的第一行包括请求方式、URI 和协议版本这 3 项内容，以空格分开：

```
POST /hello.jsp HTTP/1.1
```

根据 HTTP，HTTP 请求可以使用多种方式，主要包括以下几种：

+ GET：这种请求方式最为常见，客户程序通过这种请求方式访问服务器上的一个文档，服务器把文档发给客户程序。
+ POST：客户程序可以通过这种方式发送大量信息给服务器。在 HTTP 请求中除了包含要访问的文档的 URI，还包括大量的请求正文，这些请求正文中通常包含 HTML 表单数据。
+ HEAD：客户程序和服务器之间交流一些内部数据，服务器不会返回具体的文档。当使用 GET 和 POST 方法时，服务器最后都将特定的文档返回给客户程序。而 HEAD 请求方式则不痛，它仅仅交流一些内部的数据，这些数据不会影响用户浏览网页的过程，可以说对用户是透明的。HEAD 请求方式通常不单独使用，而是对其他请求方式起辅助作用。一些搜索引擎使用 HEAD 请求方式来获得网页的标志信息，还有一些 HTTP 服务器进行安全认证时，用这个方式来传递认证信息。
+ PUT：客户程序通过这种方式把文档上传给服务器。
+ DELETE：客户程序通过这种方式来删除远程服务器上的某个文档。客户程序可以利用 PUT 和 DELETE 请求方式来管理远程服务器上的文档。

### 2. 请求头（Request Header）

请求头包含许多有关客户端环境和请求正文的有用信息。例如，请求头可以声明浏览器的类型、所用的语音、请求正文的类型，以及请求正文的长度等。

```
Accept: image/gif, image/jpeg, */*
Referer: http://localhost/login.html
Accept-Language: en,zh-cn;q=0.5
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64;
		Trident/7.0; rv:11.0) like Gecko
Host: localhost
Content-Length: 40
Connection: Keep-Alive
Cache-Control: no-cache
```

### 3. 请求正文（Request Content）

HTTP 规定，请求头和请求正文之间必须以空行分隔（即只有 CRLF 符号的行），这个空行非常重要，它表示请求头已经结束，接下来是请求正文。请求正文中可以包含客户以 POSt 方式提交的表单数据：

```
username=Tom&password=1234&submit=submit
```

> 提示：CRLF（Carriage Return Linefeed）是指回车符和行结束符 "\r\n"。