### 7.6　创建Go Web服务

创建Go Web服务并不是一件困难的事情：如果你仔细地阅读并理解了前面各个章节介绍的内容，那么掌握接下来要介绍的知识对你来说应该是轻而易举的。

本节将要构建一个简单的基于REST的Web服务，它允许我们对论坛帖子执行创建、获取、更新以及删除操作。具体来说，我们将会使用第6章介绍过的CRUD函数来包裹起一个Web服务接口，并通过JSON格式来传输数据。除了本章之外，后续的章节也会沿用这个Web服务作为例子，对其他概念进行介绍。

代码清单7-14展示了实现Web服务需要用到的数据库操作，这些操作和6.4节介绍过的操作基本相同，只是做了一些简化。这些代码定义了Web服务需要对数据库执行的所有操作，它们都隶属于 `main` 包，并且被放置到了 `data.go文件` 中。

代码清单7-14　使用 `data.go` 访问数据库

```go
package main
import (
　"database/sql"
　_ "github.com/lib/pq"
)
var Db *sql.DB
func init() {  ❶
　var err error
　Db, err = sql.Open("postgres", "user=gwp dbname=gwp password=gwp sslmode=
　 disable")
　if err != nil {
　　panic(err)
　}
}
func retrieve(id int) (post Post, err error) {  ❷
　post = Post{}
　err = Db.QueryRow("select id, content, author from posts where id = $1",
　 id).Scan(&post.Id, &post.Content, &post.Author)
　return
}
func (post *Post) create() (err error) {  ❸
　statement := "insert into posts (content, author) values ($1, $2) returning
　 id"
　stmt, err := Db.Prepare(statement)
　if err != nil {
　　return
　}
　defer stmt.Close()
　err = stmt.QueryRow(post.Content, post.Author).Scan(&post.Id)
　return
}
func (post *Post) update() (err error) {  ❹
　_, err = Db.Exec("update posts set content = $2, author = $3 where id =
　$1", post.Id, post.Content, post.Author)
　return
}
func (post *Post) delete() (err error) {  ❺
　_, err = Db.Exec("delete from posts where id = $1", post.Id)
　return
}
```

❶ 连接到数据库

❷ 获取指定的帖子

❸ 创建一篇新帖子

❹ 更新指定的帖子

❺ 删除指定的帖子

正如所见，这些代码跟前面代码清单6-6展示过的代码非常相似，只是在函数名和方法名上稍有区别，因此我们在这里就不再一一解释了。如果你需要重温一下这些代码的作用，那么可以去复习一下6.4节。

在拥有了对数据库执行CRUD操作的能力之后，让我们来学习一下如何实现真正的Web服务。代码清单7-15展示了整个Web服务的实现代码，这些代码保存在文件 `server.go` 中。

代码清单7-15　定义在 `server.go文件` 内的Go Web服务

```go
package main
import (
　"encoding/json"
　"net/http"
　"path"
　"strconv"
)
type Post struct {
　Id　　　int　　`json:"id"`
　Content string `json:"content"`
　Author　string `json:"author"`
}
func main() {
　server := http.Server{
　　Addr: "127.0.0.1:8080",
　}
　http.HandleFunc("/post/", handleRequest)
   server.ListenAndServe()
}
func handleRequest(w http.ResponseWriter, r *http.Request) {  ❶
　var err error
　switch r.Method {
　case "GET":
　　err = handleGet(w, r)
　case "POST":
　　err = handlePost(w, r)
　case "PUT":
　　err = handlePut(w, r)
　case "DELETE":
　　err = handleDelete(w, r)
　}
　if err != nil {
　　http.Error(w, err.Error(), http.StatusInternalServerError)
　　return
　}
}
func handleGet(w http.ResponseWriter, r *http.Request) (err error) {  ❷
　id, err := strconv.Atoi(path.Base(r.URL.Path))
　if err != nil {
　　return
　}
　post, err := retrieve(id)
　if err != nil {
　　return
　}
　output, err := json.MarshalIndent(&post, "", "\t\t")
　if err != nil {
　　return
　}
　w.Header().Set("Content-Type", "application/json")
　w.Write(output)
　return
}
func handlePost(w http.ResponseWriter, r *http.Request) (err error) {  ❸
　len := r.ContentLength
　body := make([]byte, len)
　r.Body.Read(body)
　var post Post
　json.Unmarshal(body, &post)
　err = post.create()
　if err != nil {
　　return
　}
　w.WriteHeader(200)
　return
}
func handlePut(w http.ResponseWriter, r *http.Request) (err error) {  ❹
 id, err := strconv.Atoi(path.Base(r.URL.Path))
　if err != nil {
　　return
　}
　post, err := retrieve(id)
　if err != nil {
　　return
　}
　len := r.ContentLength
　body := make([]byte, len)
　r.Body.Read(body)
　json.Unmarshal(body, &post)
　err = post.update()
　if err != nil {
　　return
　}
　w.WriteHeader(200)
　return
}
func handleDelete(w http.ResponseWriter, r *http.Request) (err error) {  ❺
 id, err := strconv.Atoi(path.Base(r.URL.Path))
　if err != nil {
　　return
　}
　post, err := retrieve(id)
　if err != nil {
　　return
　}
　err = post.delete()
　if err != nil {
　　return
　}
　w.WriteHeader(200)
　return
}
```

