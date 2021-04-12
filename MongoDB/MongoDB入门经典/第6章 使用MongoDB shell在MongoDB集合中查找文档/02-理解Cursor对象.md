### 6.1　理解Cursor对象

在MongoDB shell中对Collection对象执行有些操作时，结果是以Cursor对象的方式返回的。Cursor对象相当于一个指针，可通过迭代它来访问数据库中的一组对象。例如，当您使用find()时，返回的并非实际文档，而是一个Cursor对象，您可以使用它来读取结果中的文档。

由于Cursor对象是可以迭代的，因此在内部存储了一个指向当前位置的索引，这让您能够每次读取一个文档。别忘了，有些操作只影响Cursor中的当前文档，并将索引加1；而有些操作影响当前索引之后的所有文档。

为让您对Cursor对象有大致了解，表6.1列出了可调用Cursor对象的基本方法。这些方法让您能够操作Cursor对象，并控制对其表示的实际对象的访问。

<center class="my_markdown"><b class="my_markdown">表6.1　　Cursor对象的基本方法</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| batchSize(size) | 指定MongoDB在每个网络响应中向客户端返回的文档数，默认为20 |
| count() | 返回Cursor对象表示的文档数 |
| explain() | 返回一个文档，它描述了将用来返回查询结果的查询执行计划，包括要使用的索引。这提供了一种排除缓慢查询故障或优化请求的极佳方式 |
| forEach(function) | 迭代Cursor对象中的每个文档，并对其执行指定的JavaScript函数。指定的JavaScript函数必须将文档作为唯一的参数。下面是一个示例： myColl.find().forEach(function(doc){ print("name: " + doc.name); }); |
| hasNext() | 在使用next()迭代游标时使用。如果游标中还有其他文档，可以继续迭代，则返回true |
| hint(index) | 强制MongoDB使用一个或多个特定的索引进行查询。index可以是字符串，如hint("myIndex_1")；也可以是文档，其中的属性为索引名，而值为1，如hint({ myIndex: 1}) |
| limit(maxItems) | 将游标的结果集限制为maxItems指定的大小 |
| map(function) | 迭代Cursor中的每个文档，并对其执行指定的函数。将每次迭代的返回值都加入到一个数组中，并返回这个数组。例如： names = myColl.find().map(function(doc){ return doc.name; }); |
| max(indexBounds) | 指定Cursor返回的文档中字段的最大值，例如： max({ height: 60, age: 10 }) |
| min() | 指定Cursor返回的文档中字段的最小值，例如： min({ height: 60, age: 10 }) |
| next() | 从Cursor返回下一个文档，并将迭代索引加1 |
| objsLeftInBatch() | 指出Cursor返回的当前那批文档中还余下多少个。迭代到最前那批文档中最后一个后，需要再次向服务器发出请求以取回下批文档 |
| readPref(mode, tagSet) | 指定Cursor的读取首选项，以控制客户端向副本集发送查询的方式 |
| size() | 在执行方法skip()和limit()后，返回Cursor中的文档数 |
| skip(n) | 返回另一个Cursor，它从n个文档后开始返回结果 |
| snapshot() | 强制Cursor使用根据_id字段创建的索引，确保Cursor只返回每个文档一次 |
| sort(sortObj) | 将结果按sortObj指定的方式排序。sortObj应包含用于排序的字段，并使用-1指定降序或使用1指定升序，例如： sort({ name: 1, age: -1 }) |
| toArray() | 返回一个JavaScript对象数组，表示Cursor返回的所有文档。 |

