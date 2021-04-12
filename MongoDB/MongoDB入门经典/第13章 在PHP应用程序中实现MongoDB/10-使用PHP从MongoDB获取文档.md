### 13.2.1　使用PHP从MongoDB获取文档

> **使用PHP从MongoDB检索文档**
> 在本节中，您将编写一个简单的PHP应用程序，它使用find()和findOne()从示例数据库中检索文档。通过这个示例，您将熟悉如何使用方法find()和findOne()以及如何处理响应。程序清单13.3显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，再调用其他方法来查找并显示文档。
> 方法getOne()调用方法findOne()从集合中获取单个文档，再显示该文档；方法getManyWhile()查找所有的文档，再使用while循环和方法hasNext()逐个获取这些文档，并计算总字符数。
> 方法getManyForEach()查找集合中的所有文档，再使用foreach循环和方法getNext()来显示前10个单词。
> 请执行如下步骤，创建并运行这个在示例数据集中查找文档并显示结果的PHP应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour13中新建一个文件，并将其命名为PHPFind.php。
> 4．在这个文件中输入程序清单13.3所示的代码。这些代码使用了方法find()和findOne()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour13。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单13.4显示了这个应用程序的输出。
> **程序清单13.3　PHPFind.php：在PHP应用程序中查找并检索集合中的文档**
> **程序清单13.4　PHPFind.php-output：在PHP应用程序中查找并检索集合中文档的输出**
> ▲

MongoCollection对象提供了方法find()和findOne()，它们与MongoDB shell中的同名方法类似，也分别查找一个和多个文档。

调用findOne()时，将以Array对象的方式从服务器返回单个文档，然后您就可根据需要在应用程序中使用这个对象，如下所示：

```go
$doc = myColl->findOne();
```

MongoCollection对象的方法find()返回一个MongoCursor对象，这个对象表示找到的文档，但不取回它们。可以多种不同的方式迭代MongoCursor对象。

可以使用while循环和方法hasNext()来判断是否到达了游标末尾，如下所示：

```go
$cursor = $myColl->find();
while($cursor->hasNext()){
   $doc = $cursor->getNext();
   print_r($doc);
}
```

还可使用PHP foreach语法来迭代MongoCursor对象。例如，下面的代码查找集合中的所有文档，再使用foreach来显示每个文档：

```go
cursor = $collection->find();
foreach ($cursor as $id => $doc){
   print_r($doc["word"]);
}
```

▼　Try It Yourself

```go
php PHPFind.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   getOne($collection);
06   getManyWhile($collection);
07   getManyForEach($collection);
08   function getOne($collection){
09     $doc = $collection->findOne();
10     print_r("Single Document: \n");
11     print_r(json_encode($doc));
12   }
13   function getManyWhile($collection){
14     print_r("\n\nMany Using While Loop: \n");
15     $cursor = $collection->find();
16     $cursor->limit(10);
17     while($cursor->hasNext()){
18       $doc = $cursor->getNext();
19       print_r($doc["word"]);
20       print_r(",");
21     }
22   }
23   function getManyForEach($collection){
24     print_r("\n\nMany Using For Each Loop: \n");
25     $cursor = $collection->find();
26     $cursor->limit(10);
27     foreach ($cursor as $id => $doc){
28       print_r($doc["word"]);
29       print_r(",");
30     }
31   }
32 ?>
```

```go
Single Document:
{ "_id":{"$id":"52e89477c25e849855325f6a"},"word":"the","first":"t","last" :"e",
  "size":3,"letters":["t","h","e"],"stats":{"vowels":1,"consonants":2},
  "charsets":[{"type":"consonants","chars":["t","h"]},
                {"type":"vowels","chars":["e"]}]}
Many Using While Loop:
the,be,and,of,a,in,to,have,it,i,
Many Using For Each Loop:
the,be,and,of,a,in,to,have,it,i,
```

