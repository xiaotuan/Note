### 16.1.1　理解Python对象MongoClient

Python对象MongoClient提供了连接到MongoDB服务器和访问数据库的功能。要在Python应用程序中实现MongoDB，首先需要创建一个MongoClient对象实例，然后就可使用它来访问数据库，设置写入关注以及执行其他操作（如表16.1所示）。

要创建MongoClient对象实例，需要使用合适的选项调用new MongoClient()。最基本的方式是连接到本地主机的默认端口：

```go
mongo = new MongoClient("")
```

您还可以使用如下格式的连接字符串：

```go
mongodb://username:password@host:port/database?options
```

例如，要使用用户名test和密码myPass连接到主机1.1.1.1的端口8888上的数据库words，可使用如下代码：

```go
mongo = MongoClient("mongodb://test:myPass@1.1.1.1:8888/words")
```

创建MongoClient对象实例后，就可使用表16.1所示的方法来访问数据库和设置选项。

<center class="my_markdown"><b class="my_markdown">表16.1　　Python对象MongoClient的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| close() | 关闭连接 |
| database_names() | 返回一个数组，其中包含当前服务器中的所有数据库 |
| drop_database(name) | 删除指定的数据库 |
| read_preference | MongoClient对象的一个属性，指定了读取首选项，可设置为下列值之一： pymongo.read_preferences.ReadPreference.PRIMARY pymongo.read_preferences.ReadPreference.PRIMARY_SECONDARY pymongo.read_preferences.ReadPreference.SECONDARY pymongo.read_preferences.ReadPreference.SECONDARY_SECONDARY pymongo.read_preferences.ReadPreference.NEAREST |
| write_concern | MongoClient对象的一个属性，包含一个指定写入关注的字典 |

