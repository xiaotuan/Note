### 21.5　使用Node.js更新或插入文档

> **使用Node.js更新集合中的文档**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用方法update()对示例数据库执行upsert操作：先插入一个新文档，再更新这个文档。通过这个示例，您将熟悉如何在Node.js应用程序使用方法update()来执行upsert操作。程序清单21.9显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来更新文档。方法showWord()用于显示单词被添加前后以及被更新后的情况。
> 方法addUpsert()创建一个数据库中没有的新单词，再使用upsert操作来插入这个新文档。这个文档包含的信息有些不对，因此方法updateUpsert()执行upsert操作来修复这些错误；这次更新了既有文档，演示了upsert操作的更新功能。
> 请执行如下步骤，创建并运行这个Node.js应用程序，它对示例数据库中的文档执行upsert操作并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour21中新建一个文件，并将其命名为NodejsDocUpsert.js。
> 4．在这个文件中输入程序清单21.9所示的代码。这些代码使用update()来对文档执行upsert操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour21。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单21.10显示了这个应用程序的输出。
> **程序清单21.9　NodejsDocUpsert.js：在Node.js应用程序中对集合中的文档执行upsert操作**
> **程序清单21.10　NodejsDocUpsert.js-output：在Node.js应用程序中对集合中文档执行upsert操作的输出**
> ▲

在Node.js中，Collection对象的方法update()的另一种用途是，用于执行upsert操作。upsert操作先尝试更新集合中的文档；如果没有与查询匹配的文档，就使用$set运算符来创建一个新文档，并将其插入到集合中。下面显示了方法update()的语法：

```go
update(query, update, [options], callback)
```

参数query指定要修改哪些文档；参数update是一个JavaScript对象，指定了要如何修改与查询匹配的文档。要执行upsert操作，必须在参数options中将upsert设置为true，并将multi设置为false。

例如，下面的代码对name=myDoc的文档执行upsert操作。运算符$set指定了用来创建或更新文档的字段。由于参数upsert被设置为true，因此如果没有找到指定的文档，将创建它；否则就更新它：

```go
var query = {'name': 'myDoc'};
var setOp = {'name': 'myDoc',
                'number', 5,
                'score', 10};
var update = {'$set': setOp};
var options = {'upsert': true, 'multi': false};
update(query, update, options, function(err, results){
   . . .
});
```

▼　Try It Yourself

```go
node NodejsDocUpsert.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       console.log("Before Upserting:");
09       showWord(collection, addUpsert);
10    });
11 });
12 function showWord(collection, callback){
13    var query = {'word': 'righty'};
14    collection.find(query, function(err, items){
15       items.toArray(function(err, itemsArr){
16          for (var i in itemsArr){
17             console.log(itemsArr[i]);
18          }
19          callback(collection);
20       });
21    });
22 }
23 function addUpsert(collection){
24    var query = {'word' : 'righty'};
25    var update = { '$set' :
26       { 'word' : 'righty', 'first' : 'r', 'last' : 'y',
27          'size' : 4, 'category' : 'New',
28          'stats' : {'vowels' : 1, 'consonants' : 4},
29          'letters' : ["r","i","g","h"],
30          'charsets' : [
31            {'type' : 'consonants', 'chars' : ["r","g","h"]},
32            {'type' : 'vowels', 'chars' : ["i"]}]}};
33    var options = {w:1, wtimeout:5000, journal:true, fsync:false,
34                      upsert:true, multi:false};
35    collection.update(query, update, options, function(err, results){
36       console.log("\nUpsert as insert results:");
37       console.log(results);
38       console.log("\nAfter Upsert as insert:");
39       showWord(collection, updateUpsert);
40    });
41 }
42 function updateUpsert(collection){
43    var query = {'word' : 'righty'}
44    var update = { '$set' :
45       { 'word' : 'righty', 'first' : 'r', 'last' : 'y',
46          'size' : 6, 'category' : 'Updated',
47          'stats' : {'vowels' : 1, 'consonants' : 5},
48          'letters' : ["r","i","g","h","t","y"],
49          'charsets' : [
50            {'type' : 'consonants', 'chars' : ["r","g","h","t","y"]},
51            {'type' : 'vowels', 'chars' : ["i"]}]}}
52    var options = {w:1, wtimeout:5000, journal:true, fsync:false,
53       upsert:true, multi:false};
54    collection.update(query, update, options, function(err, results){
55       console.log("\nUpsert as update results:");
56       console.log(results);
57       console.log("\nAfter Upsert as update:");
58       showWord(collection, cleanup);
59    });
60 }
61 function cleanup(collection){
62    collection.remove({word:'righty'}, function(err, results){
63       myDB.close();
64    });
65 }
```

```go
Before Upserting:
Upsert as insert results:
1
After Upsert as insert:
{ _id: 52f0300af0506a15d7bb6b3d,
   category: 'New',
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   first: 'r',
   last: 'y',
   letters: [ 'r', 'i', 'g', 'h' ],
   size: 4,
   stats: { vowels: 1, consonants: 4 },
   word: 'righty' }
Upsert as update results:
1
After Upsert as update:
{ _id: 52f0300af0506a15d7bb6b3d,
   category: 'Updated',
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   first: 'r',
   last: 'y',
   letters: [ 'r', 'i', 'g', 'h', 't', 'y' ],
   size: 6,
   stats: { vowels: 1, consonants: 5 },
   word: 'righty' }
```

