使用 Node 执行 Windows 命令代码如下所示：

```js
var cmd = require('child_process').spawn('cmd', ['/c', 'dir\n'])

cmd.stdout.on('data', function (data) {
   console.log('stdout: ' + data)
})

cmd.stderr.on('data', function (data) {
   console.log('stderr: ' + data)
})

cmd.on('exit', function (code) {
   console.log('child process exited with code ' + code)
}) 
```

> 注意：传递给 cmd.exe 的第一个参数是 '/c'，它用来指示在 cmd.exe 执行完命令后就立即终止并退出。