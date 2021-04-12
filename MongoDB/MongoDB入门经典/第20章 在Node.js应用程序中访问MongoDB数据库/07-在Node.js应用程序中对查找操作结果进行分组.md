### 20.3 在Node.js应用程序中对查找操作结果进行分组

> **使用Node.js根据键值将文档分组**
> 在本节中，您将创建一个简单的Node.js应用程序，它使用Collection对象的方法group()从示例数据库检索文档，根据指定字段进行分组，并在服务器上执行reduce和finalize函数。通过这个示例，您将熟悉如何使用group()在服务器端对数据集进行处理，以生成分组数据。程序清单20.9显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找文档，进行分组并显示结果。方法displayGroup()显示分组结果。
> 方法firstIsALastIsVowel()将第一个字母为a且最后一个字母为元音字母的单词分组，其中的reduce函数计算单词数，以确定每组的单词数。
> 方法firstLetterTotals()根据第一个字母分组，并计算各组中所有单词的元音字母总数和辅音字母总数。在其中的finalize函数中，将元音字母总数和辅音字母总数相加，以提供各组单词的字符总数。
> 请执行下面的步骤，创建并运行这个Node.js应用程序，它对示例数据集中的文档进行分组和处理，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour20中新建一个文件，并将其命名为NodejsGroup.js。
> 4．在这个文件中输入程序清单20.9所示的代码。这些代码对文档集执行group()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour20。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单20.10显示了这个应用程序的输出。
> **程序清单20.9 NodejsGroup.js：在Node.js应用程序中根据字段值对单词分组以生成不同的数据**
> **程序清单20.10 NodejsGroup.js-output：在Node.js应用程序中根据字段值对单词分组以生成不同数据的输出**
> ▲

在Node.js中对大型数据集执行操作时，根据文档的一个或多个字段的值将结果分组通常很有用。这也可以在取回文档后使用代码来完成，但让MongoDB服务器在原本就要迭代文档的请求中这样做，效率要高得多。

在Node.js中，要将查询结果分组，可使用Collection对象的方法group()。分组请求首先收集所有与查询匹配的文档，再对于指定键的每个不同值，都在数组中添加一个分组对象，对这些分组对象执行操作，并返回这个分组对象数组。

方法group()的语法如下：

```go
group({keys, cond , initial, reduce, [finalize], callback})
```

其中参数keys、cond和initial都是JavaScript对象，指定了要用来分组的字段、查询以及要使用的初始文档；参数reduce和finalize为String对象，包含以字符串方式表示的JavaScript函数，这些函数将在服务器上运行以归并文档并生成最终结果。有关这些参数的更详细信息，请参阅第9章。

为演示这个方法，下面的代码实现了简单分组，它创建了对象key、cond和initial，并以字符串的方式传入了一个reduce函数：

```go
var key = {'first' : true };
var cond = {'first' : 'a', 'size': 5};
var initial = {'count' : 0};
var reduce = "function (obj, prev) { prev.count++; }";
collection.group(key, cond, initial, reduce, function(err, results){
   . . .
});
```

方法group()返回一个包含分组结果的数组。下面的代码逐项地显示了分组结果的内容：

```go
for (var i in results){
   console.log(results[i]);
}
```

▼　Try It Yourself

```go
node NodejsGroup.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       firstIsALastIsVowel(collection);
09       setTimeout(function(){myDB.close();}, 3000);
10    });
11 });
12 function displayGroup(results){
13    for (var i in results){
14       console.log(results[i]);
15    }
16 }
17 function firstIsALastIsVowel(collection){
18    var key = {'first' : true, "last" : true};
19    var cond = {'first' : 'a', 'last' :
20                       {'$in' : ["a","e","i","o","u"]}};
21    var initial = {'count' : 0};
22    var reduce = "function (obj, prev) { prev.count++; }";
23    collection.group(key, cond, initial, reduce,
24       function(err, results){
25       console.log("\n'A' words grouped by first and last" +
26                      " letter that end with a vowel:");
27       displayGroup(results);
28       firstLetterTotals(collection);
29    });
30 }
31 function firstLetterTotals(collection){
32    var key = {'first' : true};
33    var cond = {};
34    var initial = {'vowels' : 0, 'cons' : 0};
35    var reduce = "function (obj, prev) { " +
36                       "prev.vowels += obj.stats.vowels; " +
37                       "prev.cons += obj.stats.consonants; " +
38                    "}";
39    finalize = "function (obj) { " +
40                     "obj.total = obj.vowels + obj.cons; " +
41                 "}"
42 collection.group(key, cond, initial, reduce, finalize,
43    function(err, results){
44       console.log("\nWords grouped by first letter " +
45                      "with totals:");
46       displayGroup(results);
47    });
48 }
```

```go
'A' words grouped by first and last letter that end with a vowel:
{ first: 'a', last: 'a', count: 3 }
{ first: 'a', last: 'o', count: 2 }
{ first: 'a', last: 'e', count: 52 }
Words grouped by first letter with totals:
{ first: 't', vowels: 333, cons: 614 }
{ first: 'b', vowels: 246, cons: 444 }
{ first: 'a', vowels: 545, cons: 725 }
{ first: 'o', vowels: 204, cons: 237 }
{ first: 'i', vowels: 384, cons: 522 }
{ first: 'h', vowels: 145, cons: 248 }
{ first: 'f', vowels: 258, cons: 443 }
{ first: 'y', vowels: 26, cons: 41 }
{ first: 'w', vowels: 161, cons: 313 }
{ first: 'd', vowels: 362, cons: 585 }
{ first: 'c', vowels: 713, cons: 1233 }
{ first: 's', vowels: 640, cons: 1215 }
{ first: 'n', vowels: 136, cons: 208 }
{ first: 'g', vowels: 134, cons: 240 }
{ first: 'm', vowels: 262, cons: 417 }
{ first: 'k', vowels: 22, cons: 48 }
{ first: 'u', vowels: 93, cons: 117 }
{ first: 'p', vowels: 550, cons: 964 }
{ first: 'j', vowels: 47, cons: 73 }
{ first: 'l', vowels: 189, cons: 299 }
{ first: 'v', vowels: 117, cons: 143 }
{ first: 'e', vowels: 482, cons: 630 }
{ first: 'r', vowels: 414, cons: 574 }
{ first: 'q', vowels: 28, cons: 32 }
{ first: 'z', vowels: 2, cons: 2 }
```

