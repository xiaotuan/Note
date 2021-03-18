[toc]

### 5.3.1　PyQt还是PySide

Qt框架有两种可以使用的Python库，分别是 `PyQt` 和 `PySide` 。 `PyQt` 最初于1998年发布，但在用于商业项目时需要购买许可。由于该原因，开发Qt的公司（原先是诺基亚，现在是Digia）后来在2009年开发了另一个Python库 `PySide` ，并且使用了更加宽松的LGPL许可。

虽然这两个库有少许区别，但是本章中的例子在两个库中都能够正常工作。下面的代码片段用于导入已安装的任何一种Qt库。

```python
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtWebKit import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtWebKit import *
```

在这段代码中，如果 `PySide` 不可用，则会抛出 `ImportError` 异常，然后导入 `PyQt` 模块。如果 `PyQt` 模块也不可用，则会抛出另一个 `ImportError` 异常，然后退出脚本。

> <img class="my_markdown" src="../images/42.jpg" style="zoom:50%;" />
> 下载和安装这两种Qt库Python版本的说明可以分别参考网上的相应介绍。对于你正在使用的Python 3的版本，可能存在没有对应库的情况，不过其发布很频繁，因此你可以经常回来查看一下。

#### 1．使用Qt进行调试

无论你使用的是PySide还是PyQt，可能都会遇到需要调试应用或脚本的网站。我们已经介绍了一种方式可以实现该目的，就是通过使用 `QWebView` 这个GUI的 `show()` 方法来“查看”你加载的页面上渲染了什么。你也可以使用 `page().mainFrame().toHtml()` 链（在任何时刻使用 `BrowserRender` 类通过 `html` 方法拉取HTML时均可以很容易地引用），将其写入文件中保存下来，然后在浏览器中打开。

此外，还有一些有用的Python调试器，比如 `pdb` ，你可以将它集成到脚本中，然后使用断点单步执行可能存在错误、问题或bug的代码。针对不同库和你安装的Qt版本的不同，有一些不同的设置方式，因此我们建议搜索你的确切设置，并复查实现，以允许设置断点或跟踪。

