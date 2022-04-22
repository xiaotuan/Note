[toc]

### 1. Web 服务器代码

下面是一个简单的 Web 服务器代码：

**web.js**

```js
var http = require("http");

function process_request(req, res) {
	var body = 'Thanks for calling!\n';
	var content_lenght = body.length;
	res.writeHead(200, {
		'Content-Lenght': content_lenght,
		'Content-Type': 'text/plain'
	});
	res.end(body);
}

var s = http.createServer(process_request);
s.listen(8080);
```

### 2. 启动 Web 服务

通过如下命令启动 Web 服务：

```shell
node web.js
```

### 3. 查看 Web 页面

1. 然后在浏览器中的地址栏输入：<http://localhost:8080> ，按 <kbd>Enter</kbd> 键就看到网页上显示 "Thanks for calling!" 文字了。

2. 也可以在 Linux / Mac 系统终端上输入如下命令查看：

   ```shell
   curl -i http://localhost:8080
   ```

### 4. 停止 Web 服务

在终端上按下 <kbd>Ctrl</kbd> + <kbd>C</kbd> 组合键即可停止 Web 服务。

