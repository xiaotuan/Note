### 3.3.6　创建contract

contract有点像为爬虫设计的单元测试。它可以让你快速知道哪里有运行异常。例如，假设你在几个星期之前编写了一个抓取程序，其中包含几个爬虫，今天想要检查一下这些爬虫是否仍然能够正常工作，就可以使用这种方式。contract包含在紧挨着函数名的注释（即文档字符串）中，并且以@开头。下面来看几个contract的例子。

```python
def parse(self, response):
　　""" This function parses a property page.
　　@url http://web:9312/properties/property_000000.html
　　@returns items 1
　　@scrapes title price description address image_urls
　　@scrapes url project spider server date
　　"""
```

上述代码的含义是，检查该URL，并找到我列出的字段中有值的一个Item。现在，当你运行 `scrapy check` 时，就会去检查contract是否能够满足。

```python
$ scrapy check basic
----------------------------------------------------------------
Ran 3 contracts in 1.640s
OK

```

如果将 `url` 字段留空（通过注释掉该行来设置），你会得到一个失败描述。

```python
FAIL: [basic] parse (@scrapes post-hook)
------------------------------------------------------------------
ContractFail: 'url' field is missing

```

contract失败的原因可能是爬虫代码无法运行，或者是你要检查的URL的XPath表达式已经过时了。虽然结果并不详尽，但它是抵御坏代码的第一道灵巧的防线。

综合上面的内容，下面给出我们的第一个基础爬虫的代码。

```python
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem
import datetime
import urlparse
import socket
import scrapy
class BasicSpider(scrapy.Spider):
　　name = "basic"
　　allowed_domains = ["web"]
　　# Start on a property page
　　start_urls = (
　　　　'http://web:9312/properties/property_000000.html',
　　)
　　def parse(self, response):
　　　　""" This function parses a property page.
　　　　@url http://web:9312/properties/property_000000.html
　　　　@returns items 1
　　　　@scrapes title price description address image_urls
　　　　@scrapes url project spider server date
　　　　"""
　　　　# Create the loader using the response
　　　　l = ItemLoader(item=PropertiesItem(), response=response)
　　　　# Load fields using XPath expressions
　　　　l.add_xpath('title', '//­*[@itemprop="name"][1]/text()',
　　　　　　　　　　MapCompose(unicode.strip, unicode.title))
　　　　l.add_xpath('price', './/­*[@itemprop="price"][1]/text()',
　　　　　　　　　　MapCompose(lambda i: i.replace(',', ''),
　　　　　　　　　　float),
　　　　　　　　　　re='[,.0-9]+')
　　　　l.add_xpath('description', '//­*[@itemprop="description"]'
　　　　　　　　　　'[1]/text()',
　　　　　　　　　　MapCompose(unicode.strip), Join())
　　　　l.add_xpath('address',
　　　　　　　　　　'//­*[@itemtype="http://schema.org/Place"]'
　　　　　　　　　　'[1]/text()',
　　　　　　　　　　MapCompose(unicode.strip))
　　　　l.add_xpath('image_urls', '//­*[@itemprop="image"]'
　　　　　　　　　　'[1]/@src', MapCompose(
　　　　　　　　　　lambda i: urlparse.urljoin(response.url, i)))
　　　　# Housekeeping fields
　　　　l.add_value('url', response.url)
　　　　l.add_value('project', self.settings.get('BOT_NAME'))
　　　　l.add_value('spider', self.name)
　　　　l.add_value('server', socket.gethostname())
　　　　l.add_value('date', datetime.datetime.now())
　　　　return l.load_item()
```

