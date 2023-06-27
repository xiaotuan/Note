`match()` 函数试图从字符串的起始部分对模式进行匹配。如果匹配成功，就返回一个匹配对象；如果匹配失败，就返回 `None`，匹配对象的 `group()` 方法能够用于显示那个成功的匹配：

```python
import re

displaySize = "10.10 inches"
m = re.match('\d{1,2}.\d{1,2}', displaySize)
if m is not None:
    print(m.group())
```

运行结果如下：

```
10.10
```

另一个示例：

```python
import re

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
```

运行结果如下：

```
abc
123
('abc', '123')
```

