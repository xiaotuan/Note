`re` 模块和正则表达式的对象方法 `split()` 对于相对应字符串的工作方法是类似的，但是与分割一个固定字符串相比，它们基于正则表达式的模式分隔字符串。如果你不想为每次模式的出现都分割字符串，就可以通过 `max` 参数设定一个值来指定最大分割数。

如果给定分隔符不是使用特殊符号来匹配多重模式的正则表达式，那么 `re.split()` 与 `str.split()` 的工作方式相同。

```python
import re

DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
    )

for datum in DATA:
    print(re.split(',|(?=(?:\d{5}|[A-Z]{2}))', datum))
```

运行结果如下：

```
['Mountain View', ' ', 'CA ', '94040']
['Sunnyvale', ' ', 'CA']
['Los Altos', ' ', '94023']
['Cupertino ', '95014']
['Palo Alto ', 'CA']
```

