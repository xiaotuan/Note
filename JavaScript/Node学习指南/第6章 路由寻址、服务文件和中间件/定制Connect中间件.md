Connect 中间件函数签名如下：

```js
function name(req, res, next)
```

三个参数分别是 HTTP request、HTTP response 和回调函数 next。

下面是 serve-favicon 中间件的实现代码： 

```js
function favicon (path, options) {
  var opts = options || {}

  var icon // favicon cache
  var maxAge = calcMaxAge(opts.maxAge)

  if (!path) {
    throw new TypeError('path to favicon.ico is required')
  }

  if (Buffer.isBuffer(path)) {
    icon = createIcon(Buffer.from(path), maxAge)
  } else if (typeof path === 'string') {
    path = resolveSync(path)
  } else {
    throw new TypeError('path to favicon.ico must be string or buffer')
  }

  return function favicon (req, res, next) {
    if (getPathname(req) !== '/favicon.ico') {
      next()
      return
    }

    if (req.method !== 'GET' && req.method !== 'HEAD') {
      res.statusCode = req.method === 'OPTIONS' ? 200 : 405
      res.setHeader('Allow', 'GET, HEAD, OPTIONS')
      res.setHeader('Content-Length', '0')
      res.end()
      return
    }

    if (icon) {
      send(req, res, icon)
      return
    }

    fs.readFile(path, function (err, buf) {
      if (err) return next(err)
      icon = createIcon(buf, maxAge)
      send(req, res, icon)
    })
  }
}
```

**示例6-9 创建一个定制的错误处理中间件模块**

```js
var fs = require('fs')

module.exports = function customHandler(path, missingmsg, directorymsg) {
  if (arguments.length < 3) throw new Error('missing parameter in customHandler')
  return function customHandler (req, res, next) {
    var pathname = path + req.url
    console.log(pathname)
    fs.stat(pathname, function (err, stats) {
      if (err) {
        res.writeHead(404)
        res.write(missingmsg)
        res.end()
      } else if (!stats.isFile()) {
        res.writeHead(403)
        res.write(directorymsg)
        res.end()
      } else {
        next()
      }
    })
  }
}
```

测试程序：

```js
var connect = require('connect')
var http = require('http')
var fs = require('fs')
var custom = require('./CustomErrorHandler')
var favicon = require('serve-favicon')
var logger = require('morgan')
var staticServe = require('serve-static')

http.createServer(connect()
    .use(favicon('./public_html/favicon.ico'))
    .use(logger('dev'))
    .use(custom('./public_html', '404 File Not Found', '403 Directory Access Forbidden'))
    .use(staticServe('./public_html'))
).listen(8124)
```