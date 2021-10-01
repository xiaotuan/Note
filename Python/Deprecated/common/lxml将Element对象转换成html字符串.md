方法如下：

```python
from lxml.html import fromstring, tostring
from lxml import etree

origin_html = """<p class="zw">如果你想了解Selenium是否支持你系统中的浏览器，<code>kdfjlsdfljsdf sdk sdkfjs</code>以
及你可能需要安装的其他依赖或驱动，请查阅Selenium文档中关于支持平台的介绍。</p>"""

element = fromstring(origin_html)

# 将 Element 转换成 html 字符串
html = etree.tostring(element, pretty_print=True, encoding='utf-8').decode('utf-8')
print(html)
```

