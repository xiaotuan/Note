### 10.1.2　理解Java对象DB

Java对象DB提供了身份验证、用户账户管理以及访问和操作集合的功能。要获取DB对象实例，最简单的方式是调用MongoClient对象的方法getDB()。

下面的示例使用MongoClient获取一个DB对象示例：

```go
import com.mongodb.MongoClient;
import com.mongodb.DB;
MongoClient mongoClient = new MongoClient("localhost", 27017);
DB db = mongoClient.getDB("myDB");
```

创建DB对象实例后，就可使用它来访问数据库了。表10.2列出了DB对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表10.2　　Java对象DB的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| addUser(username, password) | 在当前数据库中添加一个具有读写权限的用户账户 |
| authenticate(username, password) | 使用用户凭证向数据库验证身份 |
| createCollection(name, options) | 在服务器上创建一个集合。参数options是一个BasicDBObject（将在后面介绍），指定了集合创建选项 |
| dropDatabase() | 删除当前数据库 |
| getCollection(name) | 返回一个与name指定的集合相关联的DBCollection对象 |
| getLastError() | 返回最后一次访问数据库导致的错误 |
| getLastError(w, wtimeout, fsync) | 设置数据库写入操作的写入关注、超时和fsync设置 |
| isAuthenticated() | 如果数据库连接是经过身份验证的，就返回true |
| removeUser(username) | 从数据库删除用户账户 |
| setReadPreference(prefer ence) | 与前一小节介绍的MongoClient的同名方法相同 |
| setWriteConcern(concern) | 与前一小节介绍的MongoClient的同名方法相同 |

