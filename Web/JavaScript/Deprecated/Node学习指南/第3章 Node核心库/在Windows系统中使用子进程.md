**示例3-10 在 Windows 系统中运行一个子进程**

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

传递给 cmd.exe 的第一个参数是 '/c'，它用来指示在 cmd.exe 执行完命令后就立即终止并退出。如果没有这个参数，这段 Node 程序将不能正常工作。当然，我们更不想传送参数 '/k' 给 cmd.exe，因为它会告诉 cmd.exe 执行命令并保持，这样你的应用程序将不会终止。

