```python
print('输出的内容', end='\n')
```

> 在 Python 中，print() 默认自带 `end='\n'` 这个换行结束符，所以导致每两个 `print` 直接会换行展示，用户可以按需求更改结束符。

```python
print('hello', end='\n')
print('hello', end='\t')
print('hello', end='...')
print('Python')
```

