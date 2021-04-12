### 17.1.1 使用Python限制结果集的大小

> **使用将对象表示的文档减少到指定的数量**
> 在本节中，您将编写一个简单的Python应用程序，它使用limit()来限制find()操作返回的结果。通过这个示例，您将熟悉如何结合使用limit()和find()，并了解limit()对结果的影响。程序清单17.1显示了这个示例的代码。
> 在这个示例中，函数__main__连接到MongoDB数据库，获取一个Collection对象，并调用其他方法来查找并显示数量有限的文档。方法displayCursor()迭代游标并显示找到的单词。
> 方法limitResults()接受一个limit参数，查找以p打头的单词，并返回参数limit指定的单词数。
> 请执行如下步骤，创建并运行这个Python应用程序，它在示例数据集中查找指定数量的文档并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour17中新建一个文件，并将其命名为PythonFindLimit.py。
> 4．在这个文件中输入程序清单17.1所示的代码。这些代码使用了方法find()和limit()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour17。
> 7．执行下面的命令来运行这个Python应用程序。程序清单17.2显示了这个应用程序的输出。
> **程序清单17.1 PythonFindLimit.py：在Python应用程序中在集合中查找指定数量的文档**
> **程序清单17.2 PythonFindLimit.py-output：在Python应用程序中在集合中查找指定数量文档的输出**
> ▲

要限制find()或其他查询请求返回的数据量，最简单的方法是对find()操作返回的Cursor对象调用方法limit()，它让Cursor对象返回指定数量的文档，可避免检索的对象量超过应用程序的处理能力。

例如，下面的代码只显示集合中的前10个文档，即便匹配的文档有数千个：

```go
cursor = wordsColl.find()
cursor.limit(10)
for word in cursor:
   print (word)
```

▼　Try It Yourself

```go
python PythonFindLimit.py
```

```go
01 from pymongo import MongoClient
02 def displayCursor(cursor):
03      words = ''
04      for doc in cursor:
05         words += doc["word"] + ","
06      if len(words) > 65:
07         words = words[:65] + "..."
08      print (words)
09 def limitResults(collection, limit):
10      query = {'first': 'p'}
11      cursor = collection.find(query)
12      cursor.limit(limit)
13      print ("\nP words Limited to " + str(limit) +" :")
14      displayCursor(cursor)
15 if __name__=="__main__":
16      mongo = MongoClient('mongodb://localhost:27017/')
17      db = mongo['words']
18      collection = db['word_stats']
19      limitResults(collection, 1)
20      limitResults(collection, 3)
21      limitResults(collection, 5)
22      limitResults(collection, 7)
```

```go
P words Limited to 1 :
people,
P words Limited to 3 :
people,put,problem,
P words Limited to 5 :
people,put,problem,part,place,
P words Limited to 7 :
people,put,problem,part,place,program,play,
```

