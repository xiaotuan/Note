### 16.3　使用Python计算文档数

> **在** Python应用程序中使用 **count** ()获取 **Cursor** 对象表示的文档数
> 在本节中，您将编写一个简单的Python应用程序，它使用查询对象和find()从示例数据库检索特定的文档集，并使用count()来获取游标表示的文档数。通过这个示例，您将熟悉如何在检索并处理文档前获取文档数。程序清单16.7显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来查找特定的文档并显示找到的文档数。方法countWords()使用查询对象、find()和count()来计算数据库中的单词总数以及以a打头的单词数。
> 请执行如下步骤，创建并运行这个Python应用程序，它查找示例数据集中的特定文档，计算找到的文档数并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour16中新建一个文件，并将其命名为PythonFindCount.py。
> 4．在这个文件中输入程序清单16.7所示的代码。这些代码使用方法find()和查询对象查找特定文档，并计算找到的文档数。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour16。
> 7．执行下面的命令来运行这个Python应用程序。程序清单16.8显示了这个应用程序的输出。
> **程序清单16.7　PythonFindCount.py：在Python应用程序中计算在集合中找到的特定文档的数量**
> **程序清单16.8　PythonFindCount.py-output：在Python应用程序中计算在集合中找到的特定文档数量的输出**
> ▲

使用Python访问MongoDB数据库中的文档集时，您可能想先确定文档数，再决定是否检索它们。无论是在MongoDB服务器还是客户端，计算文档数的开销都很小，因为不需要传输实际文档。

Cursor对象的方法count()让您能够获取游标表示的文档数。例如，下面的代码使用方法find()来获取一个Cursor对象，再使用方法count()来获取文档数：

```go
cursor = wordsColl.find()
itemCount = cursor.count()
```

itemCount的值为与find()操作匹配的单词数。

▼　Try It Yourself

```go
python PythonFindCount.py
```

```go
01 from pymongo import MongoClient
02 def countWords(collection):
03      cursor = collection.find();
04      print ("Total words in the collection:")
05      print (cursor.count())
06      query = {'first': 'a'}
07      cursor = collection.find(query)
08      print ("\nTotal words starting with A:")
09      print (cursor.count())
10 if __name__=="__main__":
11     mongo = MongoClient('mongodb://localhost:27017/')
12     db = mongo['words']
13     collection = db['word_stats']
14     countWords(collection)
```

```go
Total words in the collection:
2673
Total words starting with A:
192
```

