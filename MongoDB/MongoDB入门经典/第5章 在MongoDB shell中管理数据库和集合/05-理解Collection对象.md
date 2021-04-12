### 5.1.3　理解Collection对象

Collection对象表示MongoDB数据库中的集合，您可使用它来访问集合中的文档、添加文档、查询文档等。

访问集合的方式有两种。如果集合的名称是MongoDB shell JavaScript语法支持的，可使用句点表示法通过Database对象直接访问，例如，下面的代码显示集合myCollection的统计信息：

```go
db.myCollection.stats()
```

您还可使用Database对象的方法getCollection()来创建Collection对象实例，如下所示：

```go
myColl = db.getCollection("myCollection");
myColl.stats()
```

表5.3列出了Collection对象的基本方法。这些方法让您能够在集合中添加和修改文档、查找文档以及删除集合。

<center class="my_markdown"><b class="my_markdown">表5.3　　Collection对象的基本方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| aggregate() | 让您能够访问聚合流水线（参见第9章） |
| count() | 返回集合中的文档数或满足查询条件的文档数 |
| copyTo(newCollection) | 将当前集合中的文档复制到当前服务器中的另一个集合中 |
| createIndex() | 使用ensureIndex()为集合创建索引 |
| dataSize() | 返回集合的大小 |
| distinct(field, query) | 根据参数query指定的查询返回一个文档数组，这些文档包含指定字段的不同值 |
| drop() | 从数据库中删除指定的集合 |
| dropIndex(index) | 从集合中删除指定的索引 |
| dropIndexes() | 删除当前集合的所有索引 |
| ensureIndex(keys, options) | 创建一个索引——如果它不存在（参见第21章） |
| find(query, projection) | 对集合执行查询并返回一个Cursor对象（参见第6章） |
| findAndModify(document) | 以原子方式修改并返回一个文档（参见第8章） |
| findOne(query, projection) | 执行查询并返回一个文档（参见第6章） |
| getIndexes() | 返回一个文档数组，这些文档描述集合的索引 |
| group(document) | 提供一种基本聚合，即根据指定的字段将文档分组（参见第9章） |
| insert(document) | 在集合中插入新文档（参见第8章） |
| isCapped() | 如果集合为固定集合，就返回true，否则返回false |
| mapReduce(map, reduce, options) | 提供映射-归并聚合功能（参见第9章） |
| reIndex() | 重建集合的所有索引 |
| remove(query, justOne) | 将集合中满足查询条件（由参数query指定）的文档删除；如果参数justOne为true，则只删除第一个满足条件的文档 |
| renameCollection(target, dropTarget) | 将当前集合的名称改为target指定的名称。如果参数dropTarget为true，将在重命名当前集合前删除集合target |
| save(document) | 包装了insert()和update()，用于插入新文档。如果文档不存在，就插入它；否则就更新它 |
| stats() | 返回一个文档，其中包含有关集合的统计信息 |
| storageSize() | 返回一个文档，指出了集合占用的总存储空间，单位为字节 |
| totalSize() | 返回一个文档，指出了集合的总空间，包括集合中所有文档和索引的大小 |
| totalIndexSize() | 返回一个文档，指出了集合索引占据的总空间 |
| update(query, update, options) | 修改集合中的一个或多个文档（参见第8章） |
| validate() | 对集合执行诊断操作 |

