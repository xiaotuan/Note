```js
// load http module
const fs = require('fs');
var http = require('http')
var https = require('https');
var querystring = require('querystring');

var options = {
    key: fs.readFileSync('./sslkey/www.amazingrace.cn.key'),
    cert: fs.readFileSync('./sslkey/www.amazingrace.cn.pem')
}

var httpsServer = https.createServer(options, function(request, response) {
    console.log(request.url)
    if (request.url == '/logindemo') {
        if (request.method == 'POST') {
            var body = '';
            // append data chunk to body
            request.on('data', function (data) {
                body += data;
            });
            // data transmitted
            request.on('end', function () {
                var post = querystring.parse(body);
                console.log("username: " + post["username"] + ", password: " + post["password"]);
                response.writeHead(200, { 'Content-Type': 'text/plain' });
                if (post["username"] == 'sheran' && post["password"] == 's3kr3tc0dez') {
                    response.end('Login success!!')
                } else {
                    response.end('Login failed!!\n');
                }
            });
        } else if (request.method == 'GET') {
            response.writeHead(200, { 'Content-Type': 'text/plain' });
            response.end('Hello World\n');
        }
    } else {
        response.writeHead(200, { 'Content-Type': 'text/plain' });
        response.end('Hello World\n');
    }
}).listen(443);

var httpServer = http.createServer(function(request, response) {
    console.log(request.url)
    if (request.url == '/logindemo') {
        if (request.method == 'POST') {
            var body = '';
            // append data chunk to body
            request.on('data', function (data) {
                body += data;
            });
            // data transmitted
            request.on('end', function () {
                var post = querystring.parse(body);
                console.log("username: " + post["username"] + ", password: " + post["password"]);
                response.writeHead(200, { 'Content-Type': 'text/plain' });
                if (post["username"] == 'sheran' && post["password"] == 's3kr3tc0dez') {
                    response.end('Login success!!')
                } else {
                    response.end('Login failed!!\n');
                }
            });
        } else if (request.method == 'GET') {
            response.writeHead(200, { 'Content-Type': 'text/plain' });
            response.end('Hello World\n');
        }
    } else {
        response.writeHead(200, { 'Content-Type': 'text/plain' });
        response.end('Hello World\n');
    }
}).listen(80)
console.log('server listening on 80');
```

