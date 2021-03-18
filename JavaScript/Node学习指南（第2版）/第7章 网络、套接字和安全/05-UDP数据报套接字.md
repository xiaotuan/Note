

### 7.1.3　UDP/数据报套接字

TCP需要在两个终端之间建立一个专门的连接。UDP则是一个无连接的协议，也就意味着两个终端之间并不保证一定有连接存在。出于这个原因，UDP比TCP的可靠性和稳定性都差一点。然而，UDP又比TCP速度快，所以更适用于对实时性要求比较高的场景，以及那些使用TCP连接可能会对信号质量造成负面影响的场景，比如基于IP的语音传输（VoIP）。

Node核心对两种套接字都是支持的，在上一节中我演示了TCP的功能。现在轮到UDP了。

UDP模块的名称是dgram：

```python
require ('dgram');
```

要创建一个UDP套接字，需要使用 `createSocket` 方法传入套接字类型—— `udp4` 或者 `udp6` 。我们还可以传入一个回调函数，用来监听事件。和用TCP发送的消息不同，使用UDP发送的消息必须使用缓冲器，而不能用字符串。

例7-5包含了展示UDP客户端的代码。代码中使用 `process.stdin` 来获取数据，然后使用UDP套接字来发送。注意，我们不需要设置字符串的编码，因为UDP套接字只支持缓冲器，而 `process.stdin` 的数据刚好就是缓冲器。但是我们还是需要使用缓冲器的 `toString` 方法将缓冲器转化为有意义的字符串，然后使用 `console.log ()` 来打印。

**例7-5　一个将终端输入的内容发送出去的数据报客户端**

```python
var dgram = require('dgram');
var client = dgram.createSocket("udp4");
process.stdin.on('data', function (data) {
   console.log(data.toString('utf8'));
   client.send(data, 0, data.length, 8124, "examples.burningbird.net",
      function (err, bytes) {
        if (err)
          console.error('error: ' + err);
        else
          console.log('successful');
   });
});
```

在例7-6中，UDP服务端甚至比客户端还要简单。服务端程序所做的事情就是创建套接字，将其绑定到一个端口上（8124），然后监听消息（message）事件。当接收到消息时，程序会用 `console.log` 将该消息、发送者的IP地址和端口一起打印出来。无须编码就可以打印——内容会自动从缓冲器转化为字符串。

并不是一定要将套接字绑定到一个端口。但是如果不绑定，套接字将会试图对所有的端口进行监听。

**例7-6　一个绑定在8124端口并且监听消息的UDP套接字服务**

```python
var dgram = require('dgram');
var server = dgram.createSocket("udp4");
server.on ("message", function(msg, rinfo) {
   console.log("Message: " + msg + " from " + rinfo.address + ":"
                + rinfo.port);
});
server.bind(8124);
```

我不需要在客户端发出消息或者服务端接收消息之后调用 `close` 方法：因为客户端和服务端之间并不存在连接——套接字本身就有发送和接收消息的功能。

