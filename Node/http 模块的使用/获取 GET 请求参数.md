可以使用请求变量 `req` 的 `url` 变量构建 `URL` 类，通过 `URL` 类的 `searchParams` 值获取 `GET` 请求参数，代码如下所示：

```js
var http = require("http")

var server = http.createServer(function(req, res) {
    if ('GET' == req.method) {
        var url = new URL('http://127.0.0.1:8124' + req.url)
        url.searchParams.forEach((value, key) => {
            console.log('Param key: ' + key + ', value: ' + value)
        });
    }
    res.writeHead(200, {'Content-Type':'text/plain'})
    res.end('Hello World')
});

server.listen(8124, function() {
    console.log('Server running at port 8124')
})
```

> 提示：
>
> 以前可以使用 `url` 模块来解析 `GET` 请求参数，只是现在这个模块已经标记为过时。具体代码如下：
>
> ```js
> var http = require("http")
> 
> var server = http.createServer(function(req, res) {
>     if ('GET' == req.method) {
>         var query = require('url').parse(req.url, true).query
>         for (let key in query) {
>             console.log('Param key: ' + key + ', value: ' + query[key])
>         }
>     }
>     res.writeHead(200, {'Content-Type':'text/plain'})
>     res.end('Hello World')
> });
> 
> server.listen(8124, function() {
>     console.log('Server running at port 8124')
> })
> ```

