### 8.8　使用MongoDB shell在集合中更新或插入文档

> **使用MongoDB shell在集合中更新或插入文档**
> 在本节中，您将编写一个简单的MongoDB shell脚本，在示例数据集中更新或插入文档。这个示例旨在让您熟练使用upsert来新建文档或更新既有文档。程序清单8.7显示了这个示例的代码。
> 这个示例使用upsert添加一个新单词，但其值不正确，因此再次使用upsert来更新它。另外请注意，使用了print()语句来显示结果，让您能够明白upsert以及核实正确地执行了upsert。
> 请执行如下步骤来编写并运行这个在示例数据集中更新或插入文档的MongoDB shell脚本。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour08中新建一个文件，并将其命名为doc_upsert.js。
> 4．在这个文件中输入程序清单8.7所示的代码。这些代码连接到数据库words，获取表示集合word_stats的Collection对象，并使用update()（将参数upsert设置为true）来更新或插入单词。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour08。
> 7．执行下面的命令以运行这个脚本，它在示例集合word_stats中插入或更新文档并显示结果。程序清单8.8显示了这个脚本的输出。
> **程序清单8.7　doc_upsert.js：使用MongoDB shell在集合中更新或插入文档**
> **程序清单8.8　doc_upsert.js-output：使用MongoDB shell在集合中更新或插入文档的输出**
> ▲



可对文档执行的另一种操作是upsert，这将在文档存在时更新它，在文档不存在时插入它。常规更新不会自动插入文档，因为这需要判断文档是否存在。如果您确定文档存在，可使用常规update()，其效率高得多；同样，如果您确定文档不存在，可使用insert()。

要实现upsert，只需将方法update()的参数upsert设置为true。这告诉请求，如果文档存在，就尝试更新它；否则就插入一个新文档，其字段值由方法update()的参数在update指定。

例如，在下面的代码中，如果数据库中包含color字段为azure的文档，就更新它；否则就插入指定的文档：

```go
update({color:"azure"}, {$set:{red:0, green:127, blue:255}}, true, false);
```

警告：

> 为避免多次插入同一个文档，请仅在根据查询字段建立了唯一的索引时，才使用upsert: true。

▼　Try It Yourself

```go
mongo doc_upsert.js
```

```go
01 mongo = new Mongo('localhost');
02 wordsDB = mongo.getDB('words');
03 wordsDB.runCommand( { getLastError: 1, w: 1, j: true, wtimeout: 1000 } );
04 wordsColl = wordsDB.getCollection('word_stats');
05 cursor = wordsColl.find({word: 'righty'},
06                              {word:1, size:1, stats:1, letters:1});
07 print("Before Upsert: ");
08 printjson(cursor.toArray());
09 wordsColl.update({    word: 'righty'},
10                      {    $set: {word:'righty', size: 4,
11                            letters: ['r','i','g','h'],
12                            'stats.consonants': 3, 'stats.vowels': 1}},
13                      true, true);
14 cursor = wordsColl.find({word: 'righty'},
15                              {word:1, size:1, stats:1, letters:1});
16 print("After Upsert: ");
17 printjson(cursor.toArray());
18 wordsColl.update({ word: 'righty'},
19       { $set: {word:'righty', size: 6,
20         letters: ['r','i','g','h','t','y'],
21         'stats.consonants': 5, 'stats.vowels': 1}}, true, true);
22 cursor = wordsColl.find({word: 'righty'},
23                              {word:1, size:1, stats:1, letters:1});
24 print("After Second Upsert: ");
25 printjson(cursor.toArray());
```

```go
Before Upsert:
[ ]
After Upsert:
[
         {
                  "_id" : ObjectId("52e29f7de2c3cd20463ff664"),
                  "letters" : ["r","i","g","h"],
                  "size" : 4,
                  "stats" : {
                           "consonants" : 3,
                           "vowels" : 1
                  },
                  "word" : "righty"
         }
]
After Second Upsert:
[
         {
                  "_id" : ObjectId("52e29f7de2c3cd20463ff664"),
                  "letters" : ["r","i","g","h","t","y"],
                  "size" : 6,
                  "stats" : {
                           "consonants" : 5,
                           "vowels" : 1
                  },
                  "word" : "righty"
         }
]
```

