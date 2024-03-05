默认情况下，`urllib2` 使用 `Python-urllib/2.7` 作为用户代理下载网页内容，其中 `2.7` 是 `Python` 的版本号。一些网站会封禁这个默认的用户代理。下面是一个设定用户代理的示例代码：

```python
import urllib2

def download(url, user_agent='wswp', num_retries=2):
	print 'Downloading:', url
	headers = { 'User-agent': user_agent }
	request = urllib2.Request(url, headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				#recursively retry 5xx HTTP error
				return download(url, num_retries - 1)
	return html

content = download('https://www.bookabc.cc/abc/94/94102/')
print content
```

