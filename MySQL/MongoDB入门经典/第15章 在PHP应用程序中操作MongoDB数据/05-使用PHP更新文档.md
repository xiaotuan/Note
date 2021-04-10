### 15.4　使用PHP更新文档

> **使用PHP更新集合中的文档**
> 在本节中，您将编写一个简单的PHP应用程序，它使用MongoCollection对象的方法update()来更新示例数据库的一个集合中的既有文档。通过这个示例，您将熟悉如何在PHP中使用MongoDB更新运算符来更新文档。程序清单15.7显示了这个示例的代码。
> 在这个示例中，主脚本连接到MongoDB数据库，获取一个MongoCollection对象，再调用其他方法更新文档。方法showWord()显示更新前和更新后的文档。
> 方法updateDoc()创建一个查询对象，它从数据库获取表示单词left的文档；再创建一个更新对象，它将字段word的值改为lefty，将字段size和stats.consonants的值加1，并将字母y压入到数组字段letters中。方法resetDoc()将文档恢复原样，以演示如何将字段值减1以及如何从数组字段中弹出值。
> 请执行下面的步骤，创建并运行这个更新示例数据库中文档并显示结果的PHP应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了PHP MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour15中新建一个文件，并将其命名为PHPDocUpdate.php。
> 4．在这个文件中输入程序清单15.7所示的代码。这些代码使用update()来更新文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour15。
> 7．执行下面的命令来运行这个PHP应用程序。程序清单15.8显示了这个应用程序的输出。
> **程序清单15.7　PHPDocUpdate.php：在PHP应用程序中更新集合中的文档**
> **程序清单15.8　PHPDocUpdate.php-output：在PHP应用程序中更新集合中文档的输出**
> ▲

将文档插入集合后，经常需要使用PHP根据数据变化更新它们。MongoCollection对象的方法update()让您能够更新集合中的文档，它多才多艺，但使用起来非常容易。下面是方法update()的语法：

```go
update(query, update, [options])
```

参数query是一个Array对象，指定了要修改哪些文档。请求将判断query指定的属性和值是否与文档的字段和值匹配，进而更新匹配的文档。参数update是一个Array对象，指定了要如何修改与查询匹配的文档。第8章介绍了可在这个对象中使用的更新运算符。

参数options是一个Array对象，指定了更新操作选项。对于update()请求，可在这个参数中设置upsert和multiple字段。如果将字段upsert设置为true，则没有文档与查询匹配时，将插入一个新文档。如果将字段multiple设置为true，将更新所有与查询匹配的文档；如果为false，将只更新与查询匹配的第一个文档。

例如，对于集合中字段category为new的文档，下面的代码将其字段category改为old。在这里，upsert被设置为false，因此即便没有字段category为new的文档，也不会插入新文档；而multiple被设置为true，因此将更新所有匹配的文档：

```go
$query = array('category' => 'New');
$update = array('$set' =>
     array('category' => 'Old'));
$options = array('upsert' => false, 'multiple' => true);
$myColl->update($query, $update, $options);
```

▼　Try It Yourself

```go
php PHPDocUpdate.php
```

```go
01 <?php
02   $mongo = new MongoClient("");
03   $db = $mongo->words;
04   $collection = $db->word_stats;
05   print_r("\nBefore Updating: \n");
06   showWord($collection);
07   updateDoc($collection);
08   resetDoc($collection);
09   function showWord($collection){
10     $query = array('word' => array('$in' => ['left', 'lefty']));
11     $cursor = $collection->find($query);
12     foreach ($cursor as $id => $doc){
13       print_r(json_encode($doc)."\n");
14     }
15   }
16   function updateDoc($collection){
17     $query = array('word' => "left");
18     $update = array(
19           '$set' => array('word' => 'lefty'),
20           '$inc' => array('size' => 1, 'stats.consonants' => 1),
21           '$push' => array('letters' => 'y'));
22     $options = array('w' => 1, 'j' => true,
23                         'upsert' => false, 'multiple' => false);
24     $results = $collection->update($query, $update, $options);
25     print_r("\nUpdate Doc Result: \n");
26     print_r(json_encode($results)."\n");
27     print_r("\nAfter Updating Doc: \n");
28     showWord($collection);
29   }
30   function resetDoc($collection){
31     $query = array('word' => "lefty");
32     $update = array(
33           '$set' => array('word' => 'left'),
34           '$inc' => array('size' => -1, 'stats.consonants' => -1),
35           '$pop' => array('letters' => 1));
36     $options = array('w' => 1, 'j' => true, 'upsert' => false,
37                         'multiple' => false);
38     $results = $collection->update($query, $update, $options);
39     print_r("\nReset Doc Result: \n");
40     print_r(json_encode($results)."\n");
41     print_r("\nAfter Resetting Doc: \n");
42     showWord($collection);
43   }
44 ?>
```

```go
Before Updating:
{ "_id":{"$id":"52e89477c25e84985532622e"},
  "charsets":[{"type":"consonants","chars":["l","f","t"]},
                {"type":"vowels","chars":["e"]}],
  "first":"l","last":"t","letters":["l","e","f","t"],"size":4,
  "stats":{"consonants":3,"vowels":1},"word":"left"}
Update Doc Result:
{"updatedExisting":true,"n":1,"connectionId":20,"err":null,"ok":1}
After Updating Doc:
{ "_id":{"$id":"52e89477c25e84985532622e"},
  "charsets":[{"type":"consonants","chars":["l","f","t"]},
                {"type":"vowels","chars":["e"]}],
  "first":"l","last":"t","letters":["l","e","f","t","y"],"size":5,
  "stats":{"consonants":4,"vowels":1},"word":"lefty"}
Reset Doc Result:
{"updatedExisting":true,"n":1,"connectionId":20,"err":null,"ok":1}
After Resetting Doc:
{ "_id":{"$id":"52e89477c25e84985532622e"},
  "charsets":[{"type":"consonants","chars":["l","f","t"]},
                {"type":"vowels","chars":["e"]}],
  "first":"l","last":"t","letters":["l","e","f","t"],"size":4,
  "stats":{"consonants":3,"vowels":1},"word":"left"}
```

