```js
var http = require("http")

function process_request(req, res) {
  var body = 'Thanks for calling!\n'
  var content_length = body.length
  res.writeHead(200, {
    'Content-Length': content_length,
    'Content-Type': 'text/plain'
  })
  res.end(body)
}

var s = http.createServer(process_request)
s.listen(8080)
```

要运行这个文件，需要输入：

```shell
$ node web.js
```

可以使用 `curl` 来测试它：

```shell
$ curl -i localhost:8080
```

前面将 `-i`  参数传给 `curl` 命令，会将请求内容和响应的头信息一起打印出来。

也可以在浏览器中打开：<http://localhost:8080>

也可以使用 `wget` 进行测试：

```shell
$ wget http://localhost:8080
```

