### 16.1.2　在for循环中，从reader对象读取数据

对于大型的CSV文件，你需要在一个 `for` 循环中使用 `reader` 对象。这样可以避免将整个文件一次性装入内存。例如，在交互式环境中输入以下代码：

```javascript
>>> import csv
>>> exampleFile = open('example.csv')
>>> exampleReader = csv.reader(exampleFile)
>>> for row in exampleReader: 
 print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
Row #1 ['4/5/2015 13:34', 'Apples', '73']
Row #2 ['4/5/2015 3:41', 'Cherries', '85']
Row #3 ['4/6/2015 12:46', 'Pears', '14']
Row #4 ['4/8/2015 8:59', 'Oranges', '52']
Row #5 ['4/10/2015 2:07', 'Apples', '152']
Row #6 ['4/10/2015 18:10', 'Bananas', '23']
Row #7 ['4/10/2015 2:40', 'Strawberries', '98']
```

在导入 `csv` 模块，并从CSV文件得到 `reader` 对象之后，就可以循环遍历 `reader` 对象中的行了。每一行是一个值的列表，每个值表示一个单元格。

`print()` 函数将输出当前行的编号以及该行的内容。要取得行号，就使用 `reader` 对象的 `line_num` 变量，它包含了当前行的编号。

`reader` 对象只能循环遍历一次。要再次读取CSV文件，必须调用 `csv.reader` 来创建一个对象。

