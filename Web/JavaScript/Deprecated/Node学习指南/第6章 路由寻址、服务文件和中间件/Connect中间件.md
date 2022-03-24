**serve-static**

可以使用 `serve-static` 创建一个简单的静态文件服务器。

```js
var http = require('http')
var connect = require('connect')
var serveStatic = require('serve-static')
var logger = require('morgan')
var path = require('path')

http.createServer(connect()
    .use(logger('dev'))
    .use(serveStatic(path.join(__dirname, 'public_html')))
).listen(8124)
```

`serve-static` 将根目录作为第一个参数，第二个参数可选，第二个参数可以有以下选项：

+ immutable 
在Cache-Control响应标头中启用或禁用不可变指令，默认为false。 如果设置为true，则还应指定maxAge选项以启用缓存。 不可变指令将阻止受支持的客户端在maxAge选项有效期内提出条件请求，以检查文件是否已更改。
+ index
默认情况下，此模块将发送“ index.html”文件以响应目录请求。 要禁用此设置false或提供新的索引，请按首选顺序传递字符串或数组。
+ lastModified
启用或禁用Last-Modified标头，默认为true。 使用文件系统的最后修改值。
+ maxAge
提供HTTP缓存的最大时间（以毫秒为单位），默认为0。这也可以是ms模块接受的字符串。
+ redirect
当路径名是目录时，重定向到结尾的“ /”。 默认为true。
+ setHeaders
用于在响应时设置自定义标头的函数。 标头的更改需要同步进行。 该函数称为fn（res，path，stat），其中参数为：
    + res： 响应对象
    + path：正在发送的文件路径
    + stat： 正在发送的文件的stat对象

> 具体使用方法请查阅：<https://www.npmjs.com/package/serve-static> 

**morgan (logger)**

`morgan` 中间件模块记录对流的请求，默认输出到 stdout。你可以修改流和其他一些选项，包括缓冲时间、样式，还有 `immediate` 标识，决定立即写入 log 或者在响应时写入。

> 具体使用方法请查阅：<https://www.npmjs.com/package/morgan>

**示例6-5 将 log 写入文件并改变样式**

```js
var http = require('http')
var fs = require('fs')
var connect = require('connect')
var logger = require('morgan')
var staticServe = require('serve-static')
var path = require('path')

var writeStream = fs.createWriteStream('./log.txt', {
  'flags': 'a',
  'encoding': 'utf8',
  'mode': 0666
})

http.createServer(connect()
    .use(logger({format: 'dev', stream: writeStream}))
    .use(staticServe(path.join(__dirname, 'public_html')))
).listen(8124)
```

**cookie-parser 和 cookie-session**

`cookie-parser` 中间件允许我们访问服务器上的 cookie 数据，它解析 cookie 头部，用 cookie/data 得到 req.cookies 。

**示例6-6 访问 HTTP request cookie，用于 console 信息**

```js
var connect = require('connect')
var http = require('http')
var logger = require('morgan')
var cookieParser = require('cookie-parser')
var staticServe = require('serve-static')

var app = connect()
    .use(logger('dev'))
    .use(cookieParser())
    .use(function (req, res, next) {
      console.log('tracking ' + req.cookies.username)
      next()
    })
    .use(staticServe('./public_html'))

http.createServer(app).listen(8124)
console.log('Server listening on port 8124')
```

**示例6-7 使用 session cookie 来跟踪资源访问**

```js
var http = require('http')
var connect = require('connect')
var cookieSession = require('cookie-session')
var logger = require('morgan')
var cookieParser = require('cookie-parser')
var staticServe = require('serve-static')

// 清除 session 数据
function clearSession(req, res, next) {
  if ('/clear' == req.url) {
    req.session = null
    res.statusCode = 302
    res.setHeader('Location', '/')
    res.end()
  } else {
    next()
  }
}

// 跟踪用户
function trackUser(req, res, next) {
  res.session.ct = req.session.ct || 0
  req.session.username = req.session.username || req.cookies.username
  console.log(req.cookies.username + ' requested ' + req.session.ct++ + ' resoureces this session')
  next()
}

// cookie 和 session
var app = connect()
    .use(logger('dev'))
    .use(cookieParser('mumble'))
    .use(cookieSession({
      name: 'session',
      keys: ['tracking']
    }))
    .use(clearSession)
    .use(trackUser)

// 静态服务器
app.use(staticServe('./public_html'))
// 启动服务器开始监听
http.createServer(app).listen(8124)
console.log('Server listening on port 8124')

```