### 20.1.2 使用Node.js限制返回的字段

> **在方法find()中使用参数fields来减少Cursor对象表示的文档中的字段数**
> 在本节中，您将编写一个简单的Node.js应用程序，它在方法find()中使用参数fields来限制返回的字段。通过这个示例，您将熟悉如何使用方法find()的参数fields，并了解它对结果的影响。程序清单20.3显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找文档并显示其指定的字段。方法displayCursor()迭代游标并显示找到的文档。
> 方法includeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，使其只返回指定的字段；方法excludeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，以排除指定的字段。
> 请执行如下步骤，创建并运行这个Node.js应用程序，它在示例数据集中查找文档，限制返回的字段并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour20中新建一个文件，并将其命名为NodejsFindFields.js。
> 4．在这个文件中输入程序清单20.3所示的代码。这些代码在调用方法find()时传递了参数fields。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour20。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单20.4显示了这个应用程序的输出。
> **程序清单20.3 NodejsFindFields.js：在Node.js应用程序中限制从集合返回的文档包含的字段**
> 程序清单20.4 NodejsFindFields.js-output：在Node.js应用程序中限制从集合返回的文档包含的字段的输出
> ▲



为限制文档检索时返回的数据量，另一种极有效的方式是限制要返回的字段。文档可能有很多字段在有些情况下很有用，但在其他情况下没用。从MongoDB服务器检索文档时，需考虑应包含哪些字段，并只请求必要的字段。

要对Collection对象的方法find()从服务器返回的字段进行限制，可使用参数fields。这个参数是一个JavaScript对象，它使用值true来包含字段，使用值false来排除字段。

例如，要在返回文档时排除字段stats、value和comments，可使用下面的fields参数：

```go
var fields = {'stats' : false, 'value' : false, 'comments' : false);
var cursor = myColl.find({}, {'fields': fields});
```

这里将查询对象指定成了null，因为您要查找所有的文档。

仅包含所需的字段通常更容易。例如，如果只想返回first字段为t的文档的word和size字段，可使用下面的代码：

```go
var query = {'first' : 't'};
var fields = {'word' : true, 'size' : true};
var cursor = myColl.find(query, fields);
```

▼　Try It Yourself

```go
node NodejsFindFields.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       includeFields(collection, ['word', 'size']);
09       includeFields(collection, ['word', 'letters']);
10       excludeFields(collection, ['lettes', 'stats', 'charsets']);
11       setTimeout(function(){myDB.close();}, 3000);
12    });
13 });
14 function displayCursor(doc, msg){
15    console.log("\n" + msg);
16    console.log(doc);
17 }
18 function includeFields(collection, fields){
19    var query = {'first': 'p'};
20    var fieldObj = {};
21    for (var i in fields){
22       fieldObj[fields[i]] = true;
23    }
24    collection.findOne(query, {fields: fieldObj}, function(err, doc){
25       displayCursor(doc, "Including " + fields +" fields:");
26    });
27 }
28 function excludeFields(collection, fields){
29    var query = {'first': 'p'};
30    var fieldObj = {};
31    for (var i in fields){
32       fieldObj[fields[i]] = false;
33    }
34    collection.findOne(query, {fields: fieldObj}, function(err, doc){
35       displayCursor(doc, "Excluding " + fields +" fields:");
36    });
37 }
```

```go
Including word,size fields:
{ _id: 52eff3508101065e6a93e35f, word: 'people', size: 6 }
Including word,letters fields:
{ _id: 52eff3508101065e6a93e35f,
   word: 'people',
   letters: [ 'p', 'e', 'o', 'l' ] }
Excluding lettes,stats,charsets fields:
{ _id: 52eff3508101065e6a93e35f,
word: 'people',
first: 'p',
last: 'e',
size: 6,
letters: [ 'p', 'e', 'o', 'l' ] }
```

