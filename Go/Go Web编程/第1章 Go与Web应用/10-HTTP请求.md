### 1.5　HTTP请求

HTTP是一种请求-响应协议，协议涉及的所有事情都以一个请求开始。HTTP请求跟其他所有HTTP报文（message）一样，都由一系列文本行组成，这些文本行会按照以下顺序进行排列：

（1）请求行（request-line）；

（2）零个或任意多个请求首部（header）；

（3）一个空行；

（4）可选的报文主体（body）。

一个典型的HTTP请求看上去是这个样子的：

```go
GET /Protocols/rfc2616/rfc2616.html HTTP/1.1
Host: www.w3.org
User-Agent: Mozilla/5.0
(empty line)
```

这个请求中的第一个文本行就是请求行：

```go
GET /Protocols/rfc2616/rfc2616.html HTTP/1.1
```

请求行中的第一个单词为请求方法（request method），之后跟着的是统一资源标识符（Uniform Resource Identifier，URI）以及所用的HTTP版本。位于请求行之后的两个文本行为请求的首部。注意，这个报文的最后一行为空行，即使报文的主体部分为空，这个空行也必须存在，至于报文是否包含主体则需要根据请求使用的方法而定。

