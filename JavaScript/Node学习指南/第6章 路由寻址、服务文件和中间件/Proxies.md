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
var connect = require('connect'),
    http = require('http'),
    fs = require('fs'),
    path = require('path'),
    crossroads = require('crossroads'),
    httpProxy = require('http-proxy'),
    base = 'E:\\Workspace\\JavaScriptSpace\\LearningNodejs\\public'

var proxy = httpProxy.createProxyServer();

// 创建代理，监听请求
http.createServer(function (req, res) {
    if (req.url.match(/^\/node\//)) {
        proxy.web(req, res, {
            target: 'http://127.0.0.1:8000'
          });
    } else {
        proxy.web(req, res, {
            target: 'http://127.0.0.1:8124'
          });
    }
}).listen(9000)

// 对动态资源的请求添加路由
crossroads.addRoute('/node/{id}/', function (id) {
    console.log('accessed node ' + id)
})

// 动态文件服务器
http.createServer(function (req, res) {
    crossroads.parse(req.url)
    res.end('that\'s all!')
}).listen(8000)

// 静态文件服务器
var serveFavicon = require('serve-favicon')
var morgan = require('morgan')
var serveStatic = require('serve-static')
http.createServer(connect()
    .use(serveFavicon(path.join(__dirname, 'public', 'favicon.ico')))
    .use(morgan('dev'))
    .use(serveStatic(base))
).listen(8124)

console.log("__dirname: " + path.join(__dirname, 'public', 'favicon.ico'))
```

测试目录结构：

test.js
[favicon.ico](https://www.baidu.com/favicon.ico)
example1.html

测试文件：

**example1.html**
```
<!DOCTYPE html>
<html lang="en">
    <header>
        <meta charset="utf-8" />
        <title>Example1</title>
    </header>
    <body>
        <span>这是示例1.</span>
    </body>
</html>
```

在浏览器中输入下面网址进行测试：

http://localhost:9000/node/34
http://localhost:9000/example1.html

