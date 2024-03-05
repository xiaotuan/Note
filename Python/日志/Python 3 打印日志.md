**方法一：**

```python
novelwebaddress = {
    '寒门枭士' : 'https://www.bookabc.cc/abc/24/24228/',
    '我的二师兄吕少卿' : 'https://www.bookabc.cc/abc/94/94102/'
}
# 打印小说菜单
print("小说列表：")
print()
index = 1
for key in novelwebaddress:
    print("%d. %s" % (index, key))
    index += 1
```

**方法二：**

```python
novelwebaddress = {
    '寒门枭士' : 'https://www.bookabc.cc/abc/24/24228/',
    '我的二师兄吕少卿' : 'https://www.bookabc.cc/abc/94/94102/'
}
# 打印小说菜单
print("小说列表：")
print()
index = 1
for key in novelwebaddress:
    print(str(index) + ". " + str(key))
    index += 1
```

**方法三：打印日志不换行**

```python
print("请选择要阅读的小说编号：", end='')
```

**方法四：**

```python
```

