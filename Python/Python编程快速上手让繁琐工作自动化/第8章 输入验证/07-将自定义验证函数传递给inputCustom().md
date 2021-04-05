### 8.1.5　将自定义验证函数传递给inputCustom()

你可以编写函数以执行自定义的验证逻辑，并将函数传递给 `inputCustom()` 。例如，假设你希望用户输入一系列数字，这些数字的总和为10。虽然没有 `pyinputplus. inputAddsUpToTen()` 函数，但是你可以创建自己的函数，使得它具有以下功能。

+ 接收单个字符串参数，即用户输入的内容。
+ 如果字符串验证失败，则引发异常。
+ 如果 `inputCustom()` 应该返回不变的该字符串，则返回 `None` （或没有 `return` 语句）。
+ 如果 `inputCustom()` 返回的字符串与用户输入的字符串不同，则返回非 `None` 值。
+ 作为第一个参数传递给 `inputCustom()。`

例如，我们可以创建自己的 `addsUpToTen()` 函数，然后将其传递给 `inputCustom()` 。请注意，函数调用看起来像 `inputCustom(addsUpToTen)` 而不是 `inputCustom(addsUpToTen())` ，因为我们是将 `addsUpToTen()` 函数本身传递给 `inputCustom()` ，而不是调用 `addsUpToTen()` 并传递其返回值：

```javascript
>>> import pyinputplus as pyip
>>> def addsUpToTen(numbers):
... numbersList = list(numbers)
... for i, digit in enumerate(numbersList):
...   numbersList[i] = int(digit)
... if sum(numbersList) != 10:
...   raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
... return int(numbers) # Return an int form of numbers.
... 
>>> response = pyip.inputCustom(addsUpToTen) # No parentheses after addsUpToTen here.
123
The digits must add up to 10, not 6.
1235
The digits must add up to 10, not 11.
1234
>>> response # inputStr() returned an int, not a string. 
1234
>>> response = pyip.inputCustom(addsUpToTen) 
hello
invalid literal for int() with base 10: 'h'
55
>>> response
```

`inputCustom()` 函数还支持常规的PyInputPlus功能，该功能可通过 `blank` 、 `limit` 、 `timeout` 、 `default` 、 `allowRegexes` 和 `blockRegexes` 关键字参数实现。如果很难或不可能编写用于有效输入的正则表达式（例如“加起来等于10”的示例），那么编写自定义验证函数将非常有用。

