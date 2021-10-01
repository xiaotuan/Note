[toc]

### 1. range() 函数的使用

`range()` 函数用于生成一系列数。

```python
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
```

`range()` 函数最多可以传递 3 个参数：

+ 当只传递一个参数 n 时，生成是数列从 0 到 n - 1。

+ 当传递两个参数 a, b 时，生成数列从 a 到 b - 1。

+ 当传递三个参数时，第三个参数表示步长。例如：

  ```python
  range(2, 12, 2)
  // 2, 4, 6, 8, 10
  ```

  

