对序列或集合这一类数据类型，比如字符串、列表或元组，我们可以使用操作符 `in` 来测试成员关系，用 `not in` 来测试非成员关系。例如：

```python
>>> p = (4, 'frog', 9, -33, 9, 2) 
>>> 2 in p
True
>>> 'dog' not in p
True
>>> phrase = 'Wild Swans by Jung Chang'
>>> 'J' in phrase
True
>>> 'han' in phrase
True
```

> 注意：对列表与元组，`in` 操作符使用线性搜索，对非常大的组合类型（包含数万个或更多的数据项），速度可能会较慢；而对字典或集合，`in` 操作可以非常快。