❶ 多路复用器负责将请求转发给正确的处理器函数

❷ 获取指定的帖子

❸ 创建新的帖子

❹ 更新指定的帖子

❺ 删除指定的帖子

这段代码的结构非常直观： `handleRequest` 多路复用器会根据请求使用的HTTP方法，把请求转发给相应的CRUD处理器函数，这些函数都接受一个 `ResponseWriter` 和一个 `Request` 作为参数，并返回可能出现的错误作为函数的执行结果； `handleRequest` 会检查这些函数的执行结果，并在发现错误时通过 `StatusInternalServerError` 返回一个500状态码。

接下来，让我们首先从帖子的创建操作开始，对Go Web服务的各个部分进行详细的解释， `handlePost` 函数如代码清单7-16所示。

代码清单7-16　用于创建帖子的函数

```go
func handlePost(w http.ResponseWriter, r *http.Request) (err error) {
 len := r.ContentLength
 body := make([]byte, len)  ❶❷
　r.Body.Read(body)
　var post Post
    json.Unmarshal(body, &post) ❸
　err = post.create()  ❹
　if err != nil {
　　return
　}
　w.WriteHeader(200)
　return
}
```

❶ 读取请求主体，并将其存储在字节切片中; ❷创建一个字节切片

❸ 把切片存储的数据解封至Post 结构

❹ 创建数据库记录

`handlePost` 函数首先会根据内容的长度创建出一个字节切片，然后将请求主体记录的JSON字符串读取到字节切片里面。之后，函数会声明一个 `Post` 结构，并将字节切片存储的内容解封到这个结构里面。这样一来，函数就拥有了一个填充了数据的 `Post` 结构，于是它调用结构的 `Create` 方法，把记录在结构中的数据存储到了数据库里面。

为了调用Web服务，我们需要用到第3章介绍过的cURL，并在终端中执行以下命令：

```go
curl -i -X POST -H "Content-Type: application/json"　-d '{"content":"My first 
➥post","author":"Sau Sheong"}' http://127.0.0.1:8080/post/
```

这个命令首先会把 `Content-Type` 首部设置为 `application/json` ，然后通过 `POST` 方法，向地址 `http://127.0.0.1/post/` 发送一条主体为JSON字符串的HTTP请求。如果一切顺利，应该会看到以下结果：

```go
HTTP/1.1 200 OK
Date: Sun, 12 Apr 2015 13:32:14 GMT
Content-Length: 0
Content-Type: text/plain; charset=utf-8
```

不过这个结果只能证明处理器函数在处理这个请求的时候没有发生任何错误，却无法说明帖子真的已经创建成功了。为了验证这一点，我们需要通过执行以下SQL查询来检视一下数据库：

```go
psql -U gwp -d gwp -c "select * from posts;"
```

如果帖子创建成功了，应该会看到以下结果：

```go
 id |　　content　　|　 author
----+---------------+------------
　1 | My first post | Sau Sheong
(1 row)
```

除了 `handlePost` 函数之外，我们的Web服务的每个处理器函数都会假设目标帖子的 `id` 已经包含在了URL里面。比如说，当用户想要获取一篇帖子时，Web服务接收到的请求应该指向以下URL：

```go
/post/<id>
```

而这个URL中的 `<id>` 记录的就是帖子的 `id` 。代码清单7-17展示了函数是如何通过这一机制来获取帖子的。

代码清单7-17　用于获取帖子的函数

```go
func handleGet(w http.ResponseWriter, r *http.Request) (err error) {
　id, err := strconv.Atoi(path.Base(r.URL.Path))
　if err != nil {
　　return
　}
   post, err := retrieve(id) ❶
　if err != nil {
　　return
　}
   output, err := json.MarshalIndent(&post, "", "\t\t")  ❷
　if err != nil {
　　return
　}
    w.Header().Set("Content-Type", "application/json")  ❸
　w.Write(output)
　return
}
```

❶ 从数据库里获取数据，并将其填充到Post 结构中

❷ 把Post 结构封装为JSON 字符串

❸ 把JSON 数据写入ResponseWriter

`handleGet` 函数首先通过 `path.Base` 函数，从URL的路径中提取出字符串格式的帖子 `id` ，接着使用 `strconv.Atoi` 函数把这个 `id` 转换成整数格式，然后通过把这个 `id` 传递给 `retrivePost` 函数来获得填充了帖子数据的 `Post` 结构。

