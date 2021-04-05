### 4.2.4　enumerate()函数与列表一起使用

如果在 `for` 循环中不用 `range(len(someList))` 技术来获取列表中各表项的整数索引，还可以调用 `enumerate()` 函数。在循环的每次迭代中， `enumerate()` 函数将返回两个值：列表中表项的索引和列表中的表项本身。例如，这段代码等价于4.2.1小节“列表用于循环”中的代码：

```javascript
>>>  supplies = ['pens', 'staplers', 'flamethrowers', 'binders'] 
>>> for index, item in enumerate(supplies): 
..．     print('Index ' + str(index) + ' in supplies is: ' + item) 
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
```

如果在循环块中同时需要表项和表项的索引，那么 `enumerate()` 函数很有用。

