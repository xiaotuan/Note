### 14.2　使用PHP查找不同的字段值

> **使用PHP检索一组文档中指定字段的不同值**
> 在本节中，您将编写一个PHP应用程序，它使用MongoCollection对象的方法distinct() 来检索示例数据库中不同的字段值。通过这个示例，您将熟练地生成数据集中的不同字段值列表。程序清单14.7显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他的方法来找出并显示不同的字段值。
> 方法sizesOfAllWords()找出并显示所有单词的各种长度；方法sizesOfQWords()找出并显示以q打头的单词的各种长度；方法firstLetterOfLongWords()找出并显示长度超过12的单词的各种长度。
> 请执行下面的步骤，创建并运行这个PHP应用程序，它找出示例数据集中文档集的不同字段值，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour14中新建一个文件，并将其命名为PHPFindDistinct.php。
> 4．在这个文件中输入程序清单14.7所示的代码。这些代码对文档集执行distinct()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour14。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单14.8显示了这个应用程序的输出。
> **程序清单14.7　PHPFindDistinct.php：在PHP应用程序中找出文档集中不同的字段值**
> **程序清单14.8　PHPFindDistinct.php-output：在PHP应用程序中找出文档集中不同字段值的输出**
> ▲

一种很有用的MongoDB集合查询是，获取一组文档中某个字段的不同值列表。不同（distinct）意味着纵然有数千个文档，您只想知道那些独一无二的值。

MongoCollection对象的方法distinct()让您能够找出指定字段的不同值列表，这个方法的语法如下：

```go
distinct(key, [query])
```

其中参数key是一个字符串，指定了要获取哪个字段的不同值。要获取子文档中字段的不同值，可使用句点语法，如stats.count。参数query是一个包含标准查询选项的对象，指定了要从哪些文档中获取不同的字段值。

例如，假设有一些包含字段first、last和age的用户文档，要获取年龄超过65岁的用户的不同姓，可使用下面的操作：

```go
$query = array('age' =>
     array('$gt' => 65));
$lastNames = $myCollection.distinct('last', $query);
```

方法distinct()返回一个数组，其中包含指定字段的不同值，例如：

```go
["Smith", "Jones", ...]
```

▼　Try It Yourself

```go
php PHPFindDistinct.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   sizesOfAllWords($collection);
06   sizesOfQWords($collection);
07   firstLetterOfLongWords($collection);
08   function sizesOfAllWords($collection){
09     $results = $collection->distinct("size");
10     print_r("\nDistinct Sizes of words: \n");
11     print_r(json_encode($results)."\n");
12   }
13   function sizesOfQWords($collection){
14     $query = array('first' => 'q');
15     $results = $collection->distinct("size", $query);
16     print_r("\nDistinct Sizes of words starting with Q: \n");
17     print_r(json_encode($results)."\n");
18   }
19   function firstLetterOfLongWords($collection){
20     $query = array('size' => array('$gt' => 12));
21     $results = $collection->distinct("first", $query);
22     print_r("\nDistinct first letters of words longer than".
23               " 12 characters: \n");
24     print_r(json_encode($results)."\n");
25   }
26 ?>
```

```go
Distinct Sizes of words:
[3,2,1,4,5,9,6,7,8,10,11,12,13,14]
Distinct Sizes of words starting with Q:
[8,5,7,4]
Distinct first letters of words longer than 12 characters:
["i","a","e","r","c","u","s","p","t"]
```

