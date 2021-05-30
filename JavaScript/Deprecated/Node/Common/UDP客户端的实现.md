UDP 客户端实现代码如下所示（可以与 [UDP服务端的实现](./UDP服务端的实现.md) 配合使用：

```js
var dgram = require('dgram')

var client = dgram.createSocket('udp4')

// prepare for input from terminal
process.stdin.resume()

process.stdin.on('data', function (data) {
   console.log(data.toString('utf8'))
   client.send(data, 0, data.length, 8124, 'examples.burningbird.net', function (err, bytes) {
      if (err) {
         console.log('error: ' + err)
      } else {
         console.log('successful')
      }
   })
})
```

> 提示：套接字类型参数可以是 udp4 或 udp6。