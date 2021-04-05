### 8.1　PyInputPlus模块

`PyInputPlus` 包含与 `input()` 类似的、用于多种数据（如数字、日期、E-mail地址等）的函数。如果用户输入了无效的内容，例如格式错误的日期或超出预期范围的数字，那么 `PyInputPlus` 会再次提示他们输入。 `PyInputPlus` 还包含其他有用的功能，例如提示用户的次数限制和时间限制（如果要求用户在时限内做出响应）。

`PyInputPlus` 不是Python标准库的一部分，因此必须利用pip单独安装。要安装 `PyInputPlus` ，请在命令行中运行 `pip install --user pyinputplus` 。附录A包含了安装第三方模块的完整说明。要检查 `PyInputPlus` 是否正确安装，请在交互式环境中导入它：

```javascript
>>>  import pyinputplus
```

如果在导入该模块时没有出现错误，就表明已成功安装。

`PyInputPlus` 具有以下几种用于不同类型输入的函数。

`inputStr()` 类似于内置的 `input()` 函数，但具有一般的 `PyInputPlus` 功能。你还可以将自定义验证函数传递给它。

`inputNum()` 确保用户输入数字并返回 `int` 或 `float` 值，这取决于数字是否包含小数点。

`inputChoice()` 确保用户输入系统提供的选项之一。

`inputMenu()` 与 `inputChoice()` 类似，但提供一个带有数字或字母选项的菜单。

`inputDatetime()` 确保用户输入日期和时间。

`inputYesNo()` 确保用户输入“yes”或“no”响应。

`inputBool()` 类似 `inputYesNo()` ，但接收“True”或“False”响应，并返回一个布尔值。

`inputEmail()` 确保用户输入有效的E-mail地址。

`inputFilepath()` 确保用户输入有效的文件路径和文件名，并可以选择检查是否存在具有该名称的文件。

`inputPassword()` 类似于内置的 `input()` ，但是在用户输入时显示 `*` 字符，因此不会在屏幕上显示口令或其他敏感信息。

只要输入了无效内容，这些函数就会自动提示用户：

```javascript
>>> import pyinputplus as pyip
>>> response = pyip.inputNum() 
five
'five' is not a number.
42
>>>  response
42
```

每次要调用 `PyInputPlus` 模块的函数时， `import` 语句中的 `as pyip` 代码让我们不必输入 `pyinputplus` ，而是可以使用较短的 `pyip` 名称。如果看一下示例，就会发现这些函数与 `input()` 不同，它们返回的是 `int` 或 `float` 值，如 `42` 或 `3.14` ，而不是字符串 `'42'` 或 `'3.14'` 。

正如可以将字符串传递给 `input()` 以提供提示一样，你也可以将字符串传递给 `PyInputPlus` 模块的函数的 `prompt` 关键字参数来显示提示：

```javascript
>>> response = input('Enter a number: ')
Enter a number:  42
>>> response
'42'
>>> import pyinputplus as pyip
>>> response = pyip.inputInt(prompt='Enter a number: ')
Enter a number: cat 
'cat' is not  an  integer.
Enter a number: 42
>>>  response
42
```

请使用 Python的  `help()` 函数查找有关这些函数的更多信息。例如， `help(pyip. inputChoice)` 显示 `inputChoice()` 函数的帮助信息。

与Python的内置 `input()` 不同， `PyInputPlus` 模块的函数包含一些用于输入验证的附加功能。

