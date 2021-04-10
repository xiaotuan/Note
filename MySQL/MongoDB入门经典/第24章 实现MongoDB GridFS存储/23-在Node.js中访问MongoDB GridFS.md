### 24.6.1　在Node.js中访问MongoDB GridFS

在Node.js中，通过GridStore对象来访问MongoDB GridFS。这种对象提供了列出、添加、获取和删除MongoDB GridFS文件所需的方法。要访问MongoDB GridFS，需要获取一个GridStore对象实例来将数据写入GridFS。然而，您也可以调用其静态方法来列出和删除文件。要创建用于写入的GridStore对象，可使用如下语法，其中db是一个Db对象：

```go
myFS = new GridStore(db, filename, mode, [options]);
```

例如，下面的Node.js代码获取一个用于写入文件的GridStore对象实例：

```go
mongo.connect("mongodb://localhost/myFS", function(err, db) {
   var myFS = new GridStore(db, 'myFile.txt', 'w');
});
```

