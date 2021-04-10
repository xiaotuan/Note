### 16.1.3　理解Python对象Collection

Python对象Collection提供了访问和操作集合中文档的功能。与Database对象相关联的集合存储在Database对象的内部字典中。要获取Collection对象实例，最简单的方式是直接使用Database对象和集合名。例如，下面的代码获取一个Collection对象，它与数据库words中的集合word_stats相关联：

```go
mongo = MongoClient("")
db = mongo["words"]
collection = db["word_stats"]
```

创建Collection对象实例后，就可使用它来访问集合了。表16.3列出了Collection对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表16.3　　Python对象Collection的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| aggregate(pipeline) | 应用聚合选项流水线。流水线中的每个选项都是一个表示聚合操作的Dictionary对象。Dictionary对象将在本章后面讨论，而聚合操作在第9章讨论过 |
| count([query]) | 返回集合中与指定查询匹配的文档数。参数query是一个描述查询的Dictionary对象 |
| distinct(key) | 返回一个数组，其中包含指定字段的不同值 |
| drop() | 删除集合 |
| drop_index(keys) | 删除keys指定的索引 |
| ensure_index(keys, [options]) | 添加keys和可选参数options描述的索引，这两个参数都是Dictionary对象 |
| find([query], [fields]) | 返回一个表示集合中文档的Cursor对象。可选参数query是一个Dictionary对象，让您能够限制要包含的文档；可选参数fields也是一个Dictionary对象，让您能够指定要返回文档中的哪些字段 |
| find_and_modify(query, update, fields, upsert, sort) | 以原子方式查找并更新集合中的文档，并返回修改后的文档。参数query是一个Dictionary对象，指定要更新哪些文档；参数update是一个Dictionary对象，指定要使用的更新运算符；参数fields是一个Dictionary对象，指定要返回更新后的文档中的哪些字段；参数sort是一个指定排序方式的列表，而参数upsert为True时将执行upsert操作 |
| find_one([query], [fields]) | 返回一个Dictionary对象，表示集合中的一个文档。可选参数query是一个Dictionary对象，让您能够限制要包含的文档；可选参数fields也是一个Dictionary对象，让您能够指定要返回文档中的哪些字段 |
| group(key, condition, initial, reduce, [finalize]) | 对集合执行分组操作（参见第9章） |
| insert(objects) | 在集合中插入一个或多个对象 |
| remove([query]) | 从集合中删除文档。如果没有指定参数query，将删除所有文档；否则只删除与查询匹配的文档 |
| rename(newName) | 重命名集合 |
| save(object) | 将对象保存到集合中。如果指定的对象不存在，就插入它 |
| update(query, update, [upsert],[manipulate], [safe], [multi]) | 更新集合中的文档。参数query是一个Dictionary对象，指定要更新哪些文档；参数update是一个Dictionary对象，指定更新运算符。您可使用布尔参数upsert来指定是否执行upsert操作；如果参数multi为False，将只更新第一个文档 |
| read_preference | 与前面介绍的MongoClient的同名属性相同 |
| write_concern | 与前面介绍的MongoClient的同名属性相同 |

