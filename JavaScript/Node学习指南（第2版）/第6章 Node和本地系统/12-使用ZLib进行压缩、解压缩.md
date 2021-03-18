

### 6.6　使用ZLib进行压缩/解压缩

ZLib模块为我们提供了压缩/解压缩的功能。它也是基于转换流的，当你看到Node文档中关于压缩文件的例子时，就会明白了。我会对示例稍作修改，从而可以操作大文件。

```python
var zlib = require('zlib');
var fs = require('fs');
var gzip = zlib.createGzip();
var inp = fs.createReadStream('test.png');
var out = fs.createWriteStream('test.png.gz');
inp.pipe(gzip).pipe(out);
```

输入流跟输出流通过中间的gzip压缩器直接连接起来，进行内容转换——在本例中压缩的是PNG文件。

Zlib为我们使用 `zlib` 或 `deflate` 压缩提供了支持， `deflate` 是一个更加复杂、可控的压缩算法。要注意， `deflate和zlib` 不一样，在 `zlib` 中可以用 `gunzip` （或 `unzip` ）命令来解压文件，在 `deflate` 中却不能这样做。你必须使用Node或一些其他功能来解压缩用 `deflate` 压缩的文件。

为了演示压缩文件和解压文件这两个功能，我们创建两个命令行工具： `compress` 和 `uncompress` 。第一个工具会使用 `gzip` 或 `deflate` 其中一个来压缩文件。由于有不同的参数，所以还会使用Commander模块来处理命令行参数：

```python
var zlib = require('zlib');
var program = require('commander');
var fs = require('fs');
program
   .version ('0.0.1')
   .option ('-s, --source [file name]', 'Source File Name')
   .option ('-f, --file [file name]', 'Destination File name')
   .option ('-t, --type <mode>', /^(gzip|deflate)$/i)
   .parse(process.argv);
var compress;
if (program.type == 'deflate')
   compress = zlib.createDeflate();
else
   compress = zlib.createGzip();
var inp = fs.createReadStream(program.source);
var out = fs.createWriteStream(program.file);
inp.pipe(compress).pipe(out);
```

这是一个既有意思又很好用的工具程序（尤其在Windows环境中，因为Windows系统原生不支持这种类型的压缩功能），但压缩技术更广泛的使用场景却是在Web请求中（Web request）。Node文档中包含了一些使用Zlib来处理Web请求的例子。同时也有一些使用 `Request` 模块和 `http.request()` 函数获取压缩文件的例子（在第5章中介绍过）。

这里我们不演示如何下载压缩文件，而是演示如何将压缩后的文件上传到服务器，然后在服务器端将其解压。我会调整例5-1和例5-2中的服务器和客户端应用程序，修改代码以压缩大型PNG文件，并通过HTTP请求发送压缩后的文件，然后让服务器解压并保存文件。

服务器端的代码如例6-5所示。需要注意的是，发送的数据会以数据块数组的格式被接收，最后使用 `buffer.concat()` 来合成一个新的缓冲器。因为这里处理的是一个缓冲器而不是一个流，所以不能使用 `pipe()` 函数。不过，我会使用 `zlib` 中一个很便捷的函数 `zlib.unzip` ，需要给它传入缓冲器和一个回调函数。回调函数具有两个参数—— `error` 和 `result` 。这里的 `result` 也是一个缓冲器，它会被  `write()` 函数写入一个新创建的可写流。为了确保同名文件不会被覆盖，我给文件名加上了时间戳。

**例6-5　创建一个Web服务器来接收压缩后的数据并将其解压到一个文件中**

```python
var http = require('http');
var zlib = require('zlib');
var fs = require('fs');
var server = http.createServer().listen(8124);
server.on('request', function(request,response) {
   if (request.method == 'POST') {
      var chunks = [];
      request.on('data', function(chunk) {
         chunks.push(chunk);
      }); 
      request.on('end', function() {
         var buf = Buffer.concat(chunks);
         zlib.unzip(buf, function(err, result) {
            if (err) {
               response.writeHead(500);
               response.end();
               return console.log('error ' + err);
            }
            var timestamp = Date.now();
            var filename = './done' + timestamp + '.png';
            fs.createWriteStream(filename).write(result);
         }); 
         response.writeHead(200, {'Content-Type': 'text/plain'});
         response.end('Received and undecompressed file\n');
      });
   } 
}); 
console.log('server listening on 8214');
```

客户端代码（如例6-6所示）的关键在于，确保头中给出了合适的 `Content- Encoding` ，应该是 `'gzip,deflate'` 。 `Content-Type` 也要相应地修改成 `application/javascript` 。

**例6-6　压缩文件并将其传入Web请求的客户端**

```python
var http = require('http');
var fs = require('fs');
var zlib = require('zlib');
var gzip = zlib.createGzip();
var options = {
  hostname: 'localhost',
  port: 8124,
  method: 'POST',
  headers: {
    'Content-Type': 'application/javascript',
    'Content-Encoding': 'gzip,deflate'
  }
}; 
var req = http.request(options, function(res) {
  res.setEncoding('utf8');
  var data = '';
  res.on('data', function (chunk) {
      data+=chunk;
  });
  res.on('end', function() {
    console.log(data)
  }) 
}); 
req.on('error', function(e) {
  console.log('problem with request: ' + e.message);
}); 
// stream gzipped file to server
var readable = fs.createReadStream('./test.png');
readable.pipe(gzip).pipe(req);
```

客户端打开要压缩的文件，然后将其传入Zlib压缩转换流，压缩后的结果被传入Web请求（一个可写流）。因为在这段代码中我们只是处理流，所以可以使用之前用过的 `pipe()` 功能。但不能在服务器中使用管道，因为在服务器中数据将以缓存块的形式传输。

在内存中缓存文件可能导致性能问题，所以另一种方式是保存压缩文件，解压它，然后删除那个临时的压缩文件。这个就作为读者课后的练习吧。

