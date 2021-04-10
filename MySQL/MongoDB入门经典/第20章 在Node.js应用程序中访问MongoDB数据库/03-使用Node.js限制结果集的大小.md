### 20.1.1 使用Node.js限制结果集的大小

> 使用 **limit** ()将 **Node** . **js** 对象 **Cursor** 表示的文档减少到指定的数量
> 在本节中，您将编写一个简单的Node.js应用程序，它使用limit()来限制find()操作返回的结果。通过这个示例，您将熟悉如何结合使用limit()和find()，并了解limit()对结果的影响。程序清单20.1显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他方法来查找并显示数量有限的文档。方法displayCursor()迭代游标并显示找到的单词。
> 方法limitResults()接受一个limit参数，查找以p打头的单词，并返回参数limit指定的单词数。
> 请执行如下步骤，创建并运行这个Node.js应用程序，它在示例数据集中查找指定数量的文档并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour20中新建一个文件，并将其命名为NodejsFindLimit.js。
> 4．在这个文件中输入程序清单20.1所示的代码。这些代码使用了方法find()和limit()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour20。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单20.2显示了这个应用程序的输出。
> **程序清单20.1 NodejsFindLimit.js：在Node.js应用程序中在集合中查找指定数量的文档**
> **程序清单20.2 NodejsFindLimit.js-output：在Node.js应用程序中在集合中查找指定数量文档的输出**
> ▲

要限制find()或其他查询请求返回的数据量，最简单的方法是对find()操作返回的Cursor对象调用方法limit()，它让Cursor对象返回指定数量的文档，可避免检索的对象量超过应用程序的处理能力。

例如，下面的代码只显示集合中的前10个文档，即便匹配的文档有数千个：

```go
var cursor = wordsColl.find();
cursor.limit(10, function(err, items){
   items.each(function(err, word){
      if(word){
         console.log(word);
      }
   }
});
```

▼　Try It Yourself

```go
node NodejsFindLimit.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       limitResults(collection, 1);
09    });
10 });
11 function displayCursor(cursor, callback, collection, limit){
12    cursor.toArray(function(err, itemArr){
13       var wordStr = "";
14       for(var i in itemArr){
15          wordStr += itemArr[i].word + ",";
16       }
17       if (wordStr.length > 65){
18          wordStr = wordStr.slice(0, 65) + "...";
19       }
20       console.log(wordStr);
21       if(collection){
22          callback(collection, limit);
23       } else {
24          myDB.close();
25       }
26    });
27 }
28 function limitResults(collection, limit){
29    var query = {'first': 'p'};
30    var cursor = collection.find(query);
31    cursor.limit(limit, function(err, items){
32       console.log("\nP words Limited to " + limit + ":");
33       if(limit < 7){
34          displayCursor(items, limitResults, collection, limit + 2);
35       } else {
36          displayCursor(items, limitResults, null, null);
37       }
38    });
39 }
```

```go
P words Limited to 1:
people,
P words Limited to 3:
people,put,problem,
P words Limited to 5:
people,put,problem,part,place,
P words Limited to 7:
people,put,problem,part,place,program,play,
```

