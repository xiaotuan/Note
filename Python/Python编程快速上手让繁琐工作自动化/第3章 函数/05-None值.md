### 3.3　None值

在Python中有一个值称为 `None` ，它表示没有值。 `None` 是 `NoneType` 数据类型的唯一值（其他编程语言可能称这个值为 `null` 、 `nil` 或 `undefined` ）。就像布尔值 `True` 和 `False` 一样， `None` 的首字母N必须大写。

如果你希望变量中存储的东西不会与一个真正的值混淆，这个没有值的值就可能有用。有一个使用 `None` 的地方就是 `print()` 函数的返回值。 `print()` 函数在屏幕上显示文本，但它不需要返回任何值，这和 `len()` 函数或 `input()` 函数不同。但既然所有函数调用都需要求值为一个返回值，那么 `print()` 函数就返回 `None` 。要看到这个效果，请在交互式环境中输入以下代码：

```javascript
>>> spam = print('Hello!')
Hello!
>>> None == spam
True
```

在幕后，对于所有没有 `return` 语句的函数定义，Python都会在末尾加上 `return None` 。这类似于 `while` 或 `for` 循环隐式地以 `continue` 语句结尾。而且，如果使用不带值的 `return` 语句（也就是只有 `return` 关键字本身），也返回 `None` 。

