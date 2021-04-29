[toc]

### 1.5.6　使用requests库

尽管我们只使用 `urllib` 就已经实现了一个相对高级的解析器，不过目前Python编写的主流爬虫一般都会使用 `requests` 库来管理复杂的HTTP请求。该项目起初只是以“人类可读”的方式协助封装 `urllib` 功能的小库，不过现如今已经发展成为拥有数百名贡献者的庞大项目。可用的一些功能包括内置的编码处理、对SSL和安全的重要更新以及对POST请求、JSON、cookie和代理的简单处理。

> <img src="../images/11.jpg" style="zoom:50%;" />
> 本书在大部分情况下，都将使用 `requests` 库，因为它足够简单并且易于使用，而且它事实上也是大多数网络爬虫项目的标准。

想要安装 `requests` ，只需使用 `pip` 即可。

```python
pip install requests
```

如果你想了解其所有功能的进一步介绍，可以阅读它的文档，地址为 `http://python-requests.org` ，此外也可以浏览其源代码，地址为 `https://github.com/kennethreitz/requests` 。

为了对比使用这两种库的区别，我还创建了一个使用 `requests` 的高级链接爬虫。你可以在从异步社区中下载的源码文件中找到并查看该代码，其文件名为 `advanced_link_crawler_using_requests.py` 。在主要的 `download` 函数中，展示了其关键区别。 `requests` 版本如下所示。

```python
def download(url, user_agent='wswp', num_retries=2, proxies=None):
    print('Downloading:', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error:', e.reason)
        html = None
```

一个值得注意的区别是， `status_code` 的使用更加方便，因为每个请求中都包含该属性。另外，我们不再需要测试字符编码了，因为 `Response` 对象的 `text` 属性已经为我们自动化实现了该功能。对于无法处理的URL或超时等罕见情况，都可以使用 `RequestException` 进行处理，只需一句简单的捕获异常的语句即可。代理处理也已经被考虑进来了，我们只需传递代理的字典即可（即 `{'http': 'http://myproxy.net:1234', 'https': 'https://myproxy.net:1234'}` ）。

我们将继续对比和使用这两个库，以便根据你的需求和用例来熟悉它们。无论你是在处理更复杂的网站，还是需要处理重要的人类化方法（如cookie或session）时，我都强烈推荐使用 `requests` 。我们将会在第6章中讨论更多有关这些方法的话题。

