

### 8.1.2　child_process.fork

最后要介绍的子进程函数是 `child_process.fork()` 。这个 `spawn ()` 函数的变种主要是为了生成Node进程。

`child_process.fork()` 这个函数与众不同的地方在于，它和子进程之间会建立一个通信通道。但是请注意，每个进程都需要一个新的V8实例，既耗时又耗内存。

`child_process.fork()` 有一种用法是将功能分离到完全独立的Node实例上。假设你在Node实例上运行着一个服务，然后你想通过集成另一个可以处理服务器请求的Node实例来提升性能。Node文档提供了一个使用TCP服务的例子。那么同样的方法能不能用来创建并行的HTTP服务呢？当然可以了，在这个例子上稍加改动就可以了。

> <img class="my_markdown" src="../images/88.png" style="zoom:50%;" />
> 我要谢谢Jiale Hu，看到他写的并行HTTP服务的代码时，我才有了上面这些思路。Jiale使用了一个TCP服务将套接字终端传递给两个独立的子HTTP服务。

与Node文档中所展示的生成父/子并行TCP服务类似，在我的例子中，我在父进程中创建了HTTP服务，然后用 `child_process.send()` 函数将服务传递给了子进程。

```python
var cp = require('child_process'),
    cp1 = cp.fork('child2.js'),
    http = require('http');
var server = http.createServer();
server.on('request', function (req, res) {
   res.writeHead(200, {'Content-Type': 'text/plain'});
   res.end('handled by parent\n');
}); 
server.on('listening', function () {
    cp1.send('server', server);
});
server.listen(3000);
```

子进程会通过 `process` 对象接收到一个包含HTTP服务的消息。然后它会监听连接（connection）事件。该事件被触发后，它会再触发子进程HTTP服务上的 `connection` 事件，并将生成连接终端的套接字发送出去。

```python
var http = require('http');
var server = http.createServer(function (req, res) {
   res.writeHead(200, {'Content-Type': 'text/plain'});
   res.end('handled by child\n');
}); 
process.on('message', function (msg, httpServer) {
   if (msg === 'server') {
      httpServer.on('connection', function (socket) {
          server.emit('connection', socket);
      });
   } 
});
```

如果你通过访问域名的3000端口来测试这个程序，你会发现有时候父HTTP服务会处理请求，有时候子服务会处理。如果查看运行的进程，你会发现有两个：一个是父进程，一个是子进程。

> <img class="my_markdown" src="../images/89.png" style="zoom:50%;" />
> **Node集群**
> Node中的集群（cluster）模块就是基于 `child_process.fork()` 和其他一些功能实现的。

