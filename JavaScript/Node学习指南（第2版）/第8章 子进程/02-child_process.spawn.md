

### 8.1　child_process.spawn

有4种方法可以用来创建子进程。最常见的是用 `spawn` 方法。这种方法可以在新的进程中启动命令，同时传入任何参数。主程序和子进程之间会建立一个管道，用来传递 `stdin` 、 `stdout` 和 `stderr` 的内容。

接下来，我们创建一个子进程来调用UNIX的 `pwd` 命令来打印当前目录。这个命令没有参数：

```python
var spawn = require('child_process').spawn,
    pwd = spawn('pwd');
pwd.stdout.on('data', function (data) {
  console.log('stdout: ' + data);
}); 
pwd.stderr.on('data', function (data) {
  console.error('stderr: ' + data);
}); 
pwd.on('close', function (code) {
  console.log('child process exited with code ' + code);
});
```

注意在子进程的 `stdout` 和 `stderr` 上面捕捉到的事件。如果没有错误，那么命令输出的任何内容都会发送到子进程的 `stdout` 中，并在进程上触发一个 `data` 事件。如果有错误，比如我们传入了一个无效参数：

```python
var spawn = require('child_process').spawn,
    pwd = spawn('pwd', ['-g']);
```

然后，错误会被发送到 `stderr` ，它会把错误打印在控制台中：

```python
stderr: pwd: invalid option -- 'g' 
Try `pwd --help' for more information.
child process exited with code 1
```

接着进程退出并返回代码 `1` ，这表示有错误发生。退出代码会因操作系统和错误的不同而不同。如果没有错误，子进程退出后会返回 `0` 。

前面的代码演示了如何将 `stdout` 和 `stderr` 的输出发送给子进程，那 `stdin` 呢？Node文档中关于子进程的部分有一个例子中提到将数据直接传入 `stdin` 。它用于模拟UNIX管道（|），也就是将一个命令的结果立即指向另一个命令的输入。我对这个例子进行了调整，以演示UNIX管道的功能——让它能够查看当前目录下的所有子目录，并找到一个文件名中具有特定单词（在本例中，这个单词是test）的文件：

```python
find . -ls | grep test
```

例8-1使用子进程实现了这个功能。注意第一个执行了 `find` 操作的命令，它会接收两个参数，而第二个命令只有一个参数：用户通过 `stdin` 输入的单词。同时要注意， `grep` 子进程中的 `stdout` 是通过 `setEncoding` 来改变编码格式的。否则，在打印数据时，程序将会以缓冲器的格式来打印。

**例8-1　使用子进程在子目录中查找符合给定搜索条件（“test”）的文件**

```python
var spawn = require('child_process').spawn,
    find = spawn('find',['.','-ls']),
    grep = spawn('grep',['test']);
grep.stdout.setEncoding('utf8');
// pipe find output to grep input
find.stdout.pipe(grep.stdin);
// now run grep and output results
grep.stdout.on('data', function (data) {
  console.log(data);
});
// error handling for both
find.stderr.on('data', function (data) {
  console.log('grep stderr: ' + data);
});
grep.stderr.on('data', function (data) {
  console.log('grep stderr: ' + data);
}); 
// and exit handling for both
find.on('close', function (code) {
  if (code !== 0) {
    console.log('find process exited with code ' + code);
  }
}); 
grep.on('exit', function (code) {
  if (code !== 0) {
    console.log('grep process exited with code ' + code);
  }
});
```

运行这个程序后，你会得到一个文件列表，它包含所有当前目录或者子目录中文件名含有test的文件。

Node文档中有一条警告信息，说有一些程序会在内部使用行缓存（lire-buffered）I/O。行缓存会导致发送到程序的数据无法被立即使用。这对我们则意味着，对于某些子进程，数据在处理之前会被缓存在块中。 `grep` 子进程就是其中的一种。

在当前这个例子中， `find` 进程的输出并不多，所以 `grep` 进程的输入并没有达到一个块的大小（通常来说是4096，不过也会因操作系统和设置的不同而变化）。

> <img class="my_markdown" src="../images/87.png" style="zoom:50%;" />
> **更多关于stdio缓存的信息**
> 想深入了解缓存，可以看看How to fix stdio buffering以及它的姐妹篇Buffering in standard streams。

我们可以通过在 `grep` 中设置 `--line-buffered` 来关闭行缓存。在下面的程序中，我们使用进程状态命令（ `ps` ）来检测运行中的进程，然后搜索apache2的进程——因为 `grep` 中的行缓存已经关闭了，所以数据会被立即打印出来，而不是等到缓冲器满才打印。

```python
var spawn = require('child_process').spawn,
    ps    = spawn('ps', ['ax']),
    grep  = spawn('grep', ['--line-buffered', 'apache2']);
ps.stdout.pipe(grep.stdin);
ps.stderr.on('data', function (data) {
  console.log('ps stderr: ' + data);
}); 
ps.on('close', function (code) {
  if (code !== 0) {
    console.log('ps process exited with code ' + code);
  }
}); 
grep.stdout.on('data', function (data) {
  console.log('' + data);
}); 
grep.stderr.on('data', function (data) {
  console.log('grep stderr: ' + data);
}); 
grep.on('close', function (code) {
  if (code !== 0) {
    console.log('grep process exited with code ' + code);
  }
});
```

现在输出就不会被缓存，而是立即打印。

默认情况下 `child_process.spawn()` 不会在shell中执行命令。不过，在Node5.7.0及之后的版本中，你可以通过指定 `shell` 参数来让子进程为这个进程生成一个shell。稍后在8.2节中，我会演示如何在为Windows设计的Node应用中使用它。还有一些其他设置项，其中包括（下面不是全部的设置项，你可以在Node文档中查看完整的、最新的列表）：

+ `cwd` ，改变工作目录；
+ `env` ，含有环境变量键值对的数组；
+ `detached` ，用于使子程序独立于父程序运行；
+ `stdio` ，用于指定子进程的 `stdio` 参数数组。

`detached` 参数和 `shell` 一样，在Windows和非Windows环境中有些差别。同样的，我们会在8.2节中讲解。

`child_process.spawnSync()` 是这个函数的同步版本。

