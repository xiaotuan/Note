`findall()` 查询字符串中某个正则表达式模式全部的非重复出现的情况。这与 `search()` 在执行字符串搜索时类似，但与 `match()` 和 `search()` 的不同之处在于，`findall()` 总是返回一个列表。如果 `findall()` 没有找到匹配的部分，就返回一个空列表，但如果匹配成功，列表将包含所有成功的匹配部分（从左向右按出现顺序排列）：

```python
import re

finds = re.findall('car', 'carry the barcardi to the car')
print(finds)
```

运行结果如下：

```shell
['car', 'car', 'car']
```

`finditer()` 与 `findall()` 之间以及和其他变体函数之间的差异在于，和返回的匹配字符串相比，`finditer()` 在匹配对象中迭代：

```python
import re

s = 'This and that. This and Three.'
finds = re.findall(r'(th\w+) and (th\w+)', s, re.I)
print(finds)
for item in re.finditer(r'(th\w+) and (th\w+)', s, re.I):
    print(item)
```

运行效果如下：

```
[('This', 'that'), ('This', 'Three')]
<re.Match object; span=(0, 13), match='This and that'>
<re.Match object; span=(15, 29), match='This and Three'>
```

