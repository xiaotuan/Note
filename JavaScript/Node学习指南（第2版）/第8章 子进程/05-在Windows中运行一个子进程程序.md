

### 8.2　在Windows中运行一个子进程程序

我之前曾经说过，UNIX系统中生成子进程的命令无法在Windows中使用，反之亦然。我知道这是常识，但也不是所有人都知道（不像浏览器中的JavaScript那样人尽皆知），那就是，Node程序在不同的环境中会有不同的行为。

除了不同的操作系统和命令以外，为了在Windows中运行程序，要么使用能生成新shell的 `child_process.exec()` ，要么使用新版本的 `child_process.spawn()` 并传入 `shell` 参数。不然的话，就只能通过使用Windows的命令行工具 `cmd.exe` 来调用你想要使用的命令了。

下面的例子展示了如何在调用 `child_process.spawn()` 时使用 `shell` 参数，以在Windows上面打印出一个目录的内容。

```python
var spawn = require('child_process').spawn,
    pwd = spawn('echo', ['%cd%'], {shell: true});
pwd.stdout.on('data', function (data) {
  console.log('stdout: ' + data);
}); 
pwd.stderr.on('data', function (data) {
  console.log('stderr: ' + data);
}); 
pwd.on('close', function (code) {
  console.log('child process exited with code ' + code);
});
```

`echo` 命令会打印出Windows中 `cd` 命令的运行结果，也就是当前目录。如果没有设置 `shell` 参数的话，这个程序就会报错。

类似的结果使用 `child_process.exec()` 也可以得到。但是请注意，我不需要使用 `child_process.exec()` 来调用 `echo` 命令，因为输出已经被后面的函数缓存起来了：

```python
var exec = require('child_process').exec,
    pwd = exec('cd');
pwd.stdout.on('data', function (data) {
  console.log('stdout: ' + data);
}); 
pwd.stderr.on('data', function (data) {
  console.log('stderr: ' + data);
});
pwd.on('close', function (code) {
  console.log('child process exited with code ' + code);
});
```

例8-2展示了第三种用法：使用 `cmd` 命令（也就是Windows中的 `cmd.exe` ）来运行Windows命令。参数中的任何内容都会在shell命令中执行。在该程序中，我们使用了Windows的 `cmd.exe` 来调用一个列出目录所有内容的命令，然后执行结果被 `data` 事件的处理函数打印到控制台。

**例8-2　在Windows中运行一个子进程程序**

```python
var cmd = require('child_process').spawn('cmd', ['/c', 'dir\n']);
cmd.stdout.on('data', function (data) {
    console.log('stdout: ' + data);
}); 
cmd.stderr.on('data', function (data) {
    console.log('stderr: ' + data);
}); 
cmd.on('exit', function (code) {
    console.log('child process exited with code ' + code);
});
```

作为第一个参数被传给 `cmd.exe` 的是 `/c` 参数，这个参数的作用是告诉 `cmd.exe` ，执行完命令之后就结束进程。没有这个参数的话，我们的程序根本无法运行。要特别说明的是，千万不要给 `cmd.exe` 传 `/K` 参数，因为这个参数会使 `cmd.exe` 一直保持运行，然后你的程序也就无法结束了。

下面的代码使用 `child_process.exec()` 实现了同样的功能：

```python
var cmd = require('child_process').exec('dir');
```

我们可以使用 `child_process.execFile()` 来运行一个cmd或者bat文件，就像我们在类UNIX系统中所做的那样。比如我们要运行下面的bat文件（my.bat）：

```python
@echo off
REM Next command generates a list of program files
Dir
```

下面的程序就可以运行这个批处理文件：

```python
var execfile = require('child_process').execFile,
    child;
child = execfile('my.bat', function(error, stdout, stderr) {
  if (error == null) {
    console.log('stdout: ' + stdout);
  }
});
```



