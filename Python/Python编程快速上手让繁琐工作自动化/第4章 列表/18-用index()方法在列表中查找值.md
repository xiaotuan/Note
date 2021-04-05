### 4.4.1　用index()方法在列表中查找值

列表值有一个 `index()` 方法，可以传入一个值：如果该值存在于列表中，就返回它的索引；如果该值不在列表中，Python就报 `ValueError` 错误。在交互式环境中输入以下代码：

```javascript
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('howdy howdy howdy')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    spam.index('howdy howdy howdy')
ValueError: 'howdy howdy howdy' is not in list
```

如果列表中存在重复的值，就返回它第一次出现的索引。在交互式环境中输入以下代码，注意 `index()` 方法返回1，而不是3：

```javascript
>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
>>> spam.index('Pooka')
1
```

