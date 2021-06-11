可以通过监听请求参数 `req` 的 `data` 事件来获取 `POST` 请求的参数，代码如下所示：

```js
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

