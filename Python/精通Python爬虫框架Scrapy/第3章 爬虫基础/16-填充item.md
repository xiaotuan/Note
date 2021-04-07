### 3.3.3　填充item

我们将会对前面的代码进行少量修改，以填充 `PropertiesItem` 。你将会看到，尽管修改非常轻微，但是会“解锁”大量的新功能。

首先，需要引入 `PropertiesItem` 类。如前所述，它在 `properties` 目录的 `items.py` 文件中，也就是 `properties.items` 模块中。我们回到 `properties/spiders/basic.py` 文件，使用如下命令引入该模块。

```python
from properties.items import PropertiesItem
```

然后需要进行实例化，并返回一个对象。这非常简单。在 `parse()` 方法中，可以通过添加 `item = PropertiesItem()` 语句创建一个新的item，然后可以按如下方式为其字段分配表达式。

```python
item['title'] =
response.xpath('//­*[@itemprop="name"][1]/text()').extract()
```

最后，使用 `return item` 返回item。最新版的 `properties/spiders/basic.py` 代码如下所示。

```python
import scrapy
from properties.items import PropertiesItem
class BasicSpider(scrapy.Spider):
　　name = "basic"
　　allowed_domains = ["web"]
　　start_urls = (
　　　　'http://web:9312/properties/property_000000.html',
　　)
　　def parse(self, response):
　　　　item = PropertiesItem()
　　　　item['title'] = response.xpath(
　　　　　　'//­*[@itemprop="name"][1]/text()').extract()
　　　　item['price'] = response.xpath(
　　　　　　'//­*[@itemprop="price"][1]/text()').re('[.0-9]+')
　　　　item['description'] = response.xpath(
　　　　　　'//­*[@itemprop="description"][1]/text()').extract()
　　　　item['address'] = response.xpath(
　　　　　　'//­*[@itemtype="http://schema.org/'
　　　　　　'Place"][1]/text()').extract()
　　　　item['image_urls'] = response.xpath(
　　　　　　'//­*[@itemprop="image"][1]/@src').extract()
　　　　return item
```

现在，如果你再像之前那样运行 `scrapy crawl basic` ，就会发现一个非常小但很重要的区别。我们不再在日志中记录抓取值（所以没有包含字段值的 `DEBUG:` 行了），而是看到如下的输出行。

```python
DEBUG: Scraped from <200
http://...000.html>
　{'address': [u'Angel, London'],
　 'description': [u'website ... offered'],
　 'image_urls': [u'.../images/i01.jpg'],
　 'price': [u'334.39'],
　 'title': [u'set unique family well']}
```

这是从本页面抓取得到的 `PropertiesItem` 。非常好，因为Scrapy是围绕着 `Items` 的概念构建的，也就是说你现在可以使用后续章节中介绍的管道，对其进行过滤和丰富了，并且可以通过“Feed exports”将其以不同的格式导出存储到不同的地方。

