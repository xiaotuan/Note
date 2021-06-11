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

### 4. 完整代码

```js
var http = require('http');
http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Hello World\n');
}).listen(8124);
console.log('Server running at http://127.0.0.1:8124/');
```

响应Web请求的回调函数支持两个参数： `request` 和 `response` 。第二个参数 `response` 是 `http.ServerResponse类` 的一个对象。它是一个支持众多函数的可写流，其中包括创建响应头的 `response.writeHead()` 、向响应中写数据的 `response.write()` 和结束响应的 `response.end()` 。

第一个参数 `request` 是 `IncomingMessage` 类的一个实例，它是一个可读流。以下是一些可以从 `request` 中得到的信息。

+ `request.headers` ， `request/response header` 对象。
+ `request.httpVersion` ， `request` 的HTTP版本。
+ `request.method` ，该属性只适用于 `http.Server` 的请求，用来返回HTTP请求方法（GET或POST）。
+ `request.rawHeaders` ，原始头部。
+ `request.rawTrailers` ，原始尾部。

为了看出 `request.headers` 和 `request.rawHeaders` 的不同，你可以在请求中把它们用 `console.log` 打印出来。注意， `request.headers` 打印出来的是键值对，而 `request.raw Headers` 打印出来的是数组，数组中第一个元素对应的是键名，第二个元素对应的是值，这样你就可以访问每个单独的值了：

```js
console.log(request.headers);
console.log(request.rawHeaders);
// pulling host
console.log(request.headers.host);
console.log(request.rawHeaders[0] +  ' is ' + request.rawHeaders[1]);
```

