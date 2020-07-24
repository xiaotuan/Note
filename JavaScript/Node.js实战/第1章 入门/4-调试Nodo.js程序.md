```js
var http = require("http")

function process_request(req, res) {
  var body = 'Thanks for calling!\n'
  var content_length = body.lenggth
  res.writeHead(200, {
    'Content-Length': content_length,
    'Content-Type': 'text/plain'
  })
  res.end(body)
}

var s = http.createServer(process_request)
s.listen(8080)
```

再次运行该程序：

```shell
$ node debugging.js
```

当尝试连接到 <http://localhost:8080> 的时候，可能会得到：

```shell
$ curl -i localhost:8080
curl: (56) Recv failure: Connection was reset
```

`Node.js` 内置了一个调试器。如果想使用，只需要在启动的时候将 inspect参数添加到程序名称的前面即可：

```shell
node inspect debugging.js
```

