[toc]

### 2.2.2　Beautiful Soup

**Beautiful Soup** 是一个非常流行的Python库，它可以解析网页，并提供了定位内容的便捷接口。如果你还没有安装该模块，可以使用下面的命令安装其最新版本。

```python
pip install beautifulsoup4
```

使用Beautiful Soup的第一步是将已下载的HTML内容解析为soup文档。由于许多网页都不具备良好的HTML格式，因此Beautiful Soup需要对其标签开合状态进行修正。例如，在下面这个简单网页的列表中，存在属性值两侧引号缺失和标签未闭合的问题。

```python
<ul class=country_or_district>
    <li>Area
    <li>Population
</ul>
```

如果 `Population` 列表项被解析为 `Area` 列表项的子元素，而不是并列的两个列表项的话，我们在抓取时就会得到错误的结果。下面让我们看一下Beautiful Soup是如何处理的。

```python
>>> from bs4 import BeautifulSoup
>>> from pprint import pprint
>>> broken_html = '<ul class=country_or_district><li>Area<li>Population</ul>'
>>> # parse the HTML
>>> soup = BeautifulSoup(broken_html, 'html.parser')
>>> fixed_html = soup.prettify()
>>> pprint(fixed_html)
<ul class="country_or_district">
 <li>
  Area
  <li>
   Population
  </li>
 </li>
</ul>
```

我们可以看到，使用默认的 `html.parser` 并没有得到正确解析的HTML。从前面的代码片段可以看出，由于它使用了嵌套的 `li` 元素，因此可能会导致定位困难。幸运的是，我们还有其他解析器可以选择。我们可以安装LXML（2.2.3节中将会详细介绍），或使用 `html5lib` 。要想安装 `html5lib` ，只需使用 `pip` 。

```python
pip install html5lib
```

现在，我们可以重复这段代码，只对解析器做如下变更。

```python
>>> soup = BeautifulSoup(broken_html, 'html5lib')
>>> fixed_html = soup.prettify()
>>> pprint(fixed_html)
<html>
   <head>
   </head>
   <body>
     <ul class="country_or_district">
       <li>
         Area
       </li>
       <li>
         Population
       </li>
     </ul>
   </body>
</html>
```

此时，使用了 `html5lib` 的 `BeautifulSoup` 已经能够正确解析缺失的属性引号以及闭合标签，并且还添加了 `<html>` 和 `<body>` 标签，使其成为完整的HTML文档。当你使用 `lxml` 时，也可以看到类似的结果。

现在，我们可以使用 `find()` 和 `find_all()` 方法来定位我们需要的元素了。

```python
>>> ul = soup.find('ul', attrs={'class':'country_or_district'})
>>> ul.find('li')  # returns just the first match
<li>Area</li>
>>> ul.find_all('li')  # returns all matches
[<li>Area</li>, <li>Population</li>]
```

> <img class="my_markdown" src="../images/16.jpg" style="zoom:50%;" />
> 想要了解可用方法和参数的完整列表，请访问Beautiful Soup的官方文档。

下面是使用该方法抽取示例网站中国家（或地区）面积数据的完整代码。

```python
>>> from bs4 import BeautifulSoup
>>> url = 'http://example.python-scraping.com/places/view/United-Kingdom-239'
>>> html = download(url)
>>> soup = BeautifulSoup(html)
>>> # locate the area row
>>> tr = soup.find(attrs={'id':'places_area__row'})
>>> td = tr.find(attrs={'class':'w2p_fw'}) # locate the data element
>>> area = td.text # extract the text from the data element
>>> print(area)
244,820 square kilometres
```

这段代码虽然比正则表达式的代码更加复杂，但又更容易构造和理解。而且，像多余的空格和标签属性这种布局上的小变化，我们也无须再担心了。我们还知道即使页面中包含了不完整的HTML，Beautiful Soup也能帮助我们整理该页面，从而让我们可以从非常不完整的网站代码中抽取数据。

