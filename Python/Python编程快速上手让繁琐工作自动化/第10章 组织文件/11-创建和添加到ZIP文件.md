### 10.3.3　创建和添加到ZIP文件

要创建你自己的压缩ZIP文件，必须以“写模式”打开 `ZipFile` 对象，即传入 `'w'` 作为第二个参数（这类似于向 `open()` 函数传入 `'w'` ，以写模式打开一个文本文件）。

如果向 `ZipFile` 对象的 `write()` 方法传入一个路径，那么Python就会压缩该路径所指的文件，并将它添加到ZIP文件中。 `write()` 方法的第一个参数是一个字符串，代表要添加的文件名。第二个参数是“压缩类型”参数，它告诉计算机使用怎样的算法来压缩文件。可以总是将这个值设置为 `zipfile.ZIP_DEFLATED` （这指定了 `deflate` 压缩算法，它对各种类型的数据都很有效）。在交互式环境中输入以下代码：

```javascript
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
```

这段代码将创建一个新的ZIP文件，名为new.zip，它包含spam.txt压缩后的内容。

要记住，就像写入文件一样，写模式将擦除ZIP文件中所有原有的内容。如果只是希望将文件添加到原有的ZIP文件中，就要向 `zipfile.ZipFile()` 传入 `'a'` 作为第二个参数，以添加模式打开ZIP文件。

