### 6.3.3　字符串方法startswith()和endswith()

如果 `startswith()` 和 `endswith()` 方法所调用的字符串以该方法传入的字符串开始或结束，那么返回 `True；` 否则返回 `False` 。在交互式环境中输入以下代码：

```javascript
>>> 'Hello, world!'.startswith('Hello')
True
>>> 'Hello, world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello, world!'.startswith('Hello, world!')
True
>>> 'Hello, world!'.endswith('Hello, world!')
True
```

如果只需要检查字符串的开始或结束部分是否等于另一个字符串，而不是整个字符串，这两个方法就可以替代等于操作符==，这很有用。

