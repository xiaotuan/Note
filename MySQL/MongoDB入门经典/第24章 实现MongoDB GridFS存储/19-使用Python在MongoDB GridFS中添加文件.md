### 24.5.3　使用Python在MongoDB GridFS中添加文件

在Python中，要将文件添加到MongoDB GridFS中，可使用GridFS对象的方法put()。方法put()的语法如下：

```go
put(data, [**kwargs])
```

插入数据时，可使用参数kwargs指定文件名。例如，下面的代码在GridFS存储区插入一个字符串，并将文件名指定为test.txt：

```go
fs = gridfs.GridFS(db)
fs.put("Test Text", filename="test.txt")
```

