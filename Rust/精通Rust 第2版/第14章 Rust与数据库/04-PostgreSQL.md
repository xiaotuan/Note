### 14.3　PostgreSQL

虽然SQLite适用于原型设计和更简单的用例，但真正的关系型数据库管理系统可以让开发者的工作更轻松。PostgreSQL 就是这样一款复杂的数据库系统。为了在 Rust 中集成postgres，我们有在crates.io上创建的postgres软件包。它是一个原生的Rust客户端，这意味着它不会在C程序库上运行，而是在Rust中实现整个协议。其API的风格和rusqlite软件包的风格类似，这其实是有意为之的，SQLite客户端的API实际上是基于postgres客户端的。postgres软件包支持PostgreSQL的某些独特的功能，例如位向量、time字段、JSON支持及UUID。

在本节中，我们将通过创建初始化postgres数据库的示例程序并在其上执行一些插入和查询操作来探讨与postgres的交互。我们假定你已经在系统上设置了数据库，用于该示例的PostgreSQL是9.5版本。





![166.png](../images/166.png)
**注意**

要安装PostgreSQL数据库系统，推荐参考DigitalOcean上的文章。



postgres附带了名为psql的命令行工具，可用于运行查询、检索数据表、管理角色，查看系统信息等。我们可以通过在psql提示符下运行以下命令来查看系统上运行的postgres版本。首先我们将通过运行如下命令启动psql：

```rust
$ sudo -u postgres psql
```

进入psql之后，我们可以在提示符下运行如下命令：

```rust
postgres=# SELECT version();
```

运行上述命令之后，我们得到以下输出结果：

```rust
PostgreSQL 9.5.14 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu
5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609, 64-bit
```

为了让这个示例更简单，我们将复用在演示rusqlite时使用的书籍数据，将在以下示例中使用默认的用户名（postgres）和密码（postgres）。你需要调整以下示例来兼容新的用户信息。让我们通过运行cargo new postgres_demo命令来创建一个新项目。这是我们在Cargo. toml文件中的依赖项：

```rust
# postgres_demo/Cargo.toml
[dependencies]
postgres = "0.15.2"
serde = { version = "1.0.82"}
serde_derive = "1.0.82"
serde_json = "1.0.33"
```

让我们来看看main.rs中的代码：

```rust
// postgres_demo/src/main.rs
use postgres::{Connection, TlsMode};
const DROP_TABLE: &str = "DROP TABLE IF EXISTS books";
const CONNECTION: &str = "postgres://postgres:postgres@localhost:5432";
const CREATE_TABLE: &str = "CREATE TABLE IF NOT EXISTS books
                            (id SERIAL PRIMARY KEY,
                            title VARCHAR NOT NULL,
                            author VARCHAR NOT NULL,
                            year SERIAL)";
#[derive(Debug)]
struct Book {
    id: i32,
    title: String,
    author: String,
    year: i32
}
fn reset_db(conn: &Connection) {
    let _ = conn.execute(DROP_TABLE, &[]).unwrap();
    let _ = conn.execute(CREATE_TABLE, &[]).unwrap();
}
```

我们有一堆字符串常量，用于连接数据库以及创建和删除books表。接下来是我们的main函数：

```rust
// postgres_demo/src/main.rs
fn main() {
    let conn = Connection::connect(CONNECTION, TlsMode::None).unwrap();
    reset_db(&conn);
    let book = Book {
        id: 3,
        title: "A programmers introduction to mathematics".to_string(),
        author: "Dr. Jeremy Kun".to_string(),
        year: 2018
    };
    conn.execute("INSERT INTO books (id, title, author, year) VALUES ($1,
$2, $3, $4)",
                 &[&book.id, &book.title, &book.author,
&book.year]).unwrap();
    for row in &conn.query("SELECT id, title, author, year FROM books",
&[]).unwrap() {
        let book = Book {
            id: row.get(0),
            title: row.get(1),
            author: row.get(2),
            year: row.get(3)
        };
        println!("{:?}", book);
    }
}
```

因为这里我们并没有使用ORM，它只是一个低级接口，所以我们需要手动将值解压到数据库查询中。接下来运行该程序：

![167.png](../images/167.png)
这是程序的输出结果，以及对数据表的psql查询，以显示后续的内容：

![168.png](../images/168.png)
首先，我们在psql命令提示符下使用\dt命令显示数据库列表。接下来，我们执行查询，即“select * from books”。

这些是Rust与PostgreSQL交互的基础知识。接下来，让我们探讨如何通过使用连接池的概念来提高数据库查询的效率。

