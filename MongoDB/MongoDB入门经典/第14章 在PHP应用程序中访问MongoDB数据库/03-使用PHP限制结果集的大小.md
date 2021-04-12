### 14.1.1　使用PHP限制结果集的大小

> **使用limit ()将PHP对象MongoCursor表示的文档减少到指定的数量**
> 在本节中，您将编写一个简单的PHP应用程序，它使用limit()来限制find()操作返回的结果。通过这个示例，您将熟悉如何结合使用limit()和find()，并了解limit()对结果的影响。程序清单14.1显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他方法来查找并显示数量有限的文档。方法displayCursor()迭代游标并显示找到的单词。
> 方法limitResults()接受一个limit参数，查找以p打头的单词，并返回参数limit指定的单词数。
> 请执行如下步骤，创建并运行这个PHP应用程序，它在示例数据集中查找指定数量的文档并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour14中新建一个文件，并将其命名为PHPFindLimit.php。
> 4．在这个文件中输入程序清单14.1所示的代码。这些代码使用了方法find()和limit()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour14。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单14.2显示了这个应用程序的输出。
> **程序清单14.1　PHPFindLimit.php：在PHP应用程序中在集合中查找指定数量的文档**
> **程序清单14.2　PHPFindLimit.php-output：在PHP应用程序中在集合中查找指定数量文档的输出**
> ▲

要限制find()或其他查询请求返回的数据量，最简单的方法是对find()操作返回的MongoCursor对象调用方法limit()，它让MongoCursor对象返回指定数量的文档，可避免检索的对象量超过应用程序的处理能力。

例如，下面的代码只显示集合中的前10个文档，即便匹配的文档有数千个：

```go
$cursor = $wordsColl->find();
$cursor->limit(10);
while($cursor->hasNext()){
  $word = cursor->getNext();
  print_r($word);
}
```

▼　Try It Yourself

```go
php PHPFindLimit.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   limitResults($collection, 1);
06   limitResults($collection, 3);
07   limitResults($collection, 5);
08   limitResults($collection, 7);
09   function displayCursor($cursor){
10     $words = "";
11     foreach ($cursor as $id => $doc){
12       $words .= $doc["word"].",";
13     }
14     if (strlen($words) > 65){
15       $words = substr($words, 0, 65)."...";
16     }
17     print_r($words);
18   }
19   function limitResults($collection, $limit){
20     $query = array('first' => 'p');
21     $cursor = $collection->find($query);
22     $cursor->limit($limit);
23     print_r("\n\nP words Limited to ".$limit." :\n");
24     displayCursor($cursor);
25   }
26 ?>
```

```go
P words Limited to 1 :
people,
P words Limited to 3 :
people,put,problem,
P words Limited to 5 :
people,put,problem,part,place,
P words Limited to 7 :
people,put,problem,part,place,program,play,
```

