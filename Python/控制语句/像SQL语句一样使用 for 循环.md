```python
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

names = [rec['name'] for rec in people if rec['age'] >= 45] # 类似 SQL 查询
print(names)

ages = [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
print(ages)

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())
```

