### 14.5　Postgres和diesel ORM

使用具有原始 SQL 查询的低级数据库软件包编写复杂的应用程序是一种容易出错的解决方案。diesel是Rust的ORM（对象关系映射器）和查询构建器。它采用了大量过程宏，会在编译期检测大多数数据库交互错误，并在大多数情况下能够生成非常高效的代码，有时甚至可以用C语言进行底层访问。这是因为它能够将通常在运行时进行的检查移动到编译期。在撰写本文时，diesel为PostgreSQL、MySQL及SQLite提供了开箱即用的支持。

我们将把数据库支持集成到第13章介绍的linksnap服务器中，将使用diesel以类型安全的方式与postgres数据库进行交互。我们将复制第13章介绍的linksnap项目，并将其重命名为linksnap_v2。同时我们不会介绍其完整源代码，只会讨论影响数据库与diesel集成的部分。代码块的其余部分与第13章的完全相同。

diesel项目由许多组件构成。首先，我们有一个名为diesel-cli的命令行工具，可以自动创建数据库并在必要时执行任何数据库的迁移操作。

在我们开始实现与数据库交互的示例之前，需要安装diesel-cli工具，它将设置我们的数据库和其中的表。我们可以通过运行如下命令来安装它：

```rust
cargo install diesel_cli --no-default-features --features postgres
```

我们只会用到CLI工具中的postgres功能，因此使用了--features标记。Cargo将获取并构建deisel_cli和依赖项，并将二进制文件安装到Cargo默认的二进制文件路径，通常该路径是~/.cargo/bin/目录。

在我们的linksnap_v2目录中，将把数据库连接URL添加到根目录下的.env文件中，它包含如下内容：

```rust
DATABASE_URL=postgres://postgres:postgres@localhost/linksnap
```

在postgres中的数据库名称是linksnap，用户名和密码都是postgres。这绝不是访问数据库的安全方式，建议你采用最佳安全实践在生产环境中设置postgres数据库。

我们还需要在Cargo.toml文件中添加diesel作为依赖项，以及添加dotenv软件包。dotenv软件包通过dotfiles处理本地配置。以下是我们的Cargo.toml文件：

```rust
# linksnap_v2/Cargo.toml
[dependencies]
actix = "0.7"
actix-web = "0.7"
futures = "0.1"
env_logger = "0.5"
bytes = "0.4"
serde = "1.0.80"
serde_json = "1.0.33"
serde_derive = "1.0.80"
url = "1.7.2"
lazy_static = "1.2.0"
log = "0.4.6"
chrono = { version="0.4" }
diesel = { version = "1.3.3", features = ["extras", "postgres", "r2d2"] }
dotenv = "0.13.0"
```

请留意，我们在diesel软件包上引用了"postgres"和"r2d2"特性。接下来，我们将运行diesel setup命令：

```rust
Creating migrations directory at: /home/creativcoder/book/Mastering-RUST-
Second-Edition/Chapter14/linksnap_v2/migrations
```

这将在根目录中创建一个diesel.toml文件，其中包含以下内容：

```rust
# linksnap_v2/diesel.toml
# 关于如何配置此文件的文档，请参阅
# see diesel.rs/guides/configuring-diesel-cli
[print_schema]
file = "src/schema.rs"
```

diesel采用了大量宏，以便为用户提供一些非常棒的特性，例如编译期的额外安全性和性能。为了能够做到这一点，它需要在编译期访问数据库，这就是.env 文件如此重要的原因。diesel setup命令通过读取数据库并将其写入名为schema.rs的文件来自动生成模型类型。模型通常可查询和插入结构体，两者都是用派生宏来为不同的用例生成模型代码。除此之外，基于 diesel 的应用程序需要代码连接到数据库和一组数据库迁移（migration）命令来构建和维护数据库表。

现在，让我们通过运行以下代码来添加一个创建数据表的迁移命令：

```rust
diesel migration generate linksnap
```

上述命令会生成一个新的迁移命令，其中包含两个空的迁移文件up.sql和down.sql：

```rust
Creating migrations/2019-01-30-045330_linksnap/up.sql
Creating migrations/2019-01-30-045330_linksnap/down.sql
```

迁移文件只是普通的SQL，因此可以向其中添加早期的CREATE TABLE命令：

```rust
-- linksnap_v2/migrations/2019-01-30-045330_linksnap_db/up.sql
CREATE TABLE linksnap (
  id SERIAL PRIMARY KEY,
  title VARCHAR NOT NULL,
  url TEXT NOT NULL,
  added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
```

down.sql文件中应包含相应的DROP TABLE：

```rust
-- linksnap_v2/migrations/2019-01-30-045330_linksnap_db/down.sql
DROP TABLE linksnap
```

完成上述操作后，我们必须运行如下命令：

```rust
$ diesel migration run
```

这将通过从数据库中读取信息来创建schema.rs文件：

