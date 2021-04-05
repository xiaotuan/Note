### 13.3.1　用openpyxl模块打开Excel文档

在导入 `openpyxl` 模块后，就可以使用 `openpyxl.load_workbook()` 函数了。在交互式环境中输入以下代码：

```javascript
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
```

`openpyxl.load_workbook()` 函数接收文件名，并返回一个 `workbook` 数据类型的值。这个 `Workbook` 对象代表这个Excel文件，这有点儿类似于 `File` 对象代表一个打开的文本文件。

要记住，example.xlsx必须在当前工作目录中，你才能处理它。可以导入 `os` ，使用函数 `os.getcwd()` 弄清楚当前工作目录是什么，并使用 `os.chdir()` 改变当前工作目录。

