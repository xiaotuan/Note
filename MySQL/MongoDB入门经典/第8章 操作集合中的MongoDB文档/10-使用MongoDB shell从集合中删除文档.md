### 8.9　使用MongoDB shell从集合中删除文档

> **使用MongoDB shell从集合中删除文档**
> 在本节中，您将编写一个简单的MongoDB shell脚本，它从示例数据集中删除文档。通过这个示例，您将熟悉如何删除单个和多个文档。程序清单8.9显示了这个示例的代码。
> 这个示例使用remove()来删除字段category的值为new的文档，这些文档是在本章前面的示例中添加的。另外请注意，使用了print()语句显示结果，以帮助您理解删除并核实正确地执行了删除。
> 请执行如下步骤来编写并运行这个从示例数据集中删除文档的MongoDB shell脚本。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour08中新建一个文件，并将其命名为doc_delete.js。
> 4．在这个文件中输入程序清单8.9所示的代码。这些代码连接到数据库words，获取表示集合word_stats的Collection对象，并使用remove()来删除单词。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour08。
> 7．执行下面的命令以运行这个脚本，它从示例集合word_stats中删除单词并显示结果。程序清单8.10显示了这个脚本的输出。
> **程序清单8.9　doc_delete.js：使用MongoDB shell从集合中删除文档**
> **程序清单8.10　doc_delete.js-output：使用MongoDB shell从集合中删除文档的输出**
> ▲

为减少消耗的空间，改善性能以及保持整洁，需要从MongoDB集合中删除文档。Collection对象的方法remove()使得从集合中删除文档非常简单，其语法如下：

```go
remove([query], [justOne])
```

其中参数query是一个对象，指定要了删除哪些文档。请求将指定的属性和值与文档的字段和值进行比较，进而删除匹配的文档。如果没有指定参数query，将删除集合中的所有文档。

参数justOne是个布尔值；如果为true，将只删除与查询匹配的第一个文档。如果没有指定参数query和justOne，将删除集合中所有的文档。

例如，要删除集合words_stats中所有的文档，可使用如下代码：

```go
collection = myDB.getCollection('word_stats');
collection.remove();
```

下面的代码删除集合words_stats中所有以a打头的单词：

```go
collection = myDB.getCollection('word_stats');
collection.remove({first:'a'}, false);
```

下面的代码只删除集合words_stats中第一个以a打头的单词：

```go
collection = myDB.getCollection('word_stats');
collection.remove({first:'a'}, true);
```

▼　Try It Yourself

```go
mongo doc_delete.js
```

```go
01 mongo = new Mongo('localhost');
02 wordsDB = mongo.getDB('words');
03 wordsDB.runCommand( { getLastError: 1, w: 1, j: true, wtimeout: 1000 } );
04 wordsColl = wordsDB.getCollection('word_stats');
05 print("Before Delete One: ");
06 cursor = wordsColl.find({category: 'New'}, {word:1});
07 printjson(cursor.toArray());
08 wordsColl.remove({category: 'New'}, true);
09 cursor = wordsColl.find({category: 'New'}, {word:1});
10 print("After Delete One: ");
11 printjson(cursor.toArray());
12 wordsColl.remove({category: 'New'});
13 cursor = wordsColl.find({category: 'New'}, {word:1});
14 print("After Delete All: ");
15 printjson(cursor.toArray());
```

```go
Before Delete One:
[
        {
                "_id" : ObjectId("52e2a3a845e4ce6a26bbf884"),
                "word" : "selfie"
        },
        {
                "_id" : ObjectId("52e2a3a845e4ce6a26bbf885"),
                "word" : "tweet"
        },
        {
                "_id" : ObjectId("52e2a3a845e4ce6a26bbf886"),
                "word" : "google"
        },
        {
                "_id" : ObjectId("52e2a3c7efa77e82c3b905e3"),
                "word" : "blog"
        }
]
After Delete One:
[
        {
                "_id" : ObjectId("52e2a3a845e4ce6a26bbf885"),
                "word" : "tweet"
        },
        {
                "_id" : ObjectId("52e2a3a845e4ce6a26bbf886"),
                "word" : "google"
        },
        {
                "_id" : ObjectId("52e2a3c7efa77e82c3b905e3"),
                "word" : "blog"
        }
]
After Delete All:
[ ]
```

