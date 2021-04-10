### 15.5　使用PHP更新或插入文档

> **使用PHP更新集合中的文档**
> 在本节中，您将编写一个简单的PHP应用程序，它使用方法update()对示例数据库执行upsert操作：先插入一个新文档，再更新这个文档。通过这个示例，您将熟悉如何在PHP应用程序使用方法update()来执行upsert操作。程序清单15.9显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，再调用其他的方法来更新文档。方法showWord()用于显示单词被添加前后以及被更新后的情况。
> 方法addUpsert()创建一个数据库中没有的新单词，再使用upsert操作来插入这个新文档。这个文档包含的信息有些不对，因此方法updateUpsert()执行upsert操作来修复这些错误；这次更新了既有文档，演示了upsert操作的更新功能。
> 请执行如下步骤，创建并运行这个PHP应用程序，它对示例数据库中的文档执行upsert操作并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour15中新建一个文件，并将其命名为PHPDocUpsert.php。
> 4．在这个文件中输入程序清单15.9所示的代码。这些代码使用update()来对文档执行upsert操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour15。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单15.10显示了这个应用程序的输出。
> **程序清单15.9　PHPDocUpsert.php：在PHP应用程序中对集合中的文档执行upsert操作**
> **程序清单15.10　PHPDocUpsert.php-output：在PHP应用程序中对集合中文档执行upsert操作的输出**
> ▲

在PHP中，MongoCollection对象的方法update()的另一种用途是，用于执行upsert操作。upsert操作先尝试更新集合中的文档；如果没有与查询匹配的文档，就使用$set运算符来创建一个新文档，并将其插入到集合中。下面显示了方法update()的语法：

```go
update(query, update, [options])
```

参数query指定要修改哪些文档；参数update是一个Array对象，指定了要如何修改与查询匹配的文档；参数options指定写入关注选项以及upsert和multiple的设置。要执行upsert操作，必须将upsert设置为true，并将multiple设置为false。

例如，下面的代码对name=myDoc的文档执行upsert操作。运算符$set指定了用来创建或更新文档的字段。由于参数upsert被设置为true，因此如果没有找到指定的文档，将创建它；否则就更新它：

```go
$query = array('name' => 'myDoc');
$update = array('$set' =>
   array('name' => 'myDoc', 'number' => 5, 'score' => 10));
$options = array('w' => 1, 'j' => true, 'upsert' => true, 'multiple' => false);
$results = $collection->update($query, $update, $options);
```

▼　Try It Yourself

```go
php PHPDocUpsert.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   print_r("\nBefore Upserting: \n");
06   showWord($collection);
07   addUpsert($collection);
08   updateUpsert($collection);
09   function showWord($collection){
10     $query = array('word' => 'righty');
11     $doc = $collection->findOne($query);
12     print_r(json_encode($doc)."\n");
13   }
14   function addUpsert($collection){
15     $query = array('word' => 'righty');
16     $update = array( '$set' =>
17       array(
18         'word' => 'righty', 'first' => 'r', 'last' => 'y',
19         'size' => 4, 'category' => 'New',
20         'stats' => array('vowels' => 1, 'consonants' => 4),
21         'letters' => ["r","i","g","h"],
22         'charsets' => [
23           array('type' => 'consonants', 'chars' => ["r","g","h"]),
24           array('type' => 'vowels', 'chars' => ["i"])]
25       ));
26     $options = array('w' => 1, 'j' => true,
27                         'upsert' => true, 'multiple' => false);
28     $results = $collection->update($query, $update, $options);
29     print_r("\nUpsert as insert results: \n");
30     print_r(json_encode($results)."\n");
31     print_r("After Upsert as insert: \n");
32     showWord($collection);
33   }
34   function updateUpsert($collection){
35     $query = array('word' => 'righty');
36     $update = array( '$set' =>
37         array(
38           'word' => 'righty', 'first' => 'r', 'last' => 'y',
39           'size' => 6, 'category' => 'Updated',
40           'stats' => array('vowels' => 1, 'consonants' => 5),
41           'letters' => ["r","i","g","h","t","y"],
42           'charsets' => [
43             array('type' => 'consonants', 'chars' => ["r","g","h","t", "y"]),
44             array('type' => 'vowels', 'chars' => ["i"])]
45         ));
46     $options = array('w' => 1, 'j' => true,
47                         'upsert' => true, 'multiple' => false);
48     $results = $collection->update($query, $update, $options);
49     print_r("\nUpsert as update results: \n");
50     print_r(json_encode($results)."\n");
51     print_r("After Upsert as update: \n");
52     showWord($collection);
53     cleanupWord($collection);
54   }
55   function cleanupWord($collection){
56     $collection->remove(array('word' => 'righty'));
57   }
58 ?>
```

```go
Before Upserting:
null
Upsert as insert results:
{"updatedExisting":false,"upserted":{"$id":"52eaebf2381e4f7e1b27b411"},"n":1,
  "connectionId":120,"err":null,"ok":1}
After Upsert as insert:
{ "_id":{"$id":"52eaebf2381e4f7e1b27b411"},"category":"New",
  "charsets":[{"type":"consonants","chars":["r","g","h"]},
                {"type":"vowels","chars":["i"]}],
  "first":"r","last":"y","letters":["r","i","g","h"],"size":4,
  "stats":{"vowels":1,"consonants":4},"word":"righty"}
Upsert as update results:
{"updatedExisting":true,"n":1,"connectionId":120,"err":null,"ok":1}
After Upsert as update:
{"_id":{"$id":"52eaebf2381e4f7e1b27b411"},"category":"Updated",
  "charsets":[{"type":"consonants","chars":["r","g","h","t","y"]},
                {"type":"vowels","chars":["i"]}],
  "first":"r","last":"y","letters":["r","i","g","h","t","y"],
  "size":6,"stats":{"vowels":1,"consonants":5},"word":"righty"}
```

