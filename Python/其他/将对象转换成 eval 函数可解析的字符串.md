可以使用 `repr` 函数将对象转换成字符串，然后使用 `eval` 函数将该字符串转换成对象，例如：

```python
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

objectStr = repr(db)
db = eval(objectstr)
```

