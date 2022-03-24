安装 Connect：

```console
npm install connect
```

**示例6-3 在基于 Connect 的程序中集成 morgan(logger) 和 serve-favicon(favicon) 中间件**

```js
var connect = require('connect')
var logger = require('morgan')
var favicon = require('serve-favicon')
var http = require('http')
var path = require('path')

var app = connect()
    .use(favicon(path.join('./public_html', 'favicon.ico')))
    .use(logger('dev'))
    .use(function (req, res) {
      res.end('Hello World\n')
    })

http.createServer(app).listen(8124)
```

**示例6-4 直接在程序中加入 Connect 内建的中间件**

```js
var http = require('http')
var path = require('path')
var connect = require('connect')
var logger = require('morgan')
var favicon = require('serve-favicon')

http.createServer(connect()
    .use(favicon(path.join('./public_html', 'favicon.ico')))
    .use(logger('dev'))
    .use(function (req, res) {
      res.end('Hello World\n')
    })
).listen(8124)
```

