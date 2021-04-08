### 2.4.4　使用cookie进行访问控制

跟其他很多Web应用一样，ChitChat既拥有任何人都可以访问的公开页面，也拥有用户在登录账号之后才能看见的私人页面。

当一个用户成功登录以后，服务器必须在后续的请求中标示出这是一个已登录的用户。为了做到这一点，服务器会在响应的首部中写入一个cookie，而客户端在接收这个cookie之后则会把它存储到浏览器里面。代码清单2-4展示了 `authenticate` 处理器函数的实现代码，这个函数定义在 `route_auth.go` 文件中，它的作用就是对用户的身份进行验证，并在验证成功之后向客户端返回一个cookie。

代码清单2-4  ` `route_auth.go` ` 文件中的 `authenticate` 处理器函数

```go
func authenticate(w http.ResponseWriter, r *http.Request) {
　r.ParseForm()
　user, _ := data.UserByEmail(r.PostFormValue("email"))
　if user.Password == data.Encrypt(r.PostFormValue("password")) {
　　session := user.CreateSession()
　　cookie := http.Cookie{
　　　Name: "_cookie",
　　　Value: session.Uuid,
　　　HttpOnly: true,
　　}
　　http.SetCookie(w, &cookie)
　　http.Redirect(w, r, "/", 302)
　} else {
　　http.Redirect(w, r, "/login", 302)
　}
}
```

注意，代码清单2-4中的 `authenticate` 函数使用了两个我们尚未介绍过的函数，一个是 `data.Encrypt` ，而另一个则是 `data.UserbyEmail` 。因为本节关注的是ChitChat论坛的访问控制机制而不是数据处理方法，所以本节将不会对这两个函数的实现细节进行解释，但这两个函数的名字已经很好地说明了它们各自的作用： `data.UserByEmail` 函数通过给定的电子邮件地址获取与之对应的 `User` 结构，而 `data.Encrypt` 函数则用于加密给定的字符串。本章稍后将会对 `data` 包作更详细的介绍，但是在此之前，让我们回到对访问控制机制的讨论上来。

在验证用户身份的时候，程序必须先确保用户是真实存在的，并且提交给处理器的密码在加密之后跟存储在数据库里面的已加密用户密码完全一致。在核实了用户的身份之后，程序会使用 `User` 结构的 `CreateSession` 方法创建一个 `Session` 结构，该结构的定义如下：

```go
type Session struct {
　Id　　　　int
　Uuid　　　string
　Email　　 string
　UserId　　int
　CreatedAt time.Time
}
```

`Session` 结构中的 `Email` 字段用于存储用户的电子邮件地址，而 `UserId` 字段则用于记录用户表中存储用户信息的行的ID。 `Uuid` 字段存储的是一个随机生成的唯一ID，这个ID是实现会话机制的核心，服务器会通过cookie把这个ID存储到浏览器里面，并把 `Session` 结构中记录的各项信息存储到数据库中。

在创建了 `Session` 结构之后，程序又创建了 `Cookie` 结构：

```go
cookie := http.Cookie{
　Name:　　　"_cookie",
　Value:　　 session.Uuid,
　HttpOnly:　true,
}
```

cookie的名字是随意设置的，而cookie的值则是将要被存储到浏览器里面的唯一ID。因为程序没有给cookie设置过期时间，所以这个cookie就成了一个会话cookie，它将在浏览器关闭时自动被移除。此外，程序将 `HttpOnly` 字段的值设置成了 `true` ，这意味着这个cookie只能通过HTTP或者HTTPS访问，但是却无法通过JavaScript等非HTTP API进行访问。

在设置好cookie之后，程序使用以下这行代码，将它添加到了响应的首部里面：

```go
http.SetCookie(writer, &cookie)
```

在将cookie存储到浏览器里面之后，程序接下来要做的就是在处理器函数里面检查当前访问的用户是否已经登录。为此，我们需要创建一个名为 `session` 的工具（utility）函数，并在各个处理器函数里面复用它。代码清单2-5展示了 `session` 函数的实现代码，跟其他工具函数一样，这个函数也是在 `util.go` 文件里面定义的。再提醒一下，虽然程序把工具函数的定义都放在了 `util.go` 文件里面，但是因为 `util.go` 文件也隶属于 `main` 包，所以这个文件里面定义的所有工具函数都可以直接在整个 `main` 包里面调用，而不必像 `data.Encrypt` 函数那样需要先引入包然后再调用。

代码清单2-5　 `util.go` 文件中的 `session` 工具函数

```go
func session(w http.ResponseWriter, r *http.Request)(sess data.Session, err
　error){
　cookie, err := r.Cookie("_cookie")
　if err == nil {
　　sess = data.Session{Uuid: cookie.Value}
　　if ok, _ := sess.Check(); !ok {
　　　err = errors.New("Invalid session")
　　}
　}
　return
}
```

为了从请求中取出cookie， `session` 函数使用了以下代码：

```go
cookie, err := r.Cookie("_cookie")
```

如果cookie不存在，那么很明显用户并未登录；相反，如果cookie存在，那么 `session` 函数将继续进行第二项检查——访问数据库并核实会话的唯一ID是否存在。第二项检查是通过 `data.Session` 函数完成的，这个函数会从cookie中取出会话并调用后者的 `Check` 方法：

```go
sess = data.Session{Uuid: cookie.Value}
if ok, _ := sess.Check(); !ok {
　err = errors.New("Invalid session")
}
```

在拥有了检查和识别已登录用户和未登录用户的能力之后，让我们来回顾一下之前展示的 `index` 处理器函数，代码清单2-6中被加粗的代码行展示了这个处理器函数是如何使用 `session` 函数的。

代码清单2-6　 `index` 处理器函数

```go
func index(w http.ResponseWriter, r *http.Request) {
　threads, err := data.Threads(); if err == nil {
　　, err := session(w, r)
　　public_tmpl_files := []string{"templates/layout.html",
　　　　　　　　　　　　　　　　　"templates/public.navbar.html",
　　　　　　　　　　　　　　　　　"templates/index.html"}
　　private_tmpl_files := []string{"templates/layout.html",
　　　　　　　　　　　　　　　　　 "templates/private.navbar.html",
　　　　　　　　　　　　　　　　　 "templates/index.html"}
　　var templates *template.Template
　　if err != nil {
　　　templates = template.Must(template.ParseFiles(public_tmpl_files...))
　　} else {
　　　templates = template.Must(template.ParseFiles(private_tmpl_files...))
　　}
　　templates.ExecuteTemplate(w, "layout", threads)
　}
}
```

通过调用 `session` 函数可以取得一个存储了用户信息的 `Session` 结构，不过因为 `index` 函数目前并不需要这些信息，所以它使用空白标识符（blank identifier）（_）忽略了这一结构。 `index` 函数真正感兴趣的是 `err` 变量，程序会根据这个变量的值来判断用户是否已经登录，然后以此来选择是使用 `public` 导航条还是使用 `private` 导航条。

好的，关于ChitChat应用处理请求的方法就介绍到这里了。本章接下来会继续讨论如何为客户端生成HTML，并完整地叙述之前没有说完的部分。

