下面的示例脚本使用 `Python 2.x` 的 `urllib2` 模块下载 `URL`：

```python
import urllib2

def download(url):
	return urllib2.urlopen(url).read()

content = download('https://www.baidu.com')
print content
```

当下载网页时，我们可能会遇到一些无法控制的错误，比如请求的页面可能不存在。此时，`urllib2` 会抛出异常，然后退出脚本。下面再给出一个更健壮的版本，可以捕获这些异常：

```python
import urllib2

def download(url):
	print 'Downloading:', url
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
	return html

content = download('https://www.baidu.com')
print content
```

下载时遇到的错误经常是临时性的，比如服务器过载时返回的 `503 Service Unavailable` 错误。对于此类错误，我们可以尝试重新下载，因为这个服务器问题现在可能已解决。下面是支持重试下载功能的新版本代码：

```python
import urllib2

def download(url, num_retries=2):
	print 'Downloading:', url
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				#recursively retry 5xx HTTP error
				return download(url, num_retries - 1)
	return html

content = download('http://httpstat.us/500')
print content
```

运行结果如下：

```shell
$ python download.py 
Downloading: http://httpstat.us/500
Download error: Internal Server Error
Downloading: http://httpstat.us/500
Download error: Internal Server Error
Downloading: http://httpstat.us/500
Download error: Internal Server Error
None
```

