[toc]

### 1.4.1　检查robots.txt

大多数网站都会定义 `robots.txt` 文件，这样可以让爬虫了解爬取该网站时存在哪些限制。这些限制虽然是仅仅作为建议给出，但是良好的网络公民都应当遵守这些限制。在爬取之前，检查 `robots.txt` 文件这一宝贵资源可以将爬虫被封禁的可能性降至最低，而且还能发现和网站结构相关的线索。关于 `robots.txt` 协议的更多信息可以参见 `http://www.robotstxt.org` 。下面的代码是我们的示例文件 `robots.txt` 中的内容，可以访问 `http://example.python-scraping.com/robots.txt` 获取。

```python
# section 1
User-agent: BadCrawler
Disallow: /
# section 2
User-agent: *
Crawl-delay: 5
Disallow: /trap
# section 3
Sitemap: http://example.python-scraping.com/sitemap.xml
```

在section 1中， `robots.txt` 文件禁止用户代理为BadCrawler的爬虫爬取该网站，不过这种写法可能无法起到应有的作用，因为恶意爬虫根本不会遵从 `robots.txt` 的要求。本章后面的一个例子将会展示如何让爬虫自动遵守 `robots.txt` 的要求。

section 2规定，无论使用哪种用户代理，都应该在两次下载请求之间给出5秒的抓取延迟，我们需要遵从该建议以避免服务器过载。这里还有一个 `/trap` 链接，用于封禁那些爬取了不允许访问的链接的恶意爬虫。如果你访问了这个链接，服务器就会封禁你的IP一分钟！一个真实的网站可能会对你的IP封禁更长时间，甚至是永久封禁。不过如果这样设置的话，我们就无法继续这个例子了。

section 3定义了一个 `Sitemap` 文件，我们将在下一节中了解如何检查该文件。

