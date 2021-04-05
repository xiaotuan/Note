### 4.4.3　用remove()方法从列表中删除值

给 `remove()` 方法传入一个值，它将从被调用的列表中删除。在交互式环境中输入以下代码：

```javascript
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
```

试图删除列表中不存在的值，将导致 `ValueError` 错误。例如，在交互式环境中输入以下代码，注意显示的错误：

```javascript
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('chicken')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    spam.remove('chicken')
ValueError: list.remove(x): x not in list
```

如果该值在列表中出现多次，只有第一次出现的值会被删除。在交互式环境中输入以下代码：

```javascript
>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
```

如果知道想要删除的值在列表中的索引， `del` 语句就很好用。如果知道想要从列表中删除的值， `remove()` 方法就很好用。

