### 21.3　使用Node.js保存文档

> **使用Node.js将文档保存到集合中**
> 在本节中，您将创建一个简单的Node.js应用程序，它使用Collection对象的方法save()来更新示例数据库中的一个既有文档。通过这个示例，您将熟悉如何使用Node.js更新并保存文档对象。程序清单21.5显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来保存文档。方法showWord()显示更新前和更新后的单词ocean。
> 方法saveBlueDoc()从数据库中获取单词ocean的文档，使用put()将字段category改为blue，再使用方法save()保存这个文档。方法resetDoc()从数据库获取单词ocean的文档，使用方法put()将字段category恢复为空，再使用方法save()保存这个文档。
> 请执行如下步骤，创建并运行这个将文档保存到示例数据库中并显示结果的Node.js应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour21中新建一个文件，并将其命名为NodejsDocSave.js。
> 4．在这个文件中输入程序清单21.5所示的代码。这些代码使用save()来保存文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour21。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单21.6显示了这个应用程序的输出。
> **程序清单21.5　NodejsDocSave.js：在Node.js应用程序中将文档保存到集合中**
> **程序清单21.6　NodejsDocSave.js-output：在Node.js应用程序中将文档保存到集合中的输出**
> ▲

一种更新数据库中文档的便利方式是，使用Collection对象的方法save()，这个方法接受一个JavaScript作为参数，并将其保存到数据库中。如果指定的文档已存在于数据库中，就将其更新为指定的值；否则就插入一个新文档。

方法save()的语法如下，其中参数doc是一个JavaScript对象，表示要保存到集合中的文档：

```go
save(doc, callback)
```

方法save()将保存的文档数作为第二个参数传递给它的回调函数。

▼　Try It Yourself

```go
node NodejsDocSave.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       console.log("Before Save:");
09       showWord(collection, saveBlueDoc);
10    });
11 });
12 function showWord(collection, callback){
13    var query = {'word': 'ocean'};
14    collection.find(query, function(err, items){
15       items.toArray(function(err, itemsArr){
16          for (var i in itemsArr){
17             console.log(itemsArr[i]);
18          }
19          callback(collection);
20       });
21    });
22 }
23 function saveBlueDoc(collection){
24    var query = {'word' : "ocean"};
25    collection.findOne(query, function(err, doc){
26       doc["category"] = "blue";
27       var options = {w:1, wtimeout:5000, journal:true, fsync:false};
28       collection.save(doc, function(err, results){
29          console.log("\nSave Docs Result:");
30          console.log(results);
31          console.log("\nAfter Saving Doc:");
32          showWord(collection, resetDoc);
33       });
34    });
35 }
36 function resetDoc(collection){
37    var query = {'word' : "ocean"};
38    collection.findOne(query, function(err, doc){
39       doc["category"] = "";
40       var options = {w:1, wtimeout:5000, journal:true, fsync:false};
41       collection.save(doc, function(err, results){
42          console.log("\nReset Docs Result:");
43          console.log(results);
44          console.log("\nAfter Resetting Doc:");
45          showWord(collection, closeDB);
46       });
47    });
48 }
49 function closeDB(collection){
50    myDB.close();
51 }
```

```go
Before Save:
{ _id: 52eff3508101065e6a93e99c,
   word: 'ocean',
   first: 'o',
   last: 'n',
   size: 5,
   letters: [ 'o', 'c', 'e', 'a', 'n' ],
   stats: { vowels: 3, consonants: 2 },
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   category: '' }
Save Docs Result:
1
After Saving Doc:
{ _id: 52eff3508101065e6a93e99c,
   word: 'ocean',
   first: 'o',
   last: 'n',
   size: 5,
   letters: [ 'o', 'c', 'e', 'a', 'n' ],
   stats: { vowels: 3, consonants: 2 },
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   category: 'blue' }
Reset Docs Result:
1
After Resetting Doc:
{ _id: 52eff3508101065e6a93e99c,
   word: 'ocean',
   first: 'o',
   last: 'n',
   size: 5,
   letters: [ 'o', 'c', 'e', 'a', 'n' ],
   stats: { vowels: 3, consonants: 2 },
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   category: '' }
```

