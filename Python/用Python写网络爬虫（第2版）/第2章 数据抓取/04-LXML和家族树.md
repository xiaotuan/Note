作为示例，让我们来查看示例页面中 `table` 元素的所有子元素。

```python
import re
import requests
from lxml.html import fromstring, tostring

def download(url, user_agent='wswp', num_retries=2, proxies=None):
    print('Downloading: ', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error: ', e.reason)
        html = None
    return html

url = 'http://example.python-scraping.com/places/default/view/Albania-3'
html = download(url)
tree = fromstring(html)
table = tree.xpath('//table')[0]
children = table.getchildren()
print(children)
```

输出结果如下所示：

```console
[<Element tr at 0x1104d28f0>, 
 <Element tr at 0x1104d2a10>, 
 <Element tr at 0x1104d2b30>, 
 <Element tr at 0x1104d2b90>, 
 ...
]
```

我们还可以查看表格的兄弟元素和父元素。

```python
import re
import requests
from lxml.html import fromstring, tostring

def download(url, user_agent='wswp', num_retries=2, proxies=None):
    print('Downloading: ', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error: ', e.reason)
        html = None
    return html

url = 'http://example.python-scraping.com/places/default/view/Albania-3'
html = download(url)
tree = fromstring(html)
# area = tree.xpath('//tr[@id="places_area__row"]/td[@class="w2p_fw"]/text()')[0]
# print(area)

table = tree.xpath('//table')[0]
previous = table.getprevious()
print(previous)
next_sibling = table.getnext()
print(next_sibling)
parent = table.getparent()
print(parent)
```

输出结果如下所示：

```console
None
<Element div at 0x10e9778f0>
<Element form at 0x10e977a10>
```

