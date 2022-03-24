代码如下所示：

**MyWeb.js**

```javascript
var http = require('http');
http.createServer(function(request, response) {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World\n');
}).listen(8124);
console.log('Server running at http://127.0.0.1:8124/');
```

在终端中执行如下命令：

```shell
$ node MyWeb.js
Server running at http://127.0.0.1:8124/
```

然后在浏览器中输入如下网站即可看到自己的 web 网页了：

```txt
http://127.0.0.1:8124
```

> 注意：http 模块是 Node 的核心模块，安装 Node 后就自带该模块了，所以不需要重新安装该模块。

