### 12.5　用bs4模块解析HTML

`Beautiful Soup` 是一个模块，用于从HTML页面中提取信息（用于这个目的时，它比正则表达式好很多）。 `Beautiful Soup` 模块的名称是 `bs4` （表示Beautiful Soup第4版）。要安装它，需要在命令行中运行 `pip install beautifulsoup4` （关于安装第三方模块的指导，请查看附录 A）。虽然安装时使用的名字是 `beautifulsoup4` ，但要导入它，就使用 `import bs4` 。

在本章中， `Beautiful Soup` 的例子将解析（即分析并识别其中的一些部分）硬盘上的一个HTML文件。在IDLE中打开一个新的文件编辑器窗口，输入以下代码，并保存为example.html，或者从异步社区本书对应页面下载它：

```javascript
<!-- This is the example.html example file. -->
<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="https:// 
inv">my website</a>.</p>
<p class="slogan">Learn Python the easy way! </p>
<p>By <span  id="author">Al  Sweigart</span></p>
</body></html>
```

你可以看到，即使是一个简单的HTML文件，也包含许多不同的标签和属性。对于复杂的网站，事情很快就变得令人困惑。好在， `Beautiful Soup` 让处理HTML变得容易很多。

