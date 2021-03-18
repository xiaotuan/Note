[toc]

### 8.6　使用Scrapely实现自动化抓取

为了抓取标注域，Portia使用了 **Scrapely** 库，这是一款独立于Portia之外的非常有用的开源工具。Scrapely使用训练数据建立从网页中抓取哪些内容的模型。之后，训练模型可以在抓取相同结构的其他网页时得以应用。

你可以使用 `pip` 安装它。

```python
pip install scrapely
```

下面是该工具的运行示例。

```python
>>> from scrapely import Scraper
>>> s = Scraper()
>>> train_url = 'http://example.python-scraping.com/view/Afghanistan-1'
>>> s.train(train_url, {'name': 'Afghanistan', 'population': '29,121,286'})
>>> test_url = 'http://example. python-scraping.com/view/United-Kingdom-239'
>>> s.scrape(test_url)
[{u'name': [u'United Kingdom'], u'population': [u'62,348,447']}]
```

首先，将我们想要从 `Afghanistan` 网页中抓取的数据传给Scrapely以训练模型（本例中是国家（或地区）名称和人口数量）。然后，在另一个不同的国家（或地区）页上应用该模型，可以看出Scrapely使用该训练模型返回了正确的国家（或地区）名称和人口数量。

这一工作流允许我们无须知晓网页结构，只是把所需内容抽取出来作为训练案例（或多个训练案例），就可以抓取网页。如果网页内容是静态的，在布局发生改变时，这种方法就会非常有用。例如一个新闻网站，已发表文章的文本一般不会发生变化，但是其布局可能会更新。这种情况下，Scrapely可以使用相同的数据重新训练，针对新的网站结构生成模型。为了使该例正常工作，你需要将训练数据存储在某个地方以便复用。

在测试Scrapely时，此处使用的示例网页具有良好的结构，每个数据类型的标签和属性都是独立的，因此Scrapely可以很轻松地正确训练模型。而对于更加复杂的网页，Scrapely可能会在定位内容时失败。在Scrapely的文档中会警告你应当“谨慎训练”。由于机器学习正在逐渐变快变简单，也许会有更加稳健的自动化爬虫库发布，不过就目前而言，了解如何使用本书中介绍的技术直接抓取网站仍然是非常有用的。

