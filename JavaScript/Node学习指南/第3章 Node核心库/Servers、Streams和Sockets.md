**TCP Sockets 和 Servers**

**示例3-2 一个简单的 TCP 服务器，并在端口 8124 上监听客户端连接请求**

```js
var net = require('net')

var server = net.createServer(function (conn) {
   console.log('connected')
   conn.on('data', function (data) {
      console.log(data + ' from ' + conn.remoteAddress + ' ' + conn.remotePort)
      conn.write('Repeating: ' + data)
   })
   
   conn.on('close', function () {
      console.log('client closed connection')
   })
}).listen(8124)

console.log('listening on port 8124')
```

`createServer` 方法有一个可选参数 allowHalfOpen。如果将该参数设置为 true，那么当套接字从客户端接收到一个 FIN 包后，它不会发送另一个 FIN 作为回应。如果想关闭套接字，需要明确地使用 end 方法。默认情况下， allowHalfOpen 是 false。

在客户端套接字接口上调用 `setEncoding` 方法来对接收数据的编码处理方式。

**示例3-3 使用 TCP 客户端套接字发送数据给 TCP 服务端**

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
   client.write(data)
})

// when receive data back, print to console 
client.on('data', function (dat) {
   console.log(data)
})

// when server closed
client.on('close', function () {
   console.log('connection is closed')
})
```

**HTTP**

**示例3-4 基于 Unix 套接字的 HTTP 服务器**

```js
// create server
// and callback function
var http = require('http')
var fs = require('fs')

http.createServer(function (req, res) {
   var query = require('url').parse(req.url).query
   console.log(query)
   file = require('querystring').parse(query).file
   
   // content header
   res.writeHead(200, {'Content-Type':'text/plain'})
   
   // increment global, write to client
   for (var i = 0; i < 100; i++) {
      res.write(i + '\n')
   }
   
   // open and read in file contents
   var data = fs.readFileSync(file, 'utf8')
   res.write(data)
   res.end()
}).listen('/tmp/node-server-sock')
```

**示例3-5 连接到 Unix 套接字并输出接收的数据**

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

**UDP 数据报套接字**

UDP 模块的标识符是 "dgram"：

```js
require('dgram')
```
> 使用 UDP 发送消息时必须使用 buffer。

**示例3-6 UDP 客户端，将输入到终端的信息通过 UDP 套接字发送出去**

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

**示例3-7 创建 UDP 服务端，绑定 8124 端口并接收数据**

```js
var dgram = require('dgram')

var sever = dgram.createSocket('udp4')

server.on('message', function (msg, rinfo) {
   console.log("Message: " + msg + " from " + rinfo.address + ":" + rinfo.port)
})

server.bind(8124)
```

无论在 UDP 客户端还是服务端的代码中，当发送或者接收到数据后，我们并没有调用任何 close 方法来关闭套接字。因为在客户端和服务器端之间并没有维护一个持续连接。