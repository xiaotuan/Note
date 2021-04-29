TCP 客户端的实现代码如下（可以和 [TCP服务的实现](./TCP服务的实现.md) 中的代码进行配合使用）：

```js
var net = require('net')

var client = new net.Socket()
client.setEncoding('utf8')

// connect to server
client.connect('8124', 'localhost', function () {
   console.log('connect to server')
   client.write('Who needs a browser to communicate?')
})

// prepare for input from terminal
process.stdin.resume()

// when receive data, send to server
process.stdin.on('data', function (data) {
   client.write(data, clien)
})

// when receive data back, print to console 
client.on('data', function (data) {
   console.log(data)
})

// when server closed
client.on('close', function () {
   console.log('connection is closed')
})
```

