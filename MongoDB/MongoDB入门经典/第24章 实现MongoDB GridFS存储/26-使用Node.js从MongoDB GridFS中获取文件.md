### 24.6.4　使用Node.js从MongoDB GridFS中获取文件

在Node.js中，要从GridFS存储区获取文件，最简单的方式是使用GridStore类的静态方法read()。方法read()的语法如下：

```go
read(db, filename, callback)
```

从文件中读取的数据将作为第二个参数传递给回调函数。下面的示例演示如何从数据库获取一个文件，再读取并显示其内容：

```go
GridStore.read(db, "nodejs.txt", function(err, data){
   console.log(data.toString());
});
```

也可以为文件创建一个GridStore实例，再使用方法read([size])和seek(position)读取文件的内容。例如，下面的代码为文件创建一个GridStore对象，再从文件中读取10个字节，然后跳到偏移1000处并读取10个字节：

```go
var myFS = new GridStore(db, "test.txt", "r");
myFS.read(10, function(err, fsObj){
   fsObj.seek(1000, function(err, fsObj){
      fsObj.read(10, function(err, fsObj){
         . . .
      });
   });
});
```

