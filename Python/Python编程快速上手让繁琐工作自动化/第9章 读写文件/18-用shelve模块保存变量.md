### 9.3　用shelve模块保存变量

利用 `shelve` 模块，你可以将Python程序中的变量保存到二进制的 `shelf` 文件中。这样，程序就可以从硬盘中恢复变量的数据了。 `shelve` 模块让你在程序中添加“保存”和“打开”功能。例如，如果运行一个程序，并输入了一些设置，就可以将这些设置保存到一个 `shelf` 文件中，然后让程序下一次运行时加载它们。

在交互式环境中输入以下代码：

```javascript
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```

要利用 `shelve` 模块读写数据，首先要导入它。调用函数 `shelve.open()` 并传入一个文件名，然后将返回的值保存在一个变量中。可以对这个变量的 `shelf` 值进行修改，就像它是一个字典一样。当你完成时，在这个 `shelf` 值上调用 `close()` 。这里的 `shelf` 值保存在 `shelfFile` 中。我们创建了一个列表 `cats` ，并写下 `shelfFile['cats'] =cats` ，以将 `cats` 列表保存在 `shelfFile` 中，并作为键 `'cats'` 关联的值（就像在字典中一样）。然后我们在 `shelfFile` 上调用 `close()` 。请注意，在Python 3.7及之前版本中，你必须向 `shelf` 方法 `open()` 传入字符串文件名，否则你无法向它传入 `Path` 对象。

在Windows操作系统上运行前面的代码，你会看到在当前工作目录下有3个新文件：mydata.bak、mydata.dat和mydata.dir。在macOS上，只有mydata.db文件会被创建。

这些二进制文件包含了存储在 `shelf` 中的数据。这些二进制文件的格式并不重要，你只需要知道 `shelve` 模块做了什么，而不必知道它是怎么做的。该模块让你不用操心如何将程序的数据保存到文件中。

你的程序稍后可以使用 `shelve` 模块重新打开这些文件并取出数据。 `shelf` 值不必用读模式或写模式打开，因为它们在打开后既能读又能写。在交互式环境中输入以下代码：

```javascript
>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
```

这里，我们打开了 `shelf` 文件，检查我们的数据是否正确存储。输入 `shelfFile['cats']` 将返回我们前面保存的同一个列表，这样我们就知道该列表得到了正确存储，然后调用 `close()` 。

就像字典一样， `shelf` 值有 `keys()` 和 `values()` 方法，它们返回 `shelf` 中键和值的类似列表的值。因为这些方法返回类似列表的值，而不是真正的列表，所以应该将它们传递给 `list()` 函数来取得列表的形式。在交互式环境中输入以下代码：

```javascript
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()
```

在创建文件时，如果你需要在Notepad或TextEdit这样的文本编辑器中读取它们，那么使用纯文本就非常有用。但是，如果想要保存Python程序中的数据，那就使用 `shelve` 模块。

