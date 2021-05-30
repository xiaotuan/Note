使用 Node 执行 Linux 命令代码如下所示：

```js
var spawn = require('child-process').spawn

var pwd = spawn('pwd')

pwd.stdout.on('data', function (data) {
  console.log('stdout: ' + data)
})

pwd.stderr.on('data', function (data) {
  console.log('stderr: ' + data)
})

pwd.on('exit', function (code) {
  console.log('child process exited with code ' + code)
})
```

实现类似 shell 管道命令的代码如下所示：

```js
var spawn = require('child-process').spawn
var find = spawn('find', ['.', '-ls'])
var grep = spawn('grep', ['test'])

grep.stdout.setEncoding('utf8')

// direct results of find to grep
find.stdout.on('data', function (data) {
  grep.stdin.write(data)
})

// now run grep and output results
grep.stdout.on('data', function (data) {
  console.log(data)
})

// error handling for both
find.stderr.on('data', function (data) {
  console.log('grep stderr: ' + data)
})

grep.stderr.on('data', function (data) {
  console.log('grep stderr: ' + data)
})
```

