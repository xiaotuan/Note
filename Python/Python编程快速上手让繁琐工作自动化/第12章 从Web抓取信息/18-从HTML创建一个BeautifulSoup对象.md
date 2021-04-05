### 12.5.1　从HTML创建一个BeautifulSoup对象

`bs4.BeautifulSoup()` 函数调用时需要一个字符串，其中包含将要解析的HTML。 `bs4.BeautifulSoup()` 函数返回一个 `BeautifulSoup` 对象。在交互式环境中输入以下代码，同时保持计算机与因特网的连接：

```javascript
>>> import requests, bs4
>>> res = requests.get('https://nosta')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
>>> type(noStarchSoup)
<class 'bs4.BeautifulSoup'>
```

这段代码利用 `requests.get()` 函数从No Starch出版社网站下载主页，然后将响应结果的 `text` 属性传递给 `bs4.BeautifulSoup()` 。它返回的 `BeautifulSoup` 对象保存在变量 `noStarchSoup` 中。

也可以向 `bs4.BeautifulSoup()` 传递一个 `File` 对象，以及第二个参数，告诉 `Beautiful Soup` 使用哪个解析器来分析HTML。

在交互式环境中输入以下代码（确保example.html文件在工作目录中）：

```javascript
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
>>> type(exampleSoup)
<class 'bs4.BeautifulSoup'>
```

这里使用的 `'html.parser'` 解析器是 Python 自带的。但是，如果你安装了第三方 `lxml` 模块，你就可以使用更快的 `'lxml'` 解析器。按照附录A中的说明，运行 `pip install --user lxml` 来安装这个模块。如果忘记了包含第二个参数，将导致 `UserWarning：No parser was explicitly specified warning` 。

有了 `BeautifulSoup` 对象之后，就可以利用它的方法，定位HTML文档中的特定部分。

