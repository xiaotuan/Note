### 1.6.3　input()函数

`input()` 函数等待用户在键盘上输入一些文本，并按回车键：

```javascript
❸ myName = input()
```

这个函数的字符串，即用户输入的文本。上面的代码行将这个字符串赋给变量 `myName` 。

你可以认为 `input()` 函数调用是一个表达式，它处理用户输入的任何字符串。如果用户输入 `'Al'` ，那么该表达式的结果为 `myName = 'Al'` 。

如果调用 `input()` 并看到错误信息，例如 `NameError: name 'Al' is not defined` ，那么问题是你使用的是Python 2，而不是Python 3。

