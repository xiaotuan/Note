### 13.1.1　理解PHP对象MongoClient

PHP对象MongoClient提供了连接到MongoDB服务器和访问数据库的功能。要在PHP应用程序中实现MongoDB，首先需要创建一个MongoClient对象实例，然后就可使用它来访问数据库，设置写入关注以及执行其他操作（如表13.1所示）。

要创建MongoClient对象实例，需要使用合适的选项调用new MongoClient()。最基本的方式是连接到本地主机的默认端口：

```go
$mongo = new MongoClient("");
```

您还可以使用如下格式的连接字符串：

```go
mongodb://username:password@host:port/database?options
```

例如，要使用用户名test和密码myPass连接到主机1.1.1.1的端口8888上的数据库words，可使用如下代码：

```go
$mongo = new MongoClient("mongodb://test:myPass@1.1.1.1:8888/words");
```

创建MongoClient对象实例后，就可使用表13.1所示的方法来访问数据库和设置选项。

<center class="my_markdown"><b class="my_markdown">表13.1　　PHP对象MongoClient的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| close() | 关闭连接 |
| connect() | 重新打开已关闭的连接 |
| getConnections() | 返回一个数组，其中包含所有已打开的连接 |
| listDBs() | 返回一个数组，其中包含服务器中所有的数据库 |
| selectDB(dbName) | 返回一个与指定数据库相关联的MongoDB对象 |
| selectCollection(dbName, collName) | 返回一个MongoCollection对象，它与指定数据库中的指定集合相关联 |
| setReadPreference(preference) | 将客户端的读取首选项设置为下列值之一： MongoClient::RP_PRIMARY MongoClient::RP_PRIMARY_SECONDARY MongoClient::RP_SECONDARY MongoClient::RP_SECONDARY_SECONDARY MongoClient::RP_NEAREST |

