安装 EJS：

```console
$ npm install ejs
```

**从模板文件生成 HTML (test.ejs)**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title><%= title %></title>
    </head>
    <body>
        <% if (names.length) { %>
            <ul>
                <% names.forEach(function (name) { %>
                    <li><%= name%></li>
                <% }) %>
            </ul>
        <% } %>
    </body>
</html>
```

**示例8-1 根据数据和 EJS 模板生成 HTML**

```js
var http = require('http')
var ejs = require('ejs')

// 创建 HTTP 服务器
http.createServer(function (req, res) {
    res.writeHead(200, {'content-type': 'text/html'})

    // 加载数据
    var names = ['Joe', 'Mary', 'Sue', 'Mark']
    var title = 'Testing EJS'

    // 生成或者处理错误信息
    ejs.renderFile(__dirname + '/views/test.ejs', {title: 'testing', names: names}, function (err, result) {
        if (!err) {
            res.end(result)
        } else {
            res.end('An error occurred accessing page')
            console.log(err)
        }
    })
}).listen(8124)

console.log('Server running on 8124/')
```

目录结构：

```
|_views
    |_test.ejs
|_app.js
```

另一种渲染 EJS 的方法是 render，接收 EJS 模板作为字符串类型参数，返回生成好的 HTML：

```js
var str = fs.readFileSync(__dirname + '/view/test.ejs', 'utf8')
var html = ejs.render(str, { name: names, title: title })
res.end(html)
```

第三种 rendering 的方式是 compile，接收 EJS 模板字符串并返回可以生成 HTML 的 JavaScript 方法供调用。


