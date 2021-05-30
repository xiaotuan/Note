很容易在模板文件中添加样式。在 `Jade` 模板文件中， 我们给 `header.jade` 文件添加样式：

```jade
head
  title #{title}
  meta(charset="utf-8")
  link(type="text/css"
       rel="stylesheet"
       href="/stylesheets/style.css"
       media="all")
```

安装 `Stylus` ：

```console
$ npm install stylus
```

> 提示：更多关于 `Stylus`：<https://stylus-lang.com/docs/js.html>

`Stylus` 样式模板扩展名为 `.styl`。源目录设置为 `views/stylus`，但是样式模板期望的路径是在 public 目录下有一个名为 stylesheets 的子目录。当生成静态样式文件时，会被放在目标目录下的 stylesheets 目录中。

例如，设置网页的背景色为黄色，字体颜色为红色，Stylus 模板如下：

```styl
body
  background-color yellow
  color red
```

如果几个元素需要共享某些样式，将它们列在同一行以逗号分隔，这与 CSS 一致：

```styl
p, tr
  background-color yellow
  color red
```

或者可以用统一缩进写在不同行：

```styl
p
tr
  background-color yellow
  color red
```

如果你需要使用悬停伪类，比如 :hover，:visited，语法如下：

```styl
textarea
input
  background-color #fff
  &:hover
    background-color cyan
```

与符号（&）表示父选择器。

> 注意：在运行应用程序后，stylus 不会马上生成 CSS 文件，而是在使用到该 CSS 文件时才会生成，比如某个网页使用到该 CSS 文件，并且用户正在打开该网页，则 stylus 会马上生成该 CSS 文件。

**示例8-14 在 widget 程序中加入 CSS 模板支持**

```js
var http = require('http')
var express = require('express')
var logger = require('morgan')
var favicon = require('serve-favicon')
var staticServe = require('serve-static')
var bodyParser = require('body-parser')
var methodOverride = require('method-override')
var path = require('path')
var stylus = require('stylus')
var indexRouter = require('./routes/index')

var app = express()

app.set('views', __dirname + '/views')
app.set('view engine', 'jade')

app.use(favicon(__dirname + '/public/images/favicon.ico'))
app.use(logger('dev'))
app.use(stylus.middleware({
  src: path.join(__dirname, 'views/stylus'),
  dest: path.join(__dirname, 'public/stylesheets')
}))
// app.use(stylus.middleware(path.join(__dirname, 'views/stylus')))
app.use(staticServe(__dirname + '/public'))
app.use(bodyParser.urlencoded({extended: false}))
app.use(methodOverride(function (req, res) {
  if (req.body && typeof req.body === 'object' && '_method' in req.body) {
    // look in urlencoded POST bodies and delete it
    var method = req.body._method
    delete req.body._method
    return method
  }
}))

app.get('/', indexRouter)

app.use(function (req, res, next) {
  throw new Error(req.url + ' not fount')
})

app.use(function (err, req, res, next) {
  console.log(err)
  res.send(err.message)
})

http.createServer(app).listen(8124)

console.log('Express server listening on port 8124')
```

**示例8-15 widget 程序的 Stylus 模板**

```styl
body
  margin 50px
table
  width 90%
  border-collapse collapse
table, td, th, caption
  border 1px solid black
td 
  padding 20px
caption
  font-size larger
  background-color yellow
  padding 10px
h1
  font 1.5em Georgia, serif
ul
  list-style-type none
form
  margin 20px
  padding 20px
```