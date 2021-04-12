### 19.1.4　理解Node.js对象Collection

Node.js对象Collection提供了访问和操作集合中文档的功能。与Database对象相关联的集合存储在Database对象的内部字典中。

要获取Collection对象实例，最简单的方式是使用Database对象的方法collection()。例如，下面的实例获取一个Collection对象，它表示数据库words中的集合word_stats。注意到将这个Collection对象作为第二个参数传递给了collection()的回调函数：

```go
var MongoClient = require('mongodb').MongoClient;
var Server = require('mongodb').Server;
var mongo = new MongoClient();
mongo.connect("mongodb://localhost/", function(err, db) {
   var myDB = db.db("words");
   myDB.collection("word_stats", function(err, collection){
...
   });
});
```

创建Collection对象实例后，就可使用它来访问集合了。表19.3列出了Collection对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表19.3　　Node.js对象Collection的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| aggregate(pipeline) | 应用聚合选项流水线。参数pipeline是一个JavaScript对象数组，这些对象表示流水线中的聚合操作。结果将作为第二个参数传递给回调函数 |
| count([query], [options], callback) | 返回集合中与指定查询匹配的文档数。参数query是一个描述查询的JavaScript对象。参数options让您能够设置计数操作使用的skip值和limit值。计数结果将作为第二个参数传递给回调函数 |
| distinct(key, callback) | 返回一个数组，其中包含指定字段的不同值。这个数组作为第二个参数传递给回调函数 |
| drop(callback) | 删除集合 |
| find([query], [options], callback) | 返回一个表示集合中文档的Cursor对象。可选参数query是一个JavaScript对象，让您能够限制要包含的文档；可选参数options也是一个JavaScript对象，让您能够指定find()操作的其他选项，如fields、sort、limit和skip。生成的Cursor对象将作为第二个参数传递给回调函数。另外，方法find()也返回一个可供您使用的Cursor对象。 |
| findAndModify(query, sort, update, [options], callback) | 以原子方式查找并更新集合中的文档，并返回修改后的文档。参数query是一个JavaScript对象，指定要更新哪些文档；参数sort指定排序方式；参数update是一个JavaScript对象，指定要使用的更新运算符；参数options也是一个JavaScript对象，与find()的同名参数相同 |
| findOne([query], [options], callback) | 返回一个JavaScript对象，表示集合中的一个文档。可选参数options是一个JavaScript对象，与find()的同名参数相同。返回的文档将作为第二个参数传递给回调函数 |
| group(keys, condition, initial, reduce, [finalize], callback) | 对集合执行分组操作（参见第9章）。分组结果将作为第二个参数传递给回调函数 |
| insert(documents, [options], callback) | 在集合中插入一个或多个文档。参数options让您能够设置写入关注和其他写入选项。插入的新文档将作为第二个参数传递给回调函数 |
| remove([query], [options], callback) | 从集合中删除文档。参数options让您能够设置写入关注和其他写入选项。如果没有指定参数query，将删除所有文档；否则只删除与查询匹配的文档 |
| rename(newName, callback) | 重命名集合 |
| save(object, [options], callback) | 将对象保存到集合中。参数options让您能够设置写入关注和其他写入选项。如果指定的对象不存在，就插入它 |
| update(query, update, [options], callback) | 更新集合中的文档。参数query是一个JavaScript对象，指定了要更新哪些文档；参数update是一个JavaScript对象，指定了更新运算符；参数options是一个JavaScript对象，指定了写入关注和其他更新选项，如upsert（是否执行upsert操作）和multi（是否更新多个文档） |

