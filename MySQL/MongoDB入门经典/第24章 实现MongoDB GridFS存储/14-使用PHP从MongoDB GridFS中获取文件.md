### 24.4.4　使用PHP从MongoDB GridFS中获取文件

在PHP中，要从GridFS存储区获取文件，最简单的方式是使用前面讨论过程的方法find()或findOne()。这些方法分别返回一个MongoGridFSCursor和MongoGridFSFile对象。

下面的示例演示了如何从数据库获取一个文件，显示其内容并将其写入本地文件系统：

```go
$myFS = $db->getGridFS();
$file = $myFS->findOne('php.txt');
print_r($file->getBytes());
$file.write('local.txt');
```

