### 16.2.1　使用Python从MongoDB获取文档

> **使用Python从MongoDB检索文档**
> 在本节中，您将编写一个简单的Python应用程序，它使用find()和find_one()从示例数据库中检索文档。通过这个示例，您将熟悉如何使用方法find()和find_one()以及如何处理响应。程序清单16.3显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，再调用其他方法来查找并显示文档。
> 方法getOne()调用方法find_one()从集合中获取单个文档，再显示该文档；方法getManyFor()查找所有的文档，再使用for循环逐个获取这些文档。
> 方法getManySlice()查找集合中的所有文档，再使用Python切片语法来获取并显示第5～10个文档。
> 请执行如下步骤，创建并运行这个在示例数据集中查找文档并显示结果的Python应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour16中新建一个文件，并将其命名为PythonFind.py。
> 4．在这个文件中输入程序清单16.3所示的代码。这些代码使用了方法find()和find_one()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour16。
> 7．执行下面的命令来运行这个Python应用程序。程序清单16.4显示了这个应用程序的输出。
> **程序清单16.3　PythonFind.py：在Python应用程序中查找并检索集合中的文档**
> **程序清单16.4　PythonFind.py-output：在Python应用程序中查找并检索集合中文档的输出**
> ▲

Collection对象提供了方法find()和find_one()，它们与MongoDB shell中的同名方法类似，也分别查找一个和多个文档。

调用find_one()时，将以Dictionary对象的方式从服务器返回单个文档，然后您就可根据需要在应用程序中使用这个对象，如下所示：

```go
doc = myColl.find_one()
```

Collection对象的方法find()返回一个Cursor对象，这个对象表示找到的文档，但不取回它们。可以多种不同的方式迭代Cursor对象。

可以使用for循环来迭代，如下所示：

```go
cursor = myColl.find()
for doc in cursor:
   print (doc)
```

由于Python将游标视为列表，因此也可使用切片语法来获取游标的部分内容。例如，下面的代码查找集合中的所有文档，再显示第5～10个文档：

```go
cursor = collection.find()
slice = cursor[5:10]
for doc in slice:
   print (doc)
```

▼　Try It Yourself

```go
python PythonFind.py
```

```go
01 from pymongo import MongoClient
02 def getOne(collection):
03    doc = collection.find_one()
04    print ("Single Document:")
05    print (doc)
06 def getManyFor(collection):
07    print ("\nMany Using While Loop:")
08    cursor = collection.find()
09    words = []
10    for doc in cursor:
11       words.append(str(doc['word']))
12       if len(words) > 10:
13            break
14    print (words)
15 def getManySlice(collection):
16    print ("\nMany Using For Each Loop:")
17    cursor = collection.find()
18    cursor = cursor[5:10]
19    words = []
20    for doc in cursor:
21       words.append(str(doc['word']))
22    print (words)
23 if __name__=="__main__":
24    mongo = MongoClient('mongodb://localhost:27017/')
25    db = mongo['words']
26    collection = db['word_stats']
27    getOne(collection)
28    getManyFor(collection)
29    getManySlice(collection)
```

```go
Single Document:
{'stats': {'consonants': 2.0, 'vowels': 1.0}, 'last': 'e',
  'charsets': [{'chars': ['t', 'h'], 'type': 'consonants'},
                  {'chars': ['e'], 'type': 'vowels'}],
'first': 't', 'letters': ['t', 'h', 'e'], 'word': 'the',
'_id': ObjectId('52e89477c25e849855325f6a'), 'size': 3.0}
Many Using While Loop:
['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it', 'i', 'that']
Many Using For Each Loop:
['in', 'to', 'have', 'it', 'i']
```

