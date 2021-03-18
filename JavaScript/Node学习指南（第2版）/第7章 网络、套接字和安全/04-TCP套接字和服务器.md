

### 7.1.2　TCP套接字和服务器

TCP为大多数互联网应用提供了通信平台，比如Web服务和邮箱。它提供了一种客户端和服务器套接字之间传输数据的可靠通道。TCP为应用层的存在提供了基础架构，比如HTTP。

我们可以像创建HTTP服务器一样创建TCP服务器，只是有一些细微的差别。创建TCP服务时，我们不会向创建服务的函数传递包含 `response` 和 `request` 对象的 `requestListener` 函数，TCP回调函数只有一个参数，就是用来接收和发送数据的套接字对象。

为了更好地解释TCP的工作原理，例7-1包含了创建一个TCP服务的代码。当服务套接字被创建之后，它会监听两个事件：接收数据事件和客户端关闭连接事件。然后它会将接收到的数据打印到控制台，并将数据重新发回客户端。

TCP服务也可以对监听（listening）事件和错误（error）事件绑定事件处理函数。在前面的章节中，我直接在创建服务端之后使用 `console.log()` 打印了一个消息，这也是Node中的常见操作。但是，鉴于 `listen ()` 事件是异步的，所以这个操作从技术上来说是错误的——因为消息会在 `listening` 事件触发之前就打印出来。事实上你可以把打印消息的操作放在 `listen()` 函数的回调函数中，或者像本例中的做法，给 `listening` 事件绑定一个回调函数，然后在回调函数中输出恰当的反馈信息。

另外，我还参考Node文档中的做法提供了一个更复杂的错误处理函数。应用程序会处理 `error` 事件，而如果错误的原因是端口正在使用，程序就会等待一小段时间，然后重试。对于其他类型的错误——比如访问80端口需要提供特殊的权限，完整的错误信息会被打印到控制台。

**例7-1　一个简单的TCP服务，在8124端口监听客户端通信**

```python
var net = require('net');
const PORT = 8124;
var server = net.createServer(function(conn) {
   console.log('connected');
   conn.on('data', function (data) {
      console.log(data + ' from ' + conn.remoteAddress + ' ' +
        conn.remotePort);
      conn.write('Repeating: ' + data);
   }); 
   conn.on('close', function() {
        console.log('client closed connection');
   }); 
}).listen(PORT);
server.on('listening', function() {
    console.log('listening on ' + PORT);
}); 
server.on('error', function(err){
  if (err.code == 'EADDRINUSE') {
    console.warn('Address in use, retrying...');
    setTimeout(() => {
      server.close();
      server.listen(PORT);
    }, 1000);
  }
  else { 
    console.error(err);
  }
});
```

创建TCP套接字时，你可以传入一个可选的参数对象，该对象包含两个值： `pauseOnConnect` 和 `allowHalfOpen` 。两个参数的默认值都是 `false` ：

```python
{ allowHalfOpen: false,
pauseOnConnect: false }
```

如果将 `allowHalfOpen` 设为 `true` ，那么套接字在接收到一个FIN信号时，不会回复一个FIN信号。这样做的目的是保持套接字可写（而不可读）。要关闭套接字，必须得调用 `end ()` 方法。如果将 `pauseOnConnect` 设为 `true` ，则会允许建立连接，而不读取任何数据。如果要开始读取数据，则需要在套接字上调用 `resume ()` 方法。

你可以使用TCP客户端程序来测试我们的服务器，比如Linux和OS X下的netcat工具（nc），或者Windows下对应的工具。使用netcat时，下面的命令会连接到8124端口的服务端程序，并且读取一个文件的数据，然后将其写入服务器：

```python
nc burningbird.net 8124 < mydata.txt
```

在Windows中也有TCP工具（比如SocketTest），可以用来进行测试。

除了使用TCP工具来测试之外，你也可以创建自己的TCP客户端程序。创建TCP客户端和创建服务端一样简单，如例7-2所示。数据会使用缓冲器来传递，但是我们可以使用 `setEncoding() 函数` 来将它转换为一个UTF-8字符串。套接字的 `write()` 方法就可以传输数据。客户端程序同样可以将监听函数绑定在两个事件上： `data` 事件，在接收到数据时触发； `close` 事件，当服务端关闭连接时触发。

**例7-2　客户端套接字将数据发送给TCP服务端**

