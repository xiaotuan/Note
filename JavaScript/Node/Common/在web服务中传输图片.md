代码如下所示：

```js
var http = require('http')
var fs = require('fs')

http.createServer(function (req, res) {
    var file = 'phoenix5a.png';
    fs.stat(file, function (err, stat) {
        if (err) {
            console.error(err);
            res.writeHead(200, {'Content-Type':'text/plain'});
            res.end("Sorry, Burningbird isn't around ringht now\n");
        } else {
            var img = fs.readFileSync(file);
            res.contentType = 'image/png';
            res.contentLength = stat.size;
            res.end(img, 'binary');
        }
    });
}).listen(8124);
console.log('Server running at port 8124/');
```

