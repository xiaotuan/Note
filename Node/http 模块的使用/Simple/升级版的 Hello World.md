**hello.js**

```js
var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
   var name = require('url').parse(req.url, true).query.name;
   if (name === undefined) name = 'world';
   if (name == 'burningbird') {
      var file = 'phoenix5a.png';
      fs.stat(file, function (err, stat) {
         if (err) {
            console.error(err);
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.end("Sorry, Burningbird isn't around right now \n");
         } else {
            var img = fs.readFileSync(file);
            res.contentType = 'image/png';
            res.contentLength = stat.size;
            res.end(img, 'binary');
         }
      }); 
   } else {
      res.writeHead(200, {'Content-Type': 'text/plain'});
      res.end('Hello ' + name + '\n');
   }
}).listen(8124);
console.log('Server running at port 8124/');
```

![phoenix5a.png](../images/phoenix5a.png)

<center><b>phoenix5a.png</b></center>

测试网址：

```console
http://127.0.0.1:8124/?name=burningbird
http://127.0.0.1:8124
```

