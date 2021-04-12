### 13.1.4　理解PHP对象MongoCursor

PHP对象MongoCursor表示MongoDB服务器中的一组文档。使用查找操作查询集合时，通常返回一个MongoCursor对象，而不是向PHP应用程序返回全部文档对象，这让您能够在PHP中以受控的方式访问文档。

MongoCursor对象以分批的方式从服务器取回文档，并使用一个索引来迭代文档。在迭代期间，当索引到达当前那批文档末尾时，将从服务器取回下批文档。

下面的示例使用查找操作获取一个MongoCursor对象实例：

```go
$mongo = new MongoClient("");
$db = $mongo->words;
$collection = $db->word_stats;
$cursor = $collection->find();
```

创建MongoCursor对象实例后，就可使用它来访问集合中的文档了。表13.4列出了MongoCursor对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表13.4　　PHP对象MongoCursor的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| batchSize(size) | 指定每当读取到当前已下载的最后一个文档时，游标都将再返回多少个文档 |
| count([foundOnly]) | 返回游标表示的文档数。如果参数foundOnly为true，计算文档数时将考虑limit()和skip()设置的值，否则返回游标表示的所有文档数。参数foundOnly默认为false |
| current() | 以Array对象的方式返回游标中的当前文档，但不将索引加1 |
| getNext() | 以Array对象的方式返回游标中的下一个文档，并将索引加1 |
| hasNext() | 如果游标中还有其他可供迭代的对象，就返回true |
| limit(size) | 指定游标可最多表示多少个文档 |
| next() | 将游标的索引加1 |
| skip(size) | 在返回文档前，跳过指定数量的文档 |
| sort(sort) | 按Array参数sort指定的方式对游标中的文档排序 |

