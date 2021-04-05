### 6.3.6　用rjust()、ljust()和center()方法对齐文本

`rjust()` 和 `ljust()` 字符串方法返回调用它们的字符串的填充版本，通过插入空格来对齐文本。这两个方法的第一个参数是一个整数，代表长度，用于对齐字符串。在交互式环境中输入以下代码：

```javascript
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'               Hello'
>>> 'Hello World'.rjust(20)
'         Hello World'
>>> 'Hello'.ljust(10)
'Hello     '
```

`'Hello'.rjust(10)` 是说，我们希望右对齐，将 `'Hello'` 放在一个长度为10的字符串中。 `'Hello'` 有5个字符，所以左边会加上5个空格，得到一个10个字符的字符串，实现 `'Hello'` 右对齐。

`rjust()` 和 `ljust()` 方法的第二个可选参数将指定一个填充字符，用于取代空格字符。在交互式环境中输入以下代码：

```javascript
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
```

`center()` 字符串方法与 `ljust()` 和 `rjust()` 字符串方法类似，但它让文本居中，而不是左对齐或右对齐。在交互式环境中输入以下代码：

```javascript
>>> 'Hello'.center(20)
'       Hello       '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

如果需要输出表格式数据，并留出正确的空格，这些方法就特别有用。打开一个新的文件编辑器窗口，输入以下代码，并保存为picnicTable.py：

```javascript
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```

可以在https://autbor.com/picnictable/上查看该程序的执行情况。在这个程序中，我们定义了 `printPicnic()` 方法，它接收一个信息的字典，并利用 `center()` 、 `ljust()` 和 `rjust()` 方法，以一种干净、对齐的表格形式显示这些信息。

我们传递给 `printPicnic()` 方法的字典是 `picnicItems` 。在 `picnicItems` 中，我们有4个三明治、12个苹果、4个杯子和8000块饼干。我们希望将这些信息组织成两行，项的名字在左边，数量在右边。

要做到这一点，就需要决定左列和右列的宽度。与字典一起，我们将这些值传递给 `printPicnic()` 方法。

`printPicnic()` 方法接收一个字典， `leftWidth` 表示表的左列宽度， `rightWidth` 表示表的右列宽度。它输出标题 `PICNIC ITEMS` ，在表上方居中。然后它遍历字典，每行输出一个键-值对。键左对齐，填充圆点；值右对齐，填充空格。

在定义 `printPicnic()` 方法后，我们定义了字典 `picnicItems` ，并调用 `printPicnic()方法` 两次，传入表左右列的宽度。

运行该程序，表格就会显示两次。第一次左列宽度是12个字符，右列宽度是5个字符。第二次它们分别是20个和6个字符。代码如下：

```javascript
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........    4
apples..............   12
cups................    4
cookies............. 8000
```

利用 `rjust()` 、 `ljust()` 和 `center()` 方法能确保字符串对齐，即使你不清楚字符串有多少字符。

