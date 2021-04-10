### 18.4　使用Python更新文档

> **使用Python更新集合中的文档**
> 在本节中，您将编写一个简单的Python应用程序，它使用Collection对象的方法update()来更新示例数据库的一个集合中的既有文档。通过这个示例，您将熟悉如何在Python中使用MongoDB更新运算符来更新文档。程序清单18.7显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，再调用其他方法更新文档。方法showWord()显示更新前和更新后的文档。
> 方法updateDoc()创建一个查询对象，它从数据库获取表示单词left的文档；再创建一个更新对象，它将字段word的值改为lefty，将字段size和stats.consonants的值加1，并将字母y压入到数组字段letters中。方法resetDoc()将文档恢复原样，以演示如何将字段值减1以及如何从数组字段中弹出值。
> 请执行下面的步骤，创建并运行这个更新示例数据库中文档并显示结果的Python应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour18中新建一个文件，并将其命名为PythonDocUpdate.py。
> 4．在这个文件中输入程序清单18.7所示的代码。这些代码使用update()来更新文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour18。
> 7．执行下面的命令来运行这个Python应用程序。程序清单18.8显示了这个应用程序的输出。
> **程序清单18.7　PythonDocUpdate.py：在Python应用程序中更新集合中的文档**
> **程序清单18.8　PythonDocUpdate.py-output：在Python应用程序中更新集合中文档的输出**
> ▲

将文档插入集合后，经常需要使用Python根据数据变化更新它们。Collection对象的方法update()让您能够更新集合中的文档，它多才多艺，但使用起来非常容易。下面是方法update()的语法：

```go
update(query, update, [upsert], [manipulate], [safe], [multi])
```

参数query是一个Dictionary对象，指定了要修改哪些文档。请求将判断query指定的属性和值是否与文档的字段和值匹配，进而更新匹配的文档。参数update是一个Dictionary对象，指定了要如何修改与查询匹配的文档。第8章介绍了可在这个对象中使用的更新运算符。

对于基本的upate()操作，您需要理解的其他参数包括upsert和multi。参数upsert是个布尔值，决定了是否执行upsert操作；如果为True且没有文档与查询匹配，将插入一个新文档。参数multi也是一个布尔值；如果为True将更新所有与查询匹配的文档，否则只更新与查询匹配的第一个文档。

例如，对于集合中字段category为New的文档，下面的代码将其字段category改为Old。在这里，upsert被设置为False，因此即便没有字段category为New的文档，也不会插入新文档；而multi被设置为True，因此将更新所有匹配的文档：

```go
query = {'category' : 'New'}
update = {'$set' : {'category' : 'Old'}}
myColl.update(query, update, upsert=False, multi=True)
```

▼　Try It Yourself

```go
python PythonDocUpdate.py
```

```go
01 from pymongo import MongoClient
02 def showWord(collection):
03      query = {'word': {'$in' : ['left', 'lefty']}}
04      cursor = collection.find(query)
05      for doc in cursor:
06         print (doc)
07 def updateDoc(collection):
08      query = {'word' : "left"}
09      update = {
10           '$set' : {'word' : 'lefty'},
11           '$inc' : {'size' : 1, 'stats.consonants' : 1},
12           '$push' : {'letters' : 'y'}}
13      results = collection.update(query, update, upsert=False, multi=False)
14      print ("\nUpdate Doc Result: ")
15      print (str(results))
16      print ("\nAfter Updating Doc: ")
17      showWord(collection)
18 def resetDoc(collection):
19      query = {'word' : "lefty"}
20      update = {
21           '$set' : {'word' : 'left'},
22           '$inc' : {'size' : -1, 'stats.consonants' : -1},
23           '$pop' : {'letters' : 1}}
24      results = collection.update(query, update, upsert=False, multi=False)
25      print ("\nReset Doc Result: ")
26      print (str(results))
27      print ("\nAfter Resetting Doc: ")
28      showWord(collection)
29 if __name__=="__main__":
30      mongo = MongoClient('mongodb://localhost:27017/')
31      mongo.write_concern = {'w' : 1, 'j' : True}
32      db = mongo['words']
33      collection = db['word_stats']
34      print ("Before Updating:")
35      showWord(collection)
36      updateDoc(collection)
37      resetDoc(collection)
```

```go
Before Updating:
{ 'stats': {'consonants': 3.0, 'vowels': 1.0},
  'letters': ['l', 'e', 'f', 't'], 'word': 'left',
  'charsets': [{'chars': ['l', 'f', 't'], 'type': 'consonants'},
                  {'chars': ['e'], 'type': 'vowels'}],
  'first': 'l', 'last': 't', '_id': ObjectId('52e89477c25e84985532622e'),
  'size': 4.0}
Update Doc Result:
{'updatedExisting': True, 'connectionId': 107, 'ok': 1.0, 'err': None, 'n': 1}
After Updating Doc:
{ 'stats': {'consonants': 4.0, 'vowels': 1.0},
  'letters': ['l', 'e', 'f', 't', 'y'], 'word': 'lefty',
  'charsets': [{'chars': ['l', 'f', 't'], 'type': 'consonants'},
                  {'chars': ['e'], 'type': 'vowels'}],
  'first': 'l', 'last': 't', '_id': ObjectId('52e89477c25e84985532622e'),
  'size': 5.0}
Reset Doc Result:
{'updatedExisting': True, 'connectionId': 107, 'ok': 1.0, 'err': None, 'n': 1}
After Resetting Doc:
{ 'stats': {'consonants': 3.0, 'vowels': 1.0},
  'letters': ['l', 'e', 'f', 't'], 'word': 'left',
  'charsets': [{'chars': ['l', 'f', 't'], 'type': 'consonants'},
                  {'chars': ['e'], 'type': 'vowels'}],
  'first': 'l', 'last': 't', '_id': ObjectId('52e89477c25e84985532622e'),
  'size': 4.0}
```

