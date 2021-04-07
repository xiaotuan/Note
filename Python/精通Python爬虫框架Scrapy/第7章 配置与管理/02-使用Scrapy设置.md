### 7.1　使用Scrapy设置

在Scrapy中，可以按照5个递增的优先级修改设置。我们将会依次看到这 5 个等级。第一级是默认设置，通常不需要修改它，不过 `scrapy/settings/default_settings.py` （在系统的Scrapy源代码或Scrapy的GitHub中可以找到）中的代码确实值得一读。默认设置在命令级别中得以优化。实际上，除非想要实现自定义命令，否则无需考虑它。通常情况下，我们只会在命令级别下一级的项目 `<project_name>/settings.py` 文件中修改设置。这些设置只应用于当前项目。该级别最为方便，因为当我们将项目部署到云服务时， `settings.py` 文件将会打包在其中，并且由于它是一个文件，因此可以使用自己喜欢的文本编辑器轻松调整几十个设置。接下来一级是每个爬虫的设置。通过在爬虫定义中使用 `custom_settings` 属性，可以轻松地为每个爬虫自定义设置。比如，可以通过该设置为一个指定的爬虫启用或禁用Item管道。最后，对于一些临时修改，可以使用命令行参数 `-s` ，在命令行中传输设置。我们在前面已经使用过几次，比如 `-s CLOSESPIDR_PAGECOUNT=3` ，即用于启用爬虫关闭扩展，以便爬虫尽早关闭。在该级别中，我们可能会去设置API secrets、密码等。不要将这些信息写入 `settings.py` 文件中，因为你不会希望它们意外出现在某些公开代码库当中。

在本节中，我们将会研究一些非常重要的常用设置。为了感受不同类型，可以在任意项目中尝试如下命令。

```python
$ scrapy settings --get CONCURRENT_REQUESTS
16

```

你得到的是其默认值。然后，修改项目中的 `<project_name>/settings.py` 文件，为 `CONCURRENT_REQUESTS` 设置一个值，比如14。此时，前面的 `scrapy settings` 命令将会给出你刚刚设置的那个值，之后不要忘记恢复该值。接下来，尝试从命令行中显式设置该参数，将会得到如下结果。

```python
$ scrapy settings --get CONCURRENT_REQUESTS -s CONCURRENT_REQUESTS=19
19

```

前面的输出提示了一个很有意思的事情。 `scrapy cwarl` 和 `scrapy settings` 都只是命令。每个命令都能使用刚才描述的加载设置的方法，其示例如下所示。

```python
$ scrapy shell -s CONCURRENT_REQUESTS=19
>>> settings.getint('CONCURRENT_REQUESTS')
19

```

当需要找出项目中某个设置的有效值时，可以使用前面给出的任意一种方法。现在，我们需要更加仔细地了解Scrapy的设置。

