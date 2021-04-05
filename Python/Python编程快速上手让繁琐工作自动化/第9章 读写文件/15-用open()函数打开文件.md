### 9.2.1　用open()函数打开文件

要用 `open()` 函数打开一个文件，就要向它传递一个字符串路径，表明希望打开的文件。这既可以是绝对路径，也可以是相对路径。 `open()` 函数返回一个 `File` 对象。

尝试一下，先用 `Notepad` 或 `TextEdit` 创建一个文本文件，名为 `hello.txt` 。输入 `Hello, world!` 作为该文本文件的内容，将它保存在你的用户文件夹中。然后在交互式环境中输入以下代码：

```javascript
>>> helloFile = open(Path.home() / 'hello.txt')
```

`open()` 函数还可以接收字符串。如果你使用Windows操作系统，请在交互式环境中输入以下内容：

```javascript
>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')
```

如果使用macOS，在交互式环境中输入以下代码：

```javascript
>>> helloFile = open('/Users/your_home_folder/hello.txt')
```

请确保用你自己的计算机用户名取代 `your_home_folder` 。例如，我的计算机用户名是Al，因此我在Windows操作系统下输入 `'C:\\Users\\Al\\hello.txt'` 。

这些命令都将以“读取纯文本模式”打开文件，或简称为“读模式”。当文件以读模式打开时，Python只让你从文件中读取数据，你不能以任何方式写入或修改它。在Python中打开文件时，读模式是默认的模式。但如果你不希望依赖于Python的默认值，也可以明确指明该模式，通过向 `open()` 传入字符串 `'r'` 作为第二个参数即可。 `open('/Users/Al/hello.txt', 'r')` 和 `open('/Users/Al/hello.txt')` 做的事情一样。

调用 `open()` 将返回一个 `File` 对象。 `File` 对象代表计算机中的一个文件，它只是Python中另一种类型的值，就像你已熟悉的列表和字典。在前面的例子中，你将 `File` 对象保存在 `helloFile` 变量中。当你需要读取或写入该文件时，就可以调用 `helloFile` 变量中的 `File` 对象的方法。

