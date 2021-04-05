### 9.1.1　Windows操作系统上的倒斜杠以及macOS和Linux操作系统上的正斜杠

在Windows操作系统上，路径书写使用倒斜杠作为文件夹之间的分隔符。但在macOS和Linux操作系统上，使用正斜杠作为它们的路径分隔符。如果想要程序运行在所有操作系统上，在编写Python脚本时，就必须处理这两种情况。

好在用 `pathlib` 模块的 `Path()` 函数来做这件事很简单。如果将单个文件和路径上的文件夹名称的字符串传递给它， `Path()` 就会返回一个文件路径的字符串，包含正确的路径分隔符。在交互式环境中输入以下代码：

```javascript
>>> from pathlib import Path
>>> Path('spam','bacon','eggs')
WindowsPath('spam/bacon/eggs')
>>> str(Path('spam','bacon','eggs'))
'spam\\bacon\\eggs'
```

请注意，导入 `pathlib` 的惯例是运行 `from pathlib import Path` ，因为不这样做，我们就必须在代码中出现 `Path` 的所有地方都输入 `pathlib.Path` 。这种额外的输入不仅麻烦，而且也很多余。

我在Windows操作系统上运行这些交互式环境的例子， `Path('spam', 'bacon', 'eggs')` 为连接的路径返回一个 `WindowsPath` ，表示为 `WindowsPath('spam/ bacon/eggs')` 。尽管Windows操作系统使用了倒斜杠，但 `WindowsPath` 的表示方法在交互式环境中用正斜杠显示它们，因为开源软件开发者总是比较喜欢使用Linux操作系统。

如果要获取这个路径的简单文本字符串，可以将其传递给 `str()` 函数，该函数在我们的示例中返回 `'spam\\bacon\\eggs'` 。（请注意，由于每个倒斜杠都需要用另一个倒斜杠字符进行转义，因此倒斜杠会加倍。）如果在Linux操作系统上调用过此函数，那么 `Path()` 将返回一个 `PosixPath` 对象，该对象在传递给 `str()` 时，会返回 `'spam/bacon/eggs'` 。（POSIX是针对Linux操作系统这样的类UNIX操作系统的一组标准。）

这些 `Path` 对象（实际上是 `WindowsPath` 或 `PosixPath` 对象，具体取决于你的操作系统）将传入本章介绍的几个与文件相关的函数。例如，以下代码将一些名称从文件名列表连接到文件夹名称的末尾：

```javascript
>>> from pathlib import Path
>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
 print(Path(r'C:\Users\Al', filename))
C:\Users\Al\accounts.txt 
C:\Users\Al\details.csv 
C:\Users\Al\invite.docx
```

在Windows操作系统上，倒斜杠用于分隔目录，因此你不能在文件名中使用它。但是，你可以在macOS和Linux操作系统上的文件名中使用倒斜杠。因此，尽管 `Path(r'spam\eggs')` 在Windows操作系统上指的是两个单独的文件夹（或文件夹spam中的文件eggs），但在macOS和Linux操作系统上，同样的命令是指一个名为spam\eggs的文件夹（或文件）。因此，在你的Python代码中始终使用正斜杠通常是个好主意（本章的其余部分将继续使用正斜杠）。 `pathlib` 模块将确保它始终可在所有操作系统上运行。

请注意，Python 3.4引入了 `pathlib` 来代替旧的 `os.path()` 函数。Python标准库模块从Python 3.6开始支持它，但是如果你使用的是较老的Python 2版本，建议你使用 `pathlib2` ，它在Python 2.7上提供了 `pathlib` 的功能。附录A包含了利用 `pip` 安装 `pathlib2` 的说明。每当我用 `pathlib` 替换了较旧的 `os.path()` 函数时，都会做一个简短的说明。你可以在Python的官方网站中查找较早的函数。

