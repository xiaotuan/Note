### 7.2.4　HTTP缓存和离线运行

Scrapy的 `HttpCacheMiddleware` 组件（默认未激活）为HTTP请求和响应提供了一个低级的缓存。当启用该组件时，缓存会存储每个请求及其对应的响应。通过将 `HTTPCACHE_POLICY` 设置为 `scrapy.contrib.httpcache.RFC2616Policy` ，可以启用一个遵从 `RFC2616` 的更复杂的缓存策略。为了启用该缓存，还需要将 `HTTPCACHE_ENABLED` 设置为 `True` ，并将 `HTTPCACHE_DIR` 设置为文件系统中的一个目录（使用相对路径将会在项目的数据文件夹下创建一个目录）。

还可以选择通过设置存储后端类 `HTTPCACHE_STORAGE` 为 `scrapy.contrib.httpcache.DbmCacheStorage` ，为缓存文件指定数据库后端，并且还可以选择调整HTTPCACHE_DBM_MODULE设置（默认为任意数据库管理系统）。还有一些设置可以用于缓存行为调优，不过默认值已经能够为你很好地服务了。

#### 示例2——使用缓存的离线运行

假设你运行了如下代码：

```python
$ scrapy crawl fast -s LOG_LEVEL=INFO -s CLOSESPIDER_ITEMCOUNT=5000

```

你会发现大约一分钟后运行可以完成。如果此时无法访问Web服务器，可能就无法爬取任何数据。假设你现在使用如下代码，再次运行爬虫。

```python
$ scrapy crawl fast -s LOG_LEVEL=INFO -s CLOSESPIDER_ITEMCOUNT=5000 -s 
HTTPCACHE_ENABLED=1
...
INFO: Enabled downloader middlewares:...*HttpCacheMiddleware*

```

你会注意到此时启用了 `HttpCacheMiddleware` ，当查看当前目录下的隐藏目录时，将会发现一个新的 `.scrapy` 目录，目录结构如下所示。

```python
$ tree .scrapy | head
.scrapy
└── httpcache
　　　└── easy
　　　　　　├── 00
　　　　　　│　　├── 002054968919f13763a7292c1907caf06d5a4810
　　　　　　│　　│　　├── meta
　　　　　　│　　│　　├── pickled_meta
　　　　　　│　　│　　├── request_body
　　　　　　│　　│　　├── request_headers
　　　　　　│　　│　　├── response_body
...

```

现在，如果重新运行爬虫，获取略少于前面数量的item时，就会发现即使在无法访问Web服务器的情况下，也能完成得更加迅速。

```python
$ scrapy crawl fast -s LOG_LEVEL=INFO -s CLOSESPIDER_ITEMCOUNT=4500 -s 
HTTPCACHE_ENABLED=1

```

我们使用了略少于前面数量的item作为限制，是因为当使用 `CLOSESPIDER_ITEMCOUNT` 结束时，一般会在爬虫完全结束前读取更多的页面，但我们不希望命中的页面不在缓存范围内。要想清理缓存，只需删除缓存目录即可。

```python
$ rm -rf .scrapy

```

