### 17.1.3 使用Python将结果集分页

> **在Python中使用skip()和limit()对MongoDB集合中的文档进行分页**
> 在本节中，您将编写一个简单的Python应用程序，它使用Cursor对象的方法skip()和limit()方法对find()返回的大量文档进行分页。通过这个示例，您将熟悉如何使用skip()和limit()对较大的数据集进行分页。程序清单17.5显示了这个示例的代码。
> 在这个示例中，函数__main__连接到MongoDB数据库，获取一个Collection对象，并调用其他的方法来查找文档并以分页方式显示它们。方法displayCursor()迭代游标并显示当前页中的单词。
> 方法pageResults()接受一个skip参数，并根据它以分页方式显示以w开头的所有单词。每显示一页后，都将skip值递增，直到到达游标末尾。
> 请执行下面的步骤，创建并运行这个对示例数据集中的文档进行分页并显示结果的Python应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Python MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour17中新建一个文件，并将其命名为PythonFindPaging.py。
> 4．在这个文件中输入程序清单17.5所示的代码。这些代码实现了文档集分页。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour17。
> 7．执行下面的命令来运行这个Python应用程序。程序清单17.6显示了这个应用程序的输出。
> **程序清单17.5 PythonFindPaging.py：在Python应用程序中分页显示集合中的文档集**
> **程序清单17.6 PythonFindPaging.py-output：在Python应用程序中分页显示集合中的文档集的输出**
> ▲

为减少返回的文档数，一种常见的方法是进行分页。要进行分页，需要指定要在结果集中跳过的文档数，还需限制返回的文档数。跳过的文档数将不断增加，每次的增量都是前一次返回的文档数。

要对一组文档进行分页，需要使用Cursor对象的方法limit()和skip()。方法skip()让您能够指定在返回文档前要跳过多少个文档。

每次获取下一组文档时，都增大方法skip()中指定的值，增量为前一次调用limit()时指定的值，这样就实现了数据集分页。

例如，下面的语句查找第11～20个文档：

```go
cursor = collection.find()
cursor.limit(10)
cursor.skip(10)
```

进行分页时，务必调用方法sort()来确保文档的排列顺序不变。

▼　Try It Yourself

```go
python PythonFindPaging.py
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
09 def pageResults(collection, skip):
10      query = {'first': 'w'}
11      cursor = collection.find(query)
12      cursor.limit(10)
13      cursor.skip(skip)
14      print ("Page " + str(skip+1) + " to " + \
15             str(skip + cursor.count(True)) + ":")
16      displayCursor(cursor);
17      if(cursor.count(True) == 10):
18        pageResults(collection, skip+10);
19 if __name__=="__main__":
20      mongo = MongoClient('mongodb://localhost:27017/')
21      db = mongo['words']
22      collection = db['word_stats']
23      pageResults(collection, 0)
```

```go
Page 1 to 10:
with,won't,we,what,who,would,will,when,which,want,
Page 11 to 20:
way,well,woman,work,world,while,why,where,week,without,
Page 21 to 30:
water,write,word,white,whether,watch,war,within,walk,win,
Page 31 to 40:
wait,wife,whole,wear,whose,wall,worker,window,wrong,west,
Page 41 to 50:
whatever,wonder,weapon,wide,weight,worry,writer,whom,wish,western...
Page 51 to 60:
wind,weekend,wood,winter,willing,wild,worth,warm,wave,wonderful,
Page 61 to 70:
wine,writing,welcome,weather,works,wake,warn,wing,winner,welfare,
Page 71 to 80:
witness,waste,wheel,weak,wrap,warning,wash,widely,wedding,wheneve...
Page 81 to 90:
wire,whisper,wet,weigh,wooden,wealth,wage,wipe,whereas,withdraw,
Page 91 to 93:
working,wisdom,wealthy,
```

