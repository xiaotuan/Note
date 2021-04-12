### 8.5　使用MongoDB shell在集合中添加文档

> **使用MongoDB shell在集合中插入文档**
> 在本节中，您将编写一个简单的MongoDB shell脚本，在示例数据集中插入新的单词文档。通过这个示例，您将熟悉如何插入单个文档和文档数组。程序清单8.1显示了这个示例的代码。
> 在程序清单8.1中，第一部分定义了要插入到数据库中的三个新单词：selfie、tweet和google。另外，每一步都使用print()语句显示当前的单词，让您知道这些单词确实加入到了数据库。
> 请执行如下步骤，以创建并运行这个在示例数据集中插入文档的MongoDB shell脚本。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour08中新建一个文件，并将其命名为doc_add.js。
> 4．在这个文件中输入程序清单8.1所示的代码。这些代码连接到数据库words，获取表示集合word_stats的Collection对象，并使用insert()插入三个新单词。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour08。
> 7．执行下面的命令来运行这个脚本，它在示例集合word_stats中插入三个新单词，并显示结果。程序清单8.2显示了这个脚本的输出。
> **程序清单8.1　doc_add.js：使用MongoDB shell在集合中插入文档**
> **程序清单8.2　doc_add.js-output：使用MongoDB shell在集合中插入文档的输出**
> ▲

与MongoDB数据库交互时，另一种常见任务是在集合中插入文档。要插入文档，首先要创建一个表示该文档的JavaScript对象。插入操作之所以使用JavaScript对象，是因为MongoDB使用的BSON格式基于JavaScript表示法。

有新文档的JavaScript版本后，就可将其存储到MongoDB数据库中，为此可对相应的Collection对象实例调用方法insert()。方法insert()的语法如下，其中参数docs可以是单个文档对象，也可以是一个文档对象数组：

```go
insert(docs)
```

例如，下面的示例在集合中插入一个简单的文档：

```go
mongo = new Mongo('localhost');
myDB = mongo.getDB('myDB');
myColl = myDB.getCollection('myCollection');
myColl.insert({color:"blue", value:7, name:"Ordan"});
```

▼　Try It Yourself

```go
mongo doc_add.js
```

```go
01 selfie = {
02    word: 'selfie', first: 's', last: 'e',
03    size: 4, letters: ['s','e','l','f','i'],
04    stats: {vowels: 3, consonants: 3},
05    charsets: [ {type: 'consonants', chars: ['s','l','f']},
06                   {type: 'vowels', chars: ['e','i']} ],
07    category: 'New' };
08 tweet = {
09       word: 'tweet', first: 't', last: 't',
10       size: 4, letters: ['t','w','e'],
11       stats: {vowels: 2, consonants: 3},
12       charsets: [ {type: 'consonants', chars: ['t','w']},
13                      {type: 'vowels', chars: ['e']} ],
14       category: 'New' };
15 google = {
16       word: 'google', first: 'g', last: 'e',
17       size: 4, letters: ['g','o','l','e'],
18       stats: {vowels: 3, consonants: 3},
19       charsets : [ {type: 'consonants', chars: ['g','l']},
20                       {type: 'vowels', chars: ['o','e']} ],
21       category: 'New' };
22
23 mongo = new Mongo('localhost');
24 wordsDB = mongo.getDB('words');
25 wordsDB.runCommand( { getLastError: 1, w: 1, j: true, wtimeout: 1000 } );
26 wordsColl = wordsDB.getCollection('word_stats');
27 print('Before Inserting selfie: ');
28 cursor = wordsColl.find({word: {$in: ['tweet','google', 'selfie']}},
29                              {word:1});
30 printjson(cursor.toArray());
31 wordsColl.insert(selfie);
32 print('After Inserting selfie: ');
33 cursor = wordsColl.find({word: {$in: ['tweet','google', 'selfie']}},
34                              {word:1});
35 printjson(cursor.toArray());
36 print('After Inserring tweet and google');
37 wordsColl.insert([tweet, google]);
38 cursor = wordsColl.find({word: {$in: ['tweet','google', 'selfie']}},
39                              {word:1});
40 printjson(cursor.toArray());
```

```go
[ ]
After Inserting selfie:
[
         {
                  "_id" : ObjectId("52e292183475f9f0db342abe"),
                  "word" : "selfie" }
]
After Inserting tweet and google
[
         {
                  "_id" : ObjectId("52e292183475f9f0db342ac0"),
                  "word" : "google"
         },
         {
                  "_id" : ObjectId("52e292183475f9f0db342abe"),
                  "word" : "selfie"
         },
         {
                  "_id" : ObjectId("52e292183475f9f0db342abf"),
                  "word" : "tweet"
         }
]
```

