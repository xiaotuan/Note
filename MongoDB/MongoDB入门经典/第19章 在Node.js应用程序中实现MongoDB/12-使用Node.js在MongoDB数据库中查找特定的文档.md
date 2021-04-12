### 19.2.2　使用Node.js在MongoDB数据库中查找特定的文档

> **使用Node. js从MongoDB数据库检索特定的文档**
> 在本节中，您将编写一个简单的Node.js应用程序，它使用查询对象和方法find()从示例数据库检索一组特定的文档。通过这个示例，您将熟悉如何创建查询对象以及如何使用它们来显示数据库请求返回的文档。程序清单19.4显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找并显示特定的文档。方法displayCursor()迭代游标并显示它表示的单词。
> 方法over12()查找长度超过12的单词；方法startingABC()查找以a、b或c打头的单词；方法startEndVowels()查找以元音字母打头和结尾的单词；方法over6Vowels()查找包含的元音字母超过6个的单词；方法nonAlphaCharacters()查找包含类型为other的字符集且长度为1的单词。
> 请执行如下步骤，创建并运行这个在示例数据集中查找特定文档并显示结果的Node.js应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour19中新建一个文件，并将其命名为NodejsFindSpecific.js。
> 4．在这个文件中输入程序清单19.5所示的代码。这些代码使用了方法find()和查询对象。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour19。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单19.6显示了这个应用程序的输出。
> **程序清单19.5　NodejsFindSpecific.js：在Node.js应用程序中从集合中查找并检索特定文档**
> **程序清单19.6　NodejsFindSpecific.js-output：在Node.js应用程序中从集合中查找并检索特定文档的输出**
> ▲

一般而言，您不会想从服务器检索集合中的所有文档。方法find()和findOne()让您能够向服务器发送一个查询对象，从而像在MongoDB shell中那样限制文档。

要创建查询对象，可使用本章前面描述的JavaScript对象。对于查询对象中为子对象的字段，可创建JavaScript子对象；对于其他类型（如整型、字符串和数组）的字段，可使用相应的Node.js类型。

例如，要创建一个查询对象来查找size=5的单词，可使用下面的代码：

```go
var query = {'size' : 5};
var cursor = myColl.find(query);
```

要创建一个查询对象来查找size>5的单词，可使用下面的代码：

```go
var query = {'size' :
                  {'$gt' : 5}};
var cursor = myColl.find(query);
```

要创建一个查询对象来查找第一个字母为x、y或z的单词，可使用String数组，如下所示：

```go
var query = {'first' :
                 {'$in' : ["x", "y", "z"]}};
var cursor = myColl.find(query);
```

利用上述技巧可创建需要的任何查询对象：不仅能为查找操作创建查询对象，还能为其他需要查询对象的操作这样做。

▼　Try It Yourself

```go
node NodejsFindSpecific.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       over12(collection);
09       startingABC(collection);
10       startEndVowels(collection);
11       over6Vowels(collection);
12       nonAlphaCharacters(collection);
13       setTimeout(function(){myDB.close();}, 5000);
14    });
15 });
16 function displayCursor(cursor, msg){
17    cursor.toArray(function(err, itemArr){
18       var wordStr = "";
19       for(var i in itemArr){
20          wordStr += itemArr[i].word + ",";
21       }
22       if (wordStr.length > 65){
23          wordStr = wordStr.slice(0, 65) + "...";
24       }
25       console.log("\n" + msg + "\n" + wordStr);
26    });
27 }
28 function over12(collection){
29    var query = {'size': {'$gt': 12}};
30    var cursor = collection.find(query);
31    displayCursor(cursor, "Words with more than 12 characters:");
32 }
33 function startingABC(collection){
34    var query = {'first': {'$in': ["a","b","c"]}};
35    var cursor = collection.find(query);
36    displayCursor(cursor, "Words starting with A, B or C:");
37 }
38 function startEndVowels(collection){
39    var query = {'$and': [
40                    {'first': {'$in': ["a","e","i","o","u"]}},
41                    {'last': {'$in': ["a","e","i","o","u"]}}]};
42    var cursor = collection.find(query);
43    displayCursor(cursor, "Words starting and ending with a vowel:");
44 }
45 function over6Vowels(collection){
46    var query = {'stats.vowels': {'$gt': 5}};
47    var cursor = collection.find(query);
48    displayCursor(cursor, "Words with more than 5 vowel:");
49 }
50 function nonAlphaCharacters(collection){
51    var query = {'charsets':
52        {'$elemMatch':
53          {'$and': [
54            {'type': 'other'},
55            {'chars': {'$size': 1}}]}}};
56    var cursor = collection.find(query);
57    displayCursor(cursor, "Words with 1 non-alphabet characters:");
58 }
```

```go
Words with more than 12 characters:
international,administration,environmental,responsibility,investi...
Words with more than 5 vowel:
international,organization,administration,investigation,communica...
Words with 1 non-alphabet characters:
don't,won't,can't,shouldn't,e-mail,long-term,so-called,mm-hmm,
Words starting and ending with a vowel:
a,i,one,into,also,use,area,eye,issue,include,once,idea,ago,office...
Words starting with A, B or C:
be,and,a,can't,at,but,by,as,can,all,about,come,could,also,because...
```

