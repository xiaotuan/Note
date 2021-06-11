下面是一个使用 `http` 模块向服务器发起 POST 请求的代码：

```js
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

> 注意：
>
> 如果应用程序发出很多请求，这些请求可能会被连接池限制而产生瓶颈。解决这个问题的方法就是把传出请求中的 `agent` 属性设置为 `false`，从而禁止连接池。修改如下：
>
> ```js
> var options = {
>  hostname: 'localhost',
>  port: 8124,
>  method: 'POST',
>  headers: {
>      'Content-Type': 'application/x-www-form-urlencoded',
>      'Content-Length': postData.length
>  },
>  agent: false
> };
> ```
>
> 也可以通过 `agent.maxFreeSockets` 来修改套接字池的最大值。它默认值是 256。修改如下：
>
> ```js
> var options = {
>   hostname: 'localhost',
>   port: 8124,
>   method: 'POST',
>   headers: {
>     'Content-Type': 'application/x-www-form-urlencoded',
>     'Content-Length': postData.length
>   },
>   agent: new http.Agent({
>     maxFreeSockets: 512
>   })
> }; 
> ```
>

