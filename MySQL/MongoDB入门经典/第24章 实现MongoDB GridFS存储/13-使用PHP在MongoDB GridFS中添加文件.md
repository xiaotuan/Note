### 24.4.3　使用PHP在MongoDB GridFS中添加文件

在PHP中，要将文件添加到MongoDB GridFS中，可使用MongoGridFS对象的方法put()。方法put()的语法如下：

```go
put(filename, [metadata])
```

例如，下面的代码将文件系统中的一个文件插入GridFS存储区：

```go
$myFS = $db->getGridFS();
$file = $myFS->put('test.txt');
```

方法put()返回被存储到MongoDB GridFS存储区中的文件的_id。

