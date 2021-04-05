### 10.3.2　从ZIP文件中解压缩

`ZipFile` 对象的 `extractall()` 方法从ZIP文件中解压缩所有文件和文件夹，并将其放到当前工作目录中：

```javascript
  >>> import zipfile, os
  >>> from pathlib import Path
  >>> p = Path.home()
  >>> exampleZip = zipfile.ZipFile(p / 'example.zip')
❶ >>> exampleZip.extractall()
  >>> exampleZip.close()
```

运行这段代码后，example.zip的内容将被解压缩到C:\。或者你可以向 `extractall()` 传递一个文件夹名称，它将文件解压缩到那个文件夹，而不是当前工作目录。如果传递给 `extractall()` 方法的文件夹不存在，那么该文件夹会被创建。例如，如果你用 `exampleZip.extractall('C:\\ delicious')` 取代❶处，那么代码就会从example.zip中解压缩文件，并放到新创建的C:\delicious文件夹中。

`ZipFile` 对象的 `extract()` 方法从ZIP文件中解压缩单个文件。继续演示交互式环境中的例子：

```javascript
>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
```

传递给 `extract()` 的字符串，必须匹配 `namelist()` 返回的字符串列表中的一个。或者，你可以向 `extract()` 传递第二个参数，将文件解压缩到指定的文件夹，而不是当前工作目录。如果第二个参数指定的文件夹不存在，Python就会创建它。 `extract()` 的返回值是被压缩后文件的绝对路径。

