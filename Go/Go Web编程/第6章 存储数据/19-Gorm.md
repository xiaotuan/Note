### 6.5.2　Gorm

Gorm的开发者声称Gorm是最棒的Go语言ORM，他们的确所言非虚。Gorm是“Go-ORM”一词的缩写，这个项目是一个使用Go实现的ORM，它遵循的是与Ruby的ActiveRecord以及Java的Hibernate一样的道路。更确切地说，Gorm遵循的是数据映射器模式（Data-Mapper pattern），该模式通过提供映射器来将数据库中的数据映射为结构。（在6.3节介绍关系数据库时，使用的就是ActiveRecord模式。）

Gorm的能力非常强大，它允许程序员定义关系、实施数据迁移、串联多个查询以及执行其他很多高级的操作。除此之外，Gorm还能够设置回调函数，这些函数可以在特定的数据事件发生时执行。因为详尽地描述Gorm的各个特性可能会花掉整整一章的篇幅，所以我们在这里只会讨论它的基本特性。代码清单6-18展示了使用Gorm重新实现论坛程序的方法，跟之前一样，这次的代码也是存储在 `store.go` 文件里面。

代码清单6-18　使用Gorm实现论坛程序

```go
package main
import (
　　"fmt"
　　"github.com/jinzhu/gorm"
　　_ "github.com/lib/pq"
　　"time"
)
type Post struct {
　　Id　　　 int
　　Content　 string
　　Author　　string `sql:"not null"`
　　Comments　[]Comment
　　CreatedAt time.Time
}
type Comment struct {
　　Id　　　 int
　　Content　 string
　　Author　　string `sql:"not null"`
　　PostId　　int　　`sql:"index"`
　　CreatedAt time.Time
}
var Db gorm.DB
func init() {
　　var err error
　　Db, err = gorm.Open("postgres", "user=gwp dbname=gwp password=gwp
　　➥sslmode=disable")
　　if err != nil {
　　　　panic(err)
　　}
 　 Db.AutoMigrate(&Post{}, &Comment{})
}
func main() {
　　post := Post{Content: "Hello World!", Author: "Sau Sheong"}  ❶
　　fmt.Println(post)
  　 Db.Create(&post)  ❷
　　fmt.Println(post)  ❸
  　 comment := Comment{Content: "Good post!", Author: "Joe"}  ❹
　　Db.Model(&post).Association("Comments").Append(comment)
　　var readPost Post
   　 Db.Where("author = $1", "Sau Sheong").First(&readPost)  ❺
　　　var comments []Comment
　　　Db.Model(&readPost).Related(&comments)
fmt.Println(comments[0])   ❻
}
```

❶ {0 Hello World! Sau Sheong [] 0001-01-01 00:00:00 +0000 UTC}

❷ 创建一篇帖子

❸ {1 Hello World! Sau Sheong [] 2015-04-12 11:38:50.91815604 +0800 SGT}

❹ 添加一条评论

❺ 通过帖子获取评论

❻ {1 Good post! Joe 1 2015-04-13 11:38:50.920377 +0800 SGT}

这个新程序创建数据库句柄的方法跟我们之前创建数据库句柄的方法基本相同。另外需要注意的一点是，因为Gorm可以通过自动数据迁移特性来创建所需的数据库表，并在用户修改相应的结构时自动对数据库表进行更新，所以这个程序无需使用 `setup.sql` 文件来设置数据库表：当我们运行这个程序时，程序所需的数据库表就会自动生成。为了正确地运行这个程序，并让程序能够正常地创建数据库表，我们在执行这个程序之前必须先将之前创建的数据库表全部删除：

```go
func init() {
　　var err error
　　Db, err = gorm.Open("postgres", "user=gwp dbname=gwp password=gwp sslmode=disable")
　　if err != nil {
　　　　panic(err)
　　}
　　Db.AutoMigrate(&Post{}, &Comment{})
}
```

