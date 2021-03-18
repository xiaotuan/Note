[toc]

### 3.4.2　安装Redis

我们可以按照Redis官网说明，通过编译最新源码的方式安装Redis。如果你使用的是Windows，则需要使用MSOpenTech的项目安装Redis，或是简单地通过虚拟机（使用Vagrant）或Docker实例的方式进行安装。然后，需要使用如下命令单独安装Python客户端。

```python
pip install redis
```

如果想要测试安装是否正常，可以在本地启动Redis（或者在你的虚拟机或容器中），命令如下。

```python
$ redis-server
```

你将看到一些文本，包括版本号以及Redis标志等。在文本最后，你将看到类似如下的消息。

```python
1212:M 18 Feb 20:24:44.590 * The server is now ready to accept connections
on port 6379
```

一般情况下，你的Redis服务器将使用相同的端口，即默认端口（6379）。为了测试Python客户端并连接Redis，我们可以使用Python解释器（在下面的代码中，我使用了IPython），如下所示。

```python
In [1]: import redis
In [2]: r = redis.StrictRedis(host='localhost', port=6379, db=0)
In [3]: r.set('test', 'answer')
Out[3]: True
In [4]: r.get('test')
Out[4]: b'answer'
```

在前面的代码中，我们简单地连接了我们的Redis服务器，然后使用 `set` 命令设置了一个键为 `'test'` 、值为 `'answer'` 的记录。我们可以使用 `get` 命令很容易地取得该记录。

> <img class="my_markdown" src="../images/29.jpg" style="zoom:50%;" />
> 如果想要查看更多关于如何设置Redis作为后台进程运行的选项，我建议使用官方的Redis快速入门，或是使用你喜欢的搜索引擎搜索针对特定操作系统或安装的具体说明。

