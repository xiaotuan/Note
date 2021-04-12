### 13.3　使用PHP计算文档数

> **在PHP应用程序中使用count ()获取MongoCursor对象表示的文档数**
> 在本节中，您将编写一个简单的PHP应用程序，它使用查询对象和find()从示例数据库检索特定的文档集，再使用count()来获取游标表示的文档数。通过这个示例，您将熟悉如何在检索并处理文档前获取文档数。程序清单13.7显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，再调用其他的方法来查找特定的文档并显示找到的文档数。方法countWords()使用查询对象、find()和count()来计算数据库中的单词总数以及以a打头的单词数。
> 请执行如下步骤，创建并运行这个PHP应用程序，它查找示例数据集中的特定文档，计算找到的文档数并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour13中新建一个文件，并将其命名为PHPFindCount.php。
> 4．在这个文件中输入程序清单13.7所示的代码。这些代码使用方法find()和查询对象查找特定文档，并计算找到的文档数。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour13。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单13.8显示了这个应用程序的输出。
> **程序清单13.7　PHPFindCount.php：在PHP应用程序中计算在集合中找到的特定文档的数量**
> **程序清单13.8　PHPFindCount.php-output：在PHP应用程序中计算在集合中找到的特定文档数量的输出**
> ▲

使用PHP访问MongoDB数据库中的文档集时，您可能想先确定文档数，再决定是否检索它们。无论是在MongoDB服务器还是客户端，计算文档数的开销都很小，因为不需要传输实际文档。

MongoCursor对象的方法count()让您能够获取游标表示的文档数。例如，下面的代码使用方法find()来获取一个MongoCursor对象，再使用方法count()来获取文档数：

```go
$cursor = $wordsColl->find();
$itemCount = $cursor->count();
```

$itemCount的值为与find()操作匹配的单词数。

▼　Try It Yourself

```go
php PHPFindCount.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   countWords($collection);
06   function countWords($collection){
07     $cursor = $collection->find();
08     print_r("Total words in the collection: \n");
09     print_r($cursor->count());
10     $query = array('first' => 'a');
11     $cursor = $collection->find($query);
12     print_r("\n\nTotal words starting with A: \n");
13     print_r($cursor->count());
14   }
15 ?>
```

```go
Total words in the collection:
2673
Total words starting with A:
192
```

