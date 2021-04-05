### 16.1.1　reader对象

要用 `csv` 模块从CSV文件中读取数据，需要创建一个 `reader` 对象。 `reader` 对象让你迭代遍历CSV文件中的每一行。在交互式环境中输入以下代码，同时将example.csv放在当前工作目录中：

```javascript
❶ >>> import csv
❷ >>> exampleFile = open('example.csv')
❸ >>> exampleReader = csv.reader(exampleFile)
❹ >>> exampleData = list(exampleReader)
❺ >>> exampleData
   [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
   ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
   ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
   ['4/10/2015 2:40', 'Strawberries', '98']]
```

`csv` 模块是Python自带的，因此不需要安装就可以导入它❶。

要用 `csv` 模块读取CSV文件，首先用 `open()` 函数打开它❷，就像打开任何其他文本文件一样。但是，不用在 `open()` 返回的 `File` 对象上调用 `read()` 或 `readlines()` 方法，而是将它传递给 `csv.reader()` 函数❸。这将返回一个 `reader` 对象供你使用。请注意，不能直接将文件名字符串传递给 `csv.reader()` 函数。

要访问 `reader` 对象中的值，最直接的方法就是将它转换成一个普通Python列表，即将它传递给 `list()` ❹。在这个 `reader` 对象上应用 `list()` 函数，将返回一个列表的列表。可以将它保存在变量 `exampleData` 中。在交互式环境中输入 `exampleData` ，将显示列表的列表❺。

既然已经将CSV文件表示为列表的列表，就可以用表达式 `exampleData[row] [col]` 来访问特定行和列的值。其中， `row` 是 `exampleData` 中一个列表的索引， `col` 是该列表中你想访问的项的索引。在交互式环境中输入以下代码：

```javascript
>>> exampleData[0][0]
'4/5/2015 13:34'
>>> exampleData[0][1]
'Apples'
>>> exampleData[0][2]
'73'
>>> exampleData[1][1]
'Cherries'
>>> exampleData[6][1]
'Strawberries'
```

`exampleData[0][0]` 进入第一个列表，并给出第一个字符串； `exampleData[0][2]` 进入第一个列表，并给出第三个字符串；以此类推。

