[toc]

### 1. 错误代码

**debugging.js**

```js
var http = require("http");

function process_request(req, res) {
	var body = 'Thanks for calling!\n';
	var content_lenght = body.lenggth;
	res.writeHead(200, {
		'Content-Lenght': content_lenght,
		'Content-Type': 'text/plain'
	});
	res.end(body);
}

var s = http.createServer(process_request);
s.listen(8080);
```

### 2. 调试代码

可以执行代码时添加 `debug` 参数来启动 Nodejs 的调试功能，例如：

```shell
$ node debug node.js
(node:42766) [DEP0068] DeprecationWarning: `node debug` is deprecated. Please use `node inspect` instead.
< Debugger listening on ws://127.0.0.1:9229/b7c7d0a9-19c9-4b58-af25-eaef55100053
< For help, see: https://nodejs.org/en/docs/inspector
< Debugger attached.
Break on start in file:///home/xiaotuan/%E6%A1%8C%E9%9D%A2/node.js:1
> 1 var http = require("http");
  2 
  3 function process_request(req, res) {
```

### 3. 调试命令

Node 调试器中有一些关键的命令可供使用：

+ cont —— 继续执行。
+ next —— 跳到下一个语句。
+ step —— 进入当前执行函数中的语句（如果是函数的话；否则，跳过）。
+ out —— 跳出当前执行函数。
+ backtrace —— 显示当前调用执行帧或调用栈。
+ repl —— 启动 Node REPL，允许查看变量值和执行代码。
+ watch(expr) —— 向观察列表中添加表达式，这样调试器中进入函数者移动时会显示出来。
+ list(n) —— 列出调试器中当前停止行的前面和后面的 n 行代码。
+ setBreakpoint(n) —— 在 n 行代码处设置断点。

