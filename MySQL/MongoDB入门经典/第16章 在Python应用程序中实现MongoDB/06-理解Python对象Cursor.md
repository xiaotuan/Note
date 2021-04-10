### 16.1.4　理解Python对象Cursor

Python对象Cursor表示MongoDB服务器中的一组文档。使用查找操作查询集合时，通常返回一个Cursor对象，而不是向Python应用程序返回全部文档对象，这让您能够在Python中以受控的方式访问文档。

Cursor对象以分批的方式从服务器取回文档，并使用一个索引来迭代文档。在迭代期间，当索引到达当前那批文档末尾时，将从服务器取回下批文档。

下面的示例使用查找操作获取一个Cursor对象实例：

```go
mongo = MongoClient("")
db = mongo['words']
collection = db['word_stats']
cursor = collection.find()
```

创建Cursor对象实例后，就可使用它来访问集合中的文档了。表16.4列出了Cursor对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表16.4　　Python对象Cursor的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| batch_size(size) | 指定每当读取到当前已下载的最后一个文档时，游标都将再返回多少个文档 |
| count([foundonly]) | 返回游标表示的文档数。如果参数foundonly为True，计算文档数时将考虑limit()和skip()设置的值，否则返回游标表示的所有文档数。参数foundonly默认为False |
| distinct(key) | 返回一个数组，其中包含Cursor对象表示的文档中参数key指定的字段的不同值 |
| limit(size) | 指定Cursor对象可最多表示多少个文档 |
| skip(size) | 在返回文档前，跳过指定数量的文档 |
| sort(sort) | 根据列表参数sort指定的字段对游标中的文档进行排序。参数sort的语法如下，其中direction为1（表示升序）或-1（表示降序）： [(key, direction), ...] |

