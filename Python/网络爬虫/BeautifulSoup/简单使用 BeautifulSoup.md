BeautifulSoup 库最常用的对象恰好是 BeautifulSoup 对象：

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), features="html.parser")
print(bsObj.h1)
```

运行结果如下：

```shell
<h1>An Interesting Title</h1>
```

BeautifulSoup 对象将 HTML 内容转换成下面的结构：

```
html -> <html><head>...</head><body>...</body></html>
-- head -> <head><title>A Useful Page</title></head>
	-- title -> <title>A Useful Page</title>
-- body -> <body>h1>An Int...</h1><div>Lorem ip...</div></body>
	-- h1 -> <h1>An Interesting Title</h1>
	-- div -> <div>Lorem Ipsum dolor...</div>
```

可以看出，我们从网页中提取的 \<h1> 标签被嵌在 BeautifulSoup 对象 bsObj 结构的第二层（html -> body ->h1）。但是我们可以直接调用它：

```
bsObj.h1
```

其实，下面的所有函数调用都可以产生同样的结果：

```
bsObj.html.body.h1
bsObj.body.h1
bsObj.html.h1
```



