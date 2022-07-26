[toc]

### 1. TCP 服务端

我们可以使用 Node 中的 Net 模块来创建一个基本的 TCP 服务器和客户端。

下面是一个简单的 TCP 服务器，并在端口 8124 上监听客户端连接请求：

```js
var net = require('net')

var server = net.createServer(function(conn) {
    console.log('connected');

    conn.on('data', function(data) {
        console.log(data + ' from ' + conn.remoteAddress + ' ' + conn.remotePort);
        conn.write('Repeating: ' + data);
    });
    conn.on('close', function() {
        console.log('client closed connection');
    });
}).listen(8124);

console.log('listening on port 8124');
```

`createServer` 方法有一个可选参数 `allowHalfOpen`。如果将该参数设置为 `true`，那么当套接字从客户端接收到一个 FIN 包后，它不会发送另一个 FIN 作为回应。这样做可使得套接字接口始终打开并且可写（当然不可读）。如果想关闭套接字，你需要明确地使用 `end` 方法。默认情况下， `allowHalfOpen` 是 `false` 的。

> 注意：在 Node 中，许多可以产生事件的对象都支持通过 `on` 方法来绑定事件监听器。此方法第一个参数为事件名称，第二个参数为事件处理函数。
>
> Node 中有一个较为特殊的对象 `EventEmitter`，所有继承自它的对象都会提供 `on` 方法。

### 2. TCP 客户端

在客户端套接字接口上调用 `setEncoding` 方法来改变对接收数据的编码处理方式。下面是一个使用 TCP 客户端套接字发送数据给 TCP 服务端：

```js
var net = require('net');

var client = new net.Socket();
client.setEncoding('utf8');

// connect to server
client.connect('8124', 'localhost', function() {
    console.log('connected to server');
    client.write('Who needs a browser to communicate?');
});

// prepare for input from terminal
process.stdin.resume();

// when receive data, send to server
process.stdin.on('data', function(data) {
    client.write(data);
});

// when receive data back, print to console
client.on('data', function(data) {
    console.log(data);
});

// when server closed
client.on('close', function() {
    console.log('connection is closed');
});
```

