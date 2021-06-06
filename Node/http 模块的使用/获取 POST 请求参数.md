可以通过监听请求参数 `req` 的 `data` 事件来获取 `POST` 请求的参数，代码如下所示：

```js
var http = require("http")

var server = http.createServer(function(req, res) {
    if ('POST' == req.method) {
        req.once('data', postData => {
            console.log("post data: \n" + postData)
        })
    }
    res.writeHead(200, {'Content-Type':'text/plain'})
    res.end('Hello World')
});

server.listen(8124, function() {
    console.log('Server running at port 8124')
})
```

