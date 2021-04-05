### 第2步：下载JSON数据

OpenWeather官网提供了JSON格式的实时天气信息。首先，你必须在网站上注册一个免费的API密钥。（这个密钥是用来限制你在他们的服务器上提出请求的频率，以降低他们的带宽费用。）你的程序只需要下载页面http://api o `****`  data/2.5/forecast/daily?q=<Location>&cnt= 3&APPID=<API key>，其中<Location>是想知道天气的城市，<API key>是你的个人API密钥。将以下代码添加到getOpenWeather.py中：

```javascript
#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
--snip--
# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.op **** data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location,
APPID)
response = requests.get(url) 
response.raise_for_status()
# Uncomment to see the raw JSON text:
#print(response.text)
# TODO: Load JSON data into a Python variable.
```

我们从命令行参数中得到了 `location` 。为了生成要访问的网址，我们利用 `%s` 占位符，将 `location` 保存的字符串插入URL字符串的那个位置。结果保存在 `url` 中，然后将 `url` 传入 `requests.get()` 。 `requests.get()` 调用返回一个 `Response` 对象，它可以通过调用 `raise_for_status()` 来检查错误。如果不发生异常，下载的文本将保存在 `response.text` 中。

