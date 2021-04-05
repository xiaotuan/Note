### 4.4.4　用sort()方法将列表中的值排序

包含数值的列表或字符串的列表，能用 `sort()` 方法排序。例如，在交互式环境中输入以下代码：

```javascript
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
```

也可以指定 `reverse` 关键字参数为 `True` ，让 `sort()` 方法按逆序排序。在交互式环境中输入以下代码：

```javascript
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
```

关于 `sort()` 方法，你应该注意3件事。第一， `sort()` 方法就地对列表排序。不要写出 `spam = spam.sort()` 这样的代码，试图记录返回值。

第二，不能对既有数字又有字符串值的列表排序，因为Python不知道如何比较它们。在交互式环境中输入以下代码，注意 `TypeError` 错误：

```javascript
>>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
```

第三， `sort()` 方法对字符串排序时，使用“ASCII字符顺序”，而不是实际的字典顺序。这意味着大写字母排在小写字母之前。因此在排序时，小写的a在大写的Z之后。例如，在交互式环境中输入以下代码：

```javascript
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```

如果需要按照普通的字典顺序来排序，就在调用 `sort()` 方法时，将关键字参数 `key` 设置为 `str.lower` ：

```javascript
>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']
```

这将导致 `sort()` 方法将列表中所有的表项当成小写，但实际上并不会改变它们在列表中的值。

