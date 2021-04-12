### 15.1　使用PHP添加文档

> **使用PHP在集合中插入文档**
> 在本节中，您将编写一个简单的PHP应用程序，它使用MongoCollection对象的方法insert()在示例数据库的一个集合中插入新文档。通过这个示例，您将熟悉如何使用PHP来插入文档。程序清单15.1显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他的方法来插入文档。方法showNewDocs()显示新插入到集合中的文档。
> 方法addSelfie()新建一个表示单词selfie的文档，并使用insert()将其加入到数据库中；方法addGoogleAndTweet()创建表示单词google和tweet的新文档，并使用batchInsert()以数组的方式将它们插入数据库。
> 请执行下面的步骤，创建并运行这个在示例数据库中插入新文档并显示结果的PHP应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour15中新建一个文件，并将其命名为PHPDocAdd.php。
> 4．在这个文件中输入程序清单15.1所示的代码。这些代码使用insert()和batchInsert()来添加新文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour15。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单15.2显示了这个应用程序的输出。
> **程序清单15.1　PHPDocAdd.php：在PHP应用程序中将新文档插入到集合中**
> **程序清单15.2　PHPDocAdd.php-output：在PHP应用程序中将新文档插入到集合中的输出**
> ▲

在PHP中与MongoDB数据库交互时，一项重要的任务是在集合中插入文档。要插入文档，首先要创建一个表示该文档的Array对象。插入操作将Array对象以BSON的方式传递给MongoDB服务器，以便能够插入到集合中。

有新文档的Array版本后，就可将其存储到MongoDB数据库中，为此可对相应的MongoCollection对象实例调用方法insert()。方法insert()的语法如下，其中参数doc是单个文档对象：

```go
insert(doc)
```

例如，下面的示例在集合中插入单个文档：

```go
$doc1 = array('name' => 'Fred');
$result = $myColl->insert($doc1);
```

要在集合中插入多个文档，可使用MongoCollection对象的方法batchInsert()。这个方法将一个表示文档的Array对象数组作为参数，如下所示：

```go
$doc2 = array('name' => 'George');
$doc3 = array('name' => 'Ron');
$result = $myColl->batchInsert([$doc2, $doc3]);
```

请注意，方法insert()返回一个result对象，其中包含有关写入操作的信息。

▼　Try It Yourself

```go
php PHPDocAdd.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   print_r("\nBefore Inserting: \n");
06   showNewDocs($collection);
07   addSelfie($collection);
08   addGoogleAndTweet($collection);
09   function showNewDocs($collection){
10     $query = array('category' => 'New');
11     $cursor = $collection->find($query);
12     foreach ($cursor as $id => $doc){
13       print_r(json_encode($doc)."\n");
14     }
15   }
16   function addSelfie($collection){
17     $selfie = array(
18         'word' => 'selfie', 'first' => 's', 'last' => 'e',
19         'size' => 6, 'category' => 'New',
20         'stats' => array('vowels' => 3, 'consonants' => 3),
21         'letters' => ["s","e","l","f","i"],
22         'charsets' => [
23           array('type' => 'consonants', 'chars' => ["s","l","f"]),
24           array('type' => 'vowels', 'chars' => ["e","i"])]
25     );
26     $options = array('w' => 1, 'j' => true);
27     $results = $collection->insert($selfie, $options);
28     print_r("\nInserting One Results: \n");
29     print_r(json_encode($results)."\n");
30     print_r("After Inserting One: \n");
31     showNewDocs($collection);
32   }
33   function addGoogleAndTweet($collection){
34     $google = array(
35         'word' => 'google', 'first' => 'g', 'last' => 'e',
36         'size' => 6, 'category' => 'New',
37         'stats' => array('vowels' => 3, 'consonants' => 3),
38         'letters' => ["g","o","l","e"],
39         'charsets' => [
40           array('type' => 'consonants', 'chars' => ["g","l"]),
41           array('type' => 'vowels', 'chars' => ["o","e"])]
42     );
43     $tweet = array(
44         'word' => 'tweet', 'first' => 't', 'last' => 't',
45         'size' => 5, 'category' => 'New',
46         'stats' => array('vowels' => 2, 'consonants' => 3),
47         'letters' => ["t","w","e"],
48         'charsets' => [
49           array('type' => 'consonants', 'chars' => ["t","w"]),
50           array('type' => 'vowels', 'chars' => ["e"])]
51     );
52     $options = array('w' => 1, 'j' => true);
53     $results =
54         $collection->batchInsert([$google, $tweet], $options);
55     print_r("\nInserting Multiple Results: \n");
56     print_r(json_encode($results)."\n");
57     print_r("After Inserting Multiple: \n");
58     showNewDocs($collection);
59   }
60 ?>
```

```go
Before Inserting:
Inserting One Results:
{"n":0,"connectionId":15,"err":null,"ok":1}
After Inserting One:
{ "_id":{"$id":"52e944b8828594f041000029"},"word":"selfie","first":"s",  
"last":"e",
  "size":6,"category":"New","stats":{"vowels":3,"consonants":3},
  "letters":["s","e","l","f","i"],
  "charsets":[{"type":"consonants","chars":["s","l","f"]},
                {"type":"vowels","chars":["e","i"]}]}
Inserting Multiple Results:
{"n":0,"connectionId":15,"err":null,"ok":1}
After Inserting Multiple:
{ "_id":{"$id":"52e944b8828594f04100002b"},"word":"tweet","first":"t",  
"last":"t",
  "size":5,"category":"New","stats":{"vowels":2,"consonants":3},  
"letters":["t","w",
  "e"],
  "charsets":[{"type":"consonants","chars":["t","w"]},
                {"type":"vowels","chars":["e"]}]}
{ "_id":{"$id":"52e944b8828594f041000029"},"word":"selfie","first":"s",  
"last":"e",
  "size":6,"category":"New","stats":{"vowels":3,"consonants":3},
  "letters":["s","e","l","f","i"],
  "charsets":[{"type":"consonants","chars":["s","l","f"]},
                {"type":"vowels","chars":["e","i"]}]}
{ "_id":{"$id":"52e944b8828594f04100002a"},"word":"google","first":"g",  
"last":"e",
  "size":6,"category":"New","stats":{"vowels":3,"consonants":3},
  "letters":["g","o","l","e"],
  "charsets":[{"type":"consonants","chars":["g","l"]},
                {"type":"vowels","chars":["o","e"]}]}
```

