[toc]

### 8.1　安装Scrapy

我们可以使用 `pip` 命令安装Scrapy，如下所示。

```python
pip install scrapy
```

由于Scrapy依赖一些外部库，因此如果在安装过程中遇到困难的话，可以从其官方网站上获取到更多信息，网址为 `http://doc.scrapy.org/en/latest/intro/install.html` 。

如果Scrapy安装成功，就可以在终端里执行 `scrapy` 命令了。

```python
$ scrapy
 Scrapy 1.3.3 - no active project
Usage:
 scrapy <command> [options] [args]
Available commands:
 bench Run quick benchmark test
 commands
 fetch Fetch a URL using the Scrapy downloader
...
```

本章中我们将会使用如下几个命令。

+ `startproject` ：创建一个新项目。
+ `genspider` ：根据模板生成一个新爬虫。
+ `crawl` ：执行爬虫。
+ `shell` ：启动交互式抓取控制台。

> <img class="my_markdown" src="../images/61.jpg" style="zoom:50%;" />
> 要了解上述命令或其他命令的详细信息，可以参考 `http://doc.scrapy. org/en/latest/topics/commands.html` 。

