`\b` 表示 `ASCII` 字符的退格符，但是 `\b` 同时也是一个正则表达式的特殊符号，表示匹配一个单词的边界。对于正则表达式编译器而言，若它把两个 `\b` 视为字符串内容而不是单个退格符，就需要再字符串中使用一个反斜线转义反斜线，就像这样：`\\b`。

```python
import re

m = re.match('\bblow', 'blow')
if m:
    print(m.group())
else:
    print("Not match.")

m = re.match('\\bblow', 'blow')
if m:
    print(m.group())
else:
    print("Not match.")
```

运行结果如下：

```
Not match.
blow
```

可以在正则表达式字符串前面加 `r` 表示使用原始字符串，这是 `\b` 将不再表示退格符，而是 `\` 和 `b` 字符组成的字符串：

```python
import re

m = re.match(r'\bblow', 'blow')
if m:
    print(m.group())
else:
    print("Not match.")
```

运行结果如下：

```
blow
```

