### 20.1.3 使用Node.js将结果集分页

> 在Node.js中使用skip()和limit()对MongoDB集合中的文档进行分页
> 在本节中，您将编写一个简单的Node.js应用程序，它使用Cursor对象的方法skip()和limit()方法对find()返回的大量文档进行分页。通过这个示例，您将熟悉如何使用skip()和limit()对较大的数据集进行分页。程序清单20.5显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找文档并以分页方式显示它们。方法displayCursor()迭代游标并显示当前页中的单词。
> 方法pageResults()接受一个skip参数，并根据它以分页方式显示以w开头的所有单词。每显示一页后，都将skip值递增，直到到达游标末尾。
> 请执行下面的步骤，创建并运行这个对示例数据集中的文档进行分页并显示结果的Node.js应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Node.js MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour20中新建一个文件，并将其命名为NodejsFindPaging.js。
> 4．在这个文件中输入程序清单20.5所示的代码。这些代码实现了文档集分页。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour20。
> 7．执行下面的命令来运行这个Node.js应用程序。程序清单20.6显示了这个应用程序的输出。
> **程序清单20.5 NodejsFindPaging.js：在Node.js应用程序中分页显示集合中的文档集**
> **程序清单20.6 NodejsFindPaging.js-output：在Node.js应用程序中分页显示集合中的文档集的输出**
> ▲

为减少返回的文档数，一种常见的方法是进行分页。要进行分页，需要指定要在结果集中跳过的文档数，还需限制返回的文档数。跳过的文档数将不断增加，每次的增量都是前一次返回的文档数。

要对一组文档进行分页，需要使用Cursor对象的方法limit()和skip()。方法skip()让您能够指定在返回文档前要跳过多少个文档。

每次获取下一组文档时，都增大方法skip()中指定的值，增量为前一次调用limit()时指定的值，这样就实现了数据集分页。

例如，下面的语句查找第11～20个文档：

```go
var cursor = collection.find();
cursor = cursor.limit(10);
cursor = cursor.skip(10);
```

进行分页时，务必调用方法sort()来确保文档的排列顺序不变。

▼　Try It Yourself

```go
node NodejsFindPaging.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var mongo = new MongoClient();
04 var myDB = null;
05 mongo.connect("mongodb://localhost/", function(err, db) {
06    myDB = db.db("words");
07    myDB.collection("word_stats", function(err, collection){
08       pageResults(collection, 0);
09    });
10 });
11 function displayCursor(cursor, callback, collection, skip, more){
12    cursor.toArray(function(err, itemArr){
13       var wordStr = "";
14       for(var i in itemArr){
15          wordStr += itemArr[i].word + ",";
16       }
17       if (wordStr.length > 65){
18          wordStr = wordStr.slice(0, 65) + "...";
19       }
20       console.log(wordStr);
21       if(more){
22          callback(collection, skip);
23       } else {
24          myDB.close();
25       }
26    });
27 }
28 function pageResults(collection, skip){
29    var query = {'first': 'w'};
30    var cursor = collection.find(query);
31    cursor.skip(skip).limit(10, function(err, items){
32       items.count(true, function(err, count){
33          var pageStart = skip+1;
34          var pageEnd = skip+count;
35          var more = count==10;
36          console.log("Page " + pageStart + " to " + pageEnd + ":");
37          displayCursor(items, pageResults, collection, pageEnd, more);
38       });
39    });
40 }
```

```go
Page 1 to 10:
with,won't,we,what,who,would,will,when,which,want,
Page 11 to 20:
way,well,woman,work,world,while,why,where,week,without,
Page 21 to 30:
water,write,word,white,whether,watch,war,within,walk,win,
Page 31 to 40:
wait,wife,whole,wear,whose,wall,worker,window,wrong,west,
Page 41 to 50:
whatever,wonder,weapon,wide,weight,worry,writer,whom,wish,western...
Page 51 to 60:
wind,weekend,wood,winter,willing,wild,worth,warm,wave,wonderful,
Page 61 to 70:
wine,writing,welcome,weather,works,wake,warn,wing,winner,welfare,
Page 71 to 80:
witness,waste,wheel,weak,wrap,warning,wash,widely,wedding,wheneve...
Page 81 to 90:
wire,whisper,wet,weigh,wooden,wealth,wage,wipe,whereas,withdraw,
Page 91 to 93:
working,wisdom,wealthy,
```

