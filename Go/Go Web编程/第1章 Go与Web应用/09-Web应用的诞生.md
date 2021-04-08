### 1.4　Web应用的诞生

在万维网出现不久之后，人们开始意识到一点：尽管使用Web服务器处理静态HTML文件这个主意非常棒，但如果HTML里面能够包含动态生成的内容，那么事情将会变得更加有趣。其中，通用网关接口（Common Gateway Interface，CGI）就是在早期尝试动态生成HTML内容的技术之一。

1993年，美国国家超级计算应用中心（National Center for Supercomputing Applications， NCSA）编写了一个在Web服务器上调用可执行命令行程序的规范（specification），他们把这个规范命名为CGI，并将它包含在了NCSA开发的广受欢迎的HTTPd服务器里面。不过NCSA制定的这个规范最终并没有成为正式的互联网标准，只有CGI这个名字被后来的规范沿用了下来。

CGI是一个简单的接口，它允许Web服务器与一个独立运行于Web服务器进程之外的进程进行对接。通过CGI与服务器进行对接的程序通常被称为CGI程序，这种程序可以使用任何编程语言编写——这也是我们把这种接口称之为“通用”接口的原因，不过早期的CGI程序大多数都是使用Perl语言编写的。向CGI程序传递输入参数是通过设置环境变量来完成的，CGI程序在运行之后将向标准输出（stand output）返回结果，而服务器则会将这些结果传送至客户端。

与CGI同期出现的还有服务器端包含（server-side includes，SSI）技术，这种技术允许开发者在HTML文件里面包含一些指令（directive）：当客户端请求一个HTML文件的时候，服务器在返回这个文件之前，会先执行文件中包含的指令，并将文件中出现指令的位置替换成这些指令的执行结果。SSI最常见的用法是在HTML文件中包含其他被频繁使用的文件，又或者将整个网站都会出现的页面首部（header）以及尾部（footer）的代码段嵌入HTML文件中。

作为例子，以下代码演示了如何通过SSI指令将 `navbar.shtml` 文件中的内容包含到HTML文件中：

```go
<html>
　<head><title>Example SSI</title></head>
　<body>
　　<!--#include file="navbar.shtml" -->
　</body>
</html>
```

SSI技术的最终演化结果就是在HTML里面包含更为复杂的代码，并使用更为强大的解释器（interpreter）。这一模式衍生出了PHP、ASP、JSP和ColdFusion等一系列非常成功的引擎，开发者通过使用这些引擎能够开发出各式各样复杂的Web应用。除此之外，这一模式也是Mustache、ERB、Velocity等一系列Web模板引擎的基础。

如前所述，Web应用是为了通过HTTP向用户发送定制的动态内容而诞生的，为了弄明白Web应用的运作原理，我们必须知道HTTP的工作过程，并理解HTTP请求和响应的运作机制。

