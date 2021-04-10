### 10.1.4　理解Java对象DBCursor

Java对象DBCursor表示MongoDB服务器中的一组文档。使用查找操作查询集合时，通常返回一个DBCursor对象，而不是向Java应用程序返回全部文档对象，这让您能够在Java中以受控的方式访问文档。

DBCursor对象以分批的方式从服务器取回文档，并使用一个索引来迭代文档。在迭代期间，当索引到达当前那批文档末尾时，将从服务器取回下批文档。

下面的示例使用查找操作获取一个DBCursor对象实例：

```go
import com.mongodb.MongoClient;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
MongoClient mongoClient = new MongoClient("localhost", 27017);
DB db = mongoClient.getDB("myDB");
DBCollection collection = db.getCollection("myCollection");
DBCursor cursor = collection.find();
```

创建DBCursor对象实例后，就可使用它来访问集合中的文档了。表10.4列出了DBCursor对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表10.4　　Java对象DBCursor的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| batchSize(size) | 指定每当读取到当前已下载的最后一个文档时，游标都将再返回多少个文档 |
| close() | 关闭游标并释放它占用的服务器资源 |
| copy() | 返回游标的拷贝 |
| count() | 返回游标表示的文档数 |
| hasNext() | 如果游标中还有其他可供迭代的对象，就返回true |
| iterator() | 为游标创建一个迭代器对象 |
| limit(size) | 指定游标可最多表示多少个文档 |
| next() | 将游标中的下一个文档作为DBObject返回，并将索引加1 |
| size() | 计算与查询匹配的文档数，且不考虑limit()和skip()的影响 |
| skip(size) | 在返回文档前，跳过指定数量的文档 |
| sort(sort) | 按DBObject参数sort指定的方式对游标中的文档排序 |
| toArray([max]) | 从服务器检索所有的文档，并以列表的方式返回。如果指定了参数max，则只检索指定数量的文档 |

