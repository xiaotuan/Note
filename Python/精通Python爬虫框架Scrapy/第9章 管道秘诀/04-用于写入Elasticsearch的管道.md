### 9.1.2　用于写入Elasticsearch的管道

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 在本章，我们将在properties集合中插入房产信息。你可能需要重置properties集合，此时可以使用 `curl` 执行DELETE请求：

首先，我们要编写一个将 `Item` 存储到 **ES** （ **Elasticsearch** ）服务器的爬虫。你可能会觉得从ES开始，甚至先于MySQL，作为持久化机制进行讲解有些不太寻常，不过其实它是我们可以做的最简单的事情。ES可以是无模式的，也就是说无需任何配置就能够使用它。对于我们这个（非常简单的）用例来说， `treq` 也已经足够使用。如果想要使用更高级的ES功能，则需要考虑使用 `txes2` 或其他Python/Twisted ES包。

在我们的开发机中，已经包含正在运行的ES服务器了。下面登录到开发机中，验证其是否正在正常运行。

```python
$ curl -XDELETE http://es:9200/properties

```

```python
$ curl http://es:9200
{
　"name" : "Living Brain",
　"cluster_name" : "elasticsearch",
　"version" : { ... },
　"tagline" : "You Know, for Search"
}

```

在宿主机浏览器中，访问 `http://localhost:9200` ，也可以看到同样的结果。当访问 `http://localhost:9200/properties/property/_search` 时，可以看到返回的响应表示ES进行了全局性的尝试，但是没有找到任何与房产信息相关的索引。恭喜你，刚刚已经使用了ES的REST API。

本章中管道实现的完整代码包含很多额外的细节，如更多的错误处理等，不过我将通过凸显关键点的方式，保持这里的代码简洁。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 本章在 `ch09` 目录当中，其中本示例的代码为 `ch09/properties/properties/pipelines/es.py` 。

从本质上说，爬虫代码只包含如下4行。

```python
@defer.inlineCallbacks
def process_item(self, item, spider):
　　data = json.dumps(dict(item), ensure_ascii=False).encode("utf-
8")
　　yield treq.post(self.es_url, data)
```

其中，前两行用于定义标准的 `process_item()` 方法，可以在其中 `yield` 延迟操作（参考第8章）。

第 3 行用于准备要插入的 `data` 。首先，我们将 `Item` 转化为字典。然后使用 `json.dumps()` 将其编码为JSON格式。 `ensure_ascii=False` 的目的是通过不转义非ASCII字符，使得输出更加紧凑。然后，将这些JSON字符串编码为UTF-8，即JSON标准中的默认编码。

最后一行使用 `treq` 的 `post()` 方法执行POST请求，将文档插入到ElasticSearch中。 `es_url` 存储在 `settings.py` 文件当中（ `ES_PIPELINE_URL` 设置），如 `http:// es:9200/properties/property` ，可以提供一些基本信息，如ES服务器的IP和端口（ `es:9200` ）、集合名称（ `properties` ）以及想要写入的对象类型（ `property` ）。

要想启用该管道，需要将其添加到 `settings.py` 文件的 `ITEM_PIPELINES` 设置当中，并且使用 `ES_PIPELINE_URL` 设置进行初始化。

```python
ITEM_PIPELINES = {
　　'properties.pipelines.tidyup.TidyUp': 100,
　　'properties.pipelines.es.EsWriter': 800,
}
ES_PIPELINE_URL = 'http://es:9200/properties/property'
```

完成上述工作后，我们可以进入到适当的目录当中。

```python
$ pwd
/root/book/ch09/properties
$ ls
properties scrapy.cfg

```

然后，开始运行爬虫。

```python
$ scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=90
...
INFO: Enabled item pipelines: EsWriter...
INFO: Closing spider (closespider_itemcount)...
　 'item_scraped_count': 106,

```

如果现在再次访问 `http://localhost:9200/properties/property/_search` ，可以在响应的 `hits/total` 字段中看到已经插入的条目数量，以及前10条结果。我们还可以通过添加 `?size=100` 参数取得更多结果。在搜索URL中添加 `q=` 参数时，可以在全部或特定字段中搜索指定关键词。最相关的结果将会出现在最前面。例如， `http://localhost: 9200/properties/property/_search?q=title: london` ，将会返回标题中包含"London"的房产信息。对于更加复杂的查询，可以查阅 ES 的官方文档，网址为： `
<a class="my_markdown" href="['https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html']">https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html</a>
` 。

ES不需要配置的原因是它可以根据我们提供的第一个属性自动检测模式（字段类型）。通过访问 `http://localhost:9200/properties/` ，可以看到其自动检测的映射关系。

让我们快速查看一下性能，使用上一章结尾处给出的方式重新运行 `scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=1000` 。平均延时从0.78秒增长到0.81秒，这是因为管道的平均时间从0.12秒增长到了0.15秒。吞吐量仍然保持在每秒大约25个Item。

> <img class="my_markdown" src="../images/14.png" style="width:251px;  height: 203px; " width="10%"/>
> 使用管道将Item插入到数据库当中是不是一个好主意呢？答案是否定的。通常情况下，数据库提供的批量插入条目的方式可以有几个数量级的效率提升，因此我们应当使用这种方式。也就是说，应当将Item打包批量插入，或在爬虫结束时以后置处理的步骤执行插入。我们将在最后一章中看到这些方法。不过，许多人仍然使用Item管道插入数据库，此时使用Twisted API而不是通用/阻塞的方法实现该方案才是正确的方式。

