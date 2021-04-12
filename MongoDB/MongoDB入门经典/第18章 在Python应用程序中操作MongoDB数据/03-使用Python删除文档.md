### 18.2　使用Python删除文档

> **使用Python从集合中删除文档**
> 在本节中，您将编写一个简单的Python应用程序，它使用Collection对象的方法从示例数据库的一个集合中删除文档。通过这个示例，您将熟悉如何使用Python删除文档。程序清单18.3显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来删除文档。方法showNewDocs()显示前面创建的新文档，从而核实它们确实从集合中删除了。
> 方法removeNewDocs()使用一个查询对象来删除字段category为New的文档。
> 请执行下面的步骤，创建并运行这个从示例数据库中删除文档并显示结果的Python应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour18中新建一个文件，并将其命名为PythonDocDelete.py。
> 4．在这个文件中输入程序清单18.3所示的代码。这些代码使用remove()来删除文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour18。
> 7．执行下面的命令来运行这个Python应用程序。程序清单18.4显示了这个应用程序的输出。
> **程序清单18.3　PythonDocDelete.py：在Python应用程序中从集合中删除文档**
> **程序清单18.4　PythonDocDelete.py-output：在Python应用程序中从集合中删除文档的输出**
> ▲

在Python中，有时候需要从MongoDB集合中删除文档，以减少消耗的空间，改善性能以及保持整洁。Collection对象的方法remove()使得从集合中删除文档非常简单，其语法如下：

```go
remove([query])
```

其中参数query是一个Dictionary对象，指定要了删除哪些文档。请求将query指定的字段和值与文档的字段和值进行比较，进而删除匹配的文档。如果没有指定参数query，将删除集合中的所有文档。

例如，要删除集合words_stats中所有的文档，可使用如下代码：

```go
collection = myDB['word_stats']
results = collection.remove()
```

下面的代码删除集合words_stats中所有以a打头的单词：

```go
collection = myDB['word_stats']
query = {'first' : 'a'}
collection.remove(query)
```

▼　Try It Yourself

```go
python PythonDocDelete.py
```

```go
01 from pymongo import MongoClient
02 def showNewDocs(collection):
03      query = {'category': 'New'}
04      cursor = collection.find(query)
05      for doc in cursor:
06           print (doc)
07 def removeNewDocs(collection):
08      query = {'category': "New"}
09      results = collection.remove(query)
10      print ("Delete Docs Result:")
11      print (str(results))
12      print ("\nAfter Deleting Docs:")
13      showNewDocs(collection)
14 if __name__=="__main__":
15      mongo = MongoClient('mongodb://localhost:27017/')
16      mongo.write_concern = {'w' : 1, 'j' : True}
17      db = mongo['words']
18      collection = db['word_stats']
19      print ("Before Deleting:")
20      showNewDocs(collection)
21      removeNewDocs(collection)
```

```go
Before Deleting:
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
Delete Docs Result:
{'connectionId': 105, 'ok': 1.0, 'err': None, 'n': 3}
After Deleting Docs:
```

