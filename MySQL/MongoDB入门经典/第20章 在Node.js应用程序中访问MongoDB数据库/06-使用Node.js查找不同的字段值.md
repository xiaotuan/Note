### 20.2 使用Node.js查找不同的字段值

> **使用Node.js检索一组文档中指定字段的不同值**
> 在本节中，您将编写一个Node.js应用程序，它使用Collection对象的方法distinct() 来检索示例数据库中不同的字段值。通过这个示例，您将熟练地生成数据集中的不同字段值列表。程序清单20.7显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来找出并显示不同的字段值。
> 方法sizesOfAllWords()找出并显示所有单词的各种长度；方法sizesOfQWords()找出并显示以q打头的单词的各种长度；方法firstLetterOfLongWords()找出并显示长度超过12的单词的各种长度。
> 请执行下面的步骤，创建并运行这个Node.js应用程序，它找出示例数据集中文档集的不同字段值，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour20中新建一个文件，并将其命名为NodejsFindDistinct.js。
> 4．在这个文件中输入程序清单20.7所示的代码。这些代码对文档集执行distinct()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour20。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单20.8显示了这个应用程序的输出。
> **程序清单20.7 NodejsFindDistinct.js：在Node.js应用程序中找出文档集中不同的字段值**
> **程序清单20.8 NodejsFindDistinct.js-output：在Node.js应用程序中找出文档集中不同字段值的输出**
> ▲

一种很有用的MongoDB集合查询是，获取一组文档中某个字段的不同值列表。不同（distinct）意味着纵然有数千个文档，您只想知道那些独一无二的值。

Collection和Cursor对象的方法distinct()让您能够找出指定字段的不同值列表，这个方法的语法如下：

```go
distinct(key, callback)
```

其中参数key是一个字符串，指定了要获取哪个字段的不同值。要获取子文档中字段的不同值，可使用句点语法，如stats.count。如果要获取部分文档中指定字段的不同值，可先使用查询生成一个Cursor对象，再对这个Cursor对象调用方法distinct()。

例如，假设有一些包含字段first、last和age的用户文档，要获取年龄超过65岁的用户的不同姓，可使用下面的操作：

```go
var query = {'age' : {'$gt' : 65}};
var cursor = myCollection.find(query);
cursor.distinct('last', function(err, lastNames){
   console.log(lastNames);
}
```

方法distinct()返回一个数组，其中包含指定字段的不同值，例如：

```go
["Smith", "Jones", ...]
```

▼　Try It Yourself

```go
node NodejsFindDistinct.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       sizesOfAllWords(collection);
09       sizesOfQWords(collection);
10       firstLetterOfLongWords(collection);
11       setTimeout(function(){myDB.close();}, 3000);
12    });
13 });
14 function sizesOfAllWords(collection){
15    collection.distinct("size", function(err, results){
16       console.log("\nDistinct Sizes of words: \n" + results);
17    });
18 }
19 function sizesOfQWords(collection){
20    var query = {'first': 'q'};
21    collection.distinct("size", query, function(err, results){
22       console.log("\nDistinct Sizes of words starting with Q: \n" +
23                      results);
24    });
25 }
26 function firstLetterOfLongWords(collection){
27    var query = {'size': {'$gt': 12}};
28    collection.distinct("first", query, function(err, results){
29       console.log("\nDistinct first letters of words longer than" +
30                      " 12 characters: \n" + results);
31    });
32 }
```

```go
Distinct Sizes of words starting with Q:
8,5,7,4
Distinct Sizes of words:
3,2,1,4,5,9,6,7,8,10,11,12,13,14
Distinct first letters of words longer than 12 characters:
i,a,e,r,c,u,s,p,t
```

