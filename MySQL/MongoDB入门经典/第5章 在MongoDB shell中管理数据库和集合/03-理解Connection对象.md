### 5.1.1　理解Connection对象

MongoDB shell中的Connection对象让您能够访问MongoDB服务器，它表示到服务器的连接，让您能够获取Database对象并设置读取首选项。

要创建连接到MongoDB服务器的Connection对象，可使用如下命令：

```go
Mongo(host:port)
```

例如，要连接到本地主机的MongoDB服务器，并创建一个Connection对象，可使用下面的代码行：

```go
var myConn = new Mongo("localhost");
```

表5.1列出了可对Connection对象调用的方法。

<center class="my_markdown"><b class="my_markdown">表5.1　　Connection对象的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| new Mongo(host:port) | 连接到指定位置的MongoDB实例，并返回一个Connection对象实例 |
| getDB(database) | 返回一个Database对象，它表示参数database指定的数据库 |
| setReadPrefMode(mode, tagSet) | 设置副本集读取首选模式。参数mode可以是primary、primaryPreferred、secondary、secondaryPreferred或nearest；参数tagSet是一个副本集标记集（tag set）数组（请参见第22章） |
| getReadPrefMode() | 返回MongoDB副本集的当前读取首选模式 |
| getReadPrefTagSet() | 返回MongoDB副本集的当前读取首选标记集 |
| setSlaveOk() | 允许从副本集的备份（secondary）成员读取 |

