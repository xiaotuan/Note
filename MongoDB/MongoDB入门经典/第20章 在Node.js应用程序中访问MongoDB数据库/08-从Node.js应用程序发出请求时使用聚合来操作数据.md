### 20.4 从Node.js应用程序发出请求时使用聚合来操作数据

> **在Node.js应用程序中使用聚合来生成数据**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用Collection对象的方法aggregate()从示例数据库检索各种聚合数据。通过这个示例，您将熟悉如何使用aggregate()来利用聚合流水线在MongoDB服务器上处理数据，再返回结果。程序清单20.11显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他方法来聚合数据并显示结果。方法displayAggregate()显示聚合结果。
> 方法largeSmallVowels()使用了一条包含运算符$match、$group和$sort的聚合流水线，这条流水线查找以元音字母开头的单词，根据第一个字母将这些单词分组，并找出各组中最长和最短单词的长度。
> 方法top5AverageWordFirst()使用了一条包含运算符$group、$sort和$limit的聚合流水线，这条流水线根据第一个字母将单词分组，并找出单词平均长度最长的前5组。
> 请执行下面的步骤，创建并运行这个Node.js应用程序，它使用聚合流水线来处理示例数据集中的文档，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour20中新建一个文件，并将其命名为NodejsAggregate.js。
> 4．在这个文件中输入程序清单20.11所示的代码。这些代码对文档集执行aggregate()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour20。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单20.12显示了这个应用程序的输出。
> **程序清单20.11 NodejsAggregate.js：在Node.js应用程序中使用聚合流水线生成数据集**
> **程序清单20.12 NodejsAggregate.js-output：在Node.js应用程序中使用聚合流水线生成数据集的输出**
> ▲

在Node.js应用程序中使用MongoDB时，另一个很有用的工具是聚合框架。Collection对象提供了对数据执行聚合操作的方法aggregate()，这个方法的语法如下：

```go
aggregate(operator, [operator, ...], callback)
```

参数operator是一系列运算符对象，提供了用于聚合数据的流水线。这些运算符对象是使用聚合运算符创建的JavaScript对象。聚合运算符在第9章介绍过，您现在应该熟悉它们。

例如，下面的代码定义了运算符$group和$limit，其中运算符$group根据字段word进行分组（并将该字段的值存储在结果文档的_id字段中），使用$avg计算size字段的平均值（并将结果存储在average字段中）。请注意，在聚合运算中引用原始文档的字段时，必须在字段名前加上$：

```go
var group = {'$group' :
                   {'_id' : '$word',
                      'average' : {'$avg' : '$size'}}};
var limit = {'$limit' : 10};
collection.aggregate([group, limit], function(err, results){
   . . .
}):
```

方法aggregate()返回一个包含聚合结果的数组，其中每个元素都是一个聚合结果。为演示这一点，下面的代码逐项显示聚合结果的内容：

```go
for (var i in results){
   console.log(results[i]);
}
```

▼　Try It Yourself

```go
node NodejsAggregate.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       largeSmallVowels(collection);
09       setTimeout(function(){myDB.close();}, 3000);
10    });
11 });
12 function displayAggregate(results){
13    for (var i in results){
14       console.log(results[i]);
15    }
16 }
17 function largeSmallVowels(collection){
18    var match = {'$match' :
19                     {'first' :
20                       {'$in' : ['a','e','i','o','u']}}};
21    var group = {'$group' :
22                     { '_id' : '$first',
23                        'largest' : {'$max' : '$size'},
24                        'smallest' : {'$min' : '$size'},
25                        'total' : {'$sum' : 1}}};
26    var sort = {'$sort' : {'first' : 1}};
27    collection.aggregate([match, group, sort],
28       function(err, results){
29          console.log("\nLargest and smallest word sizes for " +
30                         "words beginning with a vowel");
31          displayAggregate(results);
32          top5AverageWordFirst(collection);
33    });
34 }
35 function top5AverageWordFirst(collection){
36    var group = {'$group' :
37                  {'_id' : '$first',
38                   'average' : {'$avg' : '$size'}}};
39    var sort = {'$sort' : {'average' : -1}};
40    var limit = {'$limit' : 5};
41    collection.aggregate([group, sort, limit],
42       function(err, results){
43          console.log("\nFirst letter of top 5 largest average " +
44                         "word size: ");
45          displayAggregate(results);
46    });
47 }
```

```go
Largest and smallest word sizes for words beginning with a vowel
{ _id: 'e', largest: 13, smallest: 3, total: 150 }
{ _id: 'u', largest: 13, smallest: 2, total: 33 }
{ _id: 'i', largest: 14, smallest: 1, total: 114 }
{ _id: 'o', largest: 12, smallest: 2, total: 72 }
{ _id: 'a', largest: 14, smallest: 1, total: 192 }
First letter of top 5 largest average word size:
{ _id: 'i', average: 7.947368421052632 }
{ _id: 'e', average: 7.42 }
{ _id: 'c', average: 7.292134831460674 }
{ _id: 'p', average: 6.881818181818182 }
{ _id: 'r', average: 6.767123287671233 }
```

