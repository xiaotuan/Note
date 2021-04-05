### 9.4　用pprint.pformat()函数保存变量

回忆一下，在5.2节“美观地输出”中， `pprint.pprint()` 函数将列表或字典中的内容“美观地输出”到屏幕，而 `pprint.pformat()` 函数将返回同样的文本字符串，但不是输出它。这个字符串不仅是易于阅读的格式，同时也是语法正确的Python代码。假定你有一个字典，保存在一个变量中，你希望保存这个变量和它的内容，以便将来使用。 `pprint.pformat()` 函数将提供一个字符串，你可以将它写入.py文件。该文件将成为你自己的模块，如果你需要使用存储在其中的变量，就可以导入它。

例如，在交互式环境中输入以下代码：

```javascript
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()
```

这里，我们导入了 `pprint` ，以便能使用 `pprint.pformat()` 。我们有一个字典的列表，保存在变量 `cats` 中。为了让 `cats` 中的列表在关闭交互式环境后仍然可用，我们利用 `pprint.pformat()` 将它返回为一个字符串。当我们有了 `cats` 中数据的字符串形式，就很容易将该字符串写入一个文件，我们将它命名为myCats.py。

`import` 语句导入的模块本身就是Python脚本。如果将来自 `pprint.pformat()` 的字符串保存为一个.py文件，那么该文件就是一个可以导入的模块，像其他模块一样。

由于Python脚本本身也是带有.py文件扩展名的文本文件，因此你的Python程序甚至可以生成其他Python程序，然后可以将这些文件导入脚本中：

```javascript
>>> import myCats
>>> myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
>>> myCats.cats[0]['name']
'Zophie'
```

创建一个.py文件（而不是利用 `shelve` 模块保存变量）的好处在于，因为它是一个文本文件，所以任何人都可以用一个简单的文本编辑器读取和修改该文件的内容。但是，对于大多数应用，利用 `shelve` 模块来保存数据是将变量保存到文件的最佳方式。只有基本数据类型，如整型、浮点型、字符串、列表和字典，可以作为简单文本写入一个文件。例如， `File` 对象就不能编码为文本。

