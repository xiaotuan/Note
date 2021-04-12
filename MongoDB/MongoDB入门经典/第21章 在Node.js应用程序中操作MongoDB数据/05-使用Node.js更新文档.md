### 21.4　使用Node.js更新文档

> **使用Node.js更新集合中的文档**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用Collection对象的方法update()来更新示例数据库的一个集合中的既有文档。这个示例旨在让您熟悉如何在Node.js中使用MongoDB更新运算符来更新文档。程序清单21.7显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，再调用其他方法更新文档。方法showWord()显示更新前和更新后的文档。
> 方法updateDoc()创建一个查询对象，它从数据库获取表示单词left的文档；再创建一个更新对象，它将字段word的值改为lefty，将字段size和stats.consonants的值加1，并将字母y压入到数组字段letters中。方法resetDoc()将文档恢复原样，以演示如何将字段值减1以及如何从数组字段中弹出值。
> 请执行下面的步骤，创建并运行这个更新示例数据库中文档并显示结果的Node.js应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour21中新建一个文件，并将其命名为NodejsDocUpdate.js。
> 4．在这个文件中输入程序清单21.7所示的代码。这些代码使用update()来更新文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour21。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单21.8显示了这个应用程序的输出。
> **程序清单21.7　NodejsDocUpdate.js：在Node.js应用程序中更新集合中的文档**
> **程序清单21.8　NodejsDocUpdate.js-output：在Node.js应用程序中更新集合中文档的输出**
> ▲

将文档插入集合后，经常需要使用Node.js根据数据变化更新它们。Collection对象的方法update()让您能够更新集合中的文档，它多才多艺，但使用起来非常容易。下面是方法update()的语法：

```go
update(query, update, [options], callback)
```

参数query是一个JavaScript对象，指定了要修改哪些文档。请求将判断query指定的属性和值是否与文档的字段和值匹配，进而更新匹配的文档。参数update是一个JavaScript对象，指定了要如何修改与查询匹配的文档。第8章介绍了可在这个对象中使用的更新运算符。

参数options让您能够设置写入关注和更新选项。对于upate()操作，您需要理解其中的参数upsert和multi。参数upsert是个布尔值，决定了是否执行upsert操作；如果为true且没有文档与查询匹配，将插入一个新文档。参数multi也是一个布尔值；如果为true将更新所有与查询匹配的文档，否则只更新与查询匹配的第一个文档。

例如，对于集合中字段category为New的文档，下面的代码将其字段category改为Old。在这里，upsert被设置为false，因此即便没有字段category为New的文档，也不会插入新文档；而multi被设置为true，因此将更新所有匹配的文档：

```go
var query = {'category' : 'New'};
var update = {'$set' : {'category' : 'Old'}};
var options = {'upsert': false, 'multi': true};
myColl.update(query, update, options, function(err, results){
. . .
});
```

方法update()将更新的文档数作为第二个参数传递给它的回调函数。

▼　Try It Yourself

```go
node NodejsDocUpdate.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       console.log("Before Updating:");
09       showWord(collection, updateDoc);
10    });
11 });
12 function showWord(collection, callback){
13    var query = {'word': {'$in' : ['left', 'lefty']}};
14    collection.find(query, function(err, items){
15       items.toArray(function(err, itemsArr){
16          for (var i in itemsArr){
17             console.log(itemsArr[i]);
18          }
19          callback(collection);
20       });
21    });
22 }
23 function updateDoc(collection){
24    var query = {'word' : "left"};
25    var update = {
26         '$set' : {'word' : 'lefty'},
27         '$inc' : {'size' : 1, 'stats.consonants' : 1},
28         '$push' : {'letters' : 'y'}};
29    var options = {w:1, wtimeout:5000, journal:true, fsync:false,
30                      upsert:false, multi:false};
31    collection.update(query, update, options, function(err, results){
32       console.log("\nUpdating Doc Results:");
33       console.log(results);
34       console.log("\nAfter Updating Doc:");
35       showWord(collection, resetDoc);
36    });
37 }
38 function resetDoc(collection){
39    var query = {'word' : "lefty"};
40    var update = {
41         '$set' : {'word' : 'left'},
42         '$inc' : {'size' : -1, 'stats.consonants' : -1},
43         '$pop' : {'letters' : 1}};
44    var options = {w:1, wtimeout:5000, journal:true, fsync:false,
45         upsert:false, multi:false};
46    collection.update(query, update, options, function(err, results){
47       console.log("\nReset Doc Results:");
48       console.log(results);
49       console.log("\nAfter Resetting Doc:");
50       showWord(collection, closeDB);
51    });
52 }
53 function closeDB(collection){
54    myDB.close();
55 }
```

```go
Before Updating:
{ _id: 52eff3508101065e6a93e5e6,
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   first: 'l',
   last: 't',
   letters: [ 'l', 'e', 'f', 't' ],
   size: 4,
   stats: { consonants: 3, vowels: 1 },
   word: 'left' }
Updating Doc Results:
1
After Updating Doc:
{ _id: 52eff3508101065e6a93e5e6,
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   first: 'l',
   last: 't',
   letters: [ 'l', 'e', 'f', 't', 'y' ],
   size: 5,
   stats: { consonants: 4, vowels: 1 },
   word: 'lefty' }
Reset Doc Results:
1
After Resetting Doc:
{ _id: 52eff3508101065e6a93e5e6,
   charsets:
    [ { type: 'consonants', chars: [Object] },
      { type: 'vowels', chars: [Object] } ],
   first: 'l',
   last: 't',
   letters: [ 'l', 'e', 'f', 't' ],
   size: 4,
   stats: { consonants: 3, vowels: 1 },
   word: 'left' }
```

