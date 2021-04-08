### 6.5.1　Sqlx

Sqlx是一个第三方库，它为 `database/sql` 包提供了一系列非常有用的扩展功能。因为Sqlx和 `database/sql` 包使用的是相同的接口，所以Sqlx能够很好地兼容使用 `database/sql` 包的程序，除此之外，Sqlx还提供了以下这些额外的功能：

+ 通过结构标签（struct tag）将数据库记录（即行）封装为结构、映射或者切片；
+ 为预处理语句提供具名参数支持。

代码清单6-17展示了如何使用Sqlx及其提供的 `StructScan` 方法来对论坛程序进行简化。另外别忘了，在使用Sqlx库之前，需要先通过执行以下命令来获取这个库：

```go
go get "github.com/jmoiron/sqlx"
```

代码清单6-17　使用 Sqlx 重新实现论坛程序

```go
package main
import (
　　"fmt"
　　"github.com/jmoiron/sqlx"
　　_ "github.com/lib/pq"
)
type Post struct {
　　Id　　 int
　　Content string
　　AuthorName string `db: author`
}
var Db *sqlx.DB
func init() {
　　var err error
　　Db, err = sqlx.Open("postgres", "user=gwp dbname=gwp password=gwp
　　➥sslmode=disable")
　　if err != nil {
　　　　panic(err)
　　}
}
func GetPost(id int) (post Post, err error) {
　　post = Post{}
　　err = Db.QueryRowx("select id, content, author from posts where id =
　　➥$1", id).StructScan(&post)
　　if err != nil {
　　　　return
　　}
　　return
}
func (post *Post) Create() (err error) {
　　err = Db.QueryRow("insert into posts (content, author) values ($1, $2)
　　➥returning id", post.Content, post.AuthorName).Scan(&post.Id)
　　return
}
func main() {
　　post := Post{Content: "Hello World!", AuthorName: "Sau Sheong"}
　　post.Create()
　　fmt.Println(post)  ❶
}
```

❶ {1 Hello World! Sau Sheong}}

代码清单中的加粗代码展示了使用Sqlx与使用 `database/sql` 之间的区别，而其余的则是一些我们之前已经看到过的代码。首先，程序现在不再导入 `database/sql` 包，而是导入 `github.com/jmoiron/sqlx` 包。在默认情况下， `StructScan` 会根据结构字段名的英文小写体，将结构中的字段映射至表中的列。为了演示如何将指定的表列映射至指定的结构字段，代码清单6-17将原来的 `Author` 字段修改成了 `AuthorName` 字段，然后通过结构标签来指示Sqlx应该从 `author` 列里面获取 `AuthorName` 字段的数据。本书将在第7章对结构标签做进一步的说明。

程序现在也会使用 `sqlx.DB` 结构来代替之前的 `sql.DB` 结构，这两种结构非常相似，只不过 `sqlx.DB` 包含了诸如 `Queryx` 以及 `QueryRowx` 等额外的方法。

修改之后的 `GetPost` 函数也使用 `QueryRowx` 代替了之前的 `QueryRow` 。 `QueryRowx` 在执行之后将返回 `Rowx` 结构，这种结构拥有 `StructScan` 方法，该方法可以将列自动地映射到相应的字段里面。另一方面，对于 `Create` 方法，我们还是跟之前一样，使用 `QueryRow` 方法进行查询。

除了这里提到的特性之外，Sqlx还拥有其他一些有趣的特性，感兴趣的读者可以通过访问Sqlx的GitHub页面来了解：https://github.com/jmoiron/sqlx。

Sqlx是一个有趣并且有用的 `database/sql` 扩展，但它支持的特性并不多。与此相反，我们接下来要学习的Gorm库不仅把 `database/sql` 包隐藏了起来，它还提供了一个完整且强大的ORM机制来代替 `database/sql` 包。

