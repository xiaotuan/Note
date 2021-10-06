`glob` 是 `Python` 自带的一个模块，该模块用于查找文件，同时支持匹配符查找。可用的匹配符有：

+ `*`：匹配 0 个或多个字符
+ `?`：匹配单个字符
+ `[]`：匹配指定范围内的字符，例如：`[0-9]`匹配数字

`glob` 模块的使用方法如下所示：

```python
import glob

pythonfiles = glob.glob('*.py')
```

上面的代码用于查找当前目录下的所有以 `.py` 结尾的文件。

如果需要在自定目录下查找文件，可以在文件名前加上目录路径，例如：

```python
import glob

pythonfiles = glob.glob('D:\GitSpace\QtyResources\ProgrammingPython4th\*.py')
```

上面的代码将会在 `D:\GitSpace\QtyResources\ProgrammingPython4th` 目录下查找所有以 `.py` 结尾的文件。

也可以查找相对路径上的文件，例如：

```python
import glob

pythonfiles = glob.glob('../*.py')
```

上面的代码将会查找当前目录的上一级目录中所有以 `.py` 结尾的文件。