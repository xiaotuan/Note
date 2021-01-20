[toc]

`urllib3` 是一个功能强大，条理清晰，用于 HTTP 客户端的`Python` 库。许多 `Python` 的原生系统已经开始使用 `urllib3`。`urllib3` 提供了很多 `Python` 标准库 `urllib ` 里所没有的重要特性：

1. 线程安全
2. 连接池
3. 客户端 SSL/TLS 验证
4. 文件分部编码上传
5. 协助处理重复请求和 HTTP 重定位
6. 支持压缩编码
7. 支持 HTTP 和 SOCKS 代理

### 一、get请求

`urllib3` 主要使用连接池进行网络请求的访问，所以访问之前我们需要创建一个连接池对象，如下所示：

```python
import urllib3 
url = "http://httpbin.org"
http = urllib3.PoolManager();
r = http.request('GET',url + "/get")
print(r.data.decode())
print(r.status) 

#带参数的get
r = http.request('get', 'http://www.baidu.com/s', fields={'wd':'周杰伦'})
print(r.data.decode())
```

经查看源码：

```python
def request(self, method, url, fields=None, headers=None, **urlopen_kw):
```

- 第一个参数 method 必选，指定是什么请求，'get'、'GET'、'POST'、'post'、'PUT'、'DELETE'等，不区分大小写。
- 第二个参数 url，必选
- 第三个参数 fields，请求的参数，可选
- 第四个参数 headers 可选

request 请求的返回值是 `<urllib3.response.HTTPResponse object at 0x000001B3879440B8>`

我们可以通过 dir() 查看其所有的属性和方法。

dir(r)

直截取了一部分

```
#'data', 'decode_content', 'enforce_content_length', 'fileno', 'flush', 'from_httplib',
# 'get_redirect_location', 'getheader', 'getheaders', 'headers', 'info', 'isatty',
# 'length_remaining', 'read', 'read_chunked', 'readable', 'readinto', 'readline',
# 'readlines', 'reason', 'release_conn', 'retries', 'seek', 'seekable', 'status',
# 'stream', 'strict', 'supports_chunked_reads', 'tell', 'truncate', 'version', 'writable',
# 'writelines']
```

### 二、post请求

```python
import urllib3
url = "http://httpbin.org"
fields = {
  'name':'xfy'
}
http = urllib3.PoolManager()
r = http.request('post',url+"/post",fields=fields)
print(r.data.decode())
```

可以看到很简单，只是第一个参数 get 换成了 post。

并且参数不需要再像 urllib 一样转换成 byte 型了。

### 三、设置headers

```python
import urllib3
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
http = urllib3.PoolManager();
r = http.request('get',url+"/get",headers = headers)
print(r.data.decode())
```

### 四、设置代理

```python
import urllib3
url = "http://httpbin.org"
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
proxy = urllib3.ProxyManager('http://101.236.19.165:8866',headers = headers)
r = proxy.request('get',url+"/ip")
print(r.data.decode())
```

### 五、当请求的参数为json

在发起请求时,可以通过定义body 参数并定义headers的Content-Type参数来发送一个已经过编译的JSON数据

```python
import urllib3
url = "http://httpbin.org"
import json
data = {'name':'徐繁韵'}

json_data = json.dumps(data)

http = urllib3.PoolManager()
r = http.request('post',url+"/post",body = json_data,headers = {'Content-Type':'application/json'})
print(r.data.decode('unicode_escape'))
```

### 六、上传文件

```python
#元组形式
with open('a.html','rb') as f:
  data = f.read()
http = urllib3.PoolManager()
r = http.request('post','http://httpbin.org/post',fields = {'filefield':('a.html',data,'text/plain')})
print(r.data.decode())

#二进制形式

r = http.request('post','http://httpbin.org/post',body = data,headers={'Content-Type':'image/jpeg'})
print(r.data.decode())
```

### 七、超时设置

```python
# 1全局设置超时
# http = urllib3.PoolManager(timeout = 3)
# 2在request里设置
# http.request('post','http://httpbin.org/post',timeout = 3)
```

### 八、重试和重定向

```python
import urllib3
http = urllib3.PoolManager()
#重试
r = http.request('post','http://httpbin.org/post',retries = 5) #请求重试测次数为5次 ，默认为3ci
print(r.retries) #Retry(total=5, connect=None, read=None, redirect=0, status=None)
#关闭重试
http.request('post','http://httpbin.org/post',retries = False) #请求重试测次数为5次 ，默认为3ci

r = http.request('get','http://httpbin.org/redirect/1',redirect = False)
print(r.retries)# Retry(total=3, connect=None, read=None, redirect=None, status=None)
print(r.status)
print(r.data.decode())
print("--------------------")
print(r.get_redirect_location())
#302不是异常
```

### 九、urllib3 本身设置了https的处理，但是有警告

虽然可以请求，但是报如下警告：

> InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
>   InsecureRequestWarning)

禁用警告：

```python
import urllib3
urllib3.disable_warnings() #禁用各种警告
url = "https://www.12306.cn/mormhweb/"
http = urllib3.PoolManager()
r = http.request('get',url)
print(r.data.decode())
```

`urllib3` 很强大，但是并没有 `requests` 好用。

