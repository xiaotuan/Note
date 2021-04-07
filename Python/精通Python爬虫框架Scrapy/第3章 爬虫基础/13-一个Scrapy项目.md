### 3.3　一个Scrapy项目

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 提醒一下，你可以从GitHub中获得本书的全部源代码。要下载该代码，可以使用如下命令：
> 本章的代码在 `ch03` 目录中，其中该示例的代码在 `ch03/properties` 目录中。

到目前为止，我们只是在通过scrapy shell“小打小闹”。现在，既然已经拥有了用于开始第一个Scrapy项目的所有必要组成部分，那么让我们按下Ctrl + D 退出scrapy shell吧。需要注意的是，你现在输入的所有内容都将丢失。显然，我们并不希望在每次爬取某些东西的时候都要输入代码，因此一定要谨记scrapy shell只是一个可以帮助我们调试页面、XPath表达式和Scrapy对象的工具。不要花费大量时间在这里编写复杂代码，因为一旦你退出，这些代码就都会丢失。为了编写真实的Scrapy代码，我们将使用项目。下面创建一个Scrapy项目，并将其命名为" `properties` "，因为我们正在抓取的数据是房产。

```python
$ scrapy startproject properties
$ cd properties
$ tree
.
├── properties
│　　├── __init__.py
│　　├── items.py
│　　├── pipelines.py
│　　├── settings.py
│　　└── spiders
│　　　　　└── __init__.py
└── scrapy.cfg
2 directories, 6 files

```

```python
git clone https://github.com/scalingexcellence/
scrapybook

```

我们可以看到这个Scrapy项目的目录结构。命令 `scrapy startproject properties` 创建了一个以项目名命名的目录，其中包含3个我们感兴趣的文件，分别是 `items.py` 、 `pipelines.py` 和 `settings.py` 。这里还有一个名为 `spiders` 的子目录，目前为止该目录是空的。在本章中，我们将主要在 `items.py` 文件和 `spiders` 目录中工作。在后续的章节里，还将对设置、管道和 `scrapy.cfg` 文件有更多探索。

