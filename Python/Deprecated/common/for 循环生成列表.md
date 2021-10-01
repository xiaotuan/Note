for 循环生成列表的语法：

```console
list = [列表元素 for 语句]
```

例如：

```python
list_0 = [ item * item for item in range(5)]
生成的列表：
[0, 1, 4, 9, 16]
```

上面的代码解析如下：

range(5) 表示生成 0 ~ 4 序列，item 为循环序列的值 0 ~ 4，列表的值为 0 ~ 4 的平方。