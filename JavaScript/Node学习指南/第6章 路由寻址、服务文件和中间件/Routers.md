使用 npm 安装 Crossroads：

```console
npm install crossroads
```

**Crossroads 的重要方法**

| 方法 | 说明 |
| :- | :- |
| addRoute | 定义一个新模式的路由监听 |
| parse | 解析字符串，并将符合的字符串转发到正确的路由 |
| matched.add | 将路由处理与路由做映射 |

可以使用冒号（:）表示可选择的部分。如下：

```
category/:type:/:id:
```

会匹配：

```
category/
category/tech/
category/history/143
```

**示例6-10 使用 Crossroads 将 URL 请求定位到具体的操作**

```js
var crossroads = require('crossroads'),
    http = require('http')

crossroads.addRoute('/category/{type}/:pub:/:id:', function (type, pub, id) {
    if (!id && !pub) {
        console.log('Accessing all entries of category ' + type)
        return
    } else if (!id) {
        console.log('Accessing all entries of category ' + type + ' and pub ' + pub)
    } else {
        console.log('Accessing item ' + id + ' of pub ' + pub + ' of category ' + type)
    }
})

http.createServer(function (req, res) {
    crossroads.parse(req.url)
    res.end('and that\'s all \n')
}).listen(8124)
```

可以使用下面请求进行测试：

```
http://localhost:8124/category/history
http://localhost:8124/category/history/journal
http://localhost:8124/category/history/journal/174
```

**示例6-11 根据给定的路径映射到路由处理函数**

```js
var crossroads = require('crossroads'),
    http = require('http')

var typeRoute = crossroads.addRoute('/{type}/{id}')

function onTypeAccess(type, id) {
    console.log('access ' + type + ' ' + id)
}

typeRoute.matched.add(onTypeAccess)

http.createServer(function (req, res) {
    crossroads.parse(req.url)
    res.end('processing')
}).listen(8124)
```

可以使用下面请求进行测试：

```
http://localhost:8124/node/174
http://localhost:8124/user/3
```