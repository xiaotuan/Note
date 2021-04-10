### 18.5　使用Python更新或插入文档

> **使用Python更新集合中的文档**
> 在本节中，您将编写一个简单的Python应用程序，它使用方法update()对示例数据库执行upsert操作：先插入一个新文档，再更新这个文档。通过这个示例，您将熟悉如何在Python应用程序使用方法update()来执行upsert操作。程序清单18.9显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来更新文档。方法showWord()用于显示单词被添加前后以及被更新后的情况。
> 方法addUpsert()创建一个数据库中没有的新单词，再使用upsert操作来插入这个新文档。这个文档包含的信息有些不对，因此方法updateUpsert()执行upsert操作来修复这些错误；这次更新了既有文档，演示了upsert操作的更新功能。
> 请执行如下步骤，创建并运行这个Python应用程序，它对示例数据库中的文档执行upsert操作并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour18中新建一个文件，并将其命名为PythonDocUpsert.py。
> 4．在这个文件中输入程序清单18.9所示的代码。这些代码使用update()来对文档执行upsert操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour18。
> 7．执行下面的命令来运行这个Python应用程序。程序清单18.10显示了这个应用程序的输出。
> **程序清单18.9　PythonDocUpsert.py：在Python应用程序中对集合中的文档执行upsert操作**
> **程序清单18.10　PythonDocUpsert.py-output：在Python应用程序中对集合中文档执行upsert操作的输出**
> ▲

在Python中，Collection对象的方法update()的另一种用途是，用于执行upsert操作。upsert操作先尝试更新集合中的文档；如果没有与查询匹配的文档，就使用$set运算符来创建一个新文档，并将其插入到集合中。下面显示了方法update()的语法：

```go
update(query, update, [upsert], [manipulate], [safe], [multi])
```

参数query指定要修改哪些文档；参数update是一个Dictionary对象，指定了要如何修改与查询匹配的文档。要执行upsert操作，必须将参数upsert设置为True，并将参数multi设置为False。

例如，下面的代码对name=myDoc的文档执行upsert操作。运算符$set指定了用来创建或更新文档的字段。由于参数upsert被设置为True，因此如果没有找到指定的文档，将创建它；否则就更新它：

```go
query = {'name' : 'myDoc'}
update = { '$set' : { 'name' : 'myDoc', 'number' : 5, 'score' : '10'}}
results = collection.update(query, update, upsert=True, multi=False)
```

▼　Try It Yourself

```go
python PythonDocUpsert.py
```

```go
01 from pymongo import MongoClient
02 def showWord(collection):
03      query = {'word' : 'righty'}
04      doc = collection.find_one(query)
05      print (doc)
06 def addUpsert(collection):
07      query = {'word' : 'righty'}
08      update = { '$set' :
09         {
10           'word' : 'righty', 'first' : 'r', 'last' : 'y',
11           'size' : 4, 'category' : 'New',
12           'stats' : {'vowels' : 1, 'consonants' : 4},
13           'letters' : ["r","i","g","h"],
14           'charsets' : [
15             {'type' : 'consonants', 'chars' : ["r","g","h"]},
16             {'type' : 'vowels', 'chars' : ["i"]}]}}
17      results = collection.update(query, update, upsert=True, multi=False)
18      print ("\nUpsert as insert results: ")
19      print (results)
20      print ("After Upsert as insert:")
21      showWord(collection)
22 def updateUpsert(collection):
23      query = {'word' : 'righty'}
24      update = { '$set' :
25        {
26           'word' : 'righty', 'first' : 'r', 'last' : 'y',
27           'size' : 6, 'category' : 'Updated',
28           'stats' : {'vowels' : 1, 'consonants' : 5},
29           'letters' : ["r","i","g","h","t","y"],
30           'charsets' : [
31             {'type' : 'consonants', 'chars' : ["r","g","h","t","y"]},
32             {'type' : 'vowels', 'chars' : ["i"]}]}}
33      results = collection.update(query, update, upsert=True, multi=False)
34      print ("\nUpsert as update results:")
35      print (results)
36      print ("After Upsert as update:")
37      showWord(collection)
38 if __name__=="__main__":
39      mongo = MongoClient('mongodb://localhost:27017/')
40      mongo.write_concern = {'w' : 1, 'j' : True}
41      db = mongo['words']
42      collection = db['word_stats']
43      print ("Before Upserting:")
44      showWord(collection)
45      addUpsert(collection)
46      updateUpsert(collection)
47      def clean(collection):
48           query = {'word': "righty"}
49           collection.remove(query)
50      clean(collection)
```

```go
Before Upserting:
None
Upsert as insert results:
{'ok': 1.0, 'upserted': ObjectId('52eaf704381e4f7e1b27b412'), 'err': None,
'connectionId': 123, 'n': 1, 'updatedExisting': False}
After Upsert as insert:
{ 'category': 'New', 'stats': {'consonants': 4, 'vowels': 1},
  'letters': ['r', 'i', 'g', 'h'], 'word': 'righty',
  'charsets': [{'chars': ['r', 'g', 'h'], 'type': 'consonants'},
                  {'chars': ['i'], 'type': 'vowels'}],
  'size': 4, 'last': 'y',
  '_id': ObjectId('52eaf704381e4f7e1b27b412'), 'first': 'r'}
Upsert as update results:
{'updatedExisting': True, 'connectionId': 123, 'ok': 1.0, 'err': None, 'n': 1}
After Upsert as update:
{ 'category': 'Updated', 'stats': {'consonants': 5, 'vowels': 1},
  'letters': ['r', 'i', 'g', 'h', 't', 'y'], 'word': 'righty',
  'charsets': [{'chars': ['r', 'g', 'h', 't', 'y'], 'type': 'consonants'},
                  {'chars': ['i'], 'type': 'vowels'}],
  'size': 6, 'last': 'y',
  '_id': ObjectId('52eaf704381e4f7e1b27b412'), 'first': 'r'}
```

