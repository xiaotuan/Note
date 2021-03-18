[toc]

## 9.3　Gap

为了演示使用网站地图查看内容，我们将使用Gap的网站。

Gap拥有一个结构化良好的网站，通过Sitemap可以帮助网络爬虫定位其最新的内容。如果我们使用第1章中学到的技术调研该网站，则会发现在 `http://www.gap.com/robots.txt` 这一网址下的 `robots.txt` 文件中包含了网站地图的链接。

```python
Sitemap: http://www.gap.com/products/sitemap_index.xml
```

下面是链接的 `Sitemap` 文件中的内容。

```python
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap>
        <loc>http://www.gap.com/products/sitemap_1.xml</loc>
        <lastmod>2017-03-24</lastmod>
    </sitemap>
    <sitemap>
        <loc>http://www.gap.com/products/sitemap_2.xml</loc>
        <lastmod>2017-03-24</lastmod>
    </sitemap>
</sitemapindex>
```

如上所示，Sitemap链接中的内容不仅仅是索引，其中又包含了其他 `Sitemap` 文件的链接。这些其他的 `Sitemap` 文件中则包含了数千种产品类目的链接，比如 `http://www.gap.com/products/womens-jogger- pants.jsp` ，如图9.8所示。

![84.png](../images/84.png)
<center class="my_markdown"><b class="my_markdown">图9.8</b></center>

这里有大量需要爬取的内容，因此我们将使用第4章中开发的多线程爬虫。你可能还记得该爬虫支持URL模式以匹配页面。我们同样可以定义一个 `scraper_callback` 关键字参数变量，可以让我们解析更多链接。

下面是爬取Gap网站中 `Sitemap` 链接的示例回调函数。

```python
from lxml import etree
from threaded_crawler import threaded_crawler
def scrape_callback(url, html):
    if url.endswith('.xml'):
        # Parse the sitemap XML file
        tree = etree.fromstring(html)
        links = [e[0].text for e in tree]
        return links
    else:
        # Add scraping code here
        pass
```

该回调函数首先检查下载到的URL的扩展名。如果扩展名为 `.xml` ，则认为下载到的URL是 `Sitemap` 文件，然后使用 `lxml` 的 `etree` 模块解析XML文件并从中抽取链接。否则，认为这是一个类目URL，不过本例中还没有实现抓取类目的功能。现在，我们可以在多线程爬虫中使用该回调函数来爬取 `gap.com` 了。

```python
In [1]: from chp9.gap_scraper_callback import scrape_callback
In [2]: from chp4.threaded_crawler import threaded_crawler
In [3]: sitemap = 'http://www.gap.com/products/sitemap_index.xml'
In [4]: threaded_crawler(sitemap, '[gap.com]*',
scraper_callback=scrape_callback)
10
[<Thread(Thread-517, started daemon 140145732585216)>]
Exception in thread Thread-517:
Traceback (most recent call last):
...
File "src/lxml/parser.pxi", line 1843, in lxml.etree._parseMemoryDocument
(src/lxml/lxml.etree.c:118282)
ValueError: Unicode strings with encoding declaration are not supported.
Please use bytes input or XML fragments without declaration.
```

不幸的是， `lxml` 期望加载来自字节或XML片段的内容，而我们存储的是Unicode的响应（因为这样可以让我们使用正则表达式进行解析，并且可以更容易地存储到磁盘中，如第3章和第4章所述）。不过，我们依然可以在本函数中访问该URL。虽然效率不高，但是我们可以再次加载页面；如果我们只对XML页面执行该操作，则可以减少请求的数量，从而不会增加太多加载时间。当然，如果我们使用了缓存的话，也可以提高效率。

下面我们将重写回调函数。

```python
import requests
def scrape_callback(url, html):
    if url.endswith('.xml'):
        # Parse the sitemap XML file
        resp = requests.get(url)
        tree = etree.fromstring(resp.content)
        links = [e[0].text for e in tree]
        return links
    else:
        # Add scraping code here
        pass
```

现在，如果我们再次尝试运行，可以看到执行成功。

```python
In [4]: threaded_crawler(sitemap, '[gap.com]*',
scraper_callback=scrape_callback)
10
[<Thread(Thread-51, started daemon 139775751223040)>]
Downloading: http://www.gap.com/products/sitemap_index.xml
Downloading: http://www.gap.com/products/sitemap_2.xml
Downloading: http://www.gap.com/products/gap-canada-français-index.jsp
Downloading: http://www.gap.co.uk/products/index.jsp
Skipping
http://www.gap.co.uk/products/low-impact-sport-bras-women-C1077315.jsp due
to depth Skipping
http://www.gap.co.uk/products/sport-bras-women-C1077300.jsp due to depth
Skipping
http://www.gap.co.uk/products/long-sleeved-tees-tanks-women-C1077314.jsp
due to depth Skipping
http://www.gap.co.uk/products/short-sleeved-tees-tanks-women-C1077312.jsp
due to depth ...
```

和预期一致， `Sitemap` 文件首先被下载，然后是服装类目。在网络爬虫项目中，你会发现自己可能需要修改及调整代码和类，以适应新的问题。这只是从互联网上抓取内容时诸多令人兴奋的挑战之一。

