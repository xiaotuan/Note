### 5.1.2　keys()、values()和items()方法

有3个字典方法，它们将返回类似列表的值，分别对应于字典的键、值和键-值对： `keys()` 、 `values()` 和 `items()` 方法。这些方法返回的值不是真正的列表，它们不能被修改，没有 `append()` 方法。但这些数据类型（分别是 `dict_keys` 、 `dict_values` 和 `dict_items` ）可以用于 `for` 循环。为了了解这些方法的工作原理，请在交互式环境中输入以下代码：

```javascript
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
...     print(v)
red
42
```

这里， `for` 循环迭代了 `spam` 字典中的每个值。 `for` 循环也可以迭代每个键或者键-值对：

```javascript
>>> for k in spam.keys():
...     print(k)
color
age
>>> for i in spam.items():
...     print(i)
('color', 'red')
('age', 42)
```

利用 `keys()` 、 `values()` 和 `items()` 方法，循环分别可以迭代键、值和键-值对。请注意， `items()` 方法返回的 `dict_items` 值包含的是键和值的元组。

如果希望通过这些方法得到一个真正的列表，就把类似列表的返回值传递给 `list()` 函数。在交互式环境中输入以下代码：

```javascript
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
```

`list(spam.keys())` 代码行接收 `keys()` 函数返回的 `dict_keys` 值，并传递给 `list()函数` ，然后返回一个列表，即 `['color', 'age']` 。

也可以利用多重赋值的技巧，在 `for` 循环中将键和值赋给不同的变量。在交互式环境中输入以下代码：

```javascript
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
...     print('Key: ' + k + ' Value: ' + str(v))
Key: age Value: 42
Key: color Value: red
```

