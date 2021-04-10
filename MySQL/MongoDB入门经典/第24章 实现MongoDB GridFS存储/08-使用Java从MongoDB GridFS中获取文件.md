### 24.3.4　使用Java从MongoDB GridFS中获取文件

在Java中，要从GridFS存储区获取文件，最简单的方式是使用GridFS对象的方法find()或findOne()。这些方法的工作原理与DBCollection对象的方法find()和findOne()类似，让您能够指定查询并返回GridFSDBFile对象。方法find()使用下面的格式，并返回一个GridFSDBFile或List<GridFSDBFile>对象：

```go
find(DBObject query)
find(DBObject query, DBObject sort)
find(ObjectId, id)
find(String filename)
find(String filename, DBObject sort)
```

方法findOne()使用下面的语法，并返回一个GridFSDBFile对象：

```go
findOne(DBObject query)
findOne(ObjectId, id)
findOne(String filename)
```

GridFSDBFile对象提供了几个很有用的方法。方法getInputStream()返回一个可从中读取数据的输入流；方法writeTo()让您能够将GridFS文件的内容写入File或OutputStream。例如，下面的代码获取一个文件，再将其内容写入磁盘：

```go
GridFS myFS = new GridFS(db);
GridFSDBFile file = myFS.findOne("java.txt");
file.writeTo(new File("JavaRetrieved.txt"));
```

