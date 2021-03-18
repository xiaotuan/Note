[toc]

### 3.4.7　探索requests-cache

有时，你可能希望缓存内部使用了 `requests` 库，或者你可能不希望管理缓存类来自己处理。如果是这样的情况，则可以使用 `requests-cache` 这个不错的库，它实现了一些不同的后端选项，用于为 `requests` 库创建缓存。当使用 `requests-cache` 时，通过 `requests` 库访问URL的所有 `get` 请求都会先检查缓存，只有没在缓存中找到的页面才会请求。

`requests-cache` 支持多种后端，包括Redis、MongoDB（一种NoSQL数据库）、SQLite（一种轻量级的关系型数据库）以及内存（非永久保存，因此不推荐）。由于我们已经安装了Redis，因此我们将使用它作为我们的后端。我们先从安装这个库开始。

```python
pip install requests-cache
```

现在，我们可以在IPython中，使用一些简单的命令安装并测试我们的缓存了。

```python
In [1]: import requests_cache
In [2]: import requests
In [3]: requests_cache.install_cache(backend='redis')
In [4]: requests_cache.clear()
In [5]: url = 'http://example.python-scraping.com/view/United-Kingdom-239'
In [6]: resp = requests.get(url)
In [7]: resp.from_cache
Out[7]: False
In [8]: resp = requests.get(url)
In [9]: resp.from_cache
Out[9]: True
```

如果我们使用它来代替我们自己的缓存类的话，只需使用 `install_cache` 命令实例化缓存，然后每个请求（只要我们使用了 `requests` 库）就都会保存在Redis后端中了。我们同样也可以使用一个简单的命令设置过期时间。

```python
from datetime import timedelta
requests_cache.install_cache(backend='redis',
expire_after=timedelta(days=30))
```

为了对比 `requests-cache` 与我们自己的实现的速度，我们需要构建新的下载器和链接爬虫。该下载器同样实现了之前推荐的 `requests` 钩子，以允许限速，其文档位于 `requests-cache` 的用户手册中，地址为 `https://requests-cache.readthedocs.io/en/latest/user_guide.html` 。

要想查看完整代码，可以访问新下载器的代码地址以及新的链接爬虫的地址，它们位于本书源码的 `chp3` 文件夹中，其名分别为 `downloader_requests_ cache.py` 和 `requests_cache_link_crawler.py` 。我们可以使用IPython测试它们，以对比性能。

```python
In [1]: from chp3.requests_cache_link_crawler import link_crawler
...
In [3]: %time link_crawler('http://example.python-scraping.com/',
'/(index|view)')
Returning from cache: http://example.python-scraping.com/
Returning from cache: http://example.python-scraping.com/index/1
Returning from cache: http://example.python-scraping.com/index/2
...
Returning from cache:http://example.python-scraping.com/view/Afghanistan-1
CPU times: user 116 ms, sys: 12 ms, total: 128 ms
Wall time: 359 ms
```

可以看到， `requests-cache` 解决方案的性能略低于我们自己的Redis方案，不过它的代码行数更少，速度依然很快（远超过磁盘缓存方案）。尤其是当你使用可能在内部使用 `requests` 管理的其他库时， `requests-cache` 的实现是一个非常不错的工具。

