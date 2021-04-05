### 6.1.3　字符串的in和not in操作符

像列表一样， `in` 和 `not in` 操作符也可以用于字符串。用 `in` 或 `not in` 连接两个字符串得到的表达式，将求值为布尔值 `True` 或 `False` 。在交互式环境中输入以下代码：

```javascript
>>> 'Hello' in 'Hello, World'
True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello, World'
False
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs'
False
```

这些表达式测试第一个字符串（精确匹配，区分大小写）是否在第二个字符串中。

