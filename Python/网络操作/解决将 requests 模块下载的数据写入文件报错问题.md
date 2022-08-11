[toc]

### 1. 问题代码

```python
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# req.text
# # 将数据写入文件
with open('btc_close.json', 'wb') as f:
    f.write(req.text)

# # 加载 json 格式
print(req.json())
```

### 2. 运行环境

操作系统：Windows 10

Python 版本：3.10.5

### 3. 报错信息

```shell
Traceback (most recent call last):
  File "C:\Users\Xiaotuan\Desktop\test.py", line 9, in <module>
    f.write(req.text)
TypeError: a bytes-like object is required, not 'str'
```

### 4. 解决方法

这是由于下载数据的字符编码不对造成的，可以使用下面方法将其转换成 utf8 字符编码：

```python
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# req.text
# # 将数据写入文件
with open('btc_close.json', 'wb') as f:
    f.write(bytes(req.text, encoding='utf8'))

# # 加载 json 格式
print(req.json())
```

