### 10.1.1　理解Java对象MongoClient

Java对象MongoClient提供了连接到MongoDB服务器和访问数据库的功能。要在Java应用程序中实现MongoDB，首先需要创建一个MongoClient对象实例，然后就可使用它来访问数据库、设置写入关注以及执行其他操作（如表10.1所示）。

要创建MongoClient对象实例，需要从驱动程序中导入它，再使用合适的选项调用new MongoClient()，如下所示：

```go
import com.mongodb.MongoClient;
MongoClient mongoClient = new MongoClient("localhost", 27017);
```

MongoClient的构造函数可接受多种不同形式的参数，下面是其中的一些。

+ MongoClient()：创建一个客户端实例，并连接到本地主机的默认端口。
+ MongoClient(String host)：创建一个客户端实例，并连接到指定主机的默认端口。
+ MongoClient(String host, int port)：创建一个客户端实例，并连接到指定主机的指定端口。
+ MongoClient(MongoClientURI uri)：创建一个客户端实例，并连接到连接字符串uri指定的服务器。uri使用如下格式：

```go
mongodb://username:password@host:port/database?options
```

创建MongoClient对象实例后，就可使用表10.1所示的方法来访问数据库和设置选项。

<center class="my_markdown"><b class="my_markdown">表10.1　　Java对象MongoClient的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| close() | 关闭连接 |
| connect(address) | 连接到另一个数据库，该数据库由一个DBAddress对象指定，如connect(new DBAddress(host, port, dbname)) |
| dropDatabase(dbName) | 删除指定的数据库 |
| getDatabaseNames() | 返回数据库名称列表 |
| getDB(dbName) | 返回一个与指定数据库相关联的DB对象 |
| setReadPreference(preference) | 将客户端的读取首选项设置为下列值之一： ReadPreference.primary() ReadPreference.primaryPreferred() ReadPreference.secondary() ReadPreference.secondaryPreferred() ReadPreference.nearest() |
| setWriteConcern concern) | 设置客户端的写入关注，可能取值如下： WriteConcern.SAFE WriteConcern.JOURNALED WriteConcern.JOURNAL_SAFE WriteConcern.NONE WriteConcern.MAJORITY |

