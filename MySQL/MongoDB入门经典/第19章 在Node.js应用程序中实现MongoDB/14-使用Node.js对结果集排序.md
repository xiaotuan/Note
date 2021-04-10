### 19.4　使用Node.js对结果集排序

> **使用sort ()以特定顺序返回Node. js对象Cursor表示的文档**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用查询对象和方法find()从示例数据库检索特定的文档集，再使用方法sort()将游标中的文档按特定顺序排列。通过这个示例，您将熟悉如何在检索并处理文档前对游标表示的文档进行排序。程序清单19.9显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来查找特定的文档，对找到的文档进行排序并显示结果。方法displayCursor()显示排序后的单词列表。
> 方法sortWordsAscending()获取以w打头的单词并将它们按升序排列；方法sortWordsDescending()获取以w打头的单词并将它们按降序排列；方法sortWordsAscAndSize()获取以q打头的单词，并将它们首先按最后一个字母升序排列，再按长度降序排列。
> 执行下面的步骤，创建并运行这个Node.js应用程序，它在示例数据集中查找特定的文档、对找到的文档进行排序并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour19中新建一个文件，并将其命名为NodejsFindSort.js。
> 4．在这个文件中输入程序清单19.9所示的代码。这些代码对Cursor对象表示的文档进行排序。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour19。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单19.10显示了这个应用程序的输出。
> **程序清单19.9　NodejsFindSort.js：在Node.js应用程序中查找集合中的特定文档并进行排序**
> **程序清单19.10　NodejsFindSort.js-output：在Node.js应用程序中查找集合中的特定文档并进行排序的输出**
> ▲

从MongoDB数据库检索文档时，一个重要方面是对文档进行排序。只想检索特定数量（如前10个）的文档或要对结果集进行分页时，这特别有帮助。排序选项让您能够指定用于排序的文档字段和方向。

Cursor对象的方法sort()让您能够指定要根据哪些字段对游标中的文档进行排序，并按相应的顺序返回文档。方法sort()将一个元组（[key, order]对）列表作为参数，其中key为用于排序的字段名，而order的值为1（升序）或-1（降序）。

例如，要按字段name升序排列文档，可使用下面的代码：

```go
var sorter = [['name', 1]];
var cursor = myCollection.find();
cursor.sort(sorter, function(err, sortedItems){
. . .
});
```

在传递给方法sort()的列表中，可指定多个字段，这样文档将按这些字段排序。还可对同一个游标调用sort()方法多次，从而依次按不同的字段进行排序。例如，要首先按字段name升序排列，再按字段value降序排列，可使用下面的代码：

```go
var sorter = [['name', 1], ['value', -1]];
var cursor = myCollection.find();
cursor.sort(sorter, function(err, sortedItems){
   . . .
});
```

也可使用下面的代码：

```go
var sorter1 = [['name', 1]];
var sorter2 = [['value', -1]];
var cursor = myCollection.find();
cursor = cursor.sort(sorter1);
cursor.sort(sorter2, function(err, sortedItems){
   . . .
});
```

▼　Try It Yourself

```go
node NodejsFindSort.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       sortWordsAscending(collection);
09       sortWordsDescending(collection);
10       sortWordsAscAndSize(collection);
11       setTimeout(function(){myDB.close();}, 3000);
12    });
13 });
14 function displayCursor(cursor, msg){
15    cursor.toArray(function(err, itemArr){
16       var wordStr = "";
17       for(var i in itemArr){
18          wordStr += itemArr[i].word + ",";
19       }
20       if (wordStr.length > 65){
21          wordStr = wordStr.slice(0, 65) + "...";
22       }
23       console.log("\n" + msg + "\n" + wordStr);
24    });
25 }
26 function sortWordsAscending(collection){
27    var query = {'first': 'w'};
28    var sorter = [['word', 1]];
29    var cursor = collection.find(query);
30    cursor = cursor.sort(sorter);
31    displayCursor(cursor, "W words ordered ascending:");
32 }
33 function sortWordsDescending(collection){
34    var query = {'first': 'w'};
35    var sorter = [['word', -1]];
36    var cursor = collection.find(query);
37    cursor = cursor.sort(sorter);
38    displayCursor(cursor, "W words ordered descending:");
39 }
40 function sortWordsAscAndSize(collection){
41    var query = {'first': 'q'};
42    var sorter = [['last', 1], ['size', -1]];
43    var cursor = collection.find(query);
44    cursor = cursor.sort(sorter);
45    displayCursor(cursor, "Q words ordered first by last "+
46                                  "letter and then by size:");
47 }
```

```go
Q words ordered first by last letter and then by size:
quite,quote,quick,question,quarter,quiet,quit,quickly,quality,qui...
W words ordered ascending:
wage,wait,wake,walk,wall,want,war,warm,warn,warning,wash,waste,wa...
W words ordered descending:
wrong,writing,writer,write,wrap,would,worth,worry,world,works,wor...
```

