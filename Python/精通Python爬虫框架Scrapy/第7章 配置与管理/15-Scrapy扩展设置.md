### 7.3.2　Scrapy扩展设置

这些设置能够让你扩展并修改Scrapy的几乎所有方面。这些设置中最重要的当属 `ITEM_PIPELINES` 。它可以让你在项目中使用Item处理管道。第9章会看到更多的例子。除了管道之外，还可以通过不同的方式扩展Scrapy，其中一些将会在第8章中进行总结。 `COMMANDS_MODULE` 允许我们添加常用命令。比如，可以在 `properties/hi.py` 文件中添加如下内容。

```python
from scrapy.commands import ScrapyCommand
class Command(ScrapyCommand):
　　default_settings = {'LOG_ENABLED': False}
　　def run(self, args, opts):
　　　　print("hello")
```

当在 `settings.py` 文件中添加 `COMMANDS_MODULE='properties.hi'` 时，就激活了这个小命令，我们可以在Scrapy帮助中看到它，并且通过 `scrapy hi` 运行。在命令的 `default_settings` 中定义的设置，会被合并到项目的设置当中，并覆盖默认值，不过其优先级低于 `settings.py` 文件或命令行中设定的设置。

Scrapy使用 `-_BASE` 字典（比如 `FEED_EXPORTERS_BASE` ）存储不同框架扩展的默认值，并允许我们在 `settings.py` 文件或命令行中，通过设置它们的非 `-_BASE` 版本（比如 `FEED_EXPORTERS` ）进行自定义。

最后，Scrapy使用 `DOWNLOADER` 、 `SCHEDULER` 等设置，保存系统基本组件的包 `/` 类名。我们可以继承默认的下载器（ `scrapy.core.downloader.Downloader` ），重载一些方法，然后将 `DOWNLOADER` 设置为自定义的类。这样可以让开发者大胆地对新特性进行实验，并且可以简化自动化测试过程，不过除非你明确了解自己做的事情，否则不要轻易修改这些设置。

