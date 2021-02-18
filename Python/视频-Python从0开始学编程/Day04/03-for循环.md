语法：

```python
for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2
    .......
```

例子：

```python
str1 = 'itheima'
for i in str1:
    print(i)
```

break 用在 for 循环：

```python
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
```

continue 用在 for 循环：

```python
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
```

