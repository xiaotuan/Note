### 3.3.5　清理——item装载器与管理字段

恭喜，你在创建基础爬虫方面做得不错！下面让我们做得更专业一些吧。

首先，我们使用一个强大的工具类—— `ItemLoader` ，以替代那些杂乱的 `extract()` 和 `xpath()` 操作。通过使用该类，我们的 `parse()` 方法会按如下进行代码变更。

```python
def parse(self, response):
　　l = ItemLoader(item=PropertiesItem(), response=response)
　　l.add_xpath('title', '//­*[@itemprop="name"][1]/text()')
　　l.add_xpath('price', './/­*[@itemprop="price"]'
　　　　　 '[1]/text()', re='[,.0-9]+')
　　l.add_xpath('description', '//­*[@itemprop="description"]'
　　　　　 '[1]/text()')
　　l.add_xpath('address', '//­*[@itemtype='
　　　　　 '"http://schema.org/Place"][1]/text()')
　　l.add_xpath('image_urls', '//­*[@itemprop="image"][1]/@src')
　　return l.load_item()
```

好多了，是不是？不过，这种写法并不只是在视觉上更加舒适，它还非常明确地声明了我们意图去做的事情，而不会将其与实现细节混淆起来。这就使得代码具有更好的可维护性以及自描述性。

`ItemLoader` 提供了许多有趣的结合数据及对数据进行格式化和清洗的方式。请注意，此类功能的开发非常活跃，因此请查阅Scrapy优秀的官方文档来发现使用它们的更高效的方式，文档地址为  `http://doc.scrapy.org/en/latest/topics/loaders.html` 。 `Itemloaders` 通过不同的处理类传递XPath/CSS表达式的值。处理器是一个快速而又简单的函数。处理器的一个例子是 `Join()` 。假设你已经使用类似 `//p`  的XPath表达式选取了很多个段落，该处理器可以将这些段落结合成一个条目。另一个非常有意思的处理器是 `MapCompose()` 。通过该处理器，你可以使用任意Python函数或Python函数链，以实现复杂的功能。比如， `MapCompose(float)` 可以将字符串数据转换为数值，而 `MapCompose(Unicode.strip, Unicode.title)` 可以删除多余的空白符，并将字符串格式化为每个单词均为首字母大写的样式。让我们看一些处理器的例子，如表3.4所示。

<center class="my_markdown"><b class="my_markdown">表3.4</b></center>

| 处　理　器 | 功　　能 |
| :-----  | :-----  | :-----  | :-----  |
| `Join()` | 把多个结果连接在一起 |
| `MapCompose(unicode.strip)` | 去除首尾的空白符 |
| `MapCompose(unicode.strip,` | `unicode. title)` | 与 `MapCompose(unicode.strip)` 相同，不过还会使结果按照标题格式 |
| `MapCompose(float)` | 将字符串转为数值 |
| `MapCompose(lambda i: i.replace` | `(',', ''), float)` | 将字符串转为数值，并忽略可能存在的','字符 |
| `MapCompose(lambda i: urlparse.` | `urljoin (response.url, i))` | 以 `response.url` 为基础，将URL相对路径转换为URL绝对路径 |

你可以使用任何Python表达式作为处理器。可以看到，我们可以很容易地将它们一个接一个地连接起来，比如，我们前面给出的去除首尾空白符以及标题化的例子。 `unicode.strip()` 和 `unicode.title()` 在某种意义上来说比较简单，它们只有一个参数，并且也只有一个返回结果。我们可以在 `MapCompose` 处理器中直接使用它们。而另一些函数，像 `replace()` 或 `urljoin()` ，就会稍微有点复杂，它们需要多个参数。对于这种情况，我们可以使用Python的“lambda表达式”。lambda表达式是一种简洁的函数。比如下面这个简洁的lambda表达式。

```python
myFunction = lambda i: i.replace(',', '')
```

可以代替：

```python
def myFunction(i):
　　return i.replace(',', '')
```

通过使用lambda，我们将类似 `replace()` 和 `urljoin()` 这样的函数包装在只有一个参数及一个返回结果的函数中。为了能够更好地理解表3.4中的处理器，下面看几个使用处理器的例子。使用 `scrapy shell` 打开任意URL，然后尝试如下操作。

