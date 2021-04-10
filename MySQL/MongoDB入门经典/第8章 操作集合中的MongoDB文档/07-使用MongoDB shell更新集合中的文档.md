### 8.6　使用MongoDB shell更新集合中的文档

> **使用MongoDB shell更新集合中的文档**
> 在本节中，您将编写一个简单的MongoDB shell脚本，对示例数据集中的单词文档进行更新。通过这个示例，您将熟悉如何更新单个和多个与查询匹配的文档。程序清单8.3显示了这个示例的代码。
> 这个示例给以q打头且以y结束的单词添加字段category，再将单词left改为lefty，让您明白如何运算符$set、$inc和$push。接下来，它将单词lefty改回到left，以演示如何使用运算符$pop。
> 在程序清单8.3中，开头的方法displayWords()以适合本书的格式显示查找操作返回的单词。注意到使用了print()语句显示了结果，以帮助您理解更新并核实正确地进行了更新。
> 请执行如下步骤来编写并运行这个MongoDB shell脚本，对示例数据集中的文档进行更新。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour08中新建一个文件，并将其命名为doc_update.js。
> 4．在这个文件中输入程序清单8.3所示的代码。这些代码连接到数据库words，获取表示集合word_stats的Collection对象，使用update()更新以q打头且以y结尾的单词，并将单词left改为lefty。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour08。
> 7．执行下面的命令以运行这个脚本，它更新示例集合word_stats中的单词，并显示结果。程序清单8.4显示了这个脚本的输出。
> **程序清单8.3　doc_update.js：使用MongoDB shell更新集合中的文档**
> **程序清单8.4　doc_update.js-output：使用MongoDB shell更新集合中文档的输出**
> ▲

将文档插入集合后，您经常需要根据数据变化更新它们。Collection对象的方法update()让您能够更新集合中的文档，它多才多艺，但使用起来非常容易。下面是方法update()的语法：

```go
update(query, update, upsert, multi)
```

参数query是一个文档，指定了要修改哪些文档。请求将判断指定的属性和值是否与文档的字段和值匹配，进而更新匹配的文档。参数update是一个对象，指定了要如何修改与查询匹配的文档。表8.4列出了可使用的运算符。

参数upsert是个布尔值；如果为true且没有文档与查询匹配，将插入一个新文档。参数multi也是一个布尔值；如果为true将更新所有与查询匹配的文档；如果为false将只更新与查询匹配的第一个文档。

例如，对于集合中字段category为new的文档，下面的代码将其字段category改为old。在这里，upsert被设置为false，因此即便没有字段category为new的文档，也不会插入新文档；而multi被设置为true，因此将更新所有匹配的文档：

```go
update({category:"new"}, {$set:{categor:"old"}}, false, true);
```

使用方法update()更新多个文档时，可隔离写入操作，禁止对文档执行其他写入操作。为此，可在查询中使用属性$isolated:1。这样做并不能实现原子写入（要么全部写入，要么什么都不写入），而只是禁止其他写入进程更新您正在写入的文档。下面是一个这样的示例：

```go
update({category:"new", $isolated:1}, {$set:{category:"old"}}, false, true);
```

▼　Try It Yourself

```go
mongo doc_update.js
```

```go
01 function displayWords(cursor){
02    words = cursor.map(function(word){
03       return word.word + "(" + word.size + ")";
04    });
05    wordStr = JSON.stringify(words);
06    if (wordStr.length > 65){
07       wordStr = wordStr.slice(0, 50) + "...";
08    }
09    print(wordStr);
10 }
11 mongo = new Mongo('localhost');
12 wordsDB = mongo.getDB('words');
13 wordsDB.runCommand( { getLastError: 1, w: 1, j: true, wtimeout: 1000 } );
14 wordsColl = wordsDB.getCollection('word_stats');
15 cursor = wordsColl.find({category:"QYwords"});
16 print("Before QYwords Update: ");
17 displayWords(cursor);
18 wordsColl.update( { $and:[{ first: "q"},{last:'y'}]},
19                       { $set: {category:'QYwords'}},
20                       false, true);
21 cursor = wordsColl.find({category:"QYwords"});
22 print("After QYwords Update: ");
23 displayWords(cursor);
24 print("Before Left Update: ");
25 word = wordsColl.findOne({word: 'left'},
26                               {word:1, size:1, stats:1, letters:1});
27 printjson(word);
28 wordsColl.update({ word: 'left'},
29                      {    $set: {word:'lefty'},
30                            $inc: {size: 1, 'stats.consonants': 1},
31                          $push: {letters: "y"}},
32                      false, false);
33 word = wordsColl.findOne({word: 'lefty'},
34                               {word:1, size:1, stats:1, letters:1});
35 print("After Left Update: ");
36 printjson(word);
37 wordsColl.update({category:"QYwords"},
38                      {$set: {category:"none"}}, false, true);
39 wordsColl.update( {    word: 'lefty'},
40                       {    $set: {word:'left'},
41                           $inc: {size: -1, 'stats.consonants': -1},
42                          $pop: {letters: 1}});
43 word = wordsColl.findOne({word: 'left'},
44      {word:1, size:1, stats:1, letters:1});
45 print("After Lefty Update: ");
46 printjson(word);
```

```go
Before QYwords Update:
[]
After QYwords Update:
["quickly(7)","quality(7)","quietly(7)"]
Before Left Update:
{
        "_id" : ObjectId("52e2992e138a073440e4663c"),
        "word" : "left",
        "size" : 4,
        "letters" : [
                "l",
                "e",
                "f",
                "t"
        ],
        "stats" : {
                "vowels" : 1,
                "consonants" : 3
        }
}
After Left Update:
{
        "_id" : ObjectId("52e2992e138a073440e4663c"),
        "letters" : [
                "l",
                "e",
                "f",
                "t",
                "y"
        ],
        "size" : 5,
        "stats" : {
                "consonants" : 4,
                "vowels" : 1
        },
        "word" : "lefty"
}
After Lefty Update:
{
        "_id" : ObjectId("52e2992e138a073440e4663c"),
        "letters" : [
                "l",
                "e",
                "f",
                "t"
        ],
        "size" : 4,
        "stats" : {
                "consonants" : 3,
                "vowels" : 1
        },
        "word" : "left"
}
```

