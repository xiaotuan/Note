### 13.1.2　理解PHP对象MongoDB

PHP对象MongoDB提供了身份验证、用户账户管理以及访问和操作集合的功能。要获取MongoDB对象实例，最简单的方式是直接使用MongoClient对象和数据库名，例如，下面的代码获取一个与数据库words相关联的MongoDB对象：

```go
$mongo = new MongoClient("");
$db = $mongo->words;
```

您还可以调用MongoClient对象的方法selectDB()来获取MongoDB对象，这在数据库名称不适合使用PHP语法->时很有用，如下所示：

```go
$mongo = new MongoClient("");
$db = $mongo->selectDB("words");
```

创建MongoDB对象实例后，就可使用它来访问数据库了。表13.2列出了MongoDB对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表13.2　　PHP对象MongoDB的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| authenticate(username, password) | 使用用户凭证向数据库验证身份 |
| createCollection(name, options) | 在服务器上创建一个集合。参数options是一个Array对象，指定了集合创建选项 |
| drop() | 删除当前数据库 |
| listCollections() | 返回一个数组，其中包含当前数据库中所有的集合 |
| selectCollection(name) | 返回一个与name指定的集合相关联的MongoCollection对象 |
| setReadPreference(prefer ence) | 与前一小节介绍的MongoClient的同名方法相同 |

