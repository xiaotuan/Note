[toc]

### 1. while ... else

语法：

```python
while 条件:
    条件成立重复执行的代码
else:
    循环正常结束之后要执行的代码
```

例子：

```python
i = 0
while i <= 5:
    print('媳妇儿，我错了')
    i += 1
else:
    print('媳妇原谅我了，真开心呐，哈哈哈哈')
```

### 2. for ... else

语法：

```python
for 临时变量 in 序列:
    重复执行的代码
    ...
else:
    循环正常结束之后要执行的代码
```

例子：

```python
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执行的代码')
```

### 3. break 和 continue 对 else 的影响

所谓 else 指的是循环正常结束之后要执行的代码，即如果是 break 终止循环的情况，else 下方缩进的代码将不执行。

因为 continue 是退出当前一次循环，继续下一次循环，所以该循环在 continue 控制下是可以正常结束的，当循环结束后，则执行了 else 缩进的代码。