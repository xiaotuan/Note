可以使用 `ZipFile.CreateFromDirectory(String, String)` 方法将指定的文件夹压缩成 zip 压缩包：

```vb
Dim dirPath As String = "C:\Users\xiaotuan\Desktop\animation"
Dim zipPath As String = "C:\Users\xiaotuan\Desktop\animation.zip"
ZipFile.CreateFromDirectory(dirPath, zipPath)
```

也可以调用 `ZipFile.CreateFromDirectory(String, String, CompressionLevel, Boolean)` 方法指定压缩级别，以及是否包括根目录名称。