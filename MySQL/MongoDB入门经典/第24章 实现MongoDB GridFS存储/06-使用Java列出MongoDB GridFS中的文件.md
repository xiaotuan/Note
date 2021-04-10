### 24.3.2　使用Java列出MongoDB GridFS中的文件

有了Java对象GridFS的实例后，就可使用方法getFileList()列出MongoDB GridFS中的文件了。可使用下述格式之一来调用getFileList()：

```go
getFileList()
getFileList(DBObject query)
getFileList(DBObject query, DBObject sort)
```

通过指定标准查询对象和排序对象，可限制返回的文件。方法getFileList()返回一个DBCursor对象，包含GridFS存储区中与查询匹配的文件。必要时可使用这个DBCursor来遍历文件。

例如，下面的代码遍历GridFS存储区中所有的文件：

```go
GridFS myFS = new GridFS(db);
DBCursor files = myFS.getFileList();
for(final DBObject file : files) {
   System.out.println(file);
}
```

