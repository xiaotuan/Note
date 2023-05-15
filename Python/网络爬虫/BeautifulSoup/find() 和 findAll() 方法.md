BeautifulSoup 文档里两者的定义是这样的：

```python
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
```

+ 标签参数 `tag`，你可以传入一个或多个标签的名称。

  ```python
  .findAll({"h1", "h2", "h3", "h4", "h5", "h6"})
  ```

+ 属性参数 `attributes` 是用一个 Python 字典封装一个标签的若干属性和对应的属性值：

  ```python
  .findAll("span", {"class":{"green", "red"}})
  ```

+ 递归参数 `recursive` 是一个布尔变量。如果 `recursive` 设置为 `True`，`findAll` 就会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签。如果 `recursive` 设置为 `False`，`findAll` 就只查找文档的一级标签。`findAll` 默认是支持递归查找的。

+ 文本参数 `text` 是用标签的文本内容去匹配，而不是用标签的属性。假如我们想查找前面网页中包含 "the prince" 内容的标签数量，可以使用如下代码：

  ```python
  nameList = bsObj.findAll(text="the prince")
  print(len(nameList))
  ```

+ 范围限制参数 `limit`，如果你只对网页中获取的前 x 项结果感兴趣，就可以设置它。但是要注意，这个参数设置之后，获得的前几项结果是按照网页上的顺序排序的，未必是你想要的那前几项。

+ 关键词参数 `keyword`，可以让你选择那些具有制定属性的标签。例如：

  ```python
  allText = bsObj.findAll(id="text")
  print(allText[0].get_text())
  ```

  > 注意：虽然关键词参数 keyword 在一些场景中很有用，但是，它是 BeautifulSoup 在技术上做的一个冗余功能。任何用关键词参数能够完成的任务，同样可以用其他方法解决。
  >
  > 例如，下面两行代码是完全一样的：
  >
  > ```python
  > bsObj.findAll(id="text")
  > bsObj.findAll("", {"id":"text"})
  > ```
  >
  > 另外，用 keyword 偶尔会出现问题，尤其是在用 class 属性查找标签的时候，因为 class 是 Python 中受保户的关键字。假如你运行下面的代码，Python 就会因为你误用 class 保留字而产生一个语法错误：
  >
  > ```python
  > bsObj.findAll(class="green")
  > ```
  >
  > 可以在 class 后面增加一个下划线来解决：
  >
  > ```python
  > bsObj.findAll(class_="green")
  > ```
  >
  > 另外，你也可以用属性参数把 class 用引号包起来：
  >
  > ```python
  > bsObj.findAll("", {"class":"green"})
  > ```

  