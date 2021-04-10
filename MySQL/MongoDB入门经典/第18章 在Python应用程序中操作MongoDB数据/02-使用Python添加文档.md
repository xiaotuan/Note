### 18.1　使用Python添加文档

> **使用Python在集合中插入文档**
> 在本节中，您将编写一个简单的Python应用程序，它使用Collection对象的方法insert()在示例数据库的一个集合中插入新文档。通过这个示例，您将熟悉如何使用Python来插入文档。程序清单18.1显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来插入文档。方法showNewDocs()显示新插入到集合中的文档。
> 方法addSelfie()新建一个表示单词selfie的文档，并使用insert()将其加入到数据库中；方法addGoogleAndTweet()创建表示单词google和tweet的新文档，并使用insert()以数组的方式将它们插入数据库。
> 请执行下面的步骤，创建并运行这个在示例数据库中插入新文档并显示结果的Python应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour18中新建一个文件，并将其命名为PythonDocAdd.py。
> 4．在这个文件中输入程序清单18.1所示的代码。这些代码使用insert()来添加新文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour18。
> 7．执行下面的命令来运行这个Python应用程序。程序清单18.2显示了这个应用程序的输出。
> **程序清单18.1　PythonDocAdd.py：在Python应用程序中将新文档插入到集合中**
> **程序清单18.2　PythonDocAdd.py-output：在Python应用程序中将新文档插入到集合中的输出**
> ▲

在Python中与MongoDB数据库交互时，一项重要的任务是在集合中插入文档。要插入文档，首先要创建一个表示该文档的Dictionary对象。插入操作将Dictionary对象以BSON的方式传递给MongoDB服务器，以便能够插入到集合中。

有新文档的Dictionary版本后，就可将其存储到MongoDB数据库中，为此可对相应的Collection对象实例调用方法insert()。方法insert()的语法如下，其中参数doc可以是单个文档对象，也可以是一个文档对象数组：

```go
insert(doc)
```

例如，下面的示例在集合中插入单个文档：

```go
doc1 = {'name' : 'Fred'}
result = myColl.insert(doc1)
```

要在集合中插入多个文档，可在调用Collection对象的方法insert()时传入一个Dictionary对象数组，如下所示：

```go
doc2 = {'name' : 'George'}
doc3 = {'name' : 'Ron'}
result = myColl.batchInsert([doc2, doc3])
```

请注意，方法insert()返回一个result对象，其中包含被插入到数据库的新文档的对象ID。

▼　Try It Yourself

```go
python PythonDocAdd.py
```

```go
01 from pymongo import MongoClient
02 def showNewDocs(collection):
03      query = {'category': 'New'}
04      cursor = collection.find(query)
05      for doc in cursor:
06           print (doc)
07 def addSelfie(collection):
08      selfie = {
09           'word' : 'selfie', 'first' : 's', 'last' : 'e',
10           'size' : 6, 'category' : 'New',
11           'stats' : {'vowels' : 3, 'consonants' : 3},
12           'letters' : ["s","e","l","f","i"],
13           'charsets' : [
14             {'type' : 'consonants', 'chars' : ["s","l","f"]},
15             {'type' : 'vowels', 'chars' : ["e","i"]}]}
16      results = collection.insert(selfie)
17      print ("\nInserting One Results:")
18      print (str(results))
19      print ("After Inserting One:")
20      showNewDocs(collection)
21 def addGoogleAndTweet(collection):
22      google = {
23           'word' : 'google', 'first' : 'g', 'last' : 'e',
24           'size' : 6, 'category' : 'New',
25           'stats' : {'vowels' : 3, 'consonants' : 3},
26           'letters' : ["g","o","l","e"],
27           'charsets' : [
28           {'type' : 'consonants', 'chars' : ["g","l"]},
29           {'type' : 'vowels', 'chars' : ["o","e"]}]}
30      tweet = {
31           'word' : 'tweet', 'first' : 't', 'last' : 't',
32           'size' : 5, 'category' : 'New',
33           'stats' : {'vowels' : 2, 'consonants' : 3},
34           'letters' : ["t","w","e"],
35           'charsets' : [
36           {'type' : 'consonants', 'chars' : ["t","w"]},
37           {'type' : 'vowels', 'chars' : ["e"]}]}
38      results = collection.insert([google, tweet])
39      print ("\nInserting Multiple Results:")
40      print (str(results))
41      print ("After Inserting Multiple:")
42      showNewDocs(collection)
43 if __name__=="__main__":
44      mongo = MongoClient('mongodb://localhost:27017/')
45      mongo.write_concern = {'w' : 1, 'j' : True}
46      db = mongo['words']
47      collection = db['word_stats']
48      print ("Before Inserting:")
49      showNewDocs(collection)
50      addSelfie(collection)
51      addGoogleAndTweet(collection)
```

```go
Before Inserting:
Inserting One Results:
52e98aba251214137874bff0
After Inserting One:
{ 'category': 'New', 'word': 'selfie', 'last': 'e',
  'charsets': [{'chars': ['s', 'l', 'f'], 'type': 'consonants'},
                  {'chars': ['e', 'i'], 'type': 'vowels'}],
  'first': 's', 'letters': ['s', 'e', 'l', 'f', 'i'],
  'stats': {'consonants': 3, 'vowels': 3},
  '_id': ObjectId('52e98aba251214137874bff0'), 'size': 6}
Inserting Multiple Results:
[ObjectId('52e98aba251214137874bff1'), ObjectId('52e98aba251214137874bff2')]
After Inserting Multiple:
{ 'category': 'New', 'word': 'google', 'last': 'e',
  'charsets': [{'chars': ['g', 'l'], 'type': 'consonants'},
                  {'chars': ['o', 'e'], 'type': 'vowels'}],
  'first': 'g', 'letters': ['g', 'o', 'l', 'e'],
  'stats': {'consonants': 3, 'vowels': 3},
  '_id': ObjectId('52e98aba251214137874bff1'), 'size': 6}
{ 'category': 'New', 'word': 'tweet', 'last': 't',
  'charsets': [{'chars': ['t', 'w'], 'type': 'consonants'},
                  {'chars': ['e'], 'type': 'vowels'}],
  'first': 't', 'letters': ['t', 'w', 'e'],
  'stats': {'consonants': 3, 'vowels': 2},
  '_id': ObjectId('52e98aba251214137874bff2'), 'size': 5}
{ 'category': 'New', 'word': 'selfie', 'last': 'e',
  'charsets': [{'chars': ['s', 'l', 'f'], 'type': 'consonants'},
                  {'chars': ['e', 'i'], 'type': 'vowels'}],
  'first': 's', 'letters': ['s', 'e', 'l', 'f', 'i'],
  'stats': {'consonants': 3, 'vowels': 3},
  '_id': ObjectId('52e98aba251214137874bff0'), 'size': 6}
```

