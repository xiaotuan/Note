`for..in` 语句的语法格式如下：

```python
for variable in iterable:
    statements
```

> 提示： `for...in` 循环也支持 `break` 语句与 `continue` 语句。

例如：

```python
for country in [ 'Denmark', 'Finland', 'Norway', 'Sweden' ]:
    print(country)
```

在实际的代码中，更常见的做法是使用变量：

```python
countries = [ 'Denmark', 'Finland', 'Norway', 'Sweden' ]
for country in countries:
    print(country)
```

实际上，完整的列表（或元组）可以使用 `print()` 函数直接打印：

```python
print(countries)
```

