### 24.5.1　在Python中访问MongoDB GridFS

在Python中，通过GridFS对象来访问MongoDB GridFS。这种对象提供了列出、添加、获取和删除MongoDB GridFS文件所需的方法。要访问MongoDB GridFS，首先需要使用下面的语法获取一个GridFS对象实例，其中db是一个Databese对象：

```go
fs = gridfs.GridFs(db)
```

例如，下面的Python代码获取一个GridFS对象实例：

```go
mongo = MongoClient('mongodb://localhost:27017/')
db = mongo['myFS']
fs = gridfs.GridFs(db)
```