负责执行数据迁移操作的 `AutoMigrate` 方法是一个变长参数方法，这种类型的方法和函数能够接受一个或多个参数作为输入。在上面展示的代码中， `AutoMigrate` 方法接受的是 `Post` 结构和 `Comment` 结构。得益于自动数据迁移特性的存在，当用户向结构里面添加新字段的时候，Gorm就会自动在数据库表里面添加相应的新列。

上面的Gorm程序使用了下面所示的 `Comment` 结构：

```go
type Comment　struct {
　　Id　　　　int
　　Content　 string
　　Author　　string `sql:"not null"`
　　PostId　　int
　　CreatedAt time.Time
}
```

`Comment` 结构里面出现了一个类型为 `time.Time` 的 `CreatedAt` 字段，包含这样一个字段意味着Gorm每次在数据库里创建一条新记录的时候，都会自动对这个字段进行设置。

此外， `Comment` 结构的其中一些字段还用到了结构标签，以此来指示Gorm应该如何创建和映射相应的字段。比如 `，Comment` 结构的 `Author` 字段就使用了结构标签 ` `'sql: "not null"'` ，` 以此来告知Gorm，该字段对应列的值不能为 `null` 。

跟前面展示过的程序的另一个不同之处在于，这个程序没有在 `Comment` 结构里设置 `Post` 字段，而是设置了一个 `PostId` 字段。Gorm会自动把这种格式的字段看作是外键，并创建所需的关系。

在了解了 `Post` 结构和 `Comment` 结构的新定义之后，现在，让我们来看看程序是如何创建并获取帖子及其评论的。首先，程序会使用以下语句来创建新的帖子：

```go
post := Post{Content: "Hello World!", Author: "Sau Sheong"}
Db.Create(&post)
```

这段代码没有什么难懂的地方，它跟之前展示过的代码的最主要区别在于——程序这次遵循了数据映射器模式：它在创建帖子时会使用数据库句柄 `gorm.DB` 作为构造器，而不是像之前遵循ActiveRecord模式时那样，通过直接调用 `Post` 结构自有的 `Create` 方法来创建帖子。

如果直接查看数据库内部，应该会看到 `created_at` 这个时间戳列在帖子创建出来的同时已经自动被设置好了。

在创建出帖子之后，程序使用了以下语句来为帖子添加评论：

```go
comment := Comment{Content: "Good post!", Author: "Joe"}
Db.Model(&post).Association("Comments").Append(comment)
```

这段代码会先创建出一条评论，然后通过串联 `Model` 方法、 `Association` 方法和 `Append` 方法来将评论添加到帖子里面。注意，在创建评论的过程中，我们无需手动对 `Comment` 结构的 `PostId` 字段执行任何操作。

最后，程序使用了以下代码来获取帖子及其评论：

```go
var readPost Post
Db.Where("author = $1", "Sau Sheong").First(&readPost)
var comments []Comment
Db.Model(&readPost).Related(&comments)
```

这段代码跟之前展示过的代码有些类似，它使用了 `gorm.DB` 的 `Where` 方法来查找第一条作者名为 `"Sau Sheong"` 的记录，并将这条记录存储在了 `readPost` 变量里面，而这条记录就是我们刚刚创建的帖子。之后，程序首先调用 `Model` 方法获取帖子的模型，接着调用 `Related` 方法获取帖子的评论，并在最后将这些评论存储到 `comments` 变量里面。

正如之前所说，本节展示的特性只是Gorm这个ORM库众多特性的一小部分，如果你对这个库感兴趣，可以通过https://github.com/jinzhu/gorm了解更多相关信息。

Gorm并不是Go语言唯一的ORM库。除Gorm之外，Go还拥有不少同样具备众多特性的ORM库，比如，Beego的ORM库以及GORP（GORP并不完全是一个ORM，但它与ORM相去不远）。

在本章中，我们了解了构建Web应用所需的基本组件，而在接下来的一章中，我们将要开始讨论如何构建Web服务。

