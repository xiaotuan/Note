### 16.4　使用Python对结果集排序

> **使用sort ()以特定顺序返回Python对象Cursor表示的文档**
> 在本节中，您将编写一个简单的Python应用程序，它使用查询对象和方法find()从示例数据库检索特定的文档集，再使用方法sort()将游标中的文档按特定顺序排列。通过这个示例，您将熟悉如何在检索并处理文档前对游标表示的文档进行排序。程序清单16.9显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，再调用其他的方法来查找特定的文档，对找到的文档进行排序并显示结果。方法displayCursor()显示排序后的单词列表。
> 方法sortWordsAscending()获取以w打头的单词并将它们按升序排列；方法sortWordsDescending()获取以w打头的单词并将它们按降序排列；方法sortWordsAscAndSize()获取以q打头的单词，并将它们首先按最后一个字母升序排列，再按长度降序排列。
> 执行下面的步骤，创建并运行这个Python应用程序，它在示例数据集中查找特定的文档，对找到的文档进行排序并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour16中新建一个文件，并将其命名为PythonFindSort.py。
> 4．在这个文件中输入程序清单16.9所示的代码。这些代码对Cursor对象表示的文档进行排序。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour16。
> 7．执行下面的命令来运行这个Python应用程序。程序清单16.10显示了这个应用程序的输出。
> **程序清单16.9　PythonFindSort.py：在Python应用程序中查找集合中的特定文档并进行排序**
> **程序清单16.10　PythonFindSort.py-output：在Python应用程序中查找集合中的特定文档并进行排序的输出**
> ▲

从MongoDB数据库检索文档时，一个重要方面是对文档进行排序。只想检索特定数量（如前10个）的文档或要对结果集进行分页时，这特别有帮助。排序选项让您能够指定用于排序的文档字段和方向。

Cursor对象的方法sort()让您能够指定要根据哪些字段对游标中的文档进行排序，并按相应的顺序返回文档。方法sort()将一个元组（(key, order)对）列表作为参数，其中key是要用于排序的字段名，而order为1（升序）或-1（降序）。

例如，要按字段name升序排列文档，可使用下面的代码：

```go
sorter = [('name', 1)]
cursor = myCollection.find()
cursor.sort(sorter)
```

在传递给方法sort()的列表中，可指定多个字段，这样文档将按这些字段排序。还可对同一个游标调用sort()方法多次，从而依次按不同的字段进行排序。例如，要首先按字段name升序排列，再按字段value降序排列，可使用下面的代码：

```go
sorter = [('name', 1), ('value', -1)];
cursor = myCollection.find()
cursor.sort(sorter)
```

也可使用下面的代码：

```go
sorter1 = [('name', 1)]
sorter2 = [('value', -1)]
cursor = myCollection.find()
cursor = cursor.sort(sorter1)
cursor.sort(sorter2)
```

▼　Try It Yourself

```go
python PythonFindSort.py
```

```go
01 from pymongo import MongoClient
02 def displayCursor(cursor):
03    words = ''
04    for doc in cursor:
05       words += doc["word"] + ","
06    if len(words) > 65:
07       words = words[:65] + "..."
08    print (words)
09 def sortWordsAscending(collection):
10    query = {'first': 'w'}
11    cursor = collection.find(query)
12    sorter = [('word', 1)]
13    cursor.sort(sorter)
14    print ("\nW words ordered ascending:")
15    displayCursor(cursor)
16 def sortWordsDescending(collection):
17    query = {'first': 'w'}
18    cursor = collection.find(query)
19    sorter = [('word', -1)]
20    cursor.sort(sorter)
21    print ("\n\nW words ordered descending:")
22    displayCursor(cursor)
23 def sortWordsAscAndSize(collection):
24    query = {'first': 'q'}
25    cursor = collection.find(query)
26    sorter = [('last', 1), ('size', -1)]
27    cursor.sort(sorter)
28    print ("\nQ words ordered first by last letter " + \
29            "and then by size:")
30    displayCursor(cursor)
31 if __name__=="__main__":
32       mongo = MongoClient('mongodb://localhost:27017/')
33       db = mongo['words']
34       collection = db['word_stats']
35       sortWordsAscending(collection)
36       sortWordsDescending(collection)
37       sortWordsAscAndSize(collection)
```

```go
W words ordered ascending:
wage,wait,wake,walk,wall,want,war,warm,warn,warning,wash,waste,wa...
W words ordered descending:
wrong,writing,writer,write,wrap,would,worth,worry,world,works,wor...
Q words ordered first by last letter and then by size:
quite,quote,quick,question,quarter,quiet,quit,quickly,quality,qui...
```

