### 6.3.1　字符串方法upper()、lower()、isupper()和islower()

`upper()` 和 `lower()` 字符串方法返回一个新字符串，其中原字符串的所有字母都被相应地转换为大写或小写。字符串中的非字母字符保持不变。

在交互式环境中输入以下代码：

```javascript
>>> spam = 'Hello, world!'
>>> spam = spam.upper()
>>> spam
'HELLO, WORLD!'
>>> spam = spam.lower()
>>> spam
'hello, world!'
```

请注意，这些方法没有改变字符串本身，而是返回一个新字符串。如果你希望改变原来的字符串，就必须在该字符串上调用 `upper()` 或 `lower()` 方法，然后将这个新字符串赋给保存原来字符串的变量。这就是为什么必须使用 `spam = spam.upper()` ，才能改变 `spam` 变量中的字符串，而不是仅仅使用 `spam.upper()` （这就好比如果变量 `eggs` 中包含值10，写下 `eggs + 3` 并不会改变 `eggs` 变量的值，但是 `eggs = eggs + 3` 会改变 `eggs` 变量的值）。

如果需要进行与大小写无关的比较， `upper()` 和 `lower()` 方法就很有用。字符串 `'great'` 和 `'GREat'` 彼此不相等。但在下面的小程序中，用户输入 `Great` 、 `GREAT` 或 `grEAT` 都没关系，因为字符串首先被转换成小写：

```javascript
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
```

在运行该程序时，先显示问题，然后输入变形的 `great` ，如 `GREat` ，程序将输出 `I feel great too` 。在程序中加入代码来处理多种用户输入或输入错误的情况，例如大小写不一致，这会让程序更容易使用，且更不容易失效：

```javascript
How are you?
GREat
I feel great too.
```

可以在https://autbor.com/convertlowercase/上查看该程序的执行情况。如果字符串中含有字母，并且所有字母都是大写或小写，那么 `isupper()` 和 `islower()` 方法就会相应地返回布尔值 `True` ；否则，该方法返回 `False` 。在交互式环境中输入以下代码，并注意每个方法调用的返回值：

```javascript
>>> spam = 'Hello, world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
```

因为 `upper()` 和 `lower()` 字符串方法本身返回字符串，所以也可以在那些返回的字符串上继续调用字符串方法。使用这种方式编写的表达式看起来就像方法调用链。在交互式环境中输入以下代码：

```javascript
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().lower()
'hello'
>>> 'Hello'.upper().lower().upper()
'HELLO'
>>> 'HELLO'.lower()
'hello'
>>> 'HELLO'.lower().islower()
True
```

