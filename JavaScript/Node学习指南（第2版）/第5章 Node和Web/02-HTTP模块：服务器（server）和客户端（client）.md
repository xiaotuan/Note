[toc]

### 5.1　HTTP模块：服务器（server）和客户端（client）

不要指望可以用HTTP模块来从零创建一个和Apache或Nginx有同样复杂度的Web服务器。正如Node文档所说，HTTP模块是偏底层的，并且专注于流处理和消息解析。然而，它为更复杂的功能提供了基础支持，例如第10章中将介绍的Express。

HTTP模块支持多个对象，包括 `http.Server` ，就是我们在第1章演示 `http.create Server()` 函数时返回的对象。在那个例子中，我们嵌入了一个回调函数来处理Web请求，但由于 `http.Server` 继承了 `EventEmitter` ，所以我们也可以用另一个事件：

```python
var http = require('http');
var server = http.createServer().listen(8124);
server.on('request', function(request,response) {
   response.writeHead(200, {'Content-Type': 'text/plain'});
   response.end('Hello World\n');
});
console.log('server listening on 8214');
```

你可以监听其他事件，比如建立连接（ `connect` ）事件，或者客户端请求更新（ `upgrade` ）事件。后者会在客户端要求升级HTTP版本或者升级到其他网络协议时发生。

> <img class="my_markdown" src="../images/63.png" style="zoom:50%;" />
> **HTTP的内部结构**
> 可能有些读者想要多了解一些HTTP的内部结构， `HTTP.Server` 类实际上是基于TCP的 `Net.Server` 实现的，这些将在第7章介绍。TCP提供了传输层，而HTTP则提供了应用层。

响应Web请求的回调函数支持两个参数： `request` 和 `response` 。第二个参数 `response` 是 `http.ServerResponse类` 的一个对象。它是一个支持众多函数的可写流，其中包括创建响应头的 `response.writeHead()` 、向响应中写数据的 `response.write()` 和结束响应的 `response.end()` 。

> <img class="my_markdown" src="../images/64.png" style="zoom:50%;" />
> **可读和可写流**
> 第6章会讲到可读和可写流。

第一个参数 `request` 是 `IncomingMessage` 类的一个实例，它是一个可读流。以下是一些可以从 `request` 中得到的信息。

+ `request.headers` ， `request/response header` 对象。
+ `request.httpVersion` ， `request` 的HTTP版本。
+ `request.method` ，该属性只适用于 `http.Server` 的请求，用来返回HTTP请求方法（GET或POST）。
+ `request.rawHeaders` ，原始头部。
+ `request.rawTrailers` ，原始尾部。

为了看出 `request.headers` 和 `request.rawHeaders` 的不同，你可以在请求中把它们用 `console.log` 打印出来。注意， `request.headers` 打印出来的是键值对，而 `request.raw Headers` 打印出来的是数组，数组中第一个元素对应的是键名，第二个元素对应的是值，这样你就可以访问每个单独的值了：

```python
console.log(request.headers);
console.log(request.rawHeaders);
// pulling host
console.log(request.headers.host);
console.log(request.rawHeaders[0] +  ' is ' + request.rawHeaders[1]);
```

Node文档中写到，有些 `IncomingMessage` 的属性（ `statusCode` 和 `status Message` ）只能被从 `HTTP.ClientRequest` 对象中获取的响应（而非请求）访问。除了创建一个监听请求的服务器之外，还可以创建一个发出请求的客户端。你可以用 `ClientRequest` 类来实现，并用 `http.request()` 函数来实例化该类。

为了演示服务器和客户端这两种类型的功能，我用Node文档中的示例代码创建了一个客户端，并对它进行修改从而能够访问客户端本地的服务器。我在客户端创建了一个POST方法用来发送数据，所以我要修改服务器让它能读取这些数据。这就是 `IncomingMessage` 的可读流发挥作用的地方了。应用程序并没有监听 `request` 事件，而是监听一个或多个 `data` 事件，从而获取请求中的数据块（chunk）（没错，这是一个技术术语）。应用程序将持续获取数据块，直到 `request` 对象监听到一个 `end` 事件。接着用另一个很有用的Node模块—— `Query String` （它的细节会在第5.4节中讲到）来解析数据，并且打印到控制台中。直到那时响应才会被发送回去。

