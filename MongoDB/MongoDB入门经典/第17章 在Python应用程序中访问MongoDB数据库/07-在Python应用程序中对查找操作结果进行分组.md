### 17.3 在Python应用程序中对查找操作结果进行分组

> **使用Python根据键值将文档分组**
> 在本节中，您将创建一个简单的Python应用程序，它使用Collection对象的方法group()从示例数据库检索文档，根据指定字段进行分组，并在服务器上执行reduce和finalize函数。通过这个示例，您将熟悉如何使用group()在服务器端对数据集进行处理，以生成分组数据。程序清单17.9显示了这个示例的代码。
> 在这个示例中，函数__main__连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找文档、进行分组并显示结果。方法displayGroup()显示分组结果。
> 方法firstIsALastIsVowel()将第一个字母为a且最后一个字母为元音字母的单词分组，其中的reduce函数计算单词数，以确定每组的单词数。
> 方法firstLetterTotals()根据第一个字母分组，并计算各组中所有单词的元音字母总数和辅音字母总数。在其中的finalize函数中，将元音字母总数和辅音字母总数相加，以提供各组单词的字符总数。
> 请执行下面的步骤，创建并运行这个Python应用程序，它对示例数据集中的文档进行分组和处理，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour17中新建一个文件，并将其命名为PythonGroup.py。
> 4．在这个文件中输入程序清单17.9所示的代码。这些代码对文档集执行group()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour17。
> 7．执行下面的命令来运行这个Python应用程序。程序清单17.10显示了这个应用程序的输出。
> **程序清单17.9 PythonGroup.py：在Python应用程序中根据字段值对单词分组以生成不同的数据**
> **程序清单17.10 PythonGroup.py-output：在Python应用程序中根据字段值对单词分组以生成不同数据的输出**
> ▲

在Python中对大型数据集执行操作时，根据文档的一个或多个字段的值将结果分组通常很有用。这也可以在取回文档后使用代码来完成，但让MongoDB服务器在原本就要迭代文档的请求中这样做，效率要高得多。

在Python中，要将查询结果分组，可使用Collection对象的方法group()。分组请求首先收集所有与查询匹配的文档，再对于指定键的每个不同值，都在数组中添加一个分组对象，对这些分组对象执行操作，并返回这个分组对象数组。

方法group()的语法如下：

```go
group({key, cond , initial, reduce, [finalize]})
```

其中参数key、cond和initial都是Dictionary对象，指定了要用来分组的字段、查询以及要使用的初始文档；参数reduce和finalize为String对象，包含以字符串方式表示的JavaScript函数，这些函数将在服务器上运行以归并文档并生成最终结果。有关这些参数的更详细信息，请参阅第9章。

为演示这个方法，下面的代码实现了简单分组，它创建了对象key、cond和initial，并以字符串的方式传入了一个reduce函数：

```go
key = {'first' : True }
cond = {'first' : 'a', 'size': 5}
initial = {'count' : 0}
reduce = "function (obj, prev) { prev.count++; }"
results = collection.group(key, cond, initial, reduce)
```

方法group()返回一个包含分组结果的List。下面的代码逐项地显示了分组结果的内容：

```go
for result in results:
     print (result)
```

▼　Try It Yourself

```go
python PythonGroup.py
```

```go
01 from pymongo import MongoClient
02 def displayGroup(results):
03      for result in results:
04         print (result)
05 def firstIsALastIsVowel(collection):
06      key = {'first' : True, "last" : True}
07      cond = {'first' : 'a', 'last' :
08                         {'$in' : ["a","e","i","o","u"]}}
09      initial = {'count' : 0}
10      reduce = "function (obj, prev) { prev.count++; }"
11      results = collection.group(key, cond, initial, reduce)
12      print ("\n\n'A' words grouped by first and last" + \
13             " letter that end with a vowel:")
14      displayGroup(results)
15 def firstLetterTotals(collection):
16      key = {'first' : True}
17      cond = {}
18      initial = {'vowels' : 0, 'cons' : 0}
19      reduce = "function (obj, prev) { " + \
20                       "prev.vowels += obj.stats.vowels; " + \
21                       "prev.cons += obj.stats.consonants; " + \
22                 "}"
23      finalize = "function (obj) { " + \
24                        "obj.total = obj.vowels + obj.cons; " + \
25                   "}"
26      results = collection.group(key, cond, initial, reduce, finalize)
27      print ("\n\nWords grouped by first letter " + \
28              "with totals:")
29      displayGroup(results)
30 if __name__=="__main__":
31      mongo = MongoClient('mongodb://localhost:27017/')
32      db = mongo['words']
33      collection = db['word_stats']
34      firstIsALastIsVowel(collection)
35      firstLetterTotals(collection)
```

```go
'A' words grouped by first and last letter that end with a vowel:
{'count': 3.0, 'last': 'a', 'first': 'a'}
{'count': 2.0, 'last': 'o', 'first': 'a'}
{'count': 52.0, 'last': 'e', 'first': 'a'}
Words grouped by first letter with totals:
{'total': 947.0, 'cons': 614.0, 'vowels': 333.0, 'first': 't'}
{'total': 690.0, 'cons': 444.0, 'vowels': 246.0, 'first': 'b'}
{'total': 1270.0, 'cons': 725.0, 'vowels': 545.0, 'first': 'a'}
{'total': 441.0, 'cons': 237.0, 'vowels': 204.0, 'first': 'o'}
{'total': 906.0, 'cons': 522.0, 'vowels': 384.0, 'first': 'i'}
{'total': 393.0, 'cons': 248.0, 'vowels': 145.0, 'first': 'h'}
{'total': 701.0, 'cons': 443.0, 'vowels': 258.0, 'first': 'f'}
{'total': 67.0, 'cons': 41.0, 'vowels': 26.0, 'first': 'y'}
{'total': 474.0, 'cons': 313.0, 'vowels': 161.0, 'first': 'w'}
{'total': 947.0, 'cons': 585.0, 'vowels': 362.0, 'first': 'd'}
{'total': 1946.0, 'cons': 1233.0, 'vowels': 713.0, 'first': 'c'}
{'total': 1855.0, 'cons': 1215.0, 'vowels': 640.0, 'first': 's'}
{'total': 344.0, 'cons': 208.0, 'vowels': 136.0, 'first': 'n'}
{'total': 374.0, 'cons': 240.0, 'vowels': 134.0, 'first': 'g'}
{'total': 679.0, 'cons': 417.0, 'vowels': 262.0, 'first': 'm'}
{'total': 70.0, 'cons': 48.0, 'vowels': 22.0, 'first': 'k'}
{'total': 210.0, 'cons': 117.0, 'vowels': 93.0, 'first': 'u'}
{'total': 1514.0, 'cons': 964.0, 'vowels': 550.0, 'first': 'p'}
{'total': 120.0, 'cons': 73.0, 'vowels': 47.0, 'first': 'j'}
{'total': 488.0, 'cons': 299.0, 'vowels': 189.0, 'first': 'l'}
{'total': 260.0, 'cons': 143.0, 'vowels': 117.0, 'first': 'v'}
{'total': 1112.0, 'cons': 630.0, 'vowels': 482.0, 'first': 'e'}
{'total': 988.0, 'cons': 574.0, 'vowels': 414.0, 'first': 'r'}
{'total': 60.0, 'cons': 32.0, 'vowels': 28.0, 'first': 'q'}
{'total': 4.0, 'cons': 2.0, 'vowels': 2.0, 'first': 'z'}
```

