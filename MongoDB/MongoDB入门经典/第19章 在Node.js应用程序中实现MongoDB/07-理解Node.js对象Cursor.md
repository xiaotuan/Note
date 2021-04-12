### 19.1.5　理解Node.js对象Cursor

Node.js对象Cursor表示MongoDB服务器中的一组文档。使用查找操作查询集合时，通常返回一个Cursor对象，而不是向Node.js应用程序返回全部文档对象，这让您能够在Node.js中以受控的方式访问文档。

Cursor对象以分批的方式从服务器取回文档，并使用一个索引来迭代文档。在迭代期间，当索引到达当前那批文档末尾时，将从服务器取回下批文档。

下面的示例使用查找操作获取一个Cursor对象实例：

```go
var cursor = collection.find();
```

如果给find()指定了回调函数，获得的Cursor对象将作为第二个参数传递给回调函数，如下所示：

```go
collection.find(function(err, cursor){
   . . .
});
```

创建Cursor对象实例后，就可使用它来访问集合中的文档了。表19.4列出了Cursor对象的一些常用方法。

<center class="my_markdown"><b class="my_markdown">表19.4　　Node.js对象Cursor的方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| batchSize(size, callback) | 指定每当读取到当前已下载的最后一个文档时，游标都将再返回多少个文档 |
| count([applySkipLimit] , callback) | 返回游标表示的文档数。如果参数applySkipLimit为true，计算文档数时将考虑limit()和skip()设置的值，否则返回游标表示的所有文档数。计数结果将作为第二个参数传递给回调函数 |
| limit(size, callback) | 指定游标可最多表示多少个文档。这个方法返回一个新的Cursor对象，并将一个Cursor对象作为第二个参数传递给回调函数 |
| skip(size, callback) | 在返回文档前，跳过指定数量的文档。这个方法返回一个新的Cursor对象，并将一个Cursor对象作为第二个参数传递给回调函数 |
| sort(sort, callback) | 根据列表参数sort指定的字段对游标中的文档进行排序。这个方法返回一个新的Cursor对象，并将一个Cursor对象作为第二个参数传递给回调函数。参数sort的语法如下，其中direction为1（表示升序）或-1（表示降序）： [(key, direction), ...] |
| toArray(callback) | 将游标表示的文档转换为一个JavaScript数组，让您能够访问它们。这个文档数组将作为第二个参数传递给回调函数 |

