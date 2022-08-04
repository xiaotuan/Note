可以使用 `enumerate()` 方法来获取每个元素的索引及其值：

```python
bicycles = [ 'trek', 'cannondale', 'redline', 'specialized' ]

for index, bicycle in enumerate(bicycles):
    print("index: " + str(index) + ", value: " + bicycle)
```

