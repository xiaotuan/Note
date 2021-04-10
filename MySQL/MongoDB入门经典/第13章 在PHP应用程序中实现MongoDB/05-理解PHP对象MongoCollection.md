### 13.1.3　理解PHP对象MongoCollection

PHP对象MongoCollection提供了访问和操作集合中文档的功能。要获取MongoCollection对象实例，最简单的方式是直接使用MongoDB对象和集合名。例如，下面的代码获取一个MongoCollection对象，它与数据库words中的集合word_stats相关联：

```go
$mongo = new MongoClient("");
$db = $mongo->words;
$collection = $db->word_stats;
```

您还可以调用MongoDB对象的方法selectCollection()来获取MongoCollection对象，这在集合名不适合使用PHP语法->时很有用，如下所示：

```go
$mongo = new MongoClient("");
$db = $mongo->selectDB("words");
$collection = $db->selectCollection("word_stats");
```

创建MongoCollection对象实例后，就可使用它来访问集合了。表13.3列出了MongoCollection对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表13.3　　PHP对象MongoCollection的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| aggregate(pipeline) | 应用聚合选项流水线。流水线中的每个选项都是一个表示聚合操作的Array对象。Array对象将在本章后面讨论，而聚合操作在第9章讨论过 |
| batchInsert(docs, [options])) | 在数据库中插入一个文档数组，其中参数options是一个Array对象，指定了写入关注和其他更新选项 |
| count([query]) | 返回集合中与指定查询匹配的文档数。参数query是一个描述查询的Array对象 |
| distinct(key, [query]) | 返回一个数组，其中包含指定字段的不同值。可选参数query是一个Array对象，让您能够限制要考虑哪些文档 |
| drop() | 删除集合 |
| dropIndex(keys) | 删除keys指定的索引 |
| ensureIndex(keys, [options]) | 添加keys和可选参数options描述的索引，这两个参数都是Array对象 |
| find([query], [fields]) | 返回一个表示集合中文档的MongoCursor对象。可选参数query是一个Array对象，让您能够限制要包含的文档；可选参数fields也是一个Array对象，让您能够指定要返回文档中的哪些字段 |
| findAndModify(query, update, fields, options) | 以原子方式查找并更新集合中的文档，并返回修改后的文档。参数query是一个Array对象，指定要更新哪些文档；参数update是一个Array对象，指定要使用的更新运算符；参数fields是一个Array对象，指定要返回更新后的文档中的哪些字段；参数options也是一个Array对象，指定写入关注和其他更新选项 |
| findOne([query], [fields]) | 返回一个Array对象，表示集合中的一个文档。可选参数query是一个Array对象，让您能够限制要包含的文档；可选参数fields也是一个Array对象，让您能够指定要返回文档中的哪些字段 |
| group(key, initial, reduce, [options]) | 对集合执行分组操作（参见第9章） |
| insert(object, [options]) | 在集合中插入一个对象，其中参数options是一个Array对象，指定了写入关注和其他更新选项 |
| remove([query], [options])) | 从集合中删除文档。如果没有指定参数query，将删除所有文档；否则只删除与查询匹配的文档。参数options是一个Array对象，指定了写入关注和其他更新选项 |
| save(object, [options]) | 将对象保存到集合中。如果指定的对象不存在，就插入它。参数options是一个Array对象，指定了写入关注和其他更新选项 |
| setReadPreference(preference) | 与前面介绍的MongoClient的同名方法相同 |
| update(query, update, [options]) | 更新集合中的文档。参数query是一个Array对象，指定了要更新哪些文档；参数update是一个Array对象，指定了更新运算符；参数options是一个Array对象，指定了写入关注和其他更新选项（如upsert和multiple） |

