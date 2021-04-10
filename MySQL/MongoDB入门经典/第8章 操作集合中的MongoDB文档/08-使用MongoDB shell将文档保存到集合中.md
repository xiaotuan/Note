### 8.7　使用MongoDB shell将文档保存到集合中

> **使用MongoDB shell将文档保存到集合中**
> 在本节中，您将编写一个简单的MongoDB shell脚本，它在示例数据集中查找单词、对其进行修改并保存所做的修改；这个示例还将一个新单词保存到示例数据集中。通过这个示例，您将熟悉如何保存新文档以及如何保存对既有文档所做的修改。程序清单8.5显示了这个示例的代码。
> 这个示例首先给单词ocean和sky添加字段category，并保存所做的修改，然后将新单词blog保存到示例数据集中。
> 单词blog是在程序清单8.5开头定义的。另外请注意，使用了print()语句来显示结果，这旨在让您能够理解方法save()并核实正确地进行了保存。
> 请执行如下步骤来编写并运行这个将文档保存到示例数据集中的MongoDB shell脚本。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour08中新建一个文件，并将其命名为doc_save.js。
> 4．在这个文件中输入程序清单8.5所示的代码。这些代码连接到数据库words，获取表示集合word_stats的Collection对象，并使用save()来更新和添加单词。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour08。
> 7．执行下面的命令以运行这个脚本，它将单词保存到示例集合word_stats中并显示结果。程序清单8.6显示了这个脚本的输出。
> **程序清单8.5　doc_save.js：使用MongoDB shell将文档保存到集合中**
> **程序清单8.6　doc_save.js-output：使用MongoDB shell将文档保存到集合中的输出**
> ▲

Collection对象的方法save()很有趣，可用于在数据库中插入或更新文档；尽管其效率不如直接使用insert()或update()那么高，但在有些情况下更容易使用。例如，修改从MongoDB检索的对象时，可使用方法save()而不是update()，这样无需指定query和update对象。

方法save()的语法如下，其中参数doc是一个要保存到集合中的文档对象：

```go
save(doc)
```

使用方法save()时，指定的文档对象要么是要加入到集合中的全新JavaScript对象，要么是从集合中取回的对象（您对其做了修改，并想将修改保存到数据库中）。

例如，下面的代码保存对既有文档所做的修改并插入一个新文档：

```go
existingObject = myCollection.findOne({name:"existingObj"});
existingObject.name = "updatedObj";
myCollection.save(existingObj);
myCollection.save({name:"newObj"});
```

▼　Try It Yourself

```go
mongo doc_save.js
```

```go
01 blog = {
02    word: 'blog', first: 'b', last: 'g',
03    size: 4, letters: ['b','l','o','g'],
04    stats: {vowels: 1, consonants: 3},
05    charsets: [    {type: 'consonants', chars: ['b','l','g']},
06                  {type: 'vowels', chars: ['o']} ],
07    category: 'New' };
08 mongo = new Mongo('localhost');
09 wordsDB = mongo.getDB('words');
10 wordsDB.runCommand( { getLastError: 1, w: 1, j: true, wtimeout: 1000 } );
11 wordsColl = wordsDB.getCollection('word_stats');
12 cursor = wordsColl.find({category:"blue"}, {word: 1, category:1});
13 print("Before Existing Save: ");
14 printjson(cursor.toArray());
15 word = wordsColl.findOne({word:"ocean"});
16 word.category="blue";
17 wordsColl.save(word);
18 word = wordsColl.findOne({word:"sky"});
19 word.category="blue";
20 wordsColl.save(word);
21 cursor = wordsColl.find({category:"blue"}, {word: 1, category:1});
22 print("After Existing Save: ");
23 printjson(cursor.toArray());
24 word = wordsColl.findOne({word:"blog"});
25 print("Before New Document Save: ");
26 printjson(word);
27 wordsColl.save(blog);
28 word = wordsColl.findOne({word:"blog"}, {word: 1, category:1});
29 print("After New Document Save: ");
30 printjson(word);
```

```go
Before Existing Save:
[ ]
After Existing Save:
[
        {
                "_id" : ObjectId("52e2992e138a073440e46784"),
                "word" : "sky",
                "category" : "blue"
        },
        {
                "_id" : ObjectId("52e2992e138a073440e469f2"),
                "word" : "ocean",
                "category" : "blue"
        }
]
Before New Document Save:
null
After New Document Save:
{
        "_id" : ObjectId("52e29c62073b7a59dcf89ee1"),
        "word" : "blog",
        "category" : "New"
}
```

