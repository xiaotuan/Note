### 3.2.1　URL

一切始于URL。你需要从准备抓取的网站中选择几个示例URL。我将使用Gumtree分类广告网站（ `
<a class="my_markdown" href="['https://www.gumtree.com']">https://www.gumtree.com</a>
` ）作为示例进行演示。

比如，通过访问Gumtree上的伦敦房产主页（链接为 `
<a class="my_markdown" href="['http://www.gumtree.com/flats-houses/london']">http://www.gumtree.com/flats-houses/london</a>
` ），你能够找到一些房产的示例URL。可以通过右键单击分类列表，选择Copy Link Address（复制链接地址）或你浏览器中同样的功能，来复制这些链接。比如，其中一个可能类似于 `
<a class="my_markdown" href="['https://www.gumtree.com/p/studios-bedsits-rent/split-level']">https://www.gumtree.com/p/studios-bedsits-rent/split-level</a>
` 。虽然可以在真实网站中使用这些URL来操作，但不幸的是，经过一段时间后，真实的Gumtree网站可能会发生变化，造成XPath表达式无法正常工作。此外，除非设置一个用户代理头，否则Gumtree不会回应你的请求。稍后我们会对此进行更进一步的讲解，不过就现在而言，如果想加载它们的某个页面，可以在scrapy shell中使用如下命令。

```python
scrapy shell -s USER_AGENT="Mozilla/5.0" <your url here e.g. http://www.
gumtree.com/p/studios-bedsits-rent/...>

```

如果想要在使用scrapy shell时调试问题，可以使用 `--pdb` 参数启用交互式调试，以避免发生异常。例如：

```python
scrapy shell --pdb https://gumtree.com
```

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> scrapy shell是一个非常有用的工具，能够帮助我们使用Scrapy开发。

很显然，我们并不鼓励你在学习本书内容时访问Gumtree的网站，我们也不希望本书的示例在不久之后就无法使用。此外，我们还希望即使无法连接互联网，你仍然能够开发和使用我们的示例。这就是为什么你的Vagrant开发环境中包含一个提供了类似于Gumtree网站页面的Web服务器的原因。虽然它们可能不如真实网站那么漂亮，但是从爬虫角度来说，它们其实是一样的。即便如此，我们在本章中的所有截图还是来自真实的Gumtree网站。在你Vagrant的dev机器中，可以通过 `http://web:9312/` 访问该Web服务器，而在你的浏览器中，可以通过 `http://localhost:9312/` 来访问。

在scrapy shell中打开服务器中的一个网页，并且在dev机器上输入如下内容进行操作。

```python
$ scrapy shell http://web:9312/properties/property_000000.html
...
[s] Available Scrapy objects:
[s]　 crawler　　<scrapy.crawler.Crawler object at 0x2d4fb10>
[s]　 item　　　 {}
[s]　 request　　<GET http:// web:9312/.../property_000000.html>
[s]　 response　 <200 http://web:9312/.../property_000000.html>
[s]　 settings　 <scrapy.settings.Settings object at 0x2d4fa90>
[s]　 spider　　 <DefaultSpider 'default' at 0x3ea0bd0>
[s] Useful shortcuts:
[s]　 shelp()　　　　　　Shell help (print this help)
[s]　 fetch(req_or_url) Fetch request (or URL) and update local...
[s]　 view(response)　　View response in a browser
>>>

```

我们得到了一些输出，现在可以在Python提示符下，用它来调试刚才加载的页面（一般情况下，可以使用Ctrl + D退出）。

