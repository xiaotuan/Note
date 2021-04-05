### 6.3.7　用strip()、rstrip()和lstrip()方法删除空白字符

有时候你希望删除字符串左边、右边或两边的空白字符（空格、制表符和换行符）。 `strip()` 字符串方法将返回一个新的字符串，它的开头和末尾都没有空白字符。 `lstrip()` 和 `rstrip()` 方法将相应删除左边或右边的空白字符。在交互式环境中输入以下代码：

```javascript
>>> spam = ' Hello, World '
>>> spam.strip()
'Hello, World'
>>> spam.lstrip()
'Hello, World    '
>>> spam.rstrip()
'   Hello, World'
```

`strip()` 方法可带有一个可选的字符串参数，用于指定两边的哪些字符应该删除。在交互式环境中输入以下代码：

```javascript
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
```

向 `strip()` 方法传入参数 `'ampS'` ，告诉它在变量中存储的字符串两端，删除出现的a、m、p和大写的S。在传入 `strip()` 方法的字符串中，字符的顺序并不重要： `strip('ampS')` 做的事情和 `strip('mapS')` 或 `strip('Spam')` 一样。

