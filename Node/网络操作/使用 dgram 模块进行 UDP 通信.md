UDP 模块的标识符是 `dgram`：

```js
require('dgram');
```

要创建一个 UDP 套接字，可以使用 `createSocket` 方法并传入套接字类型参数 `udp4` 或 `udp6`。你同样也可以传递一个回调函数用于监听事件。与使用 TCP 发送消息不同的是，使用 UDP 发送消息时必须使用 buffer，而不能是字符串。

**示例：UDP 客户端，将输入到终端的信息通过 UDP 套接字发送出去**

```js
var dgram = require('dgram');

var client = dgram.createSocket("udp4");

// prepare for input from terminal
process.stdin.resume();

process.stdin.on('data', function(data) {
    console.log(data.toString('utf8'));
    client.send(data, 0, data.length, 8124, "127.0.0.1", function(err, bytes) {
        if (err)
            console.log('error: ' + err);
        else
            console.log('successful');
    });
});
```

**示例：创建 UDP 服务器，绑定 8124 端口并接收数据**

```js
var dgram = require('dgram')

var server = dgram.createSocket('udp4');

server.on('message', function(msg, rinfo) {
    console.log("Message: " + msg + " from " + rinfo.address + ":" + rinfo.port);
});

server.bind(8124);
```



