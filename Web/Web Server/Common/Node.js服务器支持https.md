示例代码如下：

```js
// load http module
var http = require('http');
var https = require('https');
let fs = require('fs');

// Configuare https
const httpsOption = {
    key: fs.readFileSync("/home/sslkey/www.amazingrace.cn.key"),
    cert: fs.readFileSync("/home/sslkey/www.amazingrace.cn.pem")
}

function app(req, res) {
    // content header
    res.writeHead(200, {'content-type': 'text/plain'})
    
    // write message and signal communication is complete
    res.end("Hello, World!\n")
}

// create http server
http.createServer(app).listen(80)
https.createServer(httpsOption, app).listen(443);

console.log('Server running on 80')
```

