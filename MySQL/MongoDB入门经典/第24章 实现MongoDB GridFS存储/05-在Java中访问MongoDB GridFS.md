### 24.3.1　在Java中访问MongoDB GridFS

在Java中，通过GridFS对象来访问MongoDB GridFS。这种对象提供了列出、添加、获取和删除MongoDB GridFS文件所需的方法。要访问MongoDB GridFS，首先需要使用下面的语法获取一个GridFS对象实例，其中db是一个DB对象：

```go
GridFS myFS = new GridFS(db)
```

例如，下面的Java代码获取一个GridFS对象实例：

```go
import com.mongodb.MongoClient;
import com.mongodb.DB;
import com.mongodb.gridfs.GridFS;
MongoClient mongoClient = new MongoClient("localhost", 27017);
DB db = mongoClient.getDB("myFS");
GridFS myFS = new GridFS(db);
```

