### 15.2　使用PHP删除文档

> **使用PHP从集合中删除文档**
> 在本节中，您将编写一个简单的PHP应用程序，它使用MongoCollection对象的方法从示例数据库的一个集合中删除文档。通过这个示例，您将熟悉如何使用PHP删除文档。程序清单15.3显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，再调用其他的方法来删除文档。方法showNewDocs()显示前面创建的新文档，从而核实它们确实从集合中删除了。
> 方法removeNewDocs()使用一个查询对象来删除字段category为New的文档。
> 请执行下面的步骤，创建并运行这个从示例数据库中删除文档并显示结果的PHP应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour15中新建一个文件，并将其命名为PHPDocDelete.php。
> 4．在这个文件中输入程序清单15.3所示的代码。这些代码使用remove()来删除文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour15。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单15.4显示了这个应用程序的输出。
> **程序清单15.3　PHPDocDelete.php：在PHP应用程序中从集合中删除文档**
> **程序清单15.4　PHPDocDelete.php-output：在PHP应用程序中从集合中删除文档的输出**
> ▲

在PHP中，有时候需要从MongoDB集合中删除文档，以减少消耗的空间，改善性能以及保持整洁。MongoCollection对象的方法remove()使得从集合中删除文档非常简单，其语法如下：

```go
remove([query])
```

其中参数query是一个Array对象，指定要了删除哪些文档。请求将query指定的字段和值与文档的字段和值进行比较，进而删除匹配的文档。如果没有指定参数query，将删除集合中的所有文档。

例如，要删除集合words_stats中所有的文档，可使用如下代码：

```go
$collection = $myDB->getCollection('word_stats');
$results = $collection->remove();
```

下面的代码删除集合words_stats中所有以a打头的单词：

```go
$collection = $myDB->getCollection('word_stats');
$query = array('first' => 'a');
collection->remove($query);
```

▼　Try It Yourself

```go
php PHPDocDelete.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   print_r("\nBefore Deleting: \n");
06   showNewDocs($collection);
07   removeNewDocs($collection);
08   function showNewDocs($collection){
09     $query = array('category' => 'New');
10     $cursor = $collection->find($query);
11     foreach ($cursor as $id => $doc){
12       print_r(json_encode($doc)."\n");
13     }
14   }
15   function removeNewDocs($collection){
16     $query = array('category' => "New");
17     $options = array('w' => 1, 'j' => true);
18     $results = $collection->remove($query, $options);
19     print_r("\nDelete Docs Result: \n");
20     print_r(json_encode($results)."\n");
21     print_r("\nAfter Deleting Docs: \n");
22     showNewDocs($collection);
23   }
24 ?>
```

```go
Before Deleting:
{ "_id":{"$id":"52e944b8828594f04100002b"},"word":"tweet","first":"t",  
"last":"t",
  "size":5,"category":"New","stats":{"vowels":2,"consonants":3},  
"letters":["t","w", "e"],
  "charsets":[{"type":"consonants","chars":["t","w"]},
                {"type":"vowels","chars":["e"]}]}
{"_id":{"$id":"52e944b8828594f041000029"},"word":"selfie","first":"s", "last":"e",
  "size":6,"category":"New","stats":{"vowels":3,"consonants":3},
  "letters":["s","e","l","f","i"],
  "charsets":[{"type":"consonants","chars":["s","l","f"]},
                 {"type":"vowels","chars":["e","i"]}]}
{"_id":{"$id":"52e944b8828594f04100002a"},"word":"google","first":"g",  
"last":"e",
  "size":6,"category":"New","stats":{"vowels":3,"consonants":3},
  "letters":["g","o","l","e"],
  "charsets":[{"type":"consonants","chars":["g","l"]},
                {"type":"vowels","chars":["o","e"]}]}
Delete Docs Result:
{"n":3,"connectionId":16,"err":null,"ok":1}
After Deleting Docs:
<empty>
```

