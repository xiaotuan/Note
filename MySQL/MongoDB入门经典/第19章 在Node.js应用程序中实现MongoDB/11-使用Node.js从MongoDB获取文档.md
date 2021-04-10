### 19.2.1　使用Node.js从MongoDB获取文档

> **使用Node.js从MongoDB检索文档**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用find()和findOne()从示例数据库中检索文档。通过这个示例，您将熟悉如何使用方法find()和findOne()以及如何处理响应。程序清单19.3显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，再调用其他方法来查找并显示文档。
> 方法getOne()调用方法findOne()从集合中获取单个文档，再显示该文档；方法getManyFor()查找所有的文档，将它们转换为一个数组，并使用for循环来显示前5个文档。
> 方法getManyEach()查找集合中的前5个文档，在使用方法each()来迭代并显示这些单词。
> 请执行如下步骤，创建并运行这个在示例数据集中查找文档并显示结果的Node.js应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour19中新建一个文件，并将其命名为NodejsFind.js。
> 4．在这个文件中输入程序清单19.3所示的代码。这些代码使用了方法find()和findOne()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour19。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单19.4显示了这个应用程序的输出。
> **程序清单19.3　NodejsFind.js：在Node.js应用程序中查找并检索集合中的文档**
> **程序清单19.4　NodejsFind.js-output：在Node.js应用程序中查找并检索集合中文档的输出**
> ▲

Collection对象提供了方法find()和findOne()，它们与MongoDB shell中的同名方法类似，也分别查找一个和多个文档。

调用findOne()时，将以JavaScript对象的方式将单个文档提供给回调函数，然后您就可根据需要在应用程序中使用这个对象，如下所示：

```go
myColl.findOne(function(err, doc){
. . .
});
```

Collection对象的方法find()向回调函数提供一个Cursor对象，这个对象表示找到的文档，但不取回它们。可以多种不同的方式迭代Cursor对象。

可以使用Cursor对象的方法each()来迭代返回的文档。每个文档都将作为第二个参数传递给each()的回调函数。如果传入的文档为null，就说明已到达游标末尾。例如，下面的代码使用each()来迭代Cursor对象：

```go
var cursor = myColl.find();
cursor.each(function(err, doc){
   if(doc){
      console.log(doc);
   }
});
```

如果有足够的内存来存储游标表示的所有文档，还可使用方法toArray()将Curosr对象转换为文档对象数组。例如，下面的代码使用toArray()来迭代Cursor对象：

```go
var cursor = myColl.find();
cursor.toArray(function(err, docArr){
   for(var i in docArray){
      console.log(docArray[i]);
   }
});
```

▼　Try It Yourself

```go
node NodejsFind.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       getOne(collection);
09       setTimeout(function(){myDB.close();}, 3000);
10    });
11 });
12 function getOne(collection){
13    collection.findOne({}, function(err, item){
14       console.log("Single Document: ");
15       console.log(item);
16       getManyFor(collection);
17    });
18 }
19 function getManyFor(collection){
20    var cursor = collection.find();
21    cursor.toArray(function(err, itemArr){
22       console.log("\nWords Using Array For Loop: ");
23       for(var i=0; i<5; i++){
24          console.log(itemArr[i].word);
25       }
26       getManyEach(collection);
27    });
28 }
29 function getManyEach(collection){
30    var cursor = collection.find().limit(5);
31    console.log("\nWords Using Each Loop: ");
32    cursor.each(function(err, item){
33       if(item){
34          console.log(item['word']);
35       }
36    });
37 }
```

```go
Single Document:
{ _id: 52eff3508101065e6a93e322,
   word: 'the',
   first: 't',
   last: 'e',
   size: 3,
   letters: [ 't', 'h', 'e' ],
   stats: { vowels: 1, consonants: 2 },
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ] }
Words Using Array For Loop:
the
be
and
of
a
Words Using Each Loop:
the
be
and
of
a
```

