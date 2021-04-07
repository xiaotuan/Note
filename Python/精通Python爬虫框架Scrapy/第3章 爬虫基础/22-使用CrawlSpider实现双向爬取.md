### 3.4.2　使用CrawlSpider实现双向爬取

如果感觉上面的双向爬取有些冗长，则说明你确实发现了关键问题。Scrapy尝试简化所有此类通用情况，以使其编码更加简单。最简单的实现同样结果的方式是使用 `CrawlSpider` ，这是一个能够更容易地实现这种爬取的类。为了实现它，我们需要使用 `genspider` 命令，并设置 `-t crawl` 参数，以使用 `crawl` 爬虫模板创建一个爬虫。

```python
$ scrapy genspider -t crawl easy web
Created spider 'crawl' using template 'crawl' in module:
　properties.spiders.easy

```

现在，文件 `properties/spiders/easy.py` 包含如下内容。

```python
...
class EasySpider(CrawlSpider):
　　name = 'easy'
　　allowed_domains = ['web']
　　start_urls = ['http://www.web/']
　　rules = (
　　　　Rule(LinkExtractor(allow=r'Items/'),
callback='parse_item', follow=True),
　　)
　　def parse_item(self, response):
　　　　...
```

当你阅读这段自动生成的代码时，会发现它和之前的爬虫有些相似，不过在此处的类声明中，会发现爬虫是继承自 `CrawlSpider` ，而不再是 `Spider` 。 `CrawlSpider` 提供了一个使用 `rules` 变量实现的 `parse()` 方法，这与我们之前例子中手工实现的功能一致。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 你可能会感到疑惑，为什么我首先给出了手工实现的版本，而不是直接给出捷径。这是因为你在手工实现的示例中，学会了使用回调的 `yield` 方式的请求，这是一个非常有用和基础的技术，我们将会在后续的章节中不断使用它，因此理解该内容非常值得。

现在，我们要把 `start_urls` 设置成第一个索引页，并且用我们之前的实现替换预定义的 `parse_item()` 方法。这次我们将不再需要实现任何 `parse()` 方法。我们将预定义的 `rules` 变量替换为两条规则，即水平抓取和垂直抓取。

```python
rules = (
Rule(LinkExtractor(restrict_xpaths='//­*[contains(@class,"next")]')),
Rule(LinkExtractor(restrict_xpaths='//­*[@itemprop="url"]'),
　　　　 callback='parse_item')
)
```

这两条规则使用的是和我们之前手工实现的示例中相同的XPath表达式，不过这里没有了 `a` 或 `href` 的限制。顾名思义， `LinkExtractor` 正是专门用于抽取链接的，因此在默认情况下，它们会去查找 `a` （及 `area` ） `href` 属性。你可以通过设置 `LinkExtractor()` 的 `tags` 和 `attrs` 参数来进行自定义。需要注意的是，回调参数目前是包含回调方法名称的字符串（比如 `'parse_item'` ），而不是方法引用，如 `Request(self.parse_item)` 。最后，除非设置了 `callback` 参数，否则 `Rule` 将跟踪已经抽取的URL，也就是说它将会扫描目标页面以获取额外的链接并跟踪它们。如果设置了 `callback` ， `Rule` 将不会跟踪目标页面的链接。如果你希望它跟踪链接，应当在 `callback` 方法中使用 `return` 或 `yield` 返回它们，或者将 `Rule()` 的 `follow` 参数设置为 `true` 。当你的房源页既包含 `Item` 又包含其他有用的导航链接时，该功能可能会非常有用。

运行该爬虫，可以得到和手工实现的爬虫相同的结果，不过现在使用的是一个更加简单的源代码。

```python
$ scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=90

```

