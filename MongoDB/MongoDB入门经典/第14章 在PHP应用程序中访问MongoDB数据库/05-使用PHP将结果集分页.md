### 14.1.3　使用PHP将结果集分页

> **在PHP中使用skip()和limit()对MongoDB集合中的文档进行分页**
> 在本节中，您将编写一个简单的PHP应用程序，它使用MongoCursor对象的方法skip()和limit()方法对find()返回的大量文档进行分页。通过这个示例，您将熟悉如何使用skip()和limit()对较大的数据集进行分页。程序清单14.5显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他的方法来查找文档并以分页方式显示它们。方法displayCursor()迭代游标并显示当前页中的单词。
> 方法pageResults()接受一个skip参数，并根据它以分页方式显示以w开头的所有单词。每显示一页后，都将skip值递增，直到到达游标末尾。
> 请执行下面的步骤，创建并运行这个对示例数据集中的文档进行分页并显示结果的PHP应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour14中新建一个文件，并将其命名为PHPFindPaging.php。
> 4．在这个文件中输入程序清单14.5所示的代码。这些代码实现了文档集分页。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour14。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单14.6显示了这个应用程序的输出。
> **程序清单14.5　PHPFindPaging.php：在PHP应用程序中分页显示集合中的文档集**
> **程序清单14.6　PHPFindPaging.php-output：在PHP应用程序中分页显示集合中的文档集的输出**
> ▲

为减少返回的文档数，一种常见的方法是进行分页。要进行分页，需要指定要在结果集中跳过的文档数，还需限制返回的文档数。跳过的文档数将不断增加，每次的增量都是前一次返回的文档数。

要对一组文档进行分页，需要使用MongoCursor对象的方法limit()和skip()。方法skip()让您能够指定在返回文档前要跳过多少个文档。

每次获取下一组文档时，都增大方法skip()中指定的值，增量为前一次调用limit()时指定的值，这样就实现了数据集分页。

例如，下面的语句查找第11～20个文档：

```go
$cursor = $collection->find();
$cursor->limit(10);
$cursor->skip(10);
```

进行分页时，务必调用方法sort()来确保文档的排列顺序不变。

**▼** 　Try It Yourself

```go
php PHPFindPaging.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   pageResults($collection, 0);
06   function displayCursor($cursor){
07     $words = "";
08     foreach ($cursor as $id => $doc){
09       $words .= $doc["word"].",";
10     }
11     if (strlen($words) > 65){
12       $words = substr($words, 0, 65)."...";
13     }
14     print_r($words);
15   }
16   function pageResults($collection, $skip){
17     $query = array('first' => 'w');
18     $cursor = $collection->find($query);
19     $cursor->limit(10);
20     $cursor->skip($skip);
21     print_r("\nPage ".($skip+1)." to ");
22     print_r(($skip+$cursor->count(true)).": \n");
23     displayCursor($cursor);
24     if($cursor->count(true) == 10){
25       pageResults($collection, $skip+10);
26     }
27   }
28 ?>
```

```go
Page 1 to 10:
with,won't,we,what,who,would,will,when,which,want,
Page 11 to 20:
way,well,woman,work,world,while,why,where,week,without,
Page 21 to 30:
water,write,word,white,whether,watch,war,within,walk,win,
Page 31 to 40:
wait,wife,whole,wear,whose,wall,worker,window,wrong,west,
Page 41 to 50:
whatever,wonder,weapon,wide,weight,worry,writer,whom,wish,western...
Page 51 to 60:
wind,weekend,wood,winter,willing,wild,worth,warm,wave,wonderful,
Page 61 to 70:
wine,writing,welcome,weather,works,wake,warn,wing,winner,welfare,
Page 71 to 80:
witness,waste,wheel,weak,wrap,warning,wash,widely,wedding,wheneve...
Page 81 to 90:
wire,whisper,wet,weigh,wooden,wealth,wage,wipe,whereas,withdraw,
Page 91 to 93:
working,wisdom,wealthy,
```

