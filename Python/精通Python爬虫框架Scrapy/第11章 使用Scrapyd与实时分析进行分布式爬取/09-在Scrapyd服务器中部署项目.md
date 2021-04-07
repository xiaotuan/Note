### 11.4.4　在Scrapyd服务器中部署项目

为了能够在我们的3台Scrapyd服务器中部署爬虫，我们需要将这3台服务器添加到 `scrapy.cfg` 文件中。该文件中的每个 `[deploy:target-name]` 区域都定义了一个新的部署目标。

```python
$ pwd
/root/book/ch11/properties
$ cat scrapy.cfg
...
[deploy:scrapyd1]
url = http://scrapyd1:6800/
[deploy:scrapyd2]
url = http://scrapyd2:6800/
[deploy:scrapyd3]
url = http://scrapyd3:6800/

```

可以通过 `scrapyd-deploy -l` 查询当前可用的目标。

```python
$ scrapyd-deploy -l
scrapyd1　　　　　　 http://scrapyd1:6800/
scrapyd2　　　　　　 http://scrapyd2:6800/
scrapyd3　　　　　　 http://scrapyd3:6800/

```

通过 `scrapyd-deploy <target-name>` ，可以很容易地部署任意服务器。

```python
$ scrapyd-deploy scrapyd1
Packing version 1449991257
Deploying to project "properties" in http://scrapyd1:6800/addversion.json
Server response (200):
{"status": "ok", "project": "properties", "version": "1449991257", 
"spiders": 2, "node_name": "scrapyd1"}

```

该过程会留给我们一些额外的目录和文件（ `build` 、 `project.egg-info` 、 `setup.py` ），我们可以安全地删除它们。本质上， `scrapyd-deplo``y` 所做的事情就是打包你的项目，并使用 `addversion.jso` n上传到目标Scrapyd服务器当中。

之后，当我们使用 `scrapyd-deploy -L` 查询单台服务器时，可以确认项目是否已经被成功部署，如下所示。

```python
$ scrapyd-deploy -L scrapyd1
properties

```

我还在项目目录中使用 `touch` 创建了3个空文件（ `scrapyd1-3` ）。使用 `scrapyd*` 扩展为文件名称，同样也是目标服务器的名称。之后，你可以使用一个bash循环部署所有服务器： `for i in scrapyd*; do scrapyd-deploy $i; done` 。

