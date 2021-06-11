下面是一个使用 `http` 模块的 `get()` 方法向服务器发起 `GET` 请求的示例代码：

```js
var http = require('http');

http.get('http://localhost:8124', function(res) {
    var body = ''
    res.on('data', function(data) {
        body += data;
    });
    res.on('end', function() {
        console.log("body: " + body);
    });
}).on('error', function(data) {
    console.error("error: " + data);
});
```

