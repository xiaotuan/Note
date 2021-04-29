Unix 套接字客户端的实现代码如下（可以和 [Unix套接字服务端的实现](./Unix套接字服务端的实现.md) 文章中的代码配合使用）：

```js
var http = require('http')

var options = {
   method: 'GET',
   socketPath: '/tmp/node-server-sock',
   path: "/?file=main.txt"
}

var req = http.request(options, function (res) {
   console.log('STATUS: ' + res.statusCode)
   console.log('HEADERS: ' + JSON.stringify(res.headers))
   res.setEncoding('utf8')
   res.on('data', function (chunk) {
      console.log('chunk o\' data: ' + chunk)
   })
})

req.on('error', function (e) {
   console.log('problem with request: ' + e.message)
})

// write data to request body
req.write('data\n')
req.write('data\n')
req.end()
```



