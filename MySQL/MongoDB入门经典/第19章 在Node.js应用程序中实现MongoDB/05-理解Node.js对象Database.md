### 19.1.3　理解Node.js对象Database

Node.js对象Database提供了身份验证、用户账户管理以及访问和操作集合的功能。与MongoClient对象相关联的数据库存储在MongoClient对象的内部字典中。

要获取Database对象实例，最简单的方式是调用MongoClient对象的方法connect()，并传入一个连接字符串。例如，下面的代码获取一个表示数据库words的Database对象；注意到将这个Database对象作为第二个参数传递给了connect()的回调函数：

```go
var mongo = new MongoClient();
mongo.connect("mongodb://test:myPass@1.1.1.1:8888/words", function(err, db){
. . .
});
```

创建Data base对象实例后，就可使用它来访问数据库了。表19.2列出了Database对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表19.2　　Node.js对象Database的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| addUser(name, password, callback) | 在当前数据库中添加一个用户账户，其用户名和密码由name和password指定 |
| authenticate(username, password, callback) | 使用用户凭证向数据库验证身份 |
| createCollection(name, [options], callback) | 在服务器上创建一个集合。参数options是一个JavaScript，指定了集合创建选项 |
| dropCollection(name, callback) | 删除指定的集合 |
| collections(callback) | 将一个数组作为第二个参数传递给回调函数，其中包含当前数据库中所有的集合 |
| removeUser(username) | 从数据库删除用户账户 |

