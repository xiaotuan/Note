### 24.5.4　使用Python从MongoDB GridFS中获取文件

在Python中，要从GridFS存储区获取文件，最简单的方式是使用GridFS对象的方法get_last_version()或get_version()。这些方法的语法如下：

```go
get_last_version(filename)
get_version(filename, version)
```

这些方法返回一个GridOut对象，让您能够使用方法read()从服务器读取数据。

下面的示例演示了如何从数据库获取一个文件，再读取并显示其内容：

```go
fs = gridfs.GridFS(db)
file = fs.get_last_version(filename="python.txt")
print (file.read())
```

