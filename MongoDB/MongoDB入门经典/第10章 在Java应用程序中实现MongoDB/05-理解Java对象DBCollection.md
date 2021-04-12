### 10.1.3　理解Java对象DBCollection

Java对象DBCollection提供了访问和操作集合中文档的功能。要获取DBCollection对象实例，最简单的方式是使用DB对象的方法getCollection()。

下面的实例使用DB对象获取一个DBCollection对象实例：

```go
import com.mongodb.MongoClient;
import com.mongodb.DB;
import com.mongodb.DBCollection;
MongoClient mongoClient = new MongoClient("localhost", 27017);
DB db = mongoClient.getDB("myDB");
DBCollection collection = db.getCollection("myCollection");
```

创建DBCollection对象实例后，就可使用它来访问集合了。表10.3列出了DBCollection对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表10.3　　Java对象DBCollection的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| aggregate(pipeline) | 应用聚合选项流水线。流水线中的每个选项都是一个表示聚合操作的BasicDBObject。BasicDBObject将在本章后面讨论，而聚合操作在第9章讨论过 |
| count() | 返回集合中的文档数 |
| count(query) | 返回集合中与指定查询匹配的文档数。参数query是一个描述查询运算符的BasicDBObject |
| distinct(key, [query]) | 返回指定字段的不同值列表。可选参数query让您能够限制要考虑哪些文档 |
| drop() | 删除集合 |
| dropIndex(keys) | 删除keys指定的索引 |
| ensureIndex(keys, [options]) | 添加keys和可选参数options描述的索引，这两个参数的类型都是DBObject |
| find([query], [fields]) | 返回一个表示集合中文档的DBCursor对象。可选参数query是一个BasicDBObject对象，让您能够限制要包含的文档；可选参数fields也是一个BasicDBObject对象，让您能够指定要返回文档中的哪些字段 |
| findAndModify(query, [sort], update) | 以原子方式查找并更新集合中的文档，并返回修改后的文档 |
| findOne([query], [fields], [sort]) | 返回一个DBObject对象，表示集合中的一个文档。可选参数query是一个BasicDBObject对象，让您能够限制要包含的文档；可选参数fields是一个BasicDBObject对象，让您能够指定要返回文档中的哪些字段；可选参数sort也是一个BasicDBObject对象，让您能够指定文档的排列顺序 |
| getStats() | 返回一个CommandResult对象，其中包含当前集合的信息 |
| group(key, cond, initial, reduce, [finalize]) | 对集合执行分组操作（参见第9章） |
| insert(object, [concern]) | 在集合中插入一个对象 |
| insert(objects, [concern]) | 将一个对象数组插入到集合中 |
| mapReduce(map, reduce, output, query) | 对集合执行映射-归并操作（参见第9章） |
| remove([query], [concern])) | 从集合中删除文档。如果没有指定参数query，将删除所有文档；否则只删除与查询匹配的文档 |
| rename(newName) | 重命名集合 |
| save(dbObject, [concern]) | 将对象保存到集合中。如果指定的对象不存在，就插入它 |
| setReadPreference(preference) | 与前面介绍的MongoClient的同名方法相同 |
| setWriteConcern(concern) | 与前面介绍的MongoClient的同名方法相同 |
| update(query, update, [upsert], [multi]) | 更新集合中的文档。参数query是一个BasicDBObject对象，指定了要更新哪些文档；参数update是一个BasicDBObject对象，指定了更新运算符；布尔参数upsert指定是否执行upsert；布尔参数multi指定更新多个文档还是只更新第一个文档 |