```rust
// linksnap_v2/src/schema.rs
table! {
    linksnap (id) {
        id -> Int4,
        title -> Varchar,
        url -> Text,
        added -> Timestamp,
    }
}
```

table!宏为linksnap表生成代码，id为主键。它还指定了id、title、url及added等列名。

现在我们可以为这个数据表编写一个模型。在 diesel 中，模型可以存在于任何可见的模块中，但我们会遵循将它们放入src/models.rs中的惯例。这是我们Link模型中的内容：

```rust
// linksnap_v2/src/models.rs
use chrono::prelude::*;
use diesel::prelude::Queryable;
use chrono::NaiveDateTime;
use diesel;
use diesel::pg::PgConnection;
use diesel::prelude::*;
use crate::state::AddLink;
use crate::schema::linksnap;
use crate::schema::linksnap::dsl::{linksnap as get_links};
use serde_derive::{Serialize, Deserialize};
pub type LinkId = i32;
#[derive(Queryable, Debug)]
pub struct Link {
    pub id: i32,
    pub title: String,
    pub url: String,
    pub added: NaiveDateTime,
}
impl Link {
    pub fn add_link(new_link: AddLink, conn: &PgConnection) ->
QueryResult<usize> {
        diesel::insert_into(linksnap::table)
            .values(&new_link)
            .execute(conn)
    }
    pub fn get_links(conn: &PgConnection) -> QueryResult<Vec<Link>> {
        get_links.order(linksnap::id.desc()).load::<Link>(conn)
    }
    pub fn rm_link(id: LinkId, conn: &PgConnection) -> QueryResult<usize> {
        diesel::delete(get_links.find(id)).execute(conn)
    }
}
```

我们创建了一个可用于查询数据库的 Link 结构体。当服务器在各个端点上接收请求时，它还具有各种方法。

接下来，state.rs还包含diesel和postgres的特定代码：

```rust
// linksnap_v2/src/state.rs
use diesel::pg::PgConnection;
use actix::Addr;
use actix::SyncArbiter;
use std::env;
use diesel::r2d2::{ConnectionManager, Pool, PoolError, PooledConnection};
use actix::{Handler, Message};
use crate::models::Link;
use serde_derive::{Serialize, Deserialize};
use crate::schema::linksnap;
use std::ops::Deref;
const DB_THREADS: usize = 3;
use actix_web::{error, Error};
use actix::Actor;
use actix::SyncContext;
// 通过它创建连接池
pub type PgPool = Pool<ConnectionManager<PgConnection>>;
type PgPooledConnection =
PooledConnection<ConnectionManager<PgConnection>>;
pub struct Db(pub PgPool);
// 我们定义了一个简便方法来获取连接
impl Db {
    pub fn get_conn(&self) -> Result<PgPooledConnection, Error> {
        self.0.get().map_err(|e| error::ErrorInternalServerError(e))
    }
}
```

首先，我们为PostgreSQL连接池创建了一系列方便的别名，还有包装了PgPool类型的相同Db结构体。PgPool类型是diesel中r2d2模块的ConnectionManager。在Db结构体中，我们还定义了get_conn方法，该方法返回对池化连接的引用。

接下来继续关注同一文件：

```rust
// 然后我们在actor上实现Actor特征
impl Actor for Db {
    type Context = SyncContext<Self>;
}
pub fn init_pool(database_url: &str) -> Result<PgPool, PoolError> {
    let manager = ConnectionManager::<PgConnection>::new(database_url);
    Pool::builder().build(manager)
}
// 该类型简单地包装一个Addr
#[derive(Clone)]
pub struct State {
    pub inner: Addr<Db>
}
impl State {
    // 初始化方法init
    pub fn init() -> State {
        let database_url = env::var("DATABASE_URL").expect("DATABASE_URL
must be set");
        let pool = init_pool(&database_url).expect("Failed to create
pool");
        let addr = SyncArbiter::start(DB_THREADS, move ||
Db(pool.clone()));
        let state = State {
            inner: addr.clone()
        };
        state
    }
    pub fn get(&self) -> &Addr<Db> {
        &self.inner
    }
}
```

我们对于State类型已经很熟悉了，但init方法在这里有所不同。它首先构造了对环境变量DATABASE_URL的访问，并尝试使用线程池中的database_url进行池化连接。然后我们启动了一个SyncArbiter线程来复制线程池。最后我们将状态实例返回给调用者。

除此之外，我们不会改变linksanp代码库以前版本的大部分内容。让我们来看看构造的新服务器。我们将使用curl将一个链接插入我们的服务器：

```rust
curl --header "Content-Type: application/json" \
 --request POST \
 --data '{"title":"rust webpage","url":"https://rust-lang.org"}' \
 127.0.0.1:8080/add
```

为了确认此链接已经发送到我们的postgres数据库，让我们在psql提示符中查询此条目：

![169.png](../images/169.png)
由上述结果可知，我们的curl请求进入了postgres数据库。

diesel的学习门槛虽然有点高，但随着越来越多的示例和文档的出现，这种情况应该会有所改变。

