### 4.2.1　Form字段

上一节曾经提到过，为了提取表单传递的键值对数据，用户可能需要亲自对服务器接收到的未经处理的表单数据进行语法分析。但事实上，因为 `net/http` 库已经提供了一套用途相当广泛的函数，这些函数一般都能够满足用户对数据提取方面的需求，所以我们很少需要自行对表单数据进行语法分析。

通过调用 `Request` 结构提供的方法，用户可以将URL、主体又或者以上两者记录的数据提取到该结构的 `Form` 、 `PostForm` 和 `MultipartForm` 等字段当中。跟我们平常通过 `POST` 请求获取到的数据一样，存储在这些字段里面的数据也是以键值对形式表示的。使用 `Request` 结构的方法获取表单数据的一般步骤是：

（1）调用 `ParseForm` 方法或者 `ParseMultipartForm` 方法，对请求进行语法分析。

（2）根据步骤1调用的方法，访问相应的 `Form` 字段、 `PostForm` 字段或 `MultipartForm` 字段。

代码清单4-4展示了一个使用 `ParseForm` 方法对表单进行语法分析的例子。

代码清单4-4　对表单进行语法分析

```go
package main
import (
　　"fmt"
　　"net/http"
)
func process(w http.ResponseWriter, r *http.Request) {
　　r.ParseForm()
　　fmt.Fprintln(w, r.Form)
}
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　}
　　http.HandleFunc("/process", process)
　　server.ListenAndServe()
}
```

这段代码中最重要的就是下面这两行：

```go
r.ParseForm()
fmt.Fprintln(w, r.Form)
```

如前所述，这段代码首先使用了 `ParseForm` 方法对请求进行语法分析，然后再访问 `Form` 字段，获取具体的表单。

现在，让我们来创建一个短小精悍的HTML表单，并使用它作为客户端，向代码清单4-4所示的服务器发送请求。请创建一个名为 `client.html` 的文件，并将以下代码复制到该文件中：

```go
<html>
　<head>
　　<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
　　<title>GoWebProgramming</title>
　</head>
　<body>
　　<form action=http://127.0.0.1:8080/process?hello=world&thread=123 
　　➥method="post" enctype="application/x-www-form-urlencoded">
　　　<input type="text" name="hello" value="sau sheong"/>
　　　<input type="text" name="post" value="456"/>
　　　<input type="submit"/>
　　</form>
　</body>
</html>
```

这个HTML表单可以完成以下工作：

+ 通过 `POST` 方法将表单发送至地址http://localhost:8080/process?hello=world&thread=123；
+ 通过 `enctype` 属性将表单的内容类型设置为 `application/x-www-form-urlencoded；`
+ 将 `hello=sau sheong` 和 `post=456` 这两个HTML表单键值对发送至服务器。

需要注意的是，这个表单为相同的键 `hello` 提供了两个不同的值，其中，值 `world` 是通过URL提供的，而值 `sau sheong` 则是通过HTML表单中的文本输入行提供的。

因为客户端可以直接在浏览器上运行，所以我们并不需要使用服务器来为客户端提供服务：我们要做的就是使用浏览器打开 `client.html` 文件，然后点击表单中的发送按钮。如果一切正常，浏览器应该会显示以下输出：

```go
map[thread:[123] hello:[sau sheong world] post:[456]]
```

这是服务器在对请求进行语法分析之后，使用字符串形式显示出来的未经处理的 `Form` 结构。这个结构是一个映射，它的键是字符串，而键的值是一个由字符串组成的切片。因为映射是无序的，所以你看到的键值对排列顺序可能和这里展示的有所不同。但是无论如何，这个映射总是会包含查询值 `hello=world` 和 `thread=123` ，还有表单值 `hello=sau sheong` 和 `post=456` 。正如所见，这些值都进行了相应的URL解码，比如在 `sau` 和 `sheong` 之间就能够正常地看到空格，而不是编码之后的 `%20` 。

