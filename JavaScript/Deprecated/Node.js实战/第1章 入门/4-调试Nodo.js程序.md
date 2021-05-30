**debugging.js**

```js
var http = require("http")

function process_request(req, res) {
  var body = 'Thanks for calling!\n'
  var content_length = body.lenggth
  res.writeHead(200, {
    'Content-Length': content_length,
    'Content-Type': 'text/plain'
  })
  res.end(body)
}

var s = http.createServer(process_request)
s.listen(8080)
```

再次运行该程序：

```shell
$ node debugging.js
```

当尝试连接到 <http://localhost:8080> 的时候，可能会得到：

```shell
$ curl -i localhost:8080
curl: (52) Empty reply from server
```

`Node.js` 内置了一个调试器。如果想使用，只需要在启动的时候将 debug 参数添加到程序名称的前面即可：

```shell
node inspect debugging.js
```

> 警告：`node debug debugging.js` 命令已经过时了。

可以得到如下所示的信息：

```console
$ node inspect debugging.js 
< Debugger listening on ws://127.0.0.1:9229/0623e9dd-0251-4df3-af69-ba9613bf55fb
< For help, see: https://nodejs.org/en/docs/inspector
< Debugger attached.
Break on start in debugging.js:1
> 1 var http = require("http")
  2 
  3 function process_request(req, res) {
debug> 
```

`Node` 调试器中有一些关键的命令可供使用：

+ `cont` —— 继续执行
+ `next` —— 跳到下一个语句
+ `step` —— 进入当前执行函数中的语句（如果是函数的话；否则，跳过）
+ `out` —— 跳出当前执行函数
+ `backtrace` —— 显示当前调用执行帧或调用栈
+ `repl` —— 启动 Node REPL，允许查看变量值和执行代码
+ `watch(expr)` —— 向观察列表中添加表达式，这样在调试器中进入函数或者移动时会显示出来。
+ `list(n)` —— 列出调试器中当前停止行的前面和后面的 n 行代码。
+ `setBreakpoint(n)` —— 在第 n 行设置断点。

> 提示：退出调试环境可以输入如下命令：
>
> ```shell
> debug> .exit
> ```

