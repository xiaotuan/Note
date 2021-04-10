### 21.1　使用Node.js添加文档

> **使用Node.js在集合中插入文档**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用Collection对象的方法insert()在示例数据库的一个集合中插入新文档。通过这个示例，您将熟悉如何使用Node.js来插入文档。程序清单21.1显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来插入文档。方法showNewDocs()显示新插入到集合中的文档。
> 方法addSelfie()新建一个表示单词selfie的文档，并使用insert()将其加入到数据库中；方法addGoogleAndTweet()创建表示单词google和tweet的新文档，并使用insert()以数组的方式将它们插入数据库。
> 请执行下面的步骤，创建并运行这个在示例数据库中插入新文档并显示结果的Node.js应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour21中新建一个文件，并将其命名为NodejsDocAdd.js。
> 4．在这个文件中输入程序清单21.1所示的代码。这些代码使用insert()来添加新文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour21。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单21.2显示了这个应用程序的输出。
> **程序清单21.1　NodejsDocAdd.js：在Node.js应用程序中将新文档插入到集合中**
> **程序清单21.2　NodejsDocAdd.js-output：在Node.js应用程序中将新文档插入到集合中的输出**
> ▲

在Node.js中与MongoDB数据库交互时，一项重要的任务是在集合中插入文档。要插入文档，首先要创建一个表示该文档的JavaScript对象。插入操作将JavaScript对象以BSON的方式传递给MongoDB服务器，以便能够插入到集合中。

有新文档的JavaScript对象版本后，就可将其存储到MongoDB数据库中，为此可对相应的Collection对象实例调用方法insert()。方法insert()的语法如下，其中参数doc可以是单个文档对象，也可以是一个文档对象数组：

```go
insert(doc, callback)
```

例如，下面的示例在集合中插入单个文档：

```go
var doc1 = {'name' : 'Fred'};
myColl.insert(doc1, function(err, results){
   . . .
});
```

要在集合中插入多个文档，可在调用Collection对象的方法insert()时传入一个JavaScript对象数组，如下所示：

```go
var doc2 = {'name' : 'George'};
var doc3 = {'name' : 'Ron'};
myColl.batchInsert([doc2, doc3], function(err, results){
   . . .
});
```

方法insert()以JavaScript对象的方式返回新创建的文档，其中包含服务器为这些文档生成的_id值。

▼　Try It Yourself

```go
node NodejsDocAdd.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       console.log("Before Inserting:");
09       showDocs(collection, addSelfie);
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
23 function addSelfie(collection){
24    var selfie = {
25       word: 'selfie', first: 's', last: 'e',
26       size: 4, letters: ['s','e','l','f','i'],
27       stats: {vowels: 3, consonants: 3},
28       charsets: [ {type: 'consonants', chars: ['s','l','f']},
29                      {type: 'vowels', chars: ['e','i']} ],
30       category: 'New' };
31    var options = {w:1, wtimeout:5000, journal:true, fsync:false};
32       collection.insert(selfie, options, function(err, results){
33          console.log("\nInserting One Results:\n");
34          console.log(results);
35          console.log("\nAfter Inserting One:");
36          showDocs(collection, addGoogleAndTweet);
37    });
38 }
39 function addGoogleAndTweet(collection){
40    var tweet = {
41         word: 'tweet', first: 't', last: 't',
42         size: 4, letters: ['t','w','e'],
43         stats: {vowels: 2, consonants: 3},
44         charsets: [ {type: 'consonants', chars: ['t','w']},
45                       {type: 'vowels', chars: ['e']} ],
46         category: 'New' };
47    var google = {
48         word: 'google', first: 'g', last: 'e',
49         size: 4, letters: ['g','o','l','e'],
50         stats: {vowels: 3, consonants: 3},
51         charsets : [ {type: 'consonants', chars: ['g','l']},
52                         {type: 'vowels', chars: ['o','e']} ],
53         category: 'New' };
54    var options = {w:1, wtimeout:5000, journal:true, fsync:false};
55    collection.insert([google, tweet], options, function(err, results){
56       console.log("\nInserting Multiple Results:\n");
57       console.log(results);
58       console.log("\nAfter Inserting Multiple:");
59       showDocs(collection, closeDB);
60    });
61 }
62 function closeDB(collection){
63       myDB.close();
64 }
```

```go
Before Inserting:
Inserting One Results:
[ { word: 'selfie',
     first: 's',
     last: 'e',
     size: 4,
     letters: [ 's', 'e', 'l', 'f', 'i' ],
     stats: { vowels: 3, consonants: 3 },
     charsets: [ [Object], [Object] ],
     category: 'New',
     _id: 52f02b47a0392c380f614e19 } ]
After Inserting One:
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
Inserting Multiple Results:
[ { word: 'google',
     first: 'g',
     last: 'e',
     size: 4,
     letters: [ 'g', 'o', 'l', 'e' ],
     stats: { vowels: 3, consonants: 3 },
     charsets: [ [Object], [Object] ],
     category: 'New',
     _id: 52f02b47a0392c380f614e1a },
   { word: 'tweet',
     first: 't',
     last: 't',
     size: 4,
     letters: [ 't', 'w', 'e' ],
     stats: { vowels: 2, consonants: 3 },
     charsets: [ [Object], [Object] ],
     category: 'New',
     _id: 52f02b47a0392c380f614e1b } ]
After Inserting Multiple:
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
```

