### 24.4.1　在PHP中访问MongoDB GridFS

在PHP中，通过MongoGridFS对象来访问MongoDB GridFS。这种对象提供了列出、添加、获取和删除MongoDB GridFS文件所需的方法。要访问MongoDB GridFS，首先需要使用下面的语法获取一个MongoGridFS对象实例，其中$db是一个MongoDB对象：

```go
$db->getGridFS();
```

例如，下面的PHP代码获取一个MongoGridFS对象实例：

```go
$mongo = new MongoClient("");
$db = $mongo->myFS;
$db->getGridFS();
```

