如果用过 Python 2.x 里的 `urllib2` 库，可能会发现 urllib2 与 urllib 有些不同。在 Python 3.x 里，urllib2 改名为 urllib，被分成一些子模块：`urllib.request`、`urllib.parse` 和 `urllib.error`。尽管函数名称大多和原来一样，但是在用新的 urllib 库时需要注意哪些函数被移动到子模块里了。

`urllib` 是 Python 的标准库，可以通过 <https://docs.python.org/3/library/urllib.html> 阅读该库的 Python 文档。