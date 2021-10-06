字符串的 `split()` 方法用于分割字符串，当方法中没有参数时，默认分割符为空格（' '）。例如：

```python
bob = 'Bob Smith'
bob.split()
// ['Bob', 'Smith']
```

也可以传递用于分割字符串的字符串给 `split()` 方法（用于分割字符串的字符串不会包含在结果中）。例如：

```python
bob = 'Bob Smith'
bob.split('i')
// ['Bob sm', 'th']
```

