### 24.6.5　使用Node.js从MongoDB GridFS中删除文件

> **使用Node.js访问和操作MongoDB GridFS存储区中的文件**
> 本节将引导您完成在Node.js应用程序中实现MongoDB GridFS存储的流程，包括访问MongoDB GridFS以及列出、添加、获取和删除文件的步骤。
> 在这个示例中，主脚本连接到MongoDB数据库，并调用各种方法来访问GridFS以列出、添加、获取和删除文件。
> 方法listGridFSFiles()用于在Node.js应用程序运行期间的各个时点显示MongoDB GridFS中当前存储的文件；方法putGridFSFile()将一个文件存储到GridFS中；方法getGridFSFile()从GridFS获取一个文件并显示其内容；方法deleteGridFSFile()从GridFS中删除文件。
> 请执行如下步骤，使用Node.js来列出、获取、添加和删除文件。
> 1．确保启动了MongoDB服务器。
> 2．确保安装并配置了Node.js MongoDB驱动程序。
> 3．在文件夹code/hour24中新建一个文件，并将其命名为NodejsGridFS.js。
> 4．在这个文件中输入程序清单24.7所示的代码。这些代码访问MongoDB GridFS。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour24。
> 7．执行下面的命令运行这个Node.js应用程序。程序清单24.8显示了这个应用程序的输出。
> **程序清单24.7　NodejsGridFS.js：使用Node.js列出、添加、获取和删除MongoDB GridFS中的文件**
> **程序清单24.8　NodejsGridFS.js-output：使用Node.js列出、添加、获取和删除MongoDB GridFS中文件的输出**
> ▲

在Node.js中，要将文件从GridFS存储区中删除，最简单的方式是使用GridStore类的方法unlink()。这个方法将文件从MongoDB GridFS存储区中删除，其语法如下：

```go
GridStore.unlink(db, filename, callback)
```

例如，下面的语句删除文件test.txt：

```go
GridStore.unlink(db, " <strong>test </strong>.txt", function(err, gridStore){
   . . .
});
```

▼　Try It Yourself

```go
node NodejsGridFS.js
```

```go
01 var MongoClient = require('mongodb').MongoClient;
02 var Server = require('mongodb').Server;
03 var GridStore = require('mongodb').GridStore;
04 var fs = require('fs');
05 var mongo = new MongoClient();
06 var myDB = null;
07 mongo.connect("mongodb://localhost/myFS", function(err, db) {
08    myDB = db;
09    console.log("\nFiles Before Put:");
10    listGridFSFiles(db, putGridFSFile);
11 });
12 function listGridFSFiles(db, callback){
13    GridStore.list(db, function(err, items){
14       console.log(items);
15       callback(db);
16    });
17 }
18 function putGridFSFile(db){
19    fs.writeFile("nodejs.txt", "Stored from Node.js", function(err) {
20       var myFS = new GridStore(db, "nodejs.txt", "w");
21       myFS.writeFile("nodejs.txt", function(err, fsObj){
22          console.log("\nFiles After Put:");
23          listGridFSFiles(db, getGridFSFile);
24       });
25    });
26 }
27 function getGridFSFile(db){
28    GridStore.read(db, "nodejs.txt", function(err, data){
29       console.log("\nContents of Retrieve File:");
30       console.log(data.toString());
31       deleteGridFSFile(db, closeDB);
32    });
33 }
34 function deleteGridFSFile(db){
35    GridStore.unlink(db, "nodejs.txt", function(err, gridStore){
36       console.log("\nFiles After Delete:");
37       listGridFSFiles(db, closeDB);
38    });
39 }
40 function closeDB(db){
41    db.close();
42 }
```

```go
Files Before Put:
[]
Files After Put:
[ 'nodejs.txt' ]
Contents of Retrieve File:
Stored from Node.js
Files After Delete:
[]
```

