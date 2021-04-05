### 7.2.2　匹配Regex对象

`Regex` 对象的 `search()` 方法查找传入的字符串，以寻找该正则表达式的所有匹配。如果字符串中没有找到该正则表达式模式，那么 `search()` 方法将返回 `None` 。如果找到了该模式， `search()` 方法将返回一个 `Match` 对象。 `Match` 对象有一个 `group()` 方法，它返回被查找字符串中实际匹配的文本（稍后我会解释分组）。例如，在交互式环境中输入以下代码：

```javascript
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242
```

变量名 `mo` 是一个通用的名称，用于 `Match` 对象。这个例子可能初看起来有点复杂，但它比前面的isPhoneNumber.py程序要短很多，并且做的事情一样。

这里，我们将期待的模式传递给 `re.compile()` ，并将得到的 `Regex` 对象保存在 `phoneNumRegex` 中。然后我们在 `phoneNumRegex` 上调用 `search()` ，向它传入想查找的字符串。查找的结果保存在变量 `mo` 中。在这个例子里，我们知道模式会在这个字符串中找到，因此我们知道会返回一个 `Match` 对象。知道 `mo` 包含一个 `Match` 对象，而不是空值 `None` ，我们就可以在 `mo` 变量上调用 `group()` ，返回匹配的结果。将 `mo.group()` 写在输出语句中以显示出完整的匹配，即 `415-555-4242` 。

