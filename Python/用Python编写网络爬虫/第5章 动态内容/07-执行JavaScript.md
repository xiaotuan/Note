[toc]

### 5.3.2　执行JavaScript

为了确认你安装的WebKit能够执行JavaScript，我们可以使用位于 `http://example.python-scraping.com/dynamic` 上的这个简单示例。

该网页只是使用JavaScript在 `div` 元素中写入了 `Hello World` 。下面是其源代码。

```python
<html>
    <body>
        <div id="result"></div>
        <script>
        document.getElementById("result").innerText = 'Hello World';
        </script>
    </body>
</html>
```

使用传统方法下载原始HTML并解析结果时，得到的 `div` 元素为空值，如下所示。

```python
>>> import lxml.html
>>> from chp3.downloader import Downloader
>>> D = Downloader()
>>> url = 'http://example.python-scraping.com/dynamic'
>>> html = D(url)
>>> tree = lxml.html.fromstring(html)
>>> tree.cssselect('#result')[0].text_content()
''
```

下面是使用WebKit的初始版本代码，当然还需事先导入上一节中提到的 `PyQt` 或 `PySide` 模块。

```python
>>> app = QApplication([])
>>> webview = QWebView()
>>> loop = QEventLoop()
>>> webview.loadFinished.connect(loop.quit)
>>> webview.load(QUrl(url))
>>> loop.exec_()
>>> html = webview.page().mainFrame().toHtml()
>>> tree = lxml.html.fromstring(html)
>>> tree.cssselect('#result')[0].text_content()
'Hello World'
```

因为这里有很多新知识，所以下面我们会逐行分析这段代码。

+ 第一行初始化了 `QApplication` 对象，在其他Qt对象可以初始化之前，需要先有Qt框架。
+ 接下来，创建 `QWebView` 对象，该对象是Web文档的构件。
+ 创建 `QEventLoop` 对象，该对象用于创建本地事件循环。
+ `QWebView` 对象的 `loadFinished` 回调链接了 `QEventLoop` 的 `quit` 方法，从而可以在网页加载完成之后停止事件循环。然后，再将要加载的URL传给 `QWebView` 。
+ `PyQt` 需要将该URL字符串封装到 `QUrl` 对象当中，而对于 `PySide` 来说则是可选项。
+ 由于 `QWebView` 是异步加载的，因此执行过程会在网页加载时立即传入下一行。但我们又希望等待网页加载完成，因此需要在事件循环启动时调用 `loop.exec_()` 。
+ 网页加载完成后，事件循环退出，代码执行继续，对加载得到网页所产生的HTML使用 `toHTML` 方法执行抽取。
+ 从最后一行可以看出，我们成功执行了该JavaScript， `div` 元素抽取出了 `Hello World` 。

这里使用的类和方法在C++的Qt框架网站中都有详细的文档，读者可自行参考。虽然 `PyQt` 和 `PySide` 都有其自身的文档，但是原始C++版本的描述和格式更加详尽，一般的Python开发者可以用它替代。

