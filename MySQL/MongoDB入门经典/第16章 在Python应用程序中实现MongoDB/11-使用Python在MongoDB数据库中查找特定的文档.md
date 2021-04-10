### 16.2.2　使用Python在MongoDB数据库中查找特定的文档

> **使用** Python从 **MongoDB** 数据库检索特定的文档
> 在本节中，您将编写一个简单的Python应用程序，它使用查询对象和方法find()从示例数据库检索一组特定的文档。通过这个示例，您将熟悉如何创建查询对象以及如何使用它们来显示数据库请求返回的文档。程序清单16.4显示了这个示例的代码。
> 在这个示例中，函数 **main** 连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找并显示特定的文档。方法displayCursor()迭代游标并显示它表示的单词。
> 方法over12()查找长度超过12的单词；方法startingABC()查找以a、b或c打头的单词；方法startEndVowels()查找以元音字母打头和结尾的单词；方法over6Vowels()查找包含的元音字母超过6个的单词；方法nonAlphaCharacters()查找包含类型为other的字符集且长度为1的单词。
> 请执行如下步骤，创建并运行这个在示例数据集中查找特定文档并显示结果的Python应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour16中新建一个文件，并将其命名为PythonFindSpecific.py。
> 4．在这个文件中输入程序清单16.5所示的代码。这些代码使用了方法find()和查询对象。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour16。
> 7．执行下面的命令来运行这个Python应用程序。程序清单16.6显示了这个应用程序的输出。
> **程序清单16.5　PythonFindSpecific.py：在Python应用程序中从集合中查找并检索特定文档**
> **程序清单16.6　PythonFindSpecific.py-output：在Python应用程序中从集合中查找并检索特定文档的输出**
> ▲

一般而言，您不会想从服务器检索集合中的所有文档。方法find()和find_one()让您能够向服务器发送一个查询对象，从而像在MongoDB shell中那样限制文档。

要创建查询对象，可使用本章前面描述的Dictionary对象。对于查询对象中为子对象的字段，可创建Dictionary子对象；对于其他类型（如整型、字符串和数组）的字段，可使用相应的Python类型。

例如，要创建一个查询对象来查找size=5的单词，可使用下面的代码：

```go
query = {'size' : 5}
myColl.find(query)
```

要创建一个查询对象来查找size>5的单词，可使用下面的代码：

```go
query = {'size' :
     {'$gt' : 5}}
myColl.find(query)
```

要创建一个查询对象来查找第一个字母为x、y或z的单词，可使用String数组，如下所示：

```go
query = {'first' :
     {'$in' : ["x", "y", "z"]}}
myColl.find(query)
```

利用上述技巧可创建需要的任何查询对象：不仅能为查找操作创建查询对象，还能为其他需要查询对象的操作这样做。

▼　Try It Yourself

```go
python PythonFindSpecific.py
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
09 def over12(collection):
10    print ("\n\nWords with more than 12 characters:")
11    query = {'size': {'$gt': 12}}
12    cursor = collection.find(query)
13    displayCursor(cursor)
14 def startingABC(collection):
15    print ("\nWords starting with A, B or C:")
16    query = {'first': {'$in': ["a","b","c"]}}
17    cursor = collection.find(query)
18    displayCursor(cursor)
19 def startEndVowels(collection):
20    print ("\nWords starting and ending with a vowel:")
21    query = {'$and': [
22                {'first': {'$in': ["a","e","i","o","u"]}},
23                {'last': {'$in': ["a","e","i","o","u"]}}]}
24    cursor = collection.find(query)
25    displayCursor(cursor)
26 def over6Vowels(collection):
27    print ("\nWords with more than 5 vowels:")
28    query = {'stats.vowels': {'$gt': 5}}
29    cursor = collection.find(query)
30    displayCursor(cursor)
31 def nonAlphaCharacters(collection):
32    print ("\nWords with 1 non-alphabet characters:")
33    query = {'charsets':
34         {'$elemMatch':
35           {'$and': [
36             {'type': 'other'},
37             {'chars': {'$size': 1}}]}}}
38    cursor = collection.find(query)
39    displayCursor(cursor)
40 if __name__=="__main__":
41    mongo = MongoClient('mongodb://localhost:27017/')
42    db = mongo['words']
43    collection = db['word_stats']
44    over12(collection)
45    startEndVowels(collection)
46    over6Vowels(collection)
47    nonAlphaCharacters(collection)
```

```go
Words with more than 12 characters:
international,administration,environmental,responsibility,investi...
Words starting and ending with a vowel:
a,i,one,into,also,use,area,eye,issue,include,once,idea,ago,office...
Words with more than 5 vowels:
international,organization,administration,investigation,communica...
Words with 1 non-alphabet characters:
don't,won't,can't,shouldn't,e-mail,long-term,so-called,mm-hmm,
```

