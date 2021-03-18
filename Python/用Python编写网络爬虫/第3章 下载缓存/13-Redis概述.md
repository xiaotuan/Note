[toc]

### 3.4.3　Redis概述

下面给出了如何将示例网站数据存入Redis，而后加载它的例子。

```python
In [5]: url = 'http://example.python-scraping.com/view/United-Kingdom-239'
In [6]: html = '...'
In [7]: results = {'html': html, 'code': 200}
In [8]: r.set(url, results)
Out[8]: True
In [9]: r.get(url)
Out[9]: b"{'html': '...', 'code': 200}"
```

从 `get` 输出中可以看到，我们从Redis存储中接收到的是 `bytes` 类型，即使我们插入的是字典或字符串。我们可以通过使用 `json` 模块，按照对于 `DiskCache` 类相同的方式管理这些序列化数据。

如果我们需要更新URL的内容，会发生什么呢？

```python
In [10]: r.set(url, {'html': 'new html!', 'code': 200})
Out[10]: True
In [11]: r.get(url)
Out[11]: b"{'html': 'new html!', 'code': 200}"
```

从上面的输出中可以看到，Redis的 `set` 命令只是简单地覆盖了之前的值，这对于类似网络爬虫这样的简单存储来说非常合适。对于我们的需求而言，我们只需要每个URL有一个内容集合即可，因此它能够很好地映射为键值对存储。

让我们来看一下存储里有什么，并且清除不需要的数据。

```python
In [12]: r.keys()
Out[12]: [b'test',
b'http://example.python-scraping.com/view/United-Kingdom-239']
In [13]: r.delete('test')
Out[13]: 1
In [14]: r.keys()
Out[14]: [b'http://example.python-scraping.com/view/United-Kingdom-239']
```

`keys` 方法返回了所有可用键的列表，而 `delete` 方法可以让我们传递一个（或多个）键并从存储中删除它们。我们还可以删除所有的键，如下所示。

```python
In [15]: r.flushdb()
Out[15]: True
In [16]: r.keys()
Out[16]: []
```

Redis还有很多命令和工具，请阅读文档以进一步了解。现在，我们已经具备了使用Redis作为后端，为我们的网络爬虫创建缓存所需了解的所有内容了。

> <img class="my_markdown" src="../images/30.jpg" style="zoom:50%;" />
> Python的Redis客户端提供了良好的文档，以及多个在Python中使用Redis的用例（比如PubSub管道或作为大型连接池）。Redis的官方文档中有一个包含了教程、书籍、参考以及用例的长列表，因此如果你想要了解如何扩展、安装以及部署Redis的话，我推荐你从这里开始。如果你在云或服务器上使用Redis的话，不要忘记对你的Redis实例实施安全措施！

