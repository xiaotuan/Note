### 5.1.2　理解Database对象

MongoDB shell中的Database对象让您能够访问数据库。它表示一个数据库，让您能够执行诸如添加用户和访问集合等操作。您经常使用Database对象来访问MongoDB数据库。

要在MongoDB shell中创建Database对象，可使用两种方式之一。最简单的方法是，启动MongoDB shell，再使用下面的命令连接到<database>指定的数据库：

```go
use <database>
```

在MongoDB shell中，这个命令连接到指定的数据库并修改变量db；这样您就可使用变量db来访问数据库功能了。例如，下面的命令连接到数据库myDB并显示其名称：

```go
use myDB
db.getName()
```

您还可以使用Connection对象的方法getDB()来创建一个Database对象，例如，下面的JavaScript代码连接到数据库myDB，并使用创建的Database对象来显示数据库的名称：

```go
myConn = new Mongo("localhost");
myDB = myConn.getDB("myDB");
myDB.getName();
```

表5.2列出了Database对象的一些常用方法，有些您在本书前面见过，其他的您将在本书后面经常见到。

<center class="my_markdown"><b class="my_markdown">表5.2　　Database对象的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| addUser(document) | 根据指定的用户配置文档在数据库中添加一个用户（参见第4章） |
| auth(username, password) | 向数据库验证用户的身份 |
| changeUserPassword( username, password) | 修改既有用户的密码 |
| cloneCollection(fromHost, collection, query) | 从MongoDB服务器fromHost复制指定的集合到当前数据库中。可选参数query指定了一个查询，该查询决定了要克隆集合中的哪些文档 |
| cloneDatabase(host) | 从远程主机复制一个数据库到当前主机 |
| commandHelp(command) | 返回数据库命令的帮助信息 |
| copyDatabase(srcDatabase, destDatabase, host) | 将远程主机中的数据库srcDatabase复制到当前主机，并重命名为destDatabase |
| createCollection(name, options) | 新建一个集合。参数options让您能够指定集合选项，如创建固定集合时 |
| dropDatabase() | 删除当前数据库 |
| eval(function, arguments) | 向MongoDB服务器发送一个JavaScript函数（由第一个参数指定），并在服务器处执行；传递给这个函数的参数由后续参数指定。这让您能够在服务器上执行代码，避免将大量的数据传输到MongoDB shell |
| getCollection(collection) | 返回一个表示指定集合的Collection对象，这在集合无法使用MongoDB shell语法访问（如集合名包含空格）时很有用 |
| getCollectionNames() | 列出当前数据库中所有的集合 |
| getMongo() | 返回表示当前连接的Connection对象 |
| getName() | 返回当前数据库的名称 |
| getSiblingDB(database) | 返回一个Database对象，它表示当前服务器中的另一个数据库 |
| help() | 显示Database对象的常用方法的描述 |
| hostInfo() | 返回一个文档，其中包含运行MongoDB的系统的信息 |
| logout() | 结束到当前数据库的经过身份验证的会话 |
| removeUser(username) | 将用户从数据库中删除 |
| repairDatabase() | 对当前数据库执行修复例程 |
| runCommand(command) | 运行数据库命令。这是执行数据库命令的首选方法，因为它为MongoDB shell和驱动程序提供了一致的接口 |
| serverStatus() | 返回一个文档，其中包含有关数据库进程状态的摘要信息 |
| shutdownServer() | 干净而安全地关闭当前mongod或mongos进程 |
| version() | 返回mongod实例的版本 |

