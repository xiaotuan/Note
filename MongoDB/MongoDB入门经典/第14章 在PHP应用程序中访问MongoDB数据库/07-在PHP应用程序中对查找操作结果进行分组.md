### 14.3　在PHP应用程序中对查找操作结果进行分组

> **使用PHP根据键值将文档分组**
> 在本节中，您将创建一个简单的PHP应用程序，它使用MongoCollection对象的方法group()从示例数据库检索文档，根据指定字段进行分组，并在服务器上执行reduce和finalize函数。通过这个示例，您将熟悉如何使用group()在服务器端对数据集进行处理，以生成分组数据。程序清单14.9显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他的方法来查找文档、进行分组并显示结果。方法displayGroup()显示分组结果。
> 方法firstIsALastIsVowel()将第一个字母为a且最后一个字母为元音字母的单词分组，其中的reduce函数计算单词数，以确定每组的单词数。
> 方法firstLetterTotals()根据第一个字母分组，并计算各组中所有单词的元音字母总数和辅音字母总数。在其中的finalize函数中，将元音字母总数和辅音字母总数相加，以提供各组单词的字符总数。
> 请执行下面的步骤，创建并运行这个PHP应用程序，它对示例数据集中的文档进行分组和处理，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour14中新建一个文件，并将其命名为PHPGroup.php。
> 4．在这个文件中输入程序清单14.9所示的代码。这些代码对文档集执行group()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour14。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单14.10显示了这个应用程序的输出。
> **程序清单14.9　PHPGroup.php：在PHP应用程序中根据字段值对单词分组以生成不同的数据**
> **程序清单14.10　PHPGroup.php-output：在PHP应用程序中根据字段值对单词分组以生成不同数据的输出**
> ▲

在PHP中对大型数据集执行操作时，根据文档的一个或多个字段的值将结果分组通常很有用。这也可以在取回文档后使用代码来完成，但让MongoDB服务器在原本就要迭代文档的请求中这样做，效率要高得多。

在PHP中，要将查询结果分组，可使用MongoCollection对象的方法group()。分组请求首先收集所有与查询匹配的文档，再对于指定键的每个不同值，都在数组中添加一个分组对象，对这些分组对象执行操作，并返回这个分组对象数组。

方法group()的语法如下：

```go
group({key, cond , initial, reduce, [finalize]})
```

其中参数key、cond和initial都是Array对象，指定了要用来分组的字段、查询以及要使用的初始文档；参数reduce和finalize为String对象，包含以字符串方式表示的JavaScript函数，这些函数将在服务器上运行以归并文档并生成最终结果。有关这些参数的更详细信息，请参阅第9章。

为演示这个方法，下面的代码实现了简单分组，它创建了对象key、cond和initial，并以字符串的方式传入了一个reduce函数：

```go
$key = array('first' => true);
$cond = array('last' => 'a', 'size' => 5);
$initial = array('count' => 0);
$reduce = "function (obj, prev) { prev.count++; }";
$options = array('condition' => $cond);
$results = $collection->group($key, $initial, $reduce, $options);
```

方法group()返回一个Array对象，其中的元素retval包含分组结果。元素retval是一个聚合结果列表，下面的代码逐项地显示了分组结果的内容：

```go
foreach($results['retval'] as $idx => $result){
    print_r(json_encode($result)."\n");
}
```

▼　Try It Yourself

```go
php PHPGroup.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   firstIsALastIsVowel($collection);
06   firstLetterTotals($collection);
07   function displayGroup($results){
08     foreach($results['retval'] as $idx => $result){
09       print_r(json_encode($result)."\n");
10     }
11   }
12   function firstIsALastIsVowel($collection){
13     $key = array('first' => true, "last" => true);
14     $cond = array('first' => 'a', 'last' =>
15                        array('$in' => ["a","e","i","o","u"]));
16     $initial = array('count' => 0);
17     $reduce = "function (obj, prev) { prev.count++; }";
18     $options = array('condition' => $cond);
19     $results = $collection->group($key, $initial, $reduce, $options);
20     print_r("\n\n'A' words grouped by first and last".
21               " letter that end with a vowel:\n");
22     displayGroup($results);
23   }
24   function firstLetterTotals($collection){
25     $key = array('first' => true);
26     $cond = array();
27     $initial = array('vowels' => 0, 'cons' => 0);
28     $reduce = "function (obj, prev) { " .
29                    "prev.vowels += obj.stats.vowels; " .
30                    "prev.cons += obj.stats.consonants; " .
31                 "}";
32     $finalize = "function (obj) { " .
33                       "obj.total = obj.vowels + obj.cons; " .
34                   "}";
35     $options = array('condition' => $cond,
36                         'finalize' => $finalize);
37     $results = $collection->group($key, $initial, $reduce, $options);
38     print_r("\n\nWords grouped by first letter ".
39               "with totals:\n");
40     displayGroup($results);
41   }
42 ?>
```

```go
'A' words grouped by first and last letter that end with a vowel:
{"first":"a","last":"a","count":3}
{"first":"a","last":"o","count":2}
{"first":"a","last":"e","count":52}
Words grouped by first letter with totals:
{"first":"t","vowels":333,"cons":614,"total":947}
{"first":"b","vowels":246,"cons":444,"total":690}
{"first":"a","vowels":545,"cons":725,"total":1270}
{"first":"o","vowels":204,"cons":237,"total":441}
{"first":"i","vowels":384,"cons":522,"total":906}
{"first":"h","vowels":145,"cons":248,"total":393}
{"first":"f","vowels":258,"cons":443,"total":701}
{"first":"y","vowels":26,"cons":41,"total":67}
{"first":"w","vowels":161,"cons":313,"total":474}
{"first":"d","vowels":362,"cons":585,"total":947}
{"first":"c","vowels":713,"cons":1233,"total":1946}
{"first":"s","vowels":640,"cons":1215,"total":1855}
{"first":"n","vowels":136,"cons":208,"total":344}
{"first":"g","vowels":134,"cons":240,"total":374}
{"first":"m","vowels":262,"cons":417,"total":679}
{"first":"k","vowels":22,"cons":48,"total":70}
{"first":"u","vowels":93,"cons":117,"total":210}
{"first":"p","vowels":550,"cons":964,"total":1514}
{"first":"j","vowels":47,"cons":73,"total":120}
{"first":"l","vowels":189,"cons":299,"total":488}
{"first":"v","vowels":117,"cons":143,"total":260}
{"first":"e","vowels":482,"cons":630,"total":1112}
{"first":"r","vowels":414,"cons":574,"total":988}
{"first":"q","vowels":28,"cons":32,"total":60}
{"first":"z","vowels":2,"cons":2,"total":4}
```

