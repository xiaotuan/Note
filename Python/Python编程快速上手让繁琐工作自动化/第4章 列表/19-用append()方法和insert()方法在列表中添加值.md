### 4.4.2　用append()方法和insert()方法在列表中添加值

要在列表中添加新值，就使用 `append()` 方法和  `insert()` 方法。在交互式环境中输入以下代码，对变量 `spam` 中的列表调用 `append()` 方法：

```javascript
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
```

前面的 `append()` 方法可将参数添加到列表末尾。 `insert()` 方法可以在列表任意索引处插入一个值。 `insert()` 方法的第一个参数是新值的索引，第二个参数是要插入的新值。在交互式环境中输入以下代码：

```javascript
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
```

请注意，代码是 `spam.append('moose')` 和 `spam.insert(1, 'chicken')` ，而不是 `spam = spam.append('moose')` 和 `spam = spam.insert(1, 'chicken')` 。 `append()` 方法和 `insert()` 方法都不会将 `spam` 的新值作为其返回值（实际上， `append()` 方法和 `insert()` 方法的返回值是 `None` ，所以你肯定不希望将它保存为变量的新值）。但是，列表被“就地”修改了。4.6.1小节“可变和不可变数据类型”将更详细地介绍就地修改一个列表。

方法属于单个数据类型。 `append()` 方法和 `insert()` 方法是列表方法，只能在列表上调用，不能在其他值上调用，例如字符串和整型。在交互式环境中输入以下代码，注意产生的 `AttributeError` 错误信息：

```javascript
>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> bacon = 42
>>> bacon.insert(1, 'world')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    bacon.insert(1, 'world')
AttributeError: 'int' object has no attribute 'insert'
```