```python
var net = require('net');
var client = new net.Socket();
client.setEncoding('utf8');
// connect to server
client.connect ('8124','localhost', function () {
   console.log('connected to server');
   client.write('Who needs a browser to communicate?');
});
// when receive data, send to server
process.stdin.on('data', function (data) {
   client.write(data);
});
// when receive data back, print to console
client.on('data',function(data) {
   console.log(data);
});
// when server closed
client.on('close',function() {
   console.log('connection is closed');
});
```

两个套接字直接传输的数据是从终端输入的，按下回车键时才会发送。客户端程序会将你输入的文本发送出去，TCP服务端则会在接收到文本之后打印到控制台。服务端会将消息返回给客户端，然后被客户端打印到控制台。服务端还会使用套接字的 `remoteAddress` 和 `remotePort` 属性将客户端的IP地址和端口打印出来。下面就是在客户端发送几条消息之后，服务端的输出：

```python
Hey, hey, hey, hey-now.
 from ::ffff:127.0.0.1 57251
Don't be mean, we don't have to be mean.
 from ::ffff:127.0.0.1 57251
Cuz remember, no matter where you go,
 from ::ffff:127.0.0.1 57251
there you are.
 from ::ffff:127.0.0.1 57251
```

客户端和服务端的连接会一直保持，直到你将其中一端的进程关掉，或者使用Ctrl-C停止程序。不管是哪一端还在运行，它都会收到一个关闭（close）事件，并且打印到控制台。服务端可以同时处理多个客户端的连接，因为所有相关的函数都是异步的。

> <img class="my_markdown" src="../images/76.png" style="zoom:50%;" />
> **IPv4和IPv6的映射**
> 本书中TCP客户端和服务端的示例程序输出展示了如何将IPv4地址映射到IPv6地址，就是在后面添加 `::ffff` 。

除了在TCP服务上绑定一个端口之外，我们还可以直接绑定一个套接字。为了展示这种用法，我对前一个例子中的TCP服务进行了修改。新的例子中没有绑定端口，而是绑定了一个UNIX套接字，如例7-3所示。UNIX套接字是服务器上的一个路径。这样，我们就可以使用读写权限来限制应用程序的权限，相对于互联网套接字来说，这样做更有优势。

我还需要修改错误处理部分的代码，让它释放UNIX套接字，以防应用重启的时候检测到套接字已经被占用。在产品环境中，你需要确保没有客户端在使用套接字，才能释放它。

**例7-3　绑定在UNIX套接字上的TCP服务**

```python
var net = require('net');
var fs = require('fs');
const unixsocket = '/somepath/nodesocket';
var server = net.createServer(function(conn) {
   console.log('connected');
   conn.on('data', function (data) {
      conn.write('Repeating: ' + data);
   }); 
   conn.on('close', function() {
        console.log('client closed connection');
   }); 
}).listen(unixsocket);
server.on('listening', function() {
    console.log('listening on ' + unixsocket);
}); 
// if exit and restart server, must unlink socket
server.on('error',function(err) {
   if (err.code == 'EADDRINUSE') {
      fs.unlink(unixsocket, function() {
          server.listen(unixsocket);
      });
   } else {
      console.log(err);
   }
}); 
process.on('uncaughtException', function (err) {
    console.log(err);
});
```

我还使用了 `process` 对象来应对一些应用本身没有处理的错误。

> <img class="my_markdown" src="../images/77.png" style="zoom:50%;" />
> **检查是否有另一个实例在运行服务**
> 释放套接字之前，你可以检查当前服务是否有别的实例在运行。针对这种情况，Stack Overflow中的一个解决方案提供了一种检查技巧。

客户端程序请见例7-4。和前一个使用端口来通信的例子并无多大不同。唯一的区别是对连接点的适配。

**例7-4　连接到UNIX套接字，并打印接收到的数据**

```python
var net = require('net');
var client = new net.Socket();
client.setEncoding('utf8');
// connect to server
client.connect ('/somepath/nodesocket', function () {
   console.log('connected to server');
   client.write('Who needs a browser to communicate?');
});
// when receive data, send to server
process.stdin.on('data', function (data) {
   client.write(data);
});
// when receive data back, print to console
client.on('data',function(data) {
   console.log(data);
});
// when server closed
client.on('close',function() {
   console.log('connection is closed');
});
```

> <img class="my_markdown" src="../images/78.png" style="zoom:50%;" />
> 7.2节讲到了HTTPS，即HTTP的SSL版本，以及Crypto和TLS/SSL。

