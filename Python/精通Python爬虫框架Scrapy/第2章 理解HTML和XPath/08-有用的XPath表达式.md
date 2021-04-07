### 2.2.1　有用的XPath表达式

文档的层次结构始于 `<html>` 元素，可以使用元素名和斜线来选择文档中的元素。比如，下面是几种表达式从 `http://example.com` 页面返回的结果。

```python
$x('/html')
  [ <html>...</html> ]
$x('/html/body')
  [ <body>...</body> ]
$x('/html/body/div')
  [ <div>...</div> ]
$x('/html/body/div/h1')
  [ <h1>Example Domain</h1> ]
$x('/html/body/div/p')
  [ <p>...</p>, <p>...</p> ]
$x('/html/body/div/p[1]')
  [ <p>...</p> ]
$x('/html/body/div/p[2]')
  [ <p>...</p> ]
```

需要注意的是，因为在这个特定页面中， `<div>` 下包含两个 `<p>` 元素，因此 `html/body/div/p` 会返回两个元素。可以使用 `p[1]` 和 `p[2]` 分别访问第一个和第二个元素。

另外还需要注意的是，从抓取的角度来说，文档标题可能是 `head` 部分中我们唯一感兴趣的元素，该元素可以通过下面的表达式进行访问。

```python
$x('//html/head/title')
  [ <title>Example Domain</title> ]
```

对于大型文档，可能需要编写一个非常大的XPath表达式以访问指定元素。为了避免这一问题，可以使用 `//` 语法，它可以让你取得某一特定类型的元素，而无需考虑其所在的层次结构。比如， `//p` 将会选择所有的 `p` 元素，而 `//a` 则会选择所有的链接。

```python
$x('//p')
  [ <p>...</p>, <p>...</p> ]
$x('//a')
  [ <a href="http://www.iana.org/domains/example">More 
information...</a> ]

```

同样， `//a` 语法也可以在层次结构中的任何地方使用。比如，要想找到 `div` 元素下的所有链接，可以使用 `//div//a` 。需要注意的是，只使用单斜线的 `//div/a` 将会得到一个空数组，这是因为在example.com中，'div'元素的直接下级中并没有任何'a'元素：

```python
$x('//div//a')
  [ <a href="http://www.iana.org/domains/example">More 
information...</a> ]
$x('//div/a')
  [ ]

```

还可以选择属性。http://example.com/中的唯一属性是链接中的 `href` ，可以使用符号@来访问该属性，如下面的代码所示。

```python
$x('//a/@href')
  [ href="http://www.iana.org/domains/example" ]

```

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 实际上，在Chrome的最新版本中， `@href` 不再返回URL，而是返回一个空字符串。不过不用担心，你的XPath表达式仍然是正确的。

还可以通过使用 `text()` 函数，只选取文本。

```python
$x('//a/text()')
  [ "More information..." ]
```

可以使用*符号来选择指定层级的所有元素。比如：

```python
$x('//div/­*')
[ <h1>Example Domain</h1>, <p>...</p>, <p>...</p> ]
```

你将会发现选择包含指定属性（比如 `@class` ）或是属性为特定值的元素非常有用。可以使用更高级的谓词来选取元素，而不再是前面例子中使用过的 `p[1]` 和 `p[2]` 。比如， `//a[@href]` 可以用来选择包含 `href` 属性的链接，而 `//a[@href="<a class="my_markdown" href="['http://www.iana.org/domains/example']">http://www.iana.org/domains/example</a>"]` 则是选择 `href` 属性为特定值的链接。

更加有用的是，它还拥有找到 `href` 属性中以一个特定子字符串起始或包含的能力。下面是几个例子。

```python
$x('//a[@href]')
  [ <a href="http://www.iana.org/domains/example">More information...</a> ]
$x('//a[@href="http://www.iana.org/domains/example"]')
  [ <a href="http://www.iana.org/domains/example">More information...</a> ]
$x('//a[contains(@href, "iana")]')
  [ <a href="http://www.iana.org/domains/example">More information...</a> ]
$x('//a[starts-with(@href, "http://www.")]')
  [ <a href="http://www.iana.org/domains/example">More information...</a>]
$x('//a[not(contains(@href, "abc"))]')
  [ <a href="http://www.iana.org/domains/example">More information...</a>]

```

XPath有很多像 `not()` 、 `contains()` 和 `starts-with()` 这样的函数，你可以在在线文档 （ `
<a class="my_markdown" href="['http://www.w3schools.com/xsl/xsl_functions.asp']">http://www.w3schools.com/xsl/xsl_functions.asp</a>
` ）中找到它们，不过即使不使用这些函数，你也可以走得很远。

现在，我还要再多说一点，大家可以在Scrapy命令行中使用同样的XPath表达式。要打开一个页面并访问Scrapy命令行，只需要输入如下命令：

```python
scrapy shell http://example.com
```

在命令行中，可以访问很多在编写爬虫代码时经常需要用到的变量（参见下一章）。这其中最重要的就是响应，对于HTML文档来说就是 `HtmlResponse` 类，该类可以让你通过 `xpath()` 方法模拟Chrome中的 `$x` 。下面是一些示例。

```python
response.xpath('/html').extract()
  [u'<html><head><title>...</body></html>']
response.xpath('/html/body/div/h1').extract()
  [u'<h1>Example Domain</h1>']
response.xpath('/html/body/div/p').extract()
  [u'<p>This domain ... permission.</p>', u'<p><a href="http://www. iana.org/domains/example">More information...</a></p>']
response.xpath('//html/head/title').extract()
  [u'<title>Example Domain</title>']
response.xpath('//a').extract()
  [u'<a href="http://www.iana.org/domains/example">More 
information...</a>']
response.xpath('//a/@href').extract()
  [u'http://www.iana.org/domains/example']
response.xpath('//a/text()').extract()
  [u'More information...']
response.xpath('//a[starts-with(@href, "http://www.")]').extract()
  [u'<a href="http://www.iana.org/domains/example">More 
information...</a>']

```

这就意味着，你可以使用Chrome开发XPath表达式，然后在Scrapy爬虫中使用它们，正如我们在下一节中将要看到的那样。

