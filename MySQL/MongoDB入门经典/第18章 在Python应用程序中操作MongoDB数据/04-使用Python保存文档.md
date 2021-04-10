### 18.3　使用Python保存文档

> **使用Python将文档保存到集合中**
> 在本节中，您将创建一个简单的Python应用程序，它使用Collection对象的方法save()来更新示例数据库中的一个既有文档。通过这个示例，您将熟悉如何使用Python更新并保存文档对象。程序清单18.5显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来保存文档。方法showWord()显示更新前和更新后的单词ocean。
> 方法saveBlueDoc()从数据库中获取单词ocean的文档，使用put()将字段category改为blue，再使用方法save()保存这个文档。方法resetDoc()从数据库获取单词ocean的文档，使用方法put()将字段category恢复为空，再使用方法save()保存这个文档。
> 请执行如下步骤，创建并运行这个将文档保存到示例数据库中并显示结果的Python应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour18中新建一个文件，并将其命名为PythonDocSave.py。
> 4．在这个文件中输入程序清单18.5所示的代码。这些代码使用save()来保存文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour18。
> 7．执行下面的命令来运行这个Python应用程序。程序清单18.6显示了这个应用程序的输出。
> **程序清单18.5　PythonDocSave.py：在Python应用程序中将文档保存到集合中**
> **程序清单18.6　PythonDocSave.py-output：在Python应用程序中将文档保存到集合中的输出**
> ▲

一种更新数据库中文档的便利方式是，使用Collection对象的方法save()，这个方法接受一个Dictionary作为参数，并将其保存到数据库中。如果指定的文档已存在于数据库中，就将其更新为指定的值；否则就插入一个新文档。

方法save()的语法如下，其中参数doc是一个Dictionary对象，表示要保存到集合中的文档：

```go
save(doc)
```

▼　Try It Yourself

```go
python PythonDocSave.py
```

```go
01 from pymongo import MongoClient
02 def showWord(collection):
03      query = {'word' : 'ocean'}
04      fields = {'word' : True, 'category' : True}
05      doc = collection.find_one(query, fields)
06      print (doc)
07 def saveBlueDoc(collection):
08      query = {'word' : "ocean"}
09      doc = collection.find_one(query)
10      doc["category"] = "blue"
11      results = collection.save(doc)
12      print ("\nSave Docs Result:")
13      print (str(results))
14      print ("\nAfter Saving Doc:")
15      showWord(collection)
16 def resetDoc(collection):
17      query = {'word' : "ocean"}
18      doc = collection.find_one(query)
19      doc["category"] = ""
20      results = collection.save(doc)
21      print ("\nReset Docs Result:")
22      print (str(results))
23      print ("\nAfter Resetting Doc:")
24      showWord(collection)
25 if __name__=="__main__":
26      mongo = MongoClient('mongodb://localhost:27017/')
27      mongo.write_concern = {'w' : 1, 'j' : True}
28      db = mongo['words']
29      collection = db['word_stats']
30      print ("Before Saving:")
31      showWord(collection)
32      saveBlueDoc(collection)
33      resetDoc(collection)
```

```go
Before Saving:
{'category': '', '_id': ObjectId('52e89477c25e8498553265e4'), 'word': 'ocean'}
Save Docs Result:
52e89477c25e8498553265e4
After Saving Doc:
{'category': 'blue', '_id': ObjectId('52e89477c25e8498553265e4'), 'word': 'ocean'}
Reset Docs Result:
52e89477c25e8498553265e4
After Resetting Doc:
{'category': '', '_id': ObjectId('52e89477c25e8498553265e4'), 'word': 'ocean'}
```

