### 对ResponseWriter进行写入

`Write` 方法接受一个字节数组作为参数，并将数组中的字节写入HTTP响应的主体中。如果用户在使用 `Write` 方法执行写入操作的时候，没有为首部设置相应的内容类型，那么响应的内容类型将通过检测被写入的前512字节决定。代码清单4-8展示了 `Write` 方法的用法。

代码清单4-8　使用 `Write` 方法向客户端发送响应

```go
package main
import (
　　"net/http"
)
func writeExample(w http.ResponseWriter, r *http.Request) {
　　str := `<html>
<head><title>Go Web Programming</title></head>
<body><h1>Hello World</h1></body>
</html>`
　　w.Write([]byte(str))
}
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　}
　　http.HandleFunc("/write", writeExample)
　　server.ListenAndServe()
}
```

这段代码通过调用 `Write` 方法将一段HTML字符串写入了HTTP响应的主体中。通过向服务器发送以下命令：

```go
curl -i 127.0.0.1:8080/write
```

我们可以得到以下响应：

```go
HTTP/1.1 200 OK
Date: Tue, 13 Jan 2015 16:16:13 GMT
Content-Length: 95
Content-Type: text/html; charset=utf-8
<html>
<head><title>GoWebProgramming</title></head>
<body><h1>Hello World</h1></body>
</html>
```

注意，尽管我们没有亲自为响应设置内容类型，但程序还是通过检测自动设置了正确的内容类型。

`WriteHeader` 方法的名字带有一点儿误导性质，它并不能用于设置响应的首部（ `Header` 方法才是做这件事的）： `WriteHeader` 方法接受一个代表HTTP响应状态码的整数作为参数，并将这个整数用作HTTP响应的返回状态码；在调用这个方法之后，用户可以继续对 `ResponseWriter` 进行写入，但是不能对响应的首部做任何写入操作。如果用户在调用 `Write` 方法之前没有执行过 `WriteHeader` 方法，那么程序默认会使用200 OK作为响应的状态码。

`WriteHeader` 方法在返回错误状态码时特别有用：如果你定义了一个API，但是尚未为其编写具体的实现，那么当客户端访问这个API的时候，你可能会希望这个API返回一个状态码 `501` Not Implemented，代码清单4-9通过添加新的处理器实现了这一需求。顺带一提，千万别忘了使用 `HandleFunc` 方法将新处理器绑定到 `DefaultServeMux` 多路复用器里面！

代码清单4-9　通过 `WriteHeader` 方法将状态码写入到响应当中

```go
package main
import (
　　"fmt"
　　"net/http"
)
func writeExample(w http.ResponseWriter, r *http.Request) {
　　str := `<html>
<head><title>Go Web Programming</title></head>
<body><h1>Hello World</h1></body>
</html>`
　　w.Write([]byte(str))
}
func writeHeaderExample(w http.ResponseWriter, r *http.Request) {
　　w.WriteHeader(501)
　　fmt.Fprintln(w, "No such service, try next door")
}
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　}
　　http.HandleFunc("/write", writeExample)
　　http.HandleFunc("/writeheader", writeHeaderExample)
　　server.ListenAndServe()
}
```

通过cURL访问刚刚添加的新处理器：

```go
curl -i 127.0.0.1:8080/writeheader
```

我们将得到以下响应：

```go
HTTP/1.1 501 Not Implemented
Date: Tue, 13 Jan 2015 16:20:29 GMT
Content-Length: 31
Content-Type: text/plain; charset=utf-8
No such service, try next door
```

最后，通过调用 `Header` 方法可以取得一个由首部组成的映射（关于首部的具体细节在4.1.3节曾经讲过），修改这个映射就可以俢改首部，修改后的首部将被包含在HTTP响应里面，并随着响应一同发送至客户端。

代码清单4-10　通过编写首部实现客户端重定向

