[toc]

### 8.4　使用shell命令抓取

现在Scrapy已经可以爬取国家（或地区）页面了，下面还需要定义要抓取哪些数据。为了帮助测试如何从网页中抽取数据，Scrapy提供了一个很方便的命令—— `shell` ，可以通过Python或IPython解释器向我们展示Scrapy的API。

我们可以使用想要作为起始的URL调用命令，如下所示。

```python
$ scrapy shell http://example.python-scraping.com/view/United-Kingdom-239
...
[s] Available Scrapy objects:
[s] scrapy scrapy module (contains scrapy.Request, scrapy.Selector,
etc)
[s] crawler <scrapy.crawler.Crawler object at 0x7fd18a669cc0>
[s] item {}
[s] request <GET http://example.python-scraping.com/view/United-Kingdom-239>
[s] response <200 http://example.python-scraping.com/view/United-Kingdom-239>
[s] settings <scrapy.settings.Settings object at 0x7fd189655940>
[s] spider <CountryOrDistrictSpider 'country_or_district' at 0x7fd1893dd320>
[s] Useful shortcuts:
[s] fetch(url[, redirect=True]) Fetch URL and update local objects (by
default, redirects are followed)
[s] fetch(req) Fetch a scrapy.Request and update local
objects
[s] shelp() Shell help (print this help)
[s] view(response) View response in a browser
In [1]:
```

现在我们可以查询返回对象，检查哪些数据可以使用。

```python
In [1]: response.url
Out[1]:'http://example.python-scraping.com/view/United-Kingdom-239'
In [2]: response.status
Out[2]: 200
```

Scrapy使用 `lxml` 抓取数据，所以我们仍然可以使用第2章中用过的CSS选择器。

```python
In [3]: response.css('tr#places_country_or_district__row td.w2p_fw::text')
[<Selector xpath=u"descendant-or-self::
 tr[@id = 'places_country_or_district__row']/descendant-or-self::
 */td[@class and contains(
 concat(' ', normalize-space(@class), ' '),
 ' w2p_fw ')]/text()" data=u'United Kingdom'>]
```

该方法返回一个 `lxml` 选择器的列表。你可能还能认出Scrapy和 `lxml` 用于选择item的一些XPath语法。正如我们在第2章所学到的， `lxml` 在抽取内容之前，会把所有的CSS选择器转换成XPath。

为了从该国家（或地区）的数据行中实际获取文本，我们必须调用 `extract()` 方法。

```python
In [4]: name_css = 'tr#places_country_or_district__row td.w2p_fw::text'
In [5]: response.css(name_css).extract()
Out[5]: [u'United Kingdom']
In [6]: pop_xpath =
'//tr[@id="places_population__row"]/td[@class="w2p_fw"]/text()'
In [7]: response.xpath(pop_xpath).extract()
Out[7]: [u'62,348,447']
```

如上面的输出所示，Scrapy的 `response` 对象既可以使用 `css` 也可以使用 `xpath` 进行解析，使其变得非常灵活，无论明显的内容还是难以获取的内容都能够得到。

然后，可以在先前生成的 `example/spiders/country_or_district.py` 文件的 `parse_item()` 方法中使用这些选择器。请注意，我们使用了字典的语法设置 `scrapy.Item` 对象的属性。

```python
def parse_item(self, response):
    item = CountryItem()
    name_css = 'tr#places_country_or_district__row td.w2p_fw::text'
    item['name'] = response.css(name_css).extract()
    pop_xpath =
'//tr[@id="places_population__row"]/td[@class="w2p_fw"]/text()'
    item['population'] = response.xpath(pop_xpath).extract()
    return item
```

