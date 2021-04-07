### 9.2.1　用于写入MySQL的管道

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 在本节，我们将会向MySQL数据库中插入房产信息。如果你想擦除它们，可以使用如下命令：

MySQL是一个非常强大且流行的数据库。我们将编写一个管道，将item写入到其中。我们已经在虚拟环境中运行了一个MySQL实例。现在只需使用MySQL命令行工具执行一些基本管理即可，同样该工具也已经在开发机中预安装好了，下面执行如下操作打开MySQL控制台。

```python
$ mysql -h mysql -uroot -ppass

```

```python
mysql> DELETE FROM properties;

```

这将会得到MySQL的提示符，即 `mysq>` ，现在可以创建一个简单的数据库表，其中包含一些字段，如下所示。

```python
mysql> create database properties;
mysql> use properties
mysql> CREATE TABLE properties (
　url varchar(100) NOT NULL,
　title varchar(30),
　price DOUBLE,
　description varchar(30),
　PRIMARY KEY (url)
);
mysql> SELECT * FROM properties LIMIT 10;
Empty set (0.00 sec)

```

非常好，现在拥有了一个MySQL数据库，以及一张名为 `properties` 的表，其中包含了一些字段，此时可以准备创建管道了。请保持MySQL的控制台为开启状态，因为之后还会回来检查是否正确插入了值。如果想退出控制台，只需要输入 `exit` 即可。

我们将使用Python的MySQL客户端。我们还将安装一个名为 `dj-database-url` 的小工具模块，帮助我们解析连接的URL（仅用于为我们在IP、端口、密码等不同设置中切换节省时间）。可以使用 `pip install dj-database-url MySQL-python` 安装这两个库，不过我们已经在开发环境中安装好它们了。我们的MySQL管道非常简单，如下所示。

```python
from twisted.enterprise import adbapi
...
class MysqlWriter(object):
　　...
　　def __init__(self, mysql_url):
　　　　conn_kwargs = MysqlWriter.parse_mysql_url(mysql_url)
　　　　self.dbpool = adbapi.ConnectionPool('MySQLdb',
　　　　　　　　　　　　　　　　　　　　　　charset='utf8',
　　　　　　　　　　　　　　　　　　　　　　use_unicode=True,
　　　　　　　　　　　　　　　　　　　　　　connect_timeout=5,
　　　　　　　　　　　　　　　　　　　　　　**conn_kwargs)
　　def close_spider(self, spider):
　　　　self.dbpool.close()
　　@defer.inlineCallbacks
　　def process_item(self, item, spider):
　　　　try:
　　　　　　yield self.dbpool.runInteraction(self.do_replace, item)
　　　　except:
　　　　　　print traceback.format_exc()
　　　　defer.returnValue(item)
　　@staticmethod
　　def do_replace(tx, item):
　　　　sql = """REPLACE INTO properties (url, title, price,
　　　　description) VALUES (%s,%s,%s,%s)"""
　　　　args = (
　　　　　　item["url"][0][:100],
　　　　　　item["title"][0][:30],
　　　　　　item["price"][0],
　　　　　　item["description"][0].replace("\r\n", " ")[:30]
　　　　)
　　　　tx.execute(sql, args)
```

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 本示例的完整代码地址为 `ch09/properties/properties/pipeline/mysql.py` 。

本质上，大部分代码仍然是模板化的爬虫代码。我们省略的代码用于将 `MYSQL_PIPELINE_URL` 设置中包含的 `mysql://user:pass@ip/database` 格式的URL解析为独立参数。在爬虫的 `__init__()` 中，我们将这些参数传给 `adbapi.ConnectionPool()` ，使用 `adbapi` 的基础功能初始化MySQL连接池。第一个参数是想要导入的模块名称。在该MySQL示例中，为 `MySQLdb` 。我们还为MySQL客户端设置了一些额外的参数，用于处理Unicode和超时。所有这些参数会在每次 `adbapi` 需要打开新连接时，前往底层的 `MySQLdb.connect()` 函数。当爬虫关闭时，我们为该连接池调用 `close()` 方法。

我们的 `process_item()` 方法实际上包装了 `dbpool.runInteraction()` 。该方法将稍后调用的回调方法放入队列，当来自连接池的某个连接的 `Transaction` 对象变为可用时，调用该回调方法。 `Transaction` 对象的API与DB-API游标相似。在本例中，回调方法为 `do_replace()` ，该方法在后面几行进行了定义。 `@staticmethod` 意味着该方法指向的是类，而不是具体的类实例，因此，可以省略平时使用的 `self` 参数。当不使用任何成员时，将方法静态化是个好习惯，不过即使忘记这么做，也没有问题。该方法准备了一个SQL字符串和几个参数，调用 `Transaction` 的 `execute()` 方法执行插入。我们的SQL语句使用了 `REPLACE INTO` 来替换已经存在的条目，而不是更常见的 `INSERT INTO` ，原因是如果条目已经存在，可以使用相同的主键。在本例中这种方式非常便捷。如果想使用SQL返回数据，如 `SELECT` 语句，可以使用 `dbpool.runQuery()` 。如果想要修改默认游标，可以通过设置 `adbapi.ConnectionPool()` 的 `cursorclass` 参数来实现，比如设置 `cursorclass=MySQLdb.cursors.DictCursor` ，可以让数据获取更加便捷。

要想使用该管道，需要在 `settings.py` 文件的 `ITEM_PIPELINES` 字典中添加它，另外还需要设置 `MYSQL_PIPELINE_URL` 属性。

```python
ITEM_PIPELINES = { ...
　　'properties.pipelines.mysql.MysqlWriter': 700,
...
MYSQL_PIPELINE_URL = 'mysql://root:pass@mysql/properties'
```

执行如下命令。

```python
scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=1000

```

该命令运行后，可以回到MySQL提示符下，按如下方式查看数据库中的记录。

```python
mysql> SELECT COUNT(*) FROM properties;
+----------+
| 1006 |
+----------+
mysql> SELECT * FROM properties LIMIT 4;
+------------------+--------------------------+--------+-----------+
| url　　　　　　　| title　　　　　　　　　　| price　| description
+------------------+--------------------------+--------+-----------+
| http://...0.html | Set Unique Family Well　 | 334.39 | website c
| http://...1.html | Belsize Marylebone Shopp | 388.03 | features
| http://...2.html | Bathroom Fully Jubilee S | 365.85 | vibrant own
| http://...3.html | Residential Brentford Ot | 238.71 | go court
+------------------+--------------------------+--------+-----------+
4 rows in set (0.00 sec)

```

延时和吞吐量等性能和之前保持相同，相当不错。

