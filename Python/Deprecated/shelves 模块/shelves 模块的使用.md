[toc]

### 1. 保存数据

`shelves` 模块会自动将对象使用 `pickle` 模块进行保存或者读取。它很像必须打开着的字典，在程序退出时进行持久化。使用 `pickle` 模块需要手动打开或保存文件，但是 `shelves` 模块则会自动将修改过的对象使用 `pickle` 模块进行保存。例如：

```python
import shelve

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
```

这个脚本在当前目录下以 `people-shelve` 为前缀创建了一个或多个文件（在 Windows 的 Python 3.x 中， people-shelve.bak、people-shelve.dat、people-shelve.dir）。千万不要删除这些文件，其他脚本中访问这个 shelve 要确保使用相同的名字。

### 2. 读取数据

```python
import shelve

db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])

print(db['sue']['name'])
db.close()
```

### 3. 更新数据

```python
import shelve

tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

db = shelve.open('people-shelve')
sue = db['sue'] # fetch sue
sue['pay'] *= 1.50
db['sue'] = sue # update sue
db['tom'] = tom # add a new record
db.close()
```

