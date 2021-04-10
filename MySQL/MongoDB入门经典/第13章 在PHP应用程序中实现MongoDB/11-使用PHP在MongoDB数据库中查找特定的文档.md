### 13.2.2　使用PHP在MongoDB数据库中查找特定的文档

> **使用PHP从MongoDB数据库检索特定的文档**
> 在本节中，您将编写一个简单的PHP应用程序，它使用查询对象和方法find()从示例数据库检索一组特定的文档。通过这个示例，您将熟悉如何创建查询对象以及如何使用它们来显示数据库请求返回的文档。程序清单13.4显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他的方法来查找并显示特定的文档。方法displayCursor()迭代游标并显示它表示的单词。
> 方法over12()查找长度超过12的单词；方法startingABC()查找以a、b或c打头的单词；方法startEndVowels()查找以元音字母打头和结尾的单词；方法over6Vowels()查找包含的元音字母超过6个的单词；方法nonAlphaCharacters()查找包含类型为other的字符集且长度为1的单词。
> 请执行如下步骤，创建并运行这个在示例数据集中查找特定文档并显示结果的PHP应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour13中新建一个文件，并将其命名为PHPFindSpecific.php。
> 4．在这个文件中输入程序清单13.5所示的代码。这些代码使用了方法find()和查询对象。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour13。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单13.6显示了这个应用程序的输出。
> **程序清单13.5　PHPFindSpecific.php：在PHP应用程序中从集合中查找并检索特定文档**
> **程序清单13.6　PHPFindSpecific.php-output：在PHP应用程序中从集合中查找并检索特定文档的输出**
> ▲

一般而言，您不会想从服务器检索集合中的所有文档。方法find()和findOne()让您能够向服务器发送一个查询对象，从而像在MongoDB shell中那样限制文档。

要创建查询对象，可使用本章前面描述的Array对象。对于查询对象中为子对象的字段，可创建Array子对象；对于其他类型（如整型、字符串和数组）的字段，可使用相应的PHP类型。

例如，要创建一个查询对象来查找size=5的单词，可使用下面的代码：

```go
$query = array('size' => 5);
$myColl->find($query);
```

要创建一个查询对象来查找size>5的单词，可使用下面的代码：

```go
$query = array('size' =>
     array('$gt' => 5));
$myColl->find($query);
```

要创建一个查询对象来查找第一个字母为x、y或z的单词，可使用String数组，如下所示：

```go
$query = array('first' =>
     array('$in' => ["x", "y", "z"]));
$myColl->find($query);
```

利用上述技巧可创建需要的任何查询对象：不仅能为查找操作创建查询对象，还能为其他需要查询对象的操作这样做。

▼　Try It Yourself

```go
php PHPFindSpecific.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   over12($collection);
06   startingABC($collection);
07   startEndVowels($collection);
08   over6Vowels($collection);
09   nonAlphaCharacters($collection);
10   function displayCursor($cursor){
11     $words = "";
12     foreach ($cursor as $id => $doc){
13       $words .= $doc["word"].",";
14     }
15     if (strlen($words) > 65){
16       $words = substr($words, 0, 65)."...";
17     }
18     print_r($words);
19   }
20   function over12($collection){
21     print_r("\n\nWords with more than 12 characters: \n");
22     $query = array('size' => array('$gt' => 12));
23     $cursor = $collection->find($query);
24     displayCursor($cursor);
25   }
26   function startingABC($collection){
27     print_r("\n\nWords starting with A, B or C: \n");
28     $query = array('first' => array('$in' => ["a","b","c"]));
29     $cursor = $collection->find($query);
30     displayCursor($cursor);
31   }
32   function startEndVowels($collection){
33     print_r("\n\nWords starting and ending with a vowel: \n");
34     $query = array('$and' => [
35          array('first' => array('$in' => ["a","e","i","o","u"])),
36          array('last' => array('$in' => ["a","e","i","o","u"]))]);
37     $cursor = $collection->find($query);
38     displayCursor($cursor);
39   }
40   function over6Vowels($collection){
41     print_r("\n\nWords with more than 5 vowels: \n");
42     $query = array('stats.vowels' => array('$gt' => 5));
43     $cursor = $collection->find($query);
44     displayCursor($cursor);
45   }
46   function nonAlphaCharacters($collection){
47     print_r("\n\nWords with 1 non-alphabet characters: \n");
48     $query = array('charsets' =>
49          array('$elemMatch' =>
50             array('$and' => [
51               array('type' => 'other'),
52               array('chars' => array('$size' => 1))])));
53     $cursor = $collection->find($query);
54     displayCursor($cursor);
55   }
56 ?>
```

```go
Words with more than 12 characters:
international,administration,environmental,responsibility,investi...
Words starting with A, B or C:
be,and,a,can't,at,but,by,as,can,all,about,come,could,also,because...
Words starting and ending with a vowel:
a,i,one,into,also,use,area,eye,issue,include,once,idea,ago,office...
Words with more than 5 vowels:
international,organization,administration,investigation,communica...
Words with 1 non-alphabet characters:
don't,won't,can't,shouldn't,e-mail,long-term,so-called,mm-hmm,
```