在此之后，程序通过 `json.MarshalIndent` 函数，把 `Post` 结构转换成了JSON格式的字节切片。最后，程序把 `Content-Type` 首部设置成了 `application/json` ，并把字节切片中的JSON数据写入 `ResponseWriter` ，以此来将JSON数据返回给调用者。

为了观察 `handleGet` 函数是如何工作的，我们需要在终端里面执行以下命令：

```go
curl -i -X GET http://127.0.0.1:8080/post/1
```

这条命令会向给定的URL发送一个 `GET` 请求，尝试获取 `id` 为 `1` 的帖子。如果一切正常，那么这条命令应该会返回以下结果：

```go
HTTP/1.1 200 OK
Content-Type: application/json
Date: Sun, 12 Apr 2015 13:32:18 GMT
Content-Length: 69
{
　　"id": 1,
　　"content": "My first post",
　　"author": "Sau Sheong"
}
```

在更新帖子的时候，程序同样需要先获取帖子的数据，具体细节如代码清单7-18所示。

代码清单7-18　用于更新帖子的函数

```go
func handlePut(w http.ResponseWriter, r *http.Request) (err error) {
id, err := strconv.Atoi(path.Base(r.URL.Path))
　if err != nil {
　　return
　}
   post, err := retrieve(id)  ❶
　if err != nil {
　　return
　}
    len := r.ContentLength
    body := make([]byte, len)
    r.Body.Read(body) ❷
　json.Unmarshal(body, &post) ❸
   err = post.update() ❹
　if err != nil {
　　return
　}
　w.WriteHeader(200)
　return
}
```

❶ 从数据库里获取指定帖子的数据，并将其填充至Post 结构

❷ 从请求主体中读取JSON 数据

❸ 把JSON 数据解封至Post 结构

❹ 对数据库进行更新

在更新帖子时， `handlePut` 函数首先会获取指定的帖子，然后再根据 `PUT` 请求发送的信息对帖子进行更新。在获取了帖子对应的 `Post` 结构之后，程序会读取请求的主体，并将主体中的内容解封至 `Post` 结构，最后通过调用 `Post` 结构的 `update` 方法更新帖子。

通过在终端里面执行以下命令，我们可以对之前创建的帖子进行更新：

```go
curl -i -X PUT -H "Content-Type: application/json" -d '{"content":"Updated 
➥post","author":"Sau Sheong"}' http://127.0.0.1:8080/post/1
```

需要注意的是，跟使用 `POST` 方法创建帖子时不一样，这次我们需要通过URL来指定被更新帖子的ID。如果一切正常，这条命令应该会返回以下结果：

```go
HTTP/1.1 200 OK
Date: Sun, 12 Apr 2015 14:29:39 GMT
Content-Length: 0
Content-Type: text/plain; charset=utf-8
```

现在，我们可以通过再次执行以下SQL查询来确认更新是否已经成功：

```go
psql -U gwp -d gwp -c "select * from posts;"
```

如无意外，应该会看到以下内容：

```go
 id |　 content　　|　 author
----+--------------+------------
　1 | Updated post | Sau Sheong
(1 row)
```

代码清单7-19展示了Web服务的帖子删除操作的实现代码，这些代码会先获取指定的帖子，然后通过调用 `delete` 方法来删除帖子。

代码清单7-19　用于删除帖子的函数

```go
func handleDelete(w http.ResponseWriter, r *http.Request) (err error) {
　id, err := strconv.Atoi(path.Base(r.URL.Path))
　if err != nil {
　　return
　}
   post, err := retrieve(id) ❶
　if err != nil {
　　return
　}
   err = post.delete() ❷
　if err != nil {
　　return
　}
　w.WriteHeader(200)
　return
}
```

❶ 从数据库里获取指定帖子的数据，并将其填充至Post 结构

❷ 从数据库里删除这个帖子

注意，无论是更新帖子还是删除帖子，Web服务在操作执行成功时都会返回200状态码。但是，如果处理器函数在处理请求时出现了任何错误，那么该错误将被返回至 `handleRequest` 多路复用器，然后由多路复用器向客户端返回一个500状态码。

通过执行下面的cURL调用，我们可以删除前面创建的帖子：

```go
curl -i -X DELETE http://127.0.0.1:8080/post/1
```

如果一切正常，那么这个cURL调用将返回以下结果：

```go
HTTP/1.1 200 OK
Date: Sun, 12 Apr 2015 14:38:59 GMT
Content-Length: 0
Content-Type: text/plain; charset=utf-8
```

现在，如果我们再次执行之前的SQL查询，就会发现之前创建的帖子已经不复存在了：

```go
id | content | author
----+---------+--------
(0 rows)
```

