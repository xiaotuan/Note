`pickle` 模块可以将内存中的 `Python` 对象转化成序列化的字节流，也可以根据序列化的字节流重新构建原来内存中的对象。例如：

```python
import pickle

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

# 将对象保存成字节流文件
dbfile = open('people-pickle', 'wb')    # 使用 3.x 的二进制模式文件
pickle.dump(db, dbfile) # 字节数据，而非字符串
dbfile.close() 

# 从字节流文件中重新生成对象
dbfile = open('people-pickle', 'rb')    # 使用 3.x 的二进制模式文件
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key])
```

> 注意：用于存储 `pickle` 生成的文件必须是以二进制方式打开的。
