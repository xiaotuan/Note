### 19.1.2　理解Node.js对象MongoClient

Node.js对象MongoClient提供了连接到MongoDB服务器和访问数据库的功能。要在Node.js应用程序中实现MongoDB，首先需要创建一个MongoClient对象实例，然后就可使用它来访问数据库，设置写入关注以及执行其他操作（如表19.1所示）。

要创建MongoClient对象实例，需要调用new MongoClient()，并将一个使用主机和端口创建的Server对象作为参数。要打开连接，需要调用方法open()，这个方法将MongoClient作为第二个参数传递给回调函数。例如，下面的代码连接到本地主机的默认端口：

```go
mongo = new MongoClient(new Server("localhost", 27017));
mongo.open(function(err, mongoClient){
   var db = mongoClient.db("myDB");
   ...
});
```

您也可以调用MongoClient类的方法connect()，并传入一个连接字符串。这个方法将Database对象作为第二个参数传递给回调函数。连接字符串的格式如下：

```go
mongodb://username:password@host:port/database?options
```

例如，要使用用户名test和密码myPass连接到主机1.1.1.1的端口8888上的数据库words，可使用如下代码：

```go
MongoClient.connect("mongodb://test:myPass@1.1.1.1:8888/words", function(err, db){
. . .
});
```

创建MongoClient对象实例后，就可使用表19.1所示的方法来访问数据库和设置选项。

<center class="my_markdown"><b class="my_markdown">表19.1　　Node.js对象MongoClient的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| close() | 关闭连接 |
| connect(string, callback) | 根据指定的连接字符串打开连接。连接打开后，将执行指定的回调函数 |
| open(callback) | 根据创建MongoClient对象时使用的Server对象的设置来打开连接。连接打开后，将调用指定的回调函数 |
| db(name) | 返回一个Database对象 |

