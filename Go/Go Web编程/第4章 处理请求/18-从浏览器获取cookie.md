### 4.4.3　从浏览器获取cookie

在学习了如何将cookie存储到客户端之后，现在让我们来看看如何从客户端获取cookie，代码清单4-15展示了这一操作的具体实现方法。

代码清单4-15　从请求的首部获取cookie

```go
package main
import (
　　"fmt"
　　"net/http"
)
func setCookie(w http.ResponseWriter, r *http.Request) {
　　c1 := http.Cookie{
　　　　Name:　　 "first_cookie",
　　　　Value:　　"Go Web Programming",
　　　　HttpOnly: true,
　　}
　　c2 := http.Cookie{
　　　　Name: "second_cookie",
　　　　Value: "Manning Publications Co",
　　　　HttpOnly: true,
　　}
　　http.SetCookie(w, &c1)
　　http.SetCookie(w, &c2)
}
func getCookie(w http.ResponseWriter, r *http.Request) {
　　h := r.Header["Cookie"]
　　fmt.Fprintln(w, h)
}
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　}
　　http.HandleFunc("/set_cookie", setCookie)
　　http.HandleFunc("/get_cookie", getCookie)
　　server.ListenAndServe()
}
```

在重新编译并且重新启动这个服务器之后，使用浏览器访问http://127.0.0.1:8080/get_cookie，将会在浏览器上看到以下结果：

```go
[first_cookie=Go Web Programming; second_cookie=Manning Publications Co]
```

语句 `r.Header["Cookie"]` 返回了一个切片，这个切片包含了一个字符串，而这个字符串又包含了客户端发送的任意多个cookie。如果用户想要取得单独的键值对格式的cookie，就需要自行对 `r.Header["Cookie"]` 返回的字符串进行语法分析。不过Go也提供了一些其他方法，让用户可以更容易地获取cookie，代码清单4-16展示了这一点。

代码清单4-16　使用 `Cookie` 方法和 `Cookie` 方法

```go
package main
import (
　　"fmt"
　　"net/http"
)
func setCookie(w http.ResponseWriter, r *http.Request) {
　　c1 := http.Cookie{
　　　　Name: "first_cookie",
　　　　Value: "Go Web Programming",
　　　　HttpOnly: true,
　　}
　　c2 := http.Cookie{
　　　　Name:　　 "second_cookie",
　　　　Value:　　"Manning Publications Co",
　　　　HttpOnly: true,
　　}
　　http.SetCookie(w, &c1)
　　http.SetCookie(w, &c2)
}
func getCookie(w http.ResponseWriter, r *http.Request) {
　　c1, err := r.Cookie("first_cookie")
　　if err != nil {
　　　　fmt.Fprintln(w, "Cannot get the first cookie")
　　}
　　cs := r.Cookies()
　　fmt.Fprintln(w, c1)
　　fmt.Fprintln(w, cs)
}
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　}
　　http.HandleFunc("/set_cookie", setCookie)
　　http.HandleFunc("/get_cookie", getCookie)
　　server.ListenAndServe()
}
```

Go语言为 `Request` 结构提供了一个 `Cookie` 方法，正如代码清单4-16中的加粗行所示，这个方法可以获取指定名字的cookie。如果指定的cookie不存在，那么方法将返回一个错误。因为 `Cookie` 方法只能获取单个cookie，所以如果想要同时获取多个cookie，就需要用到 `Request` 结构的 `Cookies` 方法： `Cookies` 方法可以返回一个包含了所有cookie的切片，这个切片跟访问 `Header` 字段时获取的切片是完全相同的。在重新编译并且重新启动服务器之后，访问http://127.0.0.1:8080/get_cookie，浏览器将显示以下内容：

```go
first_cookie=Go Web Programming
[first_cookie=Go Web Programming second_cookie=Manning Publications Co]
```

因为上面展示的代码在设置cookie时并没有为这些cookie设置相应的过期时间，所以它们都是会话cookie。为了证明这一点，我们只需要退出并重启浏览器（注意，不要只关闭浏览器的标签，一定要完全退出浏览器才可以），然后再次访问http://127.0.0.1:8080/get_cookie，就会发现之前设置的cookie已经消失了。

