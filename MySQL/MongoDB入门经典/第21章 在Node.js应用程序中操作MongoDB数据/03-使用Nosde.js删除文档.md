### 21.2　使用Nosde.js删除文档

> **使用Node.js从集合中删除文档**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用Collection对象的方法从示例数据库的一个集合中删除文档。通过这个示例，您将熟悉如何使用Node.js删除文档。程序清单21.3显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来删除文档。方法showNewDocs()显示前面创建的新文档，从而核实它们确实从集合中删除了。
> 方法removeNewDocs()使用一个查询对象来删除字段category为New的文档。
> 请执行下面的步骤，创建并运行这个从示例数据库中删除文档并显示结果的Node.js应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour21中新建一个文件，并将其命名为NodejsDocDelete.js。
> 4．在这个文件中输入程序清单21.3所示的代码。这些代码使用remove()来删除文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour21。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单21.4显示了这个应用程序的输出。
> **程序清单21.3　NodejsDocDelete.js：在Node.js应用程序中从集合中删除文档**
> **程序清单21.4　NodejsDocDelete.js-output：在Node.js应用程序中从集合中删除文档的输出**
> ▲

在Node.js中，有时候需要从MongoDB集合中删除文档，以减少消耗的空间，改善性能以及保持整洁。Collection对象的方法remove()使得从集合中删除文档非常简单，其语法如下：

```go
remove([query], callback)
```

其中参数query是一个JavaScript对象，指定了要删除哪些文档。请求将query指定的字段和值与文档的字段和值进行比较，进而删除匹配的文档。如果没有指定参数query，将删除集合中的所有文档。

例如，要删除集合words_stats中所有的文档，可使用如下代码：

```go
collection.remove(function(err, results){
   . . .
});
```

下面的代码删除集合words_stats中所有以a打头的单词：

```go
var query = {'first' : 'a'};
collection.remove(query, function(err, results){
   . . .
});
```

方法remove()将删除的文档数作为第二个参数传递给其回调函数。

▼　Try It Yourself

```go
node NodejsDocDelete.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       console.log("Before Deleting:");
09       showDocs(collection, removeNewDocs);
10    });
11 });
12 function showDocs(collection, callback){
13    var query = {'category': 'New'};
14    collection.find(query, function(err, items){
15       items.toArray(function(err, itemsArr){
16          for (var i in itemsArr){
17             console.log(itemsArr[i]);
18          }
19          callback(collection);
20       });
21    });
22 }
23 function removeNewDocs(collection){
24    var options = {w:1, wtimeout:5000, journal:true, fsync:false};
25    collection.remove({'category': 'New'}, options, function(err, results){
26       console.log("Delete Docs Result:");
27       console.log(results);
28       console.log("\nAfter Deleting:");
29       showDocs(collection, closeDB);
30    });
31 }
32 function closeDB(collection){
33    myDB.close();
34 }
```

```go
Before Deleting:
{ word: 'tweet',
   first: 't',
   last: 't',
   size: 4,
   letters: [ 't', 'w', 'e' ],
   stats: { vowels: 2, consonants: 3 },
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   category: 'New',
   _id: 52f02b47a0392c380f614e1b }
{ word: 'selfie',
   first: 's',
   last: 'e',
   size: 4,
   letters: [ 's', 'e', 'l', 'f', 'i' ],
   stats: { vowels: 3, consonants: 3 },
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   category: 'New',
   _id: 52f02b47a0392c380f614e19 }
{ word: 'google',
   first: 'g',
   last: 'e',
   size: 4,
   letters: [ 'g', 'o', 'l', 'e' ],
   stats: { vowels: 3, consonants: 3 },
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   category: 'New',
   _id: 52f02b47a0392c380f614e1a }
Delete Docs Result:
3
After Deleting:
```

