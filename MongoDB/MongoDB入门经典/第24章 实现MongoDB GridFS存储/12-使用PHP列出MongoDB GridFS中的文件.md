### 24.4.2　使用PHP列出MongoDB GridFS中的文件

有了PHP对象MongoGridFS的实例后，就可使用方法find()或findOne()来列出MongoDB GridFS中的文件了。方法find()使用下面的格式，它返回一个MongoGridFSCursor对象，其中包含一系列MongoGridFSFile对象：

```go
find([query], [fields])
```

方法findOne()使用下面的格式，它返回一个MongoGridFSFile对象：

```go
findOne([query], [fields])
```

MongoGridFSFile对象包含如下方法。

+ getBytes()：以字节字符串的方式返回文件的内容。
+ getFileName()：返回文件名。
+ getSize()：返回文件长度。
+ write(path)：将文件写入文件系统。

另外，还可使用下面的语法获取MongoGridFSFile的MongoDB ID：

```go
MongoGridFSFile->file["_id"]
```

例如，下面的代码查找并迭代GridFS存储区中的所有文件：

```go
$myFS = $db->getGridFS();
$files = $myFS->find();
foreach ($files as $id => $file){
   print_r($file->getFileName());
}
```