例5-1展示了被修改的服务器代码。注意这跟之前的代码非常类似，唯一的区别是使用了新的事件处理器来处理传递过来的数据。

**例5-1　监听POST请求和处理POST数据的服务器**

```python
var http = require('http');
var querystring = require('querystring');
var server = http.createServer().listen(8124);
server.on('request', function(request,response) {
   if (request.method == 'POST') {
        var body = '';
        // append data chunk to body
        request.on('data', function (data) {
            body += data;
        });
        // data transmitted
        request.on('end', function () {
            var post = querystring.parse(body);
            console.log(post);
            response.writeHead(200, {'Content-Type': 'text/plain'});
            response.end('Hello World\n');
        }); 
   } 
});
console.log('server listening on 8214');
```

例5-2展示了新的客户端代码。它使用了 `http.ClientRequest` 。 `http.Client ``Request` 是一个可写流的实现，从示例代码中使用的 `req.write()` 方法可以看出来。

除了代码中访问的服务器外，这段代码几乎是直接从Node文档中复制过来的。因为服务器和客户端在同一台机器上，所以这里用localhost作为主机。此外，我们也没有指定 `options` 中的 `path` 属性，因为我们用“/”作为默认路径。请求头中设置了可以跟POST数据一起使用的内容类型： `application/x-www-form-urlencoded` 。同时注意客户端是通过响应来接收服务器返回的数据了。传出去的数据也是通过数据块的形式从响应中获取的，只不过这次每个数据块都在刚被接收到的时候就被打印到了控制台。因为返回消息很短，所以只触发了一个 `data` 事件。

实际上POST请求并不会被异步处理，因为我们是在初始化一个操作，而不是因为等待某个操作而产生阻塞。

**例5-2　HTTP客户端发送数据到服务器**

```python
var http = require('http');
var querystring = require('querystring');
var postData = querystring.stringify({
  'msg' : 'Hello World!'
}); 
var options = {
  hostname: 'localhost',
  port: 8124,
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': postData.length
  }
}; 
var req = http.request(options, function(res) {
  console.log('STATUS: ' + res.statusCode);
  console.log('HEADERS: ' + JSON.stringify(res.headers));
  res.setEncoding('utf8');
  // get data as chunks
  res.on('data', function (chunk) {
    console.log('BODY: ' + chunk);
  });
  // end response
  res.on('end', function() {
    console.log('No more data in response.')
  })
}); 
req.on('error', function(e) {
  console.log('problem with request: ' + e.message);
}); 
// write data to request body
req.write(postData);
req.end();
```

我们需要打开另一个终端，然后启动服务器，再运行客户端。在例5-2中，客户端所做的事情就是跟服务器打个招呼，然后接收到服务器返回的同样是打招呼信息。

上面这些内容，其实只不过是两个进程之间互相通信而已。但是通过这个例子，我们已经实现了客户端和服务器之间的双向通信，而且还使用了POST请求，而不是仅停留在GET请求。同时，我们还接触到了HTTP模块下几乎所有的类（只剩一个还没有接触过了）： `http.ClientRequest` 、 `http.Server` 、 `http.IncomingMessage` 和 `http.ServerResponse` 。

唯一一个我们还没有接触到的类是用于套接字池（pooling socket）的 `http.Agent` 。Node维护了一个套接字的池，用于处理那些通过 `http.request()` 或 `http.get()` 创建的请求。后一种请求是简化过的请求，是一个没有请求体（request body）的GET请求。如果应用程序发出很多请求，这些请求可能会被连接池限制而产生瓶颈。解决这个问题的方法就是把传出请求中的 `agent` 属性设置为 `false` ，从而禁止连接池。在例5-2中，需要做以下更改：

```python
var options = {
  hostname: 'localhost',
  port: 8124,
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': postData.length
  },
  agent: false 
}; 
```

你也可以通过 `agent.maxFreeSockets` 来修改套接字池的最大值。它的默认值是256。但请注意，更改传出请求连接池可能会对内存或其他资源的使用造成不利影响。

我们会在第7章中处理更复杂的通信，但现在，让我们先看看如何创建一个比返回“你好”更有意义的HTTP服务器。

