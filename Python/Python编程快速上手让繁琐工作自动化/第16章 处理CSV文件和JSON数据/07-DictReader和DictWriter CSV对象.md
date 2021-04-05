### 16.1.5　DictReader和DictWriter CSV对象

对于包含列标题行的CSV文件，通常使用 `DictReader` 和 `DictWriter` 对象，而不是使用 `reader` 和 `writer` 对象，因为这样会更方便。

`reader` 和 `writer` 对象通过使用列表对CSV文件的行进行读写。 `DictReader` 和 `DictWriter`  CSV对象实现相同的功能，但使用的是字典，且它们使用CSV文件的第一行作为这些字典的键。

进入异步社区本书对应页面，下载 exampleWithHeader.csv 文件。这个文件和example.csv一样，只是第一行是列标题Timestamp、Fruit和Quantity。

要读取该文件，请在交互式环境中输入以下内容：

```javascript
>>> import csv
>>> exampleFile = open('exampleWithHeader.csv')
>>> exampleDictReader = csv.DictReader(exampleFile)
>>> for row in exampleDictReader:
..．    print(row['Timestamp'], row['Fruit'], row['Quantity'])
...
4/5/2015   13:34  Apples  73
4/5/2015    3:41  Cherries  85
4/6/2015   12:46  Pears 14
4/8/2015    8:59  Oranges  52
4/10/2015   2:07  Apples 152
4/10/2015  18:10  Bananas  23
4/10/2015   2:40  Strawberries  98
```

在这个循环中， `DictReader` 对象将 `row` 设置为一个字典对象，该对象的键值来自第一行中的列标题。（从技术上来说，它把 `row` 设置为一个 `OrderedDict` 对象，你可以用和字典一样的方式使用它，它们之间的区别不在本书的范围之内。）使用 `DictReader` 对象意味着你不需要编写额外的代码来跳过第一行的列标题信息，因为 `DictReader` 对象会帮你做这件事。

如果你试图对 `example.csv` 使用 `DictReader` 对象，而 `example.csv` 在第一行中没有列标题信息，那么 `DictReader` 对象将使用 `'4/5/2015 13:34'` 、 `'Apples'` 和 `'73'` 作为字典键。为了避免这种情况，你可以在 `DictReader()` 函数中加入第二个参数，其中包含了预置的列标题名：

```javascript
>>> import csv
>>> exampleFile = open('example.csv')
>>> exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
>>> for row in exampleDictReader:
..． print(row['time'], row['name'], row['amount'])
...
4/5/2015  13:34  Apples  73
4/5/2015   3:41  Cherries  85
4/6/2015  12:46  Pears 14
4/8/2015   8:59  Oranges  52
4/10/2015  2:07  Apples  152
4/10/2015 18:10  Bananas  23
4/10/2015  2:40  Strawberries  98
```

因为 `example.csv` 的第一行中每一列的标题都没有任何文字，所以我们创建了自己的列标题： `'time'` 、 `'name'` 和 `'amount'` 。

`DictWriter` 对象使用字典来创建CSV文件。

```javascript
>>> import csv
>>> outputFile = open('output.csv', 'w', newline='')
>>> outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
>>> outputDictWriter.writeheader()
>>> outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555- 1234'})
20
>>> outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
15
>>> outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
20
>>> outputFile.close()
```

如果你想让文件包含一个标题行，那就调用 `writeheader()` 来写入这一行；否则，跳过调用 `writeheader()` 来省略文件中的标题行。然后，调用 `writerow()` 方法来写入CSV文件的每一行，并传入一个字典，该字典使用标题作为键，并包含要写入文件的数据。

这段代码创建的output.csv文件看起来是这样的：

```javascript
Name,Pet,Phone
Alice,cat,555-1234
Bob,,555-9999
Carol,dog,555-5555
```

注意，传入 `writerow()` 的字典中的键-值对的顺序并不重要：它们是按照给 `DictWriter()` 的键的顺序写的。例如，在第4行，即使你把 `Phone` 的键和值放在 `Name` 和 `Pet` 的键和值之前，在输出结果中，电话号码仍然最后出现。

另外，请注意，任何缺失的键在CSV文件中都会是空的，例如， `{'Name': 'Bob','Phone':'555-999999'}` 中没有'Pet'。

