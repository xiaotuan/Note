可以通过如下代码保存 `POST` 请求上传的文件：

```js
var http = require("http")
var fs = require('fs')
var querystring = require('querystring')

var server = http.createServer(function(req, res) {
    for (var key in req.headers) {
        console.log("Headers=>key: " + key + ", value: " + req.headers[key]);
    }
    if ("POST" == req.method) {
        if (req.headers['content-type'].indexOf('multipart/form-data') !== -1) {
            req.setEncoding('binary')
            var body = '';  // 文件数据
            var fileName = '';  // 文件名
            // 边界字符串
            var boundary = req.headers['content-type'].split('; ')[1].replace('boundary=','')
            console.log("File boundary: " + boundary)
            req.on('data', chunk => {
                body += chunk
            })
            req.on('end', () => {
                var file = querystring.parse(body, '\r\n', ':')
                var contentType = file['Content-Type']
                console.log('File content type: ' + contentType)
                console.log('File content disposition: ' + file['Content-Disposition'])
                // 获取文件名
                var fileInfo = file['Content-Disposition'].split('; ')
                for (value in fileInfo) {
                    if (fileInfo[value].indexOf('filename=') != -1) {
                        fileName = fileInfo[value].substring(10, fileInfo[value].length - 1)
                        if (fileName.indexOf('\\') != -1) {
                            fileName = fileName.substring(fileName.lastIndexOf('\\') + 1)
                        }
                    }
                }
                console.log("File name: " + fileName)
                //获取文件二进制数据开始位置，即contentType的结尾
                var entireData = body.toString();
                var upperBoundary = entireData.indexOf(contentType) + contentType.length;
                var shorterData = entireData.substring(upperBoundary);
                
                // 替换开始位置的空格
                var binaryDataAlmost = shorterData.replace(/^\s\s*/, '').replace(/\s\s*$/, '');
                
                // 去除数据末尾的额外数据，即: "--"+ boundary + "--"
                var binaryData = binaryDataAlmost.substring(0, binaryDataAlmost.indexOf('--'+boundary+'--'));
                
                // 保存文件
                fs.writeFile(fileName, binaryData, 'binary', function(err) {
                    res.writeHead(200, {'Content-Type':'text/plain'})
                	res.end('文件上传完成');
                });

            })
        }
    }
});

server.listen(8124, function() {
    console.log('Server running at port 8124')
})
```

