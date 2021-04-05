### 1.6.5　len()函数

你可以向 `len()` 函数传递一个字符串（或包含字符串的变量），然后该函数求值为一个整型值，即字符串中字符的个数：

```javascript
❺ print('The length of your name is:')
  print(len(myName))
```

在交互式环境中输入以下内容试一试：

```javascript
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.')
46
>>> len('')
0
```

就像这些例子， `len(myName)` 求值为一个整数。然后它被传递给 `print()` ，在屏幕上显示。请注意， `print()` 允许传入一个整型值或字符串。但如果在交互式环境中输入以下内容，就会报错：

```javascript
 >>> print('I am ' + 29 + ' years old.')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('I am ' + 29 + ' years old.')
TypeError: Can't convert 'int' object to str implicitly
```

导致错误的不是 `print()` 函数，而是你试图传递给 `print()` 的表达式。如果在交互式环境中单独输入这个表达式，也会得到同样的错误：

```javascript
>>> 'I am ' + 29 + ' years old.'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'I am ' + 29 + ' years old.'
TypeError: Can't convert 'int' object to str implicitly
```

报错是因为只能用+操作符加两个整数或连接两个字符串，不能让一个整数和一个字符串相加，因为这不符合Python的语法。可以使用字符串型的整数修复这个错误，这在下一小节中解释。

