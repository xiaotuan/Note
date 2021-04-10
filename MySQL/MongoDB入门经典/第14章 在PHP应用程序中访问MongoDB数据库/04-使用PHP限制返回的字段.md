### 14.1.2　使用PHP限制返回的字段

> **在方法find()中使用参数fields来减少MongoCursor对象表示的文档中的字段数**
> 在本节中，您将编写一个简单的PHP应用程序，它在方法find()中使用参数fields来限制返回的字段。通过这个示例，您将熟悉如何使用方法find()的参数fields，并了解它对结果的影响。程序清单14.3显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，并调用其他的方法来查找文档并显示其指定的字段。方法displayCursor()迭代游标并显示找到的文档。
> 方法includeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，使其只返回指定的字段；方法excludeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，以排除指定的字段。
> 请执行如下步骤，创建并运行这个PHP应用程序，它在示例数据集中查找文档，限制返回的字段并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour14中新建一个文件，并将其命名为PHPFindFields.php。
> 4．在这个文件中输入程序清单14.3所示的代码。这些代码在调用方法find()时传递了参数fields。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour14。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单14.4显示了这个应用程序的输出。
> **程序清单14.3　PHPFindFields.php：在PHP应用程序中限制从集合返回的文档包含的字段**
> **程序清单14.4　PHPFindFields.php-output：在PHP应用程序中限制从集合返回的文档包含的字段的输出**
> ▲

为限制文档检索时返回的数据量，另一种极有效的方式是限制要返回的字段。文档可能有很多字段在有些情况下很有用，但在其他情况下没用。从MongoDB服务器检索文档时，需考虑应包含哪些字段，并只请求必要的字段。

要对MongoCollection对象的方法find()从服务器返回的字段进行限制，可使用参数fields。这个参数是一个Array对象，它使用值true来包含字段，使用值false来排除字段。

例如，要在返回文档时排除字段stats、value和comments，可使用下面的fields参数：

```go
$fields = array('stats' => false, 'value' => false, 'comments' => false);
$cursor = $myColl->find(null, $fields);
```

这里将查询对象指定成了null，因为您要查找所有的文档。

仅包含所需的字段通常更容易。例如，如果只想返回first字段为t的文档的word和size字段，可使用下面的代码：

```go
$query = array('first' => 't');
$fields = array('word' => true, 'size' => true);
$cursor = $myColl->find($query, $fields);
```

▼　Try It Yourself

```go
php PHPFindFields.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   excludeFields($collection, []);
06   includeFields($collection, ["word", "size"]);
07   includeFields($collection, ["word", "letters"]);
08   excludeFields($collection, ["chars", "letter", "charsets"]);
09   function displayCursor($doc){
10     print_r(json_encode($doc)."\n");
11   }
12   function includeFields($collection, $fields){
13     $query = array('first' => 'p');
14     $fieldObj = array();
15     foreach ($fields as $id => $field){
16       $fieldObj[$field] = true;
17     }
18     $word = $collection->findOne($query, $fieldObj);
19     print_r("\nIncluding ".json_encode($fields)." fields: \n");
20     displayCursor($word);
21   }
22   function excludeFields($collection, $fields){
23     $query = array('first' => 'p');
24     $fieldObj = array();
25     foreach ($fields as $id => $field){
26       $fieldObj[$field] = false;
27     }
28     $doc = $collection->findOne($query, $fieldObj);
29     print_r("\nExcluding ".json_encode($fields)." fields: \n");
30     displayCursor($doc);
31   }
32 ?>
```

```go
Excluding [] fields:
{ "_id":{"$id":"52e89477c25e849855325fa7"},"word":"people","first":"p","last":"e",
"size":6,"letters":["p","e","o","l"],"stats":{"vowels":3,"consonants":3},
  "charsets":[{"type":"consonants","chars":["p","l"]},
                {"type":"vowels","chars":["e","o"]}]}
Including ["word","size"] fields:
{ "_id":{"$id":"52e89477c25e849855325fa7"},"word":"people","size":6}
Including ["word","letters"] fields:
{ "_id":{"$id":"52e89477c25e849855325fa7"},"word":"people","letters":["p","e","o",
"l"]}
Excluding ["chars","letter","charsets"] fields:
{ "_id":{"$id":"52e89477c25e849855325fa7"},"word":"people","first":"p","last":"e",
"size":6,"letters":["p","e","o","l"],"stats":{"vowels":3,"consonants":3}}
```

