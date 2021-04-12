### 24.6.3　使用Node.js在MongoDB GridFS中添加文件

在Node.js中，要将文件添加到MongoDB GridFS中，需要创建一个GridStore对象并指定写入模式，然后使用方法write()或writeFile()将数据写入GridFS。为演示这一点，下面的代码创建了一个新文件并在其中写入数据：

```go
var myFS = new GridStore(db, "test.txt", "w");
myFS.writeFile("nodejs.txt", function(err, fsObj){
   . . .
});
```

