### 1.6　HTTP响应

HTTP响应报文是对HTTP请求报文的回复。跟HTTP请求一样，HTTP响应也是由一系列文本行组成的，其中包括：

+ 一个状态行；
+ 零个或任意数量的响应首部；
+ 一个空行；
+ 一个可选的报文主体。

也许你已经发现了，HTTP响应的组织方式跟HTTP请求的组织方式是完全相同的。以下是一个典型的HTTP响应的样子（为了节省篇幅，我们省略了报文主体中的部分内容）：

```go
200 OK
Date: Sat, 22 Nov 2014 12:58:58 GMT
Server: Apache/2
　Last-Modified: Thu, 28 Aug 2014 21:01:33 GMT
Content-Length: 33115
Content-Type: text/html; charset=iso-8859-1
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/ 
　　 TR/xhtml1/DTD/xhtml1-strict.dtd"> <html xmlns='http://www.w3.org/1999/
　　 xhtml'> <head><title>Hypertext Transfer Protocol -- HTTP/1.1</title></ 
　　 head><body>...</body></html>
```

HTTP响应的第一行为状态行，这个文本行包含了状态码（status code）和相应的原因短语（reason phrase），原因短语对状态码进行了简单的描述。除此之外，这个例子中的HTTP响应还包含了一个HTML格式的报文主体。

