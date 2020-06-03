用 npm 安装 http-proxy：

```console
npm install http-proxy
```

http-proxy 最简单用法：

```js
var http = require('http'),
    httpProxy = require('http-proxy')

httpProxy.createProxyServer({target: 'http://localhost:8124' }).listen(8000)

http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.write('request successfully proxied!' + '\n' + JSON.stringify(req.headers, true, 2))
    res.end()
}).listen(8124)
```

也可以在命令行使用 http-proxy（无法在 bin 目录中找到该命令，可能需要全局安装 http-proxy 才有）：

```console
./node-http-proxy --port 8000 --target localhost:8124
```

**示例6-12 使用 Connect、Crossroads 和 http-proxy 处理动态和静态的请求**

```js

```