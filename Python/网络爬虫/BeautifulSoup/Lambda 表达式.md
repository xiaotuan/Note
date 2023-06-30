`BeautifulSoup` 允许把特定函数类型当做 `findAll` 函数的参数。唯一的限制条件是这些函数必须把一个标签作为参数且返回结果是布尔类型。

`BeautifulSoup` 用这个函数来评估它遇到的每个标签对象，最后把评估结果为 “真” 的标签保留，把其他标签剔除。

例如，下面的代码就是获取有两个属性的标签：

```python
soup.findAll(lambda tag: len(tag.attrs) == 2)
```



