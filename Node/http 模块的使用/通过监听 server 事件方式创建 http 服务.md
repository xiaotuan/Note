下面是通过 `on` 事件方式创建 `http` 服务的代码：

```js
var http = require('http');
var server = http.createServer().listen(8124);
server.on('request', function(request,response) {
   response.writeHead(200, {'Content-Type': 'text/plain'});
   response.end('Hello World\n');
});
console.log('server listening on 8214');
```

还可以监听其他事件，比如建立连接（`connect`）事件，或者客户端请求更新（`upgrade`） 事件。后者会在客户端要求升级 HTTP 版本或者升级到其他网络协议时发生。

