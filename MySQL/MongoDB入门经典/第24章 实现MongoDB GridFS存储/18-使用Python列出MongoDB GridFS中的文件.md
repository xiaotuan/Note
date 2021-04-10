### 24.5.2　使用Python列出MongoDB GridFS中的文件

有了Java对象GridFS的实例后，就可使用其方法list()列出MongoDB GridFS中的文件了。方法list()返回一个列表，其中包含存储在MongoDB GridFS中文件的名称。

例如，下面的代码查找并遍历GridFS存储区中所有的文件：

```go
fs = gridfs.GridFs(db)
files = fs.list()
for file in files:
  print (file)
```

