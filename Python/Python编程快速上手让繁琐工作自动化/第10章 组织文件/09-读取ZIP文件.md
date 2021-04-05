### 10.3.1　读取ZIP文件

要读取ZIP文件的内容，首先必须创建一个 `ZipFile` 对象（请注意大写首字母Z和F）。 `ZipFile` 对象在概念上与 `File` 对象相似，你在第8章中曾经看到 `open()` 函数返回 `File` 对象：它们是一些值，程序通过它们与文件打交道。

要创建一个 `ZipFile` 对象，就要调用 `zipfile.ZipFile()` 函数，向它传入一个字符串，表示ZIP文件的文件名。请注意， `zipfile` 是Python模块的名称， `ZipFile()` 是函数的名称。

例如，在交互式环境中输入以下代码：

```javascript
  >>> import zipfile, os
  >>> from pathlib import Path
  >>> p = Path.home()
  >>> exampleZip = zipfile.ZipFile(p / 'example.zip')
  >>> exampleZip.namelist()
  ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
  >>> spamInfo = exampleZip.getinfo('spam.txt')
  >>> spamInfo.file_size
  13908
  >>> spamInfo.compress_size
  3828
❶ >>> f'Compressed file is {round(spamInfo.file_size / spamInfo
  .compress_size, 2)}x smaller!'
  )
  'Compressed file is 3.63x smaller!'
  >>> exampleZip.close()
```

`ZipFile` 对象有一个 `namelist()` 方法，它返回ZIP文件中包含的所有文件和文件夹的字符串的列表。这些字符串可以传递给 `ZipFile` 对象的 `getinfo()` 方法，返回一个关于特定文件的 `ZipInfo` 对象。 `ZipInfo` 对象有自己的属性，如表示字节数的 `file_size` 和 `compress_size` ，它们分别表示原来文件大小和压缩后文件大小。 `ZipFile` 对象表示整个归档文件，而 `ZipInfo` 对象则保存该归档文件中每个文件的有用信息。

❶处的命令计算出example.zip压缩的效率，用压缩后文件的大小除以原来文件的大小，并输出这一信息。

