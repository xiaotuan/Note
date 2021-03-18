[toc]

### 2.2.3　Lxml

**Lxml** 是基于 `libxml2` 这一XML解析库构建的Python库，它使用C语言编写，解析速度比Beautiful Soup更快，不过安装过程也更为复杂，尤其是在Windows中。最新的安装说明可以参考 `http://lxml.de/installation.html` 。如果你在自行安装该库时遇到困难，也可以使用Anaconda来实现。

你可能对Anaconda不太熟悉，它是由Continuum Analytics公司员工创建的主要专注于开源数据科学包的包和环境管理器。你可以按照其安装说明下载及安装Anaconda。需要注意的是，使用Anaconda的快速安装会将你的 `PYTHON_PATH` 设置为Conda的Python安装位置。

和Beautiful Soup一样，使用 `lxml` 模块的第一步也是将有可能不合法的HTML解析为统一格式。下面是使用该模块解析同一个不完整HTML的例子。

```python
>>> from lxml.html import fromstring, tostring
>>> broken_html = '<ul class=country_or_district><li>Area<li>Population</ul>'
>>> tree = fromstring(broken_html) # parse the HTML
>>> fixed_html = tostring(tree, pretty_print=True)
>>> print(fixed_html)
<ul class="country_or_district">
    <li>Area</li>
    <li>Population</li>
</ul>
```

同样地， `lxml` 也可以正确解析属性两侧缺失的引号，并闭合标签，不过该模块没有额外添加 `<html>` 和 `<body>` 标签。这些都不是标准XML的要求，因此对于 `lxml` 来说，插入它们并不是必要的。

解析完输入内容之后，进入选择元素的步骤，此时 `lxml` 有几种不同的方法，比如XPath选择器和类似Beautiful Soup的 `find()` 方法。不过，在本例中，我们将会使用CSS选择器，因为它更加简洁，并且能够在第5章解析动态内容时得以复用。一些读者可能由于他们在jQuery选择器方面的经验或是前端Web应用开发中的使用对它们已经有所熟悉。在本章的后续部分，我们将对比这些选择器与XPath的性能。要想使用CSS选择器，你可能需要先安装 `cssselect` 库，如下所示。

```python
pip install cssselect
```

现在，我们可以使用 `lxml` 的CSS选择器，抽取示例页面中的面积数据了。

```python
>>> tree = fromstring(html)
>>> td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
>>> area = td.text_content()
>>> print(area)
244,820 square kilometres
```

通过对代码树使用 `cssselect` 方法，我们可以利用CSS语法来选择表格中ID为 `places_area__row` 的行元素，然后是类为 `w2p_fw` 的子表格数据标签。由于 `cssselect` 返回的是一个列表，我们需要获取其中的第一个结果，并调用 `text_content` 方法，以迭代所有子元素并返回每个元素的相关文本。在本例中，尽管我们只有一个元素，但是该功能对于更加复杂的抽取示例来说非常有用。