```go
package main
import (
　　"fmt"
　　"net/http"
)
func writeExample(w http.ResponseWriter, r *http.Request) {
　　str := `<html>
<head><title>Go Web Programming</title></head>
<body><h1>Hello World</h1></body>
</html>`
　　w.Write([]byte(str))
}
func writeHeaderExample(w http.ResponseWriter, r *http.Request) {
　　w.WriteHeader(501)
　　fmt.Fprintln(w, "No such service, try next door")
}
func headerExample(w http.ResponseWriter, r *http.Request) {
　　w.Header().Set("Location", "http://google.com")
　　w.WriteHeader(302)
}
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　}
　　http.HandleFunc("/write", writeExample)
　　http.HandleFunc("/writeheader", writeHeaderExample)
　　http.HandleFunc("/redirect", headerExample)
　　server.ListenAndServe()
}
```

代码清单4-10向我们展示了如何实现一次HTTP重定向：除了将状态码设置成了 `302` 之外，它还给响应添加了一个名为 `Location` 的首部，并将这个首部的值设置成了重定向的目的地。需要注意的是，因为 `WriteHeader` 方法在执行完毕之后就不允许再对首部进行写入了，所以用户必须先写入 `Location` 首部，然后再写入状态码。现在，如果我们在浏览器里面访问这个处理器，那么浏览器将被重定向到Google。

另一方面，如果我们使用cURL访问这个处理器：

```go
curl -i 127.0.0.1:8080/redirect
```

那么cURL将获得以下响应：

```go
HTTP/1.1 302 Found
Location: http://google.com
Date: Tue, 13 Jan 2015 16:22:16 GMT
Content-Length: 0
Content-Type: text/plain; charset=utf-8
```

最后，让我们来学习一下通过 `ResponseWriter` 直接向客户端返回JSON数据的方法。代码清单4-11展示了如何以JSON格式将一个名为 `Post` 的结构返回给客户端。

代码清单4-11　编写JSON输出

```go
package main
import (
　　"fmt"
　　"encoding/json"
　　"net/http"
)
type Post struct {
　　User　　string
　　Threads []string
}
func writeExample(w http.ResponseWriter, r *http.Request) {
　　str := `<html>
<head><title>Go Web Programming</title></head>
<body><h1>Hello World</h1></body>
</html>`
　　w.Write([]byte(str))
}
func writeHeaderExample(w http.ResponseWriter, r *http.Request) {
　　w.WriteHeader(501)
　　fmt.Fprintln(w, "No such service, try next door")
}
func headerExample(w http.ResponseWriter, r *http.Request) {
　　w.Header().Set("Location", "http://google.com")
　　w.WriteHeader(302)
}
func jsonExample(w http.ResponseWriter, r *http.Request) {
　　w.Header().Set("Content-Type", "application/json")
　　post := &Post{
　　　　User:　　"Sau Sheong",
　　　　Threads: []string{"first", "second", "third"},
　　}
　　json, _ := json.Marshal(post)
　　w.Write(json)
}
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　}
　　http.HandleFunc("/write", writeExample)
　　http.HandleFunc("/writeheader", writeHeaderExample)
　　http.HandleFunc("/redirect", headerExample)
　　http.HandleFunc("/json", jsonExample)
　　server.ListenAndServe()
}
```

这段代码中的 `jsonExample` 处理器就是这次的主角。因为本书将在第7章进一步介绍JSON格式，所以不了解JSON格式的读者也不必过于担心，目前来说，你只需要知道变量 `json` 是一个由 `Post` 结构序列化而成的JSON字符串就可以了。

这段程序首先使用 `Header` 方法将内容类型设置成 `application/json` ，然后调用 `Write` 方法将JSON字符串写入 `ResponseWriter` 中。现在，如果我们执行cURL命令：

```go
curl -i 127.0.0.1:8080/json
```

那么它将返回以下响应：

```go
HTTP/1.1 200 OK
Content-Type: application/json
Date: Tue, 13 Jan 2015 16:27:01 GMT
Content-Length: 58
{"User":"Sau Sheong","Threads":["first","second","third"]}
```

