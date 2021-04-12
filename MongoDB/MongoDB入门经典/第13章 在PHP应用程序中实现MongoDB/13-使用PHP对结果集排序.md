### 13.4　使用PHP对结果集排序

> **使用sort()以特定顺序返回PHP对象MongoCursor表示的文档**
> 在本节中，您将编写一个简单的PHP应用程序，它使用查询对象和方法find()从示例数据库检索特定的文档集，再使用方法sort()将游标中的文档按特定顺序排列。通过这个示例，您将熟悉如何在检索并处理文档前对游标表示的文档进行排序。程序清单13.9显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，再调用其他的方法来查找特定的文档，对找到的文档进行排序并显示结果。方法displayCursor()显示排序后的单词列表。
> 方法sortWordsAscending()获取以w打头的单词并将它们按升序排列；方法sortWordsDescending()获取以w打头的单词并将它们按降序排列；方法sortWordsAscAndSize()获取以q打头的单词，并将它们首先按最后一个字母升序排列，再按长度降序排列。
> 执行下面的步骤，创建并运行这个PHP应用程序，它在示例数据集中查找特定的文档，对找到的文档进行排序并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour13中新建一个文件，并将其命名为PHPFindSort.php。
> 4．在这个文件中输入程序清单13.9所示的代码。这些代码对MongoCursor对象表示的文档进行排序。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour13。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单13.10显示了这个应用程序的输出。
> **程序清单13.9　PHPFindSort.php：在PHP应用程序中查找集合中的特定文档并进行排序**
> **程序清单13.10　PHPFindSort.php-output：在PHP应用程序中查找集合中的特定文档并进行排序的输出**
> ▲

从MongoDB数据库检索文档时，一个重要方面是对文档进行排序。只想检索特定数量（如前10个）的文档或要对结果集进行分页时，这特别有帮助。排序选项让您能够指定用于排序的文档字段和方向。

MongoCursor对象的方法sort()让您能够指定要根据哪些字段对游标中的文档进行排序，并按相应的顺序返回文档。方法sort()将一个Array对象作为参数，这个对象将字段名用作属性名，并使用值1（升序）和-1（降序）来指定排序顺序

例如，要按字段name升序排列文档，可使用下面的代码：

```go
$sorter = array('name' => 1);
$cursor = $myCollection->find();
$cursor->sort($sorter);
```

在传递给方法sort()的对象中，可指定多个字段，这样文档将按这些字段排序。还可对同一个游标调用sort()方法多次，从而依次按不同的字段进行排序。例如，要首先按字段name升序排列，再按字段value降序排列，可使用下面的代码：

```go
$sorter = array('name' => 1, 'value' => -1);
$cursor = $myCollection->find();
$cursor->sort(sorter);
```

也可使用下面的代码：

```go
$sorter1 = array('name' => 1);
$sorter2 = array('value' => -1);
$cursor = $myCollection->find();
$cursor = $cursor->sort(sorter1)
$cursor->sort(sorter2);
```

▼　Try It Yourself

```go
php PHPFindSort.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   sortWordsAscending($collection);
06   sortWordsDescending($collection);
07   sortWordsAscAndSize($collection);
08   function displayCursor($cursor){
09     $words = "";
10     foreach ($cursor as $id => $doc){
11       $words .= $doc["word"].",";
12     }
13     if (strlen($words) > 65){
14       $words = substr($words, 0, 65)."...";
15     }
16     print_r($words);
17   }
18   function sortWordsAscending($collection){
19     $query = array('first' => 'w');
20     $cursor = $collection->find($query);
21     $sorter = array('word' => 1);
22     $cursor->sort($sorter);
23     print_r("\n\nW words ordered ascending: \n");
24     displayCursor($cursor);
25   }
26   function sortWordsDescending($collection){
27     $query = array('first' => 'w');
28     $cursor = $collection->find($query);
29     $sorter = array('word' => -1);
30     $cursor->sort($sorter);
31     print_r("\n\nW words ordered descending: \n");
32     displayCursor($cursor);
33   }
34   function sortWordsAscAndSize($collection){
35     $query = array('first' => 'q');
36     $cursor = $collection->find($query);
37     $sorter = array('last' => 1, 'size' => -1);
38     $cursor->sort($sorter);
39     print_r("\n\nQ words ordered first by last letter ");
40     print_r("and then by size: \n");
41     displayCursor($cursor);
42   }
43 ?>
```

```go
W words ordered ascending:
wage,wait,wake,walk,wall,want,war,warm,warn,warning,wash,waste,wa...
W words ordered descending:
wrong,writing,writer,write,wrap,would,worth,worry,world,works,wor...
Q words ordered first by last letter and then by size:
quite,quote,quick,question,quarter,quiet,quit,quickly,quality,qui...
```

