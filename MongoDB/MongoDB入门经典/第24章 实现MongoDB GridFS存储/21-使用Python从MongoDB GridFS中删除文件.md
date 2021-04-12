### 24.5.5　使用Python从MongoDB GridFS中删除文件

> **使用Python访问和操作MongoDB GridFS存储区中的文件**
> 本节将引导您完成在Python应用程序中实现MongoDB GridFS存储的流程，包括访问MongoDB GridFS以及列出、添加、获取和删除文件的步骤。
> 在这个示例中，主脚本连接到MongoDB数据库，并调用各种方法来访问GridFS以列出、添加、获取和删除文件。
> 方法listGridFSFiles()用于在Python应用程序运行期间的各个时点显示MongoDB GridFS中当前存储的文件；方法putGridFSFile()将一个文件存储到GridFS中；方法getGridFSFile()从GridFS获取一个文件并显示其内容；方法deleteGridFSFile()从GridFS中删除文件。
> 请执行如下步骤，使用Python列出、获取、添加和删除文件。
> 1．确保启动了MongoDB服务器。
> 2．确保安装并配置了Python MongoDB驱动程序。
> 3．在文件夹code/hour24中新建一个文件，并将其命名为PythonGridFS.py。
> 4．在这个文件中输入程序清单24.5所示的代码。这些代码访问MongoDB GridFS。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour24。
> 7．执行下面的命令运行这个Python应用程序。程序清单24.6显示了这个应用程序的输出。
> **程序清单24.5　PythonGridFS.py：使用Python列出、添加、获取和删除MongoDB GridFS中的文件**
> **程序清单24.6　PythonGridFS.py-output：使用Python列出、添加、获取和删除MongoDB GridFS中文件的输出**
> ▲

在Python中，要将文件从GridFS存储区中删除，最简单的方式是使用GridFS对象的方法remove()。这个方法将文件从MongoDB GridFS存储区中删除，其语法如下：

```go
delete(objected)
```

调用方法delete()时需要指定一个objectId，因此您需要使用获取方法返回的GridOut对象的_id属性。例如，下面的语句删除文件python.txt：

```go
fs = gridfs.GridFS(db)
file = fs.get_last_version(filename="python.txt")
fs.delete(file._id)
```

▼　Try It Yourself

```go
python PythonGridFS.py
```

```go
01 from pymongo import MongoClient
02 import gridfs
03 def listGridFSFiles(db):
04      fs = gridfs.GridFS(db)
05      print (fs.list())
06 def putGridFSFile(db):
07      fs = gridfs.GridFS(db)
08      fs.put("Stored From Python", filename="python.txt", encoding="utf8")
09 def getGridFSFile(db):
10      fs = gridfs.GridFS(db)
11      file = fs.get_last_version(filename="python.txt")
12      print (file.read())
13 def deleteGridFSFile(db):
14      fs = gridfs.GridFS(db)
15      file = fs.get_last_version(filename="python.txt")
16      fs.delete(file._id)
17 if __name__=="__main__":
18      mongo = MongoClient('mongodb://localhost:27017/')
19      mongo.write_concern = {'w' : 1, 'j' : True}
20      db = mongo['myFS']
21      print ("\nFiles Before Put:")
22      listGridFSFiles(db)
23      putGridFSFile(db)
24      print ("\nFiles After Put:")
25      listGridFSFiles(db)
26      print ("\nContents of Retrieve File:")
27      getGridFSFile(db)
28      deleteGridFSFile(db)
29      print ("\nFiles After Delete:")
30      listGridFSFiles(db)
```

```go
Files Before Put:
[]
Files After Put:
[u'python.txt']
Contents of Retrieve File:
Stored From Python
Files After Delete:
[]
```

