### 17.1.2 使用Python限制返回的字段

> **在方法中使用参数来减少对象表示的文档中的字段数**
> 在本节中，您将编写一个简单的Python应用程序，它在方法find()中使用参数fields来限制返回的字段。通过这个示例，您将熟悉如何使用方法find()的参数fields，并了解它对结果的影响。程序清单17.3显示了这个示例的代码。
> 在这个示例中，函数__main__连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找文档并显示其指定的字段。方法displayCursor()迭代游标并显示找到的文档。
> 方法includeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，使其只返回指定的字段；方法excludeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，以排除指定的字段。
> 请执行如下步骤，创建并运行这个Python应用程序，它在示例数据集中查找文档、限制返回的字段并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour17中新建一个文件，并将其命名为PythonFindFields.py。
> 4．在这个文件中输入程序清单17.3所示的代码。这些代码在调用方法find()时传递了参数fields。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour17。
> 7．执行下面的命令来运行这个Python应用程序。程序清单17.4显示了这个应用程序的输出。
> **程序清单17.3 PythonFindFields.py：在Python应用程序中限制从集合返回的文档包含的字段**
> **程序清单17.4 PythonFindFields.py-output：在Python应用程序中限制从集合返回的文档包含的字段的输出**
> ▲

为限制文档检索时返回的数据量，另一种极有效的方式是限制要返回的字段。文档可能有很多字段在有些情况下很有用，但在其他情况下没用。从MongoDB服务器检索文档时，需考虑应包含哪些字段，并只请求必要的字段。

要对Collection对象的方法find()从服务器返回的字段进行限制，可使用参数fields。这个参数是一个Dictionary对象，它使用值True来包含字段，使用值False来排除字段。

例如，要在返回文档时排除字段stats、value和comments，可使用下面的fields参数：

```go
fields = {'stats' : false, 'value' : false, 'comments' : False);
cursor = myColl.find(None, fields)
```

这里将查询对象指定成了None，因为您要查找所有的文档。

仅包含所需的字段通常更容易。例如，如果只想返回first字段为t的文档的word和size字段，可使用下面的代码：

```go
query = {'first' : 't'}
fields = {'word' : true, 'size' : True}
cursor = myColl.find(query, fields)
```

▼　Try It Yourself

```go
python PythonFindFields.py
```

```go
01 from pymongo import MongoClient
02 def displayCursor(cursor):
03      print (cursor)
04 def includeFields(collection, fields):
05      query = {'first': 'p'}
06      fieldObj = {}
07      for field in fields:
08         fieldObj[field] = True
09      word = collection.find_one(query, fieldObj)
10      print ("\nIncluding " + str(fields) +" fields:")
11      displayCursor(word)
12 def excludeFields(collection, fields):
13      query = {'first': 'p'}
14      if not len(fields):
15           fieldObj = None
16      else:
17           fieldObj = {}
18           for field in fields:
19              fieldObj[field] = False
20      doc = collection.find_one(query, fieldObj)
21      print ("\nExcluding " + str(fields) + " fields:")
22      displayCursor(doc)
23 if __name__=="__main__":
24      mongo = MongoClient('mongodb://localhost:27017/')
25      db = mongo['words']
26      collection = db['word_stats']
27      excludeFields(collection, [])
28      includeFields(collection, ['word', 'size'])
29      includeFields(collection, ['word', 'letters'])
30      excludeFields(collection, ['letters', 'stats', 'charsets'])
```

```go
Excluding [] fields:
{ 'stats': {'consonants': 3.0, 'vowels': 3.0}, 'last': 'e',
  'charsets': [{'chars': ['p', 'l'], 'type': 'consonants'},
                  {'chars': ['e', 'o'], 'type': 'vowels'}],
  'first': 'p', 'letters': ['p', 'e', 'o', 'l'], 'word': 'people',
  '_id': ObjectId('52e89477c25e849855325fa7'), 'size': 6.0}
Including ['word', 'size'] fields:
{'_id': ObjectId('52e89477c25e849855325fa7'), 'word': 'people', 'size': 6.0}
Including ['word', 'letters'] fields:
{ 'letters': ['p', 'e', 'o', 'l'],
  '_id': ObjectId('52e89477c25e849855325fa7'), 'word': 'people'}
Excluding ['letters', 'stats', 'charsets'] fields:
{ 'last': 'e', 'first': 'p', 'letters': ['p', 'e', 'o', 'l'],
  'word': 'people', '_id': ObjectId('52e89477c25e849855325fa7'), 'size': 6.0}
```

