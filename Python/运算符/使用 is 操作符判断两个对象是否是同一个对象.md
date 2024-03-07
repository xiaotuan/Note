`is` 操作符用于判断两个对象是否指向的是同一个对象，如果是则会返回 `true`：

```python
>>> a = [ 'Retention', 3, None ]
>>> b = [ 'Retention', 3, None ]
>>> a is b
False
>>> b = a
>>> a is b
True
```

使用 `is` 对数据项进行比较可能会导致直觉外的结果。例如，在前面的实例中，虽然 `a` 与 `b` 在最初设置为同样的列表值，但是列表本身是以单独的 `list` 对象存储的，因此，在第一次使用时，`is` 操作符将返回 `false`。

> 注意：`is` 操作符只需要对对象所在的内存地址进行比较——同样的地址存储的是同样的对象。

最常见的使用 `is` 的情况是将数据项与内置的空对象 `None` 进行比较：

```python
>>> a = "Something"
>>> b = None
>>> a is not None, b is None
(True, True)
```

