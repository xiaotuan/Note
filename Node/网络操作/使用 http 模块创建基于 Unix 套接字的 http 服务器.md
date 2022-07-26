所有的 server/socket 模块除了可以连接并工作在特定的网络端口上，还支持连接到 `Unix` 套接字。与网络套接字不同，Unix 或 IPC（进程间通信）套接字支持主要用来支持同一系统内的进程间通信。例如：

**服务端示例代码：**

```js
// create server
// and callback function
var http = require('http');
var fs = require('fs');

http.createServer(function(req, res) {
    var query = require('url').parse(req.url).query;
    console.log(query);
    file = require('querystring').parse(query).file;

    // content header
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    // increment global, write to client
    for (var i = 0; i < 100; i++) {
        res.write(i + '\n');
    }

    // open and read in file contents
    var data = fs.readFileSync(file, 'utf8');
    res.write(data);
    res.end();
}).listen('/tmp/node-server-sock');
```

> 注意：这里没有使用异步文件读取功能，是因为异步文件读取函数可能会在连接关闭后才被调用，而无法输出文件内容到客户端。

**客户端示例代码：**

```js
var http = require('http');

var options = {
    method: 'GET',
    socketPath: '/tmp/node-server-sock',
    path: "/?file=main.txt"
};

var req = http.request(options, function(res) {
    console.log('STATUS: ' + res.statusCode);
    console.log('HEADERS: ' + JSON.stringify(res.headers));
    res.setEncoding('utf8');
    res.on('data', function(chunk) {
        console.log('chunk o\' data: ' + chunk);
    });
});

req.on('error', function(e) {
    console.log('problem with request: ' + e.message);
});

// write data to request body
req.write('data\n');
req.write('data\n');
req.end();
```

