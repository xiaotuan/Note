### 19.3　使用Node.js计算文档数

> **在Node. js应用程序中使用count ()获取Cursor对象表示的文档数**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用查询对象和find()从示例数据库检索特定的文档集，并使用count()来获取游标表示的文档数。通过这个示例，您将熟悉如何在检索并处理文档前获取文档数。程序清单19.7显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来查找特定的文档并显示找到的文档数。方法countWords()使用查询对象、find()和count()来计算数据库中的单词总数以及以a打头的单词数。
> 请执行如下步骤，创建并运行这个Node.js应用程序，它查找示例数据集中的特定文档，计算找到的文档数并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour19中新建一个文件，并将其命名为NodejsFindCount.js。
> 4．在这个文件中输入程序清单19.7所示的代码。这些代码使用方法find()和查询对象查找特定文档，并计算找到的文档数。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour19。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单19.8显示了这个应用程序的输出。
> **程序清单19.7　NodejsFindCount.js：在Node.js应用程序中计算在集合中找到的特定文档的数量**
> **程序清单19.8　NodejsFindCount.js-output：在Node.js应用程序中计算在集合中找到的特定文档数量的输出**
> ▲

使用Node.js访问MongoDB数据库中的文档集时，您可能想先确定文档数，再决定是否检索它们。无论是在MongoDB服务器还是客户端，计算文档数的开销都很小，因为不需要传输实际文档。

Cursor对象的方法count()让您能够获取游标表示的文档数。例如，下面的代码使用方法find()来获取一个Cursor对象，再使用方法count()来获取文档数：

```go
var cursor = wordsColl.find();
cursor.count(function(err, itemCount){
   console.log("count = " + itemCount);
});
```

itemCount的值为与find()操作匹配的单词数。

▼　Try It Yourself

```go
node NodejsFindCount.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       countWords(collection);
09       setTimeout(function(){myDB.close();}, 3000);
10    });
11 });
12 function countWords(collection){
13    var allCursor = collection.find();
14    allCursor.count(function(err, cnt){
15       console.log("Total words in the collection:\n" + cnt);
16    });
17    var query = {first: 'a'};
18    var aCursor = collection.find(query);
19    aCursor.count(function(err, cnt){
20       console.log("\nTotal words starting with A:\n" + cnt);
21    });
22 }
```

```go
Total words in the collection:
2673
Total words starting with A:
192
```

