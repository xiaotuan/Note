### 15.3　使用PHP保存文档

> **使用PHP将文档保存到集合中**
> 在本节中，您将创建一个简单的PHP应用程序，它使用MongoCollection对象的方法save()来更新示例数据库中的一个既有文档。通过这个示例，您将熟悉如何使用PHP更新并保存文档对象。程序清单15.5显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他的方法来保存文档。方法showWord()显示更新前和更新后的单词ocean。
> 方法saveBlueDoc()从数据库中获取单词ocean的文档，使用put()将字段category改为blue，再使用方法save()保存这个文档。方法resetDoc()从数据库获取单词ocean的文档，使用方法put()将字段category恢复为空，再使用方法save()保存这个文档。
> 请执行如下步骤，创建并运行这个将文档保存到示例数据库中并显示结果的PHP应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour15中新建一个文件，并将其命名为PHPDocSave.php。
> 4．在这个文件中输入程序清单15.5所示的代码。这些代码使用save()来保存文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour15。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单15.6显示了这个应用程序的输出。
> **程序清单15.5　PHPDocSave.php：在PHP应用程序中将文档保存到集合中**
> **程序清单15.6　PHPDocSave.php-output：在PHP应用程序中将文档保存到集合中的输出**
> ▲

一种更新数据库中文档的便利方式是，使用MongoCollection对象的方法save()，这个方法接受一个Array对象作为参数，并将其保存到数据库中。如果指定的文档已存在于数据库中，就将其更新为指定的值；否则就插入一个新文档。

方法save()的语法如下，其中参数doc是一个Array对象，表示的是要保存到集合中的文档：

```go
save(doc)
```

▼　Try It Yourself

```go
php PHPDocSave.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   print_r("\nBefore Saving: \n");
06   showWord($collection);
07   saveBlueDoc($collection);
08   resetDoc($collection);
09   function showWord($collection){
10     $query = array('word' => 'ocean');
11     $fields = array('word' => true, 'category' => true);
12     $doc = $collection->findOne($query, $fields);
13     print_r(json_encode($doc)."\n");
14   }
15   function saveBlueDoc($collection){
16     $query = array('word' => "ocean");
17     $doc = $collection->findOne($query);
18     $doc["category"] = "blue";
19     $options = array('w' => 1, 'j' => true);
20     $results = $collection->save($doc, $options);
21     print_r("\nSave Docs Result: \n");
22     print_r(json_encode($results)."\n");
23     print_r("\nAfter Saving Doc: \n");
24     showWord($collection);
25   }
26   function resetDoc($collection){
27     $query = array('word' => "ocean");
28     $doc = $collection->findOne($query);
29     $doc["category"] = "";
30     $options = array('w' => 1, 'j' => true);
31     $results = $collection->save($doc, $options);
32     print_r("\nReset Docs Result: \n");
33     print_r(json_encode($results)."\n");
34     print_r("\nAfter Resetting Doc: \n");
35     showWord($collection);
36   }
37 ?>
```

```go
Before Saving:
{"_id":{"$id":"52e89477c25e8498553265e4"},"word":"ocean"}
Save Docs Result:
{"updatedExisting":true,"n":1,"connectionId":18,"err":null,"ok":1}
After Saving Doc:
{"_id":{"$id":"52e89477c25e8498553265e4"},"word":"ocean","category":"blue"}
Reset Docs Result:
{"updatedExisting":true,"n":1,"connectionId":18,"err":null,"ok":1}
After Resetting Doc:
{"_id":{"$id":"52e89477c25e8498553265e4"},"word":"ocean","category":""}
```

