### 12.2.1　用requests.get()函数下载一个网页

`requests.get()` 函数接收一个要下载的URL字符串。通过在 `requests. get()` 的返回值上调用 `type()` ，你可以看到它返回一个 `Response` 对象，其中包含了Web服务器对你的请求做出的响应。稍后我将更详细地解释 `Response` 对象，现在请在交互式环境中输入以下代码，并保持计算机与因特网的连接：

```javascript
  >>> import requests
❶ >>> res = requests.get(automatetheboringstuff网址的/files/rj.txt') 
 >>> type(res) 
 <class 'requests.models.Response'>
❷ >>> res.status_code == requests.codes.ok
  True
 >>> len(res.text) 
  178981
 >>> print(res.text[:250]) 
  The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare
  This eBook is for the use of anyone anywhere at no cost and with
  almost no restrictions whatsoever.  You may copy it, give it away or
  re-use it under the terms of the Project
```

该URL指向一个文本页面，其中包含整部《罗密欧与朱丽叶》，它是由古登堡计划❶提供的。通过检查 `Response` 对象的 `status_code` 属性，你可以了解对这个网页的请求是否成功。如果该值等于 `requests.codes.ok` ，那么一切都好❷（顺便说一下，HTTP中“OK”的状态码是200。你可能已经熟悉404状态码，它表示“没找到”）。你可以在维基百科找到完整的HTTP状态码及其含义列表。

如果请求成功，下载的页面就作为一个字符串保存在 `Response` 对象的 `text` 变量中。这个变量保存了包含整部戏剧的一个大字符串，调用 `len(res.text)` 表明它的长度超过178 000个字符。最后，调用 `print(res.text[:250])` 显示前250个字符。

如果请求失败并显示错误信息，如“ `Failed to establish a new connection` ”或“ `Max retries exceeded` ”，那么请检查你的网络连接。连接到服务器可能相当复杂，在这里我不能给出一个完整的问题清单。你可以在网络上搜索引号中的错误信息，找到常见的错误原因。

