### 14.4　从PHP应用程序发出请求时使用聚合来操作数据

> **在PHP应用程序中使用聚合来生成数据**
> 在本节中，您将编写一个简单的PHP应用程序，它使用MongoCollection对象的方法aggregate()从示例数据库检索各种聚合数据。通过这个示例，您将熟悉如何使用aggregate()来利用聚合流水线在MongoDB服务器上处理数据，再返回结果。程序清单14.11显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他方法来聚合数据并显示结果。方法displayAggregate()显示聚合结果。
> 方法largeSmallVowels()使用了一条包含运算符$match、$group和$sort的聚合流水线，这条流水线查找以元音字母开头的单词，根据第一个字母将这些单词分组，并找出各组中最长和最短单词的长度。
> 方法top5AverageWordFirst()使用了一条包含运算符$group、$sort和$limit的聚合流水线，这条流水线根据第一个字母将单词分组，并找出单词平均长度最长的前5组。
> 请执行下面的步骤，创建并运行这个PHP应用程序，它使用聚合流水线来处理示例数据集中的文档，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour14中新建一个文件，并将其命名为PHPAggregate.php。
> 4．在这个文件中输入程序清单14.11所示的代码。这些代码对文档集执行aggregate()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour14。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单14.12显示了这个应用程序的输出。
> **程序清单14.11　PHPAggregate.php：在PHP应用程序中使用聚合流水线生成数据集**
> **程序清单14.12　PHPAggregate.php-output：在PHP应用程序中使用聚合流水线生成数据集的输出**
> ▲

在PHP应用程序中使用MongoDB时，另一个很有用的工具是聚合框架。MongoCollection对象提供了对数据执行聚合操作的方法aggregate()，这个方法的语法如下：

```go
aggregate(operator, [operator, ...])
```

参数operator是一系列运算符对象，提供了用于聚合数据的流水线。这些运算符对象是使用聚合运算符创建的Array对象。聚合运算符在第9章介绍过，您现在应该熟悉它们。

例如，下面的代码定义了运算符$group和$limit，其中运算符$group根据字段word进行分组（并将该字段的值存储在结果文档的_id字段中），使用$avg计算size字段的平均值（并将结果存储在average字段中）。请注意，在聚合运算中引用原始文档的字段时，必须在字段名前加上$：

```go
$group = array('$group' =>
              array('_id' => '$word',
                     'average' => array('$avg' => '$size')));
$limit = array('$limit' => 10);
$result = $collection->aggregate($group, $limit);
```

方法aggregate()返回一个Array对象，其中的元素result包含聚合结果。元素result是一个聚合结果列表。为演示这一点，下面的代码逐项显示聚合结果的内容：

```go
foreach($result['result'] as $idx => $item){
    print_r(json_encode($item)."\n");
}
```

▼　Try It Yourself

```go
php PHPAggregate.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   largeSmallVowels($collection);
06   top5AverageWordFirst($collection);
07   function displayAggregate($result){
08     foreach($result['result'] as $idx => $item){
09       print_r(json_encode($item)."\n");
10     }
11   }
12   function largeSmallVowels($collection){
13     $match = array('$match' =>
14                   array('first' =>
15                      array('$in' => ['a','e','i','o','u'])));
16     $group = array('$group' =>
17                   array('_id' => '$first',
18                          'largest' => array('$max' => '$size'),
19                          'smallest' => array('$min' => '$size'),
20                          'total' => array('$sum' => 1)));
21     $sort = array('$sort' => array('first' => 1));
22     $result = $collection->aggregate($match, $group, $sort);
23     print_r("\nLargest and smallest word sizes for ".
24               "words beginning with a vowel:\n");
25     displayAggregate($result);
26   }
27   function top5AverageWordFirst($collection){
28     $group = array('$group' =>
29                  array('_id' => '$first',
30                         'average' => array('$avg' => '$size')));
31     $sort = array('$sort' => array('average' => -1));
32     $limit = array('$limit' => 5);
33     $result = $collection->aggregate($group, $sort, $limit);
34     print_r("\nFirst letter of top 5 largest average ".
35               "word size:\n");
36     displayAggregate($result);
37   }
38 ?>
```

```go
Largest and smallest word sizes for words beginning with a vowel:
{"_id":"e","largest":13,"smallest":3,"total":150}
{"_id":"u","largest":13,"smallest":2,"total":33}
{"_id":"i","largest":14,"smallest":1,"total":114}
{"_id":"o","largest":12,"smallest":2,"total":72}
{"_id":"a","largest":14,"smallest":1,"total":192}
First letter of top 5 largest average word size:
{"_id":"i","average":7.9473684210526}
{"_id":"e","average":7.42}
{"_id":"c","average":7.2921348314607}
{"_id":"p","average":6.8818181818182}
{"_id":"r","average":6.7671232876712}
```

