### 11.2　Scrapyd

现在，我们将要开始介绍Scrapyd。Scrapyd这个应用允许我们在服务器上部署爬虫，并使用它们制定爬取的计划任务。让我们来感受一下使用它是多么简单吧。我们在开发机中已经预安装了该应用，所以可以立即使用第3章中的代码对其进行测试。我们在之前使用了几乎完全相同的过程，在这里只有一个小的变化。

首先，我们访问 `http://localhost:6800/` ，来看一下Scrapyd的Web界面，如图11.1所示。

![63.png](../images/63.png)
<center class="my_markdown"><b class="my_markdown">图11.1　Scrapyd的Web界面</b></center>

可以看出，Scrapyd对于 **Jobs** 、 **Items** 、 **Logs** 和 **Documentation** 都有不同的区域。此外，它还提供了一些指引，告知我们如何使用其API定制计划任务。

为了完成该测试，我们必须先在Scrapyd服务器上部署爬虫。第一步是按照如下操作修改 `scrapy.cfg` 配置文件。

```python
$ pwd
/root/book/ch03/properties
$ cat scrapy.cfg
...
[settings]
default = properties.settings
[deploy]
url = http://localhost:6800/
project = properties

```

基本上，我们所有需要做的就是去除 **url** 一行的注释。默认的设置已经很合适了。现在，要想部署爬虫，需要使用 `scrapyd-client` 提供的 `scrapyd-deploy` 工具。 `scrapyd-client` 曾经是Scrapy的一部分，不过现在已经独立为一个单独的模块，该模块可以使用 `pip install scrapyd-client` 安装（已经在开发机中安装好了该模块）。

```python
$ scrapyd-deploy
Packing version 1450044699
Deploying to project "properties" in http://localhost:6800/addversion.
json
Server response (200):
{"status": "ok", "project": "properties", "version": "1450044699", 
"spiders": 3, "node_name": "dev"}

```

当部署成功后，可以在Scrapyd的Web界面主页的 **Available projects** 区域看到该项目。现在，可以按照提示在该页面提交一个任务。

```python
$ curl http://localhost:6800/schedule.json -d project=properties -d 
spider=easy
{"status": "ok", "jobid": " d4df...", "node_name": "dev"}

```

如果回到Web界面的 **Jobs** 区域，可以看到任务正在运行。稍后可以使用 `schedule.json` 返回的 `jobid` ，通过 `cancel.json` 取消该任务。

```python
$ curl http://localhost:6800/cancel.json -d project=properties -d
job=d4df...
{"status": "ok", "prevstate": "running", "node_name": "dev"}

```

请一定记住执行取消操作，否则你会浪费一段时间的计算机资源。

非常好！当访问 **Logs** 区域时，可以看到日志；而当访问 **Items** 区域时，可以看到刚才爬取的 `Item` 。这些都会在一定周期之后清空以释放空间，因此在几次爬取操作后这些内容可能就不再可用。

如果有合理的理由，比如冲突，那么我们可以使用 `http_port` 修改端口，这是Scrapyd提供的诸多设置之一。通过访问 `http://scrapyd. readthedocs.org/` 来了解Scrapyd的文档是非常值得的。在本章中，我们需要修改的一个重要设置是 `max_proc` 。如果将该设置保留为默认值0的话，Scrapyd将在Scrapy任务运行时允许4倍于CPU数量的并发。由于我们将运行多个Scrapyd服务器，并且大部分可能是在虚拟机当中的，因此我们将会设置该值为4，即允许至多4个任务并发运行。这与本章的需求有关，而在实际部署当中，一般情况下使用默认值就能够良好运行。

