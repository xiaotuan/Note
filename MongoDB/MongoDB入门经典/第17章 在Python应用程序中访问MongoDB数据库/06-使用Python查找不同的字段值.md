### 17.2 使用Python查找不同的字段值

> **使用Python检索一组文档中指定字段的不同值**
> 在本节中，您将编写一个Python应用程序，它使用Collection对象的方法distinct()来检索示例数据库中不同的字段值。通过这个示例，您将熟练地生成数据集中的不同字段值列表。程序清单17.7显示了这个示例的代码。
> 在这个示例中，函数__main__连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来找出并显示不同的字段值。
> 方法sizesOfAllWords()找出并显示所有单词的各种长度；方法sizesOfQWords()找出并显示以q打头的单词的各种长度；方法firstLetterOfLongWords()找出并显示长度超过12的单词的各种长度。
> 请执行下面的步骤，创建并运行这个Python应用程序，它找出示例数据集中文档集的不同字段值，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour17中新建一个文件，并将其命名为PythonFindDistinct.py。
> 4．在这个文件中输入程序清单17.7所示的代码。这些代码对文档集执行distinct()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour17。
> 7．执行下面的命令来运行这个Python应用程序。程序清单17.8显示了这个应用程序的输出。
> **程序清单17.7 PythonFindDistinct.py：在Python应用程序中找出文档集中不同的字段值**
> **程序清单17.8 PythonFindDistinct.py-output：在Python应用程序中找出文档集中不同字段值的输出**
> ▲

一种很有用的MongoDB集合查询是，获取一组文档中某个字段的不同值列表。不同（distinct）意味着纵然有数千个文档，您只想知道那些独一无二的值。

Collection和Cursor对象的方法distinct()让您能够找出指定字段的不同值列表，这个方法的语法如下：

```go
distinct(key)
```

其中参数key是一个字符串，指定了要获取哪个字段的不同值。要获取子文档中字段的不同值，可使用句点语法，如stats.count。如果要获取部分文档中指定字段的不同值，可先使用查询生成一个Cursor对象，再对这个Cursor对象调用方法distinct()。

例如，假设有一些包含字段first、last和age的用户文档，要获取年龄超过65岁的用户的不同姓，可使用下面的操作：

```go
query = {'age' : {'$gt' : 65}}
cursor = myCollection.find(query)
lastNames = cursor.distinct('last')
```

方法distinct()返回一个数组，其中包含指定字段的不同值，例如：

```go
["Smith", "Jones", ...]
```

▼　Try It Yourself

```go
python PythonFindDistinct.py
```

```go
01 from pymongo import MongoClient
02 def sizesOfAllWords(collection):
03      results = collection.distinct("size")
04      print ("\nDistinct Sizes of words: ")
05      print (str(results))
06 def sizesOfQWords(collection):
07      query = {'first': 'q'}
08      cursor = collection.find(query)
09      results = cursor.distinct("size")
10      print ("\nDistinct Sizes of words starting with Q:")
11      print (str(results))
12 def firstLetterOfLongWords(collection):
13      query = {'size': {'$gt': 12}}
14      cursor = collection.find(query)
15      results = cursor.distinct("first")
16      print ("\nDistinct first letters of words longer than" + \
17                " 12 characters:")
18      print (str(results))
19 if __name__=="__main__":
20      mongo = MongoClient('mongodb://localhost:27017/')
21      db = mongo['words']
22      collection = db['word_stats']
23      sizesOfAllWords(collection)
24      sizesOfQWords(collection)
25      firstLetterOfLongWords(collection)
```

```go
Distinct Sizes of words:
[3.0, 2.0, 1.0, 4.0, 5.0, 9.0, 6.0, 7.0, 8.0, 10.0, 11.0, 12.0, 13.0, 14.0]
Distinct Sizes of words starting with Q:
[8.0, 5.0, 7.0, 4.0]
Distinct first letters of words longer than 12 characters:
['i', 'a', 'e', 'r', 'c', 'u', 's', 'p', 't']
```

