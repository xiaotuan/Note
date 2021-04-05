### 1.6.6　str()、int()和float()函数

如果想要连接一个整数（如 `29` ）和一个字符串，再传递给 `print()` ，就需要获得值 `'29'` ，它是 `29` 的字符串形式。 `str()` 函数可以传入一个整型值，并求值为它的字符串形式，像下面这样：

```javascript
>>> str(29)
'29'
>>> print('I am ' + str(29) + ' years old.')
I am 29 years old.
```

因为 `str(29)` 求值为' `29` '，所以表达式 `'I am ' + str(29) + ' years old.'` 求值为 `'I am ' + '29' + ' years old.'` ，它又求值为 `'I am 29 years old.'` 。这就是传递给 `print()` 函数的值。

`str()` 、 `int()` 和 `float()` 函数将分别求值为传入值的字符串、整数和浮点数形式。请尝试用这些函数在交互式环境中转换一些值，看看会发生什么：

```javascript
>>> str(0)
'0'
>>> str(-3.14)
'-3.14'
>>> int('42')
42
>>> int('-99')
-99
>>> int(1.25)
1
>>> int(1.99)
1
>>> float('3.14')
3.14
>>> float(10)
10.0
```

前面的例子调用了 `str()` 、 `int()` 和 `float()` 函数，向它们传入其他数据类型的值，得到了字符串、整型或浮点型的值。

如果想要将一个整数或浮点数与一个字符串连接，那么用 `str()` 函数就很方便。如果你有一些字符串值，希望将它们用于数学运算，那么 `int()` 函数也很有用。例如， `input()` 函数总是返回一个字符串，即便用户输入的是一个数字。在交互式环境中输入 `spam = input()` ，在它等待文本时输入 `101` ：

```javascript
>>> spam = input()
101 >>> spam
'101'
```

保存在 `spam` 中的值不是整数 `101` ，而是字符串 `'101'` 。如果想要用 `spam` 中的值进行数学运算，那就用 `int()` 函数取得 `spam` 的整数形式，然后将这个新值存在 `spam` 中：

```javascript
>>> spam = int(spam)
>>> spam
101
```

现在你应该能将 `spam` 变量作为整数使用，而不是作为字符串使用：

```javascript
>>> spam * 10 / 5
202.0
```

请注意，如果你将一个不能求值为整数的值传递给 `int()` ，Python将显示错误信息：

```javascript
>>> int('99.99')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int('99.99')
ValueError: invalid literal for int() with base 10: '99.99'
>>> int('twelve')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int('twelve')
ValueError: invalid literal for int() with base 10: 'twelve'
```

如果需要对浮点数进行取整运算，也可以用 `int()` 函数：

```javascript
>>> int(7.7)
7
>>> int(7.7) + 1
8
```

在你的程序中，最后3行使用了函数 `int()` 和 `str()` ，以取得适当数据类型的值：

```javascript
❻ print('What is your age?') # ask for their age
  myAge = input()
  print('You will be ' + str(int(myAge) + 1) + ' in a year.')
```



**文本和数字相等判断**

虽然数字的字符串值被认为与整型值和浮点型值完全不同，但整型值可以与浮点型值相等：

```javascript
>>> 42 == '42'
False
>> 42 == 42.0
True
>> 42.0 == 0042.000
True
```

Python进行这种区分，主要是因为字符串是文本，而整型值和浮点型值都是数字。



`myAge` 变量包含了 `input()` 函数返回的值。因为 `input()` 函数总是返回一个字符串（即使用户输入的是数字），所以你可以使用 `int(myAge)` 返回字符串的整型值。这个整型值随后在表达式 `int(myAge) + 1` 中与1相加。

将相加的结果传递给 `str()` 函数： `str(int(myAge) + 1)` 。然后，返回的字符串与字符串 `'You will be '` 和 `' in a year.'` 连接，求值为一个更长的字符串。这个更长的字符串最终传递给 `print()` 函数，在屏幕上显示。

假定用户输入字符串 `'4'` ，保存在 `myAge` 中。字符串 `'4'` 被转换为一个整型值，所以你可以对它加1，结果是5。 `str()` 函数将这个结果转化为字符串，这样你就可以将它与第二个字符串 `'in a year.'` 连接，创建最终的消息。这些求值步骤如下所示。

![12.png](../images/12.png)
