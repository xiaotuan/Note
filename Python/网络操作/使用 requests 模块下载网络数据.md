使用 requests 模块下载网络数据方法如下：

```python
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# req.text
# # 将数据写入文件
if req.status_code == 200:
    with open('btc_close.json', 'wb') as f:
        f.write(bytes(req.text, encoding='utf8'))

    print(req.json())
```

