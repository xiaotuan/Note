

### 8.1.1　child_process.exec和child_process.execFile

除了创建一个子进程外，你还可以用 `child_process.exec()` 和 `child_ process.execFile()` 来执行命令。

`c``hild_process.exec()` 方法和 `child_process.spawn()` 方法很像，只不过 `spawn()` 会在程序运行之后返回一个流，如例8-1所示。而 `child_process.exec()` 函数则像 `child_process.execFile()` 一样，将结果缓存起来。 `exec()` 会启动一个新的shell来运行进程，而 `child_process.execFile()` 会直接运行进程。这使得 `child_process.execFile()` 比设置了shell参数的 `child_process.spawn()` 和 `child_process.exec()` 都更高效。

`child_process.exec()` 的第一个参数是需要执行命令，而 `child_process.execFile()` 的第一个参数是需要运行的文件的路径。第二个和第三个参数则是一样的，分别是命令的参数和回调函数。回调函数接收3个参数： `error` 、 `stdout` 和 `stderr` 。如果没有出现错误，数据会被缓存到 `stdout` 中。

如果可执行文件的内容如下：

```python
#!/usr/bin/node
console.log(global);
```

那么下面的程序会打印出缓存的结果：

```python
var execfile = require('child_process').execFile,
    child;
child = execfile('./app', function(error, stdout, stderr) {
  if (error == null) {
    console.log('stdout: ' + stdout);
  }
});
```

使用 `child_process.exec()` 也可以完成一样的任务：

```python
var exec = require('child_process').exec, 
    child; 
child = exec('./app', function(error, stdout, stderr) {
   if (error) return console.error(error);
   console.log('stdout: ' + stdout);
});
```

区别在于 `child_process.exec()` 会产生一个shell，而 `child_process.execFile()` 不会。

`child_process.exec()` 函数接收3个参数：要执行的命令、一个 `options` 对象和一个回调函数。 `options` 对象中包含好几个参数，如 `encoding` 、进程的 `uid` （用户 `id` ）和 `gid` （组 `id` ）。在第6章中，我创建了一个用来复制PNG文件并添加华丽特效的程序。程序使用（创建）了一个子进程来访问ImageMagick——一个强大的命令行图形工具。如果使用 `child_process.exec()` 来运行这个程序，可以使用下面的代码（其中已经集成了一个命令行参数）：

```python
var exec = require('child_process').exec,
    child;
child = exec('./polaroid -s phoenix5a.png -f phoenixpolaroid.png',
         {cwd: 'snaps'}, function(error, stdout, stderr) {
               if (error) return console.error(error);
               console.log('stdout: ' + stdout);
});
```

运行 `child_process.execFile()` 需要一个额外的参数：一个传入应用程序的命令行参数的数组。同样的程序如果使用这个函数，就要这样写：

```python
var execfile = require('child_process').execFile,
    child;
child = execfile('./snapshot',
                 ['-s', 'phoenix5a.png', '-f', 'phoenixpolaroid.png'],
                  {cwd: 'snaps'}, function(error, stdout, stderr) {
   if (error) return console.error(error);
   console.log('stdout: ' + stdout);
});
```

请注意，命令行参数被分离为数组中的不同元素，按照一个参数、一个值的顺序排列。

由于 `child_process.execFile()` 并没有创建新的shell，所以在某些情况下就无法使用。Node文档提醒我们，不能在I/O重定向和通过使用路径扩展进行文件通配（通过正则表达式或通配符）时使用这个函数。但是，如果你在尝试交互地运行一个子进程（或者程序），那么你应该使用 `child_process.execFile()` 而不是 `child_process.exec()` 。下面的代码（由来自Node基金会的Colin Ihrig编写）很好地展示了这一点：

```python
'use strict';
const cp = require('child_process');
const child = cp.execFile('node', ['-i'], (err, stdout, stderr) => {
  console.log(stdout);
});
child.stdin.write('process.versions;\n');
child.stdin.end();
```

这段程序会启动一个交互式的Node会话，然后请求进程版本，最后结束输入。

这两个函数都有各自的同步版本—— `child_process.execSync()` 和 `child_ process. execFileSync()` 。

