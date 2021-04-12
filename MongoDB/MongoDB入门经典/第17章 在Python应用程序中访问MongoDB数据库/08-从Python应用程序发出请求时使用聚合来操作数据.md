### 17.4 从Python应用程序发出请求时使用聚合来操作数据

> **在Python应用程序中使用聚合来生成数据**
> 在本节中，您将编写一个简单的Python应用程序，它使用Collection对象的方法aggregate()从示例数据库检索各种聚合数据。通过这个示例，您将熟悉如何使用aggregate()来利用聚合流水线在MongoDB服务器上处理数据，再返回结果。程序清单17.11显示了这个示例的代码。
> 在这个示例中，函数__main__连接到MongoDB数据库，获取一个Collection对象，并调用其他方法来聚合数据并显示结果。方法displayAggregate()显示聚合结果。
> 方法largeSmallVowels()使用了一条包含运算符$match、$group和$sort的聚合流水线，这条流水线查找以元音字母开头的单词，根据第一个字母将这些单词分组，并找出各组中最长和最短单词的长度。
> 方法top5AverageWordFirst()使用了一条包含运算符$group、$sort和$limit的聚合流水线，这条流水线根据第一个字母将单词分组，并找出单词平均长度最长的前5组。
> 请执行下面的步骤，创建并运行这个Python应用程序，它使用聚合流水线来处理示例数据集中的文档，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour17中新建一个文件，并将其命名为PythonAggregate.py。
> 4．在这个文件中输入程序清单17.11所示的代码。这些代码对文档集执行aggregate()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour17。
> 7．执行下面的命令来运行这个Python应用程序。程序清单17.12显示了这个应用程序的输出。
> **程序清单17.11 PythonAggregate.py：在Python应用程序中使用聚合流水线生成数据集**
> **程序清单17.12 PythonAggregate.py-output：在Python应用程序中使用聚合流水线生成数据集的输出**
> ▲

在Python应用程序中使用MongoDB时，另一个很有用的工具是聚合框架。Collection对象提供了对数据执行聚合操作的方法aggregate()，这个方法的语法如下：

```go
aggregate(operator, [operator, ...])
```

参数operator是一系列运算符对象，提供了用于聚合数据的流水线。这些运算符对象是使用聚合运算符创建的Dictionary对象。聚合运算符在第9章介绍过，您现在应该熟悉它们。

例如，下面的代码定义了运算符$group和$limit，其中运算符$group根据字段word进行分组（并将该字段的值存储在结果文档的_id字段中），使用$avg计算size字段的平均值（并将结果存储在average字段中）。请注意，在聚合运算中引用原始文档的字段时，必须在字段名前加上$：

```go
group = {'$group' :
                   {'_id' : '$word',
                     'average' : {'$avg' : '$size'}}}
limit = {'$limit' : 10}
result = collection.aggregate([group, limit])
```

方法aggregate()返回一个Dictionary对象。这个Dictionary对象包含一个result键，而该键对应的值是一个包含聚合结果的列表。为演示这一点，下面的代码逐项显示聚合结果的内容：

```go
for result in results['result']:
     print (result)
```

▼　Try It Yourself

```go
python PythonAggregate.py
```

```go
01 from pymongo import MongoClient
02 def displayAggregate(results):
03      for result in results['result']:
04           print (result)
05 def largeSmallVowels(collection):
06      match = {'$match' :
07                   {'first' :
08                         {'$in' : ['a','e','i','o','u']}}}
09      group = {'$group' :
10                   {'_id' : '$first',
11                           'largest' : {'$max' : '$size'},
12                           'smallest' : {'$min' : '$size'},
13                           'total' : {'$sum' : 1}}};
14      sort = {'$sort' : {'first' : 1}};
15      result = collection.aggregate([match, group, sort])
16      print ("\nLargest and smallest word sizes for " + \
17              "words beginning with a vowel:")
18      displayAggregate(result)
19 def top5AverageWordFirst(collection):
20      group = {'$group' :
21                   {'_id' : '$first',
22                          'average' : {'$avg' : '$size'}}}
23      sort = {'$sort' : {'average' : -1}}
24      limit = {'$limit' : 5}
25      result = collection.aggregate([group, sort, limit]);
26      print ("\nFirst letter of top 5 largest average " + \
27               "word size:")
28      displayAggregate(result)
29 if __name__=="__main__":
30      mongo = MongoClient('mongodb://localhost:27017/')
31      db = mongo['words']
32      collection = db['word_stats']
33      largeSmallVowels(collection)
34      top5AverageWordFirst(collection)
```

```go
Largest and smallest word sizes for words beginning with a vowel:
{'total': 150, '_id': 'e', 'smallest': 3.0, 'largest': 13.0}
{'total': 33, '_id': '', 'smallest': 2.0, 'largest': 13.0}
{'total': 114, '_id': 'i', 'smallest': 1.0, 'largest': 14.0}
{'total': 72, '_id': 'o', 'smallest': 2.0, 'largest': 12.0}
{'total': 192, '_id': 'a', 'smallest': 1.0, 'largest': 14.0}
First letter of top 5 largest average word size:
{'average': 7.947368421052632, '_id': 'i'}
{'average': 7.42, '_id': 'e'}
{'average': 7.292134831460674, '_id': 'c'}
{'average': 6.881818181818182, '_id': 'p'}
{'average': 6.767123287671233, '_id': 'r'}
```

