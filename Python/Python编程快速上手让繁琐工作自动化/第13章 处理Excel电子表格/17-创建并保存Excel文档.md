### 13.5.1　创建并保存Excel文档

调用 `openpyxl.Workbook()` 函数以创建一个新的空 `Workbook` 对象。在交互式环境中输入以下代码：

```javascript
>>> import openpyxl
>>> wb = openpyxl.Workbook() # Create a blank workbook.
>>> wb.sheetnames # It starts with one sheet.
['Sheet']
>>> sheet = wb.active
>>> sheet.title
'Sheet'
>>> sheet.title = 'Spam Bacon Eggs Sheet' # Change title.
>>> wb.sheetnames
['Spam Bacon Eggs Sheet']
```

工作簿将从一个名为Sheet的工作表开始。你可以将新的字符串保存在它的 `title` 属性中，从而改变工作表的名字。

当修改 `Workbook` 对象或它的工作表和单元格时，电子表格文件不会保存，除非你调用 `save()` 工作簿方法。在交互式环境中输入以下代码（让 `example.xlsx` 处于当前工作目录）：

```javascript
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.active
>>> sheet.title = 'Spam Spam Spam'
>>> wb.save('example_copy.xlsx') # Save the workbook.
```

这里，我们改变了工作表的名称。为了保存变更，我们将文件名作为字符串传递给 `save()` 方法。传入的文件名与最初的文件名不同，例如 `'example_copy. xlsx'` ，这将变更保存到电子表格的一份副本中。

当你编辑从文件中加载的一个电子表格时，总是应该将新的、编辑过的电子表格保存到不同的文件名中。这样，如果代码有bug，导致新的保存到文件中的数据不对，那么还有最初的电子表格文件可以处理。

