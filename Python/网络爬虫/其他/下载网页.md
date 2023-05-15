可以使用如下代码下载网页：

```py
from urllib.request import urlopen

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())
except HTTPError as e:
    print(e)
```

执行下面命令运行该程序：

```shell
$ python scrapetest.py
```

> 注意：如果设备上安装了 `Python 2.x`，可能需要直接指明版本才能运行：
>
> ```shell
> $ python3 scrapetest.py
> ```

