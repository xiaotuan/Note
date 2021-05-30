[toc]

### 1. 引入 `http` 模块

```js
var http = require('http')
```

### 2. 创建 `http` 服务

```js
http.createServer(function (request, response) {
      response.writeHead(200, {'Content-Type': 'text/plain'});
      response.end('Hello World\n');
});
```

### 3. 启动服务

```js
http.listen(8124);
```

