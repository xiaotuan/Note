### 24.6.2　使用Node.js列出MongoDB GridFS中的文件

使用Node.js来列出文件时，不需要GridStore对象实例，而可直接调用这个类的方法list()。这个方法返回存储在MongoDB GridFS中的文件的名称列表。

例如，下面的代码查找并遍历GridFS存储区中所有的文件：

```go
var files = GridStore.list();
for (var i in files){
   console.log(files[i];
}
```

