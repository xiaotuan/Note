### 3.3.1　声明item

我们使用一个文件编辑器打开 `items.py` 文件。现在该文件中已经包含了一些模板代码，不过还需要针对用例对其进行修改。我们将重定义 `PropertiesItem` 类，添加表3.2中总结出来的字段。

我们还会添加几个字段，我们的应用在后续会用到这些字段（这样之后就不需要再修改这个文件了）。本书后续的内容会深入解释它们。需要重点注意的一个事情是，我们声明一个字段并不意味着我们将在每个爬虫中都填充该字段，或是全部使用它。你可以随意添加任何你感觉合适的字段，因为你可以在之后更正它们。

<center class="my_markdown"><b class="my_markdown">表3.2</b></center>

| 可计算字段 | Python表达式 |
| :-----  | :-----  | :-----  | :-----  |
| `images` | 图像管道将会基于 `image_urls` 自动填充该字段。可以在后续的章节中了解更多相关内容 |
| `location` | 我们的地理编码管道将会在后面填充该字段。可以在后续的章节中了解更多相关的内容 |

我们还会添加一些管理字段（见表3.3）。这些字段不是特定于某个应用程序的，而是我个人感兴趣的字段，可能会在未来帮助我调试爬虫。你可以在项目中选择其中的一些字段，当然也可以不选择。如果你仔细观察这些字段，就会明白它们可以让我清楚何地（server、url）、何时（date）、如何（spider）执行的抓取。它们还可以自动完成一些任务，比如使item失效、规划新的抓取迭代或是删除来自有问题的爬虫的item。如果你还不能理解所有的表达式，尤其是server的表达式，也不用担心。当我们进入到后面的章节时，这些都会变得越来越清楚。

<center class="my_markdown"><b class="my_markdown">表3.3</b></center>

| 管理字段 | Python表达式 |
| :-----  | :-----  | :-----  | :-----  |
| `url` | `response.url` | 示例值： `'http://web.../property_000000. html'` |
| `project` | `self.settings.get('BOT_NAME')` | 示例值： `'properties'` |
| `spider` | `self.name` | 示例值： `'basic'` |
| `server` | `socket.gethostname()` | 示例值： `'scrapyserver1'` |
| `date` | `datetime.datetime.now()` | 示例值： `datetime.datetime(2015, 6, 25...)` |

给出字段列表之后，再去修改并自定义 `scrapy startproject` 为我们创建的 `PropertiesItem` 类，就会变得很容易。在文本编辑器中，修改 `properties/items.py` 文件，使其包含如下内容：

```python
from scrapy.item import Item, Field
class PropertiesItem(Item):
　　# Primary fields
　　title = Field()
　　price = Field()
　　description = Field()
　　address = Field()
　　image_urls = Field()
　　# Calculated fields
　　images = Field()
　　location = Field()
　　# Housekeeping fields
　　url = Field()
　　project = Field()
　　spider = Field()
　　server = Field()
　　date = Field()
```

由于这实际上是我们在文件中编写的第一个Python代码，因此需要重点指出的是，Python使用缩进作为其语法的一部分。在每个字段的起始部分，会有精确的4个空格或1个制表符，这一点非常重要。如果你在其中一行使用了4个空格，而在另一行使用了3个空格，就会出现语法错误。如果你在其中一行使用了4个空格，而在另一行使用了制表符，同样也会产生语法错误。这些空格在 `PropertiesItem` 类下，将字段声明组织到了一起。其他语言一般使用大括号（{}）或特殊的关键词（如 `begin-end` ）来组织代码，而Python使用空格。

