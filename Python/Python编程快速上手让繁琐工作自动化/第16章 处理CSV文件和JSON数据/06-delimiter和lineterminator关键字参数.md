### 16.1.4　delimiter和lineterminator关键字参数

假定你希望用制表符代替逗号来分隔单元格，并希望有两倍行距，可以在交互式环境中输入下面这样的代码：

```javascript
   >>> import csv
   >>> csvFile = open('example.tsv', 'w', newline='')
❶  >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
   >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
   24
   >>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
   17
   >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
   32
   >>> csvFile.close()
```

这改变了文件中的分隔符和行终止字符。“分隔符”是一行中单元格之间出现的字符。默认情况下，CSV文件的分隔符是逗号。“行终止字符”是出现在行末的字符。默认情况下，行终止字符是换行符。你可以利用 `csv.writer()` 的 `delimiter` 和 `lineterminator` 关键字参数，将这些字符改成不同的值。

传入 `delimiter='\t'` 和 `lineterminator='\n\n'` ❶，将单元格之间的字符改为制表符，将行之间的字符改为两个换行符。然后我们调用 `writerow()` 3次，得到3行。

这产生了文件example.tsv，它包含以下内容：

```javascript
apples  oranges grapes
eggs    bacon   ham
spam    spam     spam    spam    spam    spam
```

既然单元格是由制表符分隔的，我们就使用文件扩展名.tsv来表示制表符分隔的值。

