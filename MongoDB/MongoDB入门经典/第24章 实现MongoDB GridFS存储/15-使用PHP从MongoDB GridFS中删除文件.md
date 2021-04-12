### 24.4.5　使用PHP从MongoDB GridFS中删除文件

> **使用PHP访问和操作MongoDB GridFS存储区中的文件**
> 本节将引导您完成在Java应用程序中实现MongoDB GridFS存储的流程，包括访问MongoDB GridFS以及列出、添加、获取和删除文件的步骤。
> 在这个示例中，主脚本连接到MongoDB数据库，并调用各种方法来访问GridFS以列出、添加、获取和删除文件。
> 方法listGridFSFiles()用于在PHP应用程序运行期间的各个时点显示MongoDB GridFS中当前存储的文件；方法putGridFSFile()将一个文件存储到GridFS中；方法getGridFSFile()从GridFS获取一个文件并显示其内容；方法deleteGridFSFile()从GridFS中删除文件。
> 请执行如下步骤，使用PHP列出、获取、添加和删除文件。
> 1．确保启动了MongoDB服务器。
> 2．确保安装并配置了PHP MongoDB驱动程序。
> 3．在文件夹code/hour24中新建一个文件，并将其命名为PHPGridFS.php。
> 4．在这个文件中输入程序清单24.3所示的代码。这些代码访问MongoDB GridFS。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour24。
> 7．执行下面的命令运行这个PHP应用程序。程序清单24.4显示了这个PHP应用程序的输出。
> **程序清单24.3　PHPGridFS.php：使用PHP列出、添加、获取和删除MongoDB GridFS中的文件**
> **程序清单24.4　PHPGridFS.php-output：使用PHP列出、添加、获取和删除MongoDB GridFS中文件的输出**
> ▲

在PHP中，要将文件从GridFS存储区中删除，最简单的方式是使用MongoGridFS对象的方法remove()。这个方法将文件从MongoDB GridFS存储区中删除，其语法如下：

```go
delete(objectId)
```

例如，下面的语句删除文件test.txt：

```go
$myFS = $db->getGridFS();
$file = $myFS->findOne('test.txt');
$myFS->delete($file->file["_id"]);
```

▼　Try It Yourself

```go
php PHPGridFS.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->myFS;
04   print_r("\nFiles Before Put:");
05   listGridFSFiles($db);
06   putGridFSFile($db);
07   print_r("\nFiles After Put:");
08   listGridFSFiles($db);
09   print_r("\nContents of Retrieve File:");
10   getGridFSFile($db);
11   deleteGridFSFile($db);
12   print_r("\nFiles After Delete:");
13   listGridFSFiles($db);
14   function listGridFSFiles($db){
15     $myFS = $db->getGridFS();
16     $files = $myFS->find();
17     foreach ($files as $id => $file){
18       print_r($file->getFileName());
19     }
20   }
21   function putGridFSFile($db){
22     file_put_contents('php.txt', "Stored from PHP");
23     $myFS = $db->getGridFS();
24     $file = $myFS->put('php.txt');
25   }
26   function getGridFSFile($db){
27     $myFS = $db->getGridFS();
28     $file = $myFS->findOne('php.txt');
29     print_r($file->getBytes());
30   }
31   function deleteGridFSFile($db){
32     $myFS = $db->getGridFS();
33     $file = $myFS->findOne('php.txt');
34     $myFS->delete($file->file["_id"]);
35   }
36 ?>
```

```go
Files Before Put:
Files After Put:
php.txt
Contents of Retrieve File:
Stored from PHP
Files After Delete:
```