```python
>>> from scrapy.loader.processors import MapCompose, Join
>>> Join()(['hi','John'])
u'hi John'
>>> MapCompose(unicode.strip)([u' I',u' am\n'])
[u'I', u'am']
>>> MapCompose(unicode.strip, unicode.title)([u'nIce cODe'])
[u'Nice Code']
>>> MapCompose(float)(['3.14'])
[3.14]
>>> MapCompose(lambda i: i.replace(',', ''), float)(['1,400.23'])
[1400.23]
>>> import urlparse
>>>　mc = MapCompose(lambda i: urlparse.urljoin('http://my.com/test/abc', 
i))
>>> mc(['example.html#check'])
['http://my.com/test/example.html#check']
>>> mc(['http://absolute/url#help'])
['http://absolute/url#help']

```

这里要解决的关键问题是，处理器只是一些简单小巧的功能，用来对我们的XPath/CSS结果进行后置处理。现在，在爬虫中使用几个这样的处理器，并按照我们想要的方式输出。

```python
def parse(self, response):
　　l.add_xpath('title', '//­*[@itemprop="name"][1]/text()',
　　　　　　　　MapCompose(unicode.strip, unicode.title))
　　l.add_xpath('price', './/­*[@itemprop="price"][1]/text()',
　　　　　　　　MapCompose(lambda i: i.replace(',', ''), float),
　　　　　　　　re='[,.0-9]+')
　　l.add_xpath('description', '//­*[@itemprop="description"]'
　　　　　　　　'[1]/text()', MapCompose(unicode.strip), Join())
　　l.add_xpath('address',
　　　　　　　　'//­*[@itemtype="http://schema.org/Place"][1]/text()',
　　　　　　　　MapCompose(unicode.strip))
　　l.add_xpath('image_urls', '//­*[@itemprop="image"][1]/@src',
　　　　　　　　MapCompose(
　　　　　　　　lambda i: urlparse.urljoin(response.url, i)))

```

完整列表将会在本章后续部分给出。当你使用我们目前开发的代码运行 `scrapy crawl basic` 时，可以得到更加整洁的输出值。

```python
'price': [334.39],
'title': [u'Set Unique Family Well']

```

最后，我们可以通过使用 `add_value()` 方法，添加Python计算得出的单个值（而不是XPath/CSS表达式）。我们可以用该方法设置“管理字段”，比如URL、爬虫名称、时间戳等。我们还可以直接使用管理字段表中总结出来的表达式，如下所示。

```python
l.add_value('url', response.url)
l.add_value('project', self.settings.get('BOT_NAME'))
l.add_value('spider', self.name)
l.add_value('server', socket.gethostname())
l.add_value('date', datetime.datetime.now())
```

为了能够使用其中的某些函数，请记得引入 `datetime` 和 `socket` 模块。

好了！我们现在已经得到了非常不错的 `Item` 。此刻，你的第一感觉可能是所做的这些都很复杂，你可能想要知道这些工作是不是值得付出努力。答案当然是值得的——这是因为，这就是你为了从页面抽取数据并将其存储到 `Item` 中几乎所有需要知道的东西。如果你从零开始编写，或者使用其他语言，该代码通常都会非常难看，而且很快就会变得不可维护。而使用Scrapy时，只需要仅仅25行代码。该代码十分简洁，用于表明意图，而不是实现细节。你清楚地知道每一行代码都在做什么，并且它可以很容易地修改、复用及维护。

你可能产生的另一个感觉是所有的处理器以及 `ItemLoader` 并不值得去努力。如果你是一个经验丰富的Python开发者，可能会觉得有些不舒服，因为你必须去学习新的类，来实现通常使用字符串操作、lambda表达式以及列表推导式就可以完成的操作。不过，这只是 `ItemLoader` 及其功能的简要概述。如果你更加深入地了解它，就不会再回头了。 `ItemLoader` 和处理器是基于编写并支持了成千上万个爬虫的人们的抓取需求而开发的工具包。如果你准备开发多个爬虫的话，就非常值得去学习使用它们。

