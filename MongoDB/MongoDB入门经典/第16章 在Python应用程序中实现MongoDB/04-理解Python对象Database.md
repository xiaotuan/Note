### 16.1.2　理解Python对象Database

Python对象Database提供了身份验证、用户账户管理以及访问和操作集合的功能。与MongoClient对象相关联的数据库存储在MongoClient对象的一个内部字典中。要获取Database对象实例，最简单的方式是直接使用MongoClient对象和数据库名，例如，下面的代码获取一个与数据库words相关联的Database对象：

```go
mongo = MongoClient("")
db = mongo["words"]
```

创建Database对象实例后，就可使用它来访问数据库了。表16.2列出了Database对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表16.2　　Python对象Database的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| add_user(name, password, [read_only]) | 在当前数据库中添加一个名称和密码为指定值的用户账户。如果read_only为True，该用户将只能读取数据库 |
| authenticate(username, password) | 使用用户凭证向数据库验证身份 |
| create_collection(name, options) | 在服务器上创建一个集合。参数options是一个Dictionary对象，指定了集合创建选项 |
| drop_collection(name) | 删除指定集合 |
| collection_names() | 返回一个数组，其中包含当前数据库中所有的集合 |
| read_preference | 与前一小节介绍的MongoClient的同名属性相同 |
| write_concern | 与前一小节介绍的MongoClient的同名属性相同 |

