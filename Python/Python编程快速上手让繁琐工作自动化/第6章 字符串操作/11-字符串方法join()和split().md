### 6.3.4　字符串方法join()和split()

如果有一个字符串列表，需要将它们连接起来成为一个字符串，那么 `join()`  方法就很有用。 `join()` 方法可在字符串上被调用，参数是一个字符串列表，返回一个字符串。返回的字符串由传入列表中的每个字符串连接而成。例如，在交互式环境中输入以下代码：

```javascript
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

请注意，调用 `join()` 方法的字符串被插入列表参数中每个字符串的中间。例如，如果在 `','` 字符串上调用 `join(['cats', 'rats', 'bats'])` ，返回的字符串就是 `'cats, rats, bats'` 。

要记住， `join()` 方法是针对一个字符串调用的，并且需要传入一个列表值（很容易不小心用其他的方式调用它）。 `split()` 方法做的事情正好相反：它针对一个字符串调用，返回一个字符串列表。在交互式环境中输入以下代码：

```javascript
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```

默认情况下，字符串 `'My name is Simon'` 按照各种空白字符（诸如空格、制表符或换行符）分隔。这些空白字符不包含在返回列表的字符串中。也可以向 `split()` 方法传入一个分隔字符串，指定它按照不同的字符串分隔。例如，在交互式环境中输入以下代码：

```javascript
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

一个常见的  `split()` 用法是按照换行符分隔多行字符串的。在交互式环境中输入以下代码：

```javascript
>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the
fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.',
'Sincerely,', 'Bob']
```

向 `split()` 方法传入参数 `'\n'` ，按照换行符分隔变量中存储的多行字符串，然后返回列表中的每个表项（对应于字符串中的一行）。

