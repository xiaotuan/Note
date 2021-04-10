### 24.3.3　使用Java在MongoDB GridFS中添加文件

在Java中，要将文件添加到MongoDB GridFS中，可使用方法createFile()。调用方法 createFile()时，可使用下述格式之一：

```go
createFile(File f)
createFile(InputStream in)
createFile(InputStream in, String filename)
createFile(InputStream in, String filename, Boolean cloesStreamOnPersist)
createFile(String filename)
```

使用File可插入文件系统中的文件；使用InputStream可插入动态文件内容，而只指定文件名将在GridFS存储区中创建一个空文件。

例如，下面的代码将文件系统中的一个文件插入GridFS存储区：

```go
File newFile = new File("/tmp/myFile.txt");
GridFSInputFile gridFile = myFS.createFile(newFile);
gridFile.save();
```

方法createFile()返回一个GridFSInputFile对象。GridFSInputFile类可用于获取并输出流，还可用于保存文件。

