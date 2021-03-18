

### 6.7　管道和ReadLine模块

我们在第5章和本章中都用到了管道，最简单的管道示例就是打开一个REPL会话，然后输出以下内容：

```python
> process.stdin.resume();
> process.stdin.pipe(process.stdout);
```

你在这里输入的任何内容都会被打印出来。如果想要保持输出流为打开状态，从而输入连续的数据，可以输出数据时，加上 `{end: false}` 参数：

```python
process.stdin.pipe(process.stdout, { end : false });
```

REPL中逐行处理的功能其实是用一个核心模块： `Readline` 模块来实现的，这也是本章中我们接触到的最后一个核心模块。只要引入 `Readline` ，Node就会开启一个不会自动终止的线程，该线程用来进行数据通信。引入 `Readline` 模块的代码如下所示：

```python
var readline = require('readline');
```

要注意的是，一旦你引入了这个模块，Node程序就永远不会终止，直到你关闭交互界面。

Node站点文档包含了一些如何开始和结束 `Readline` 界面的例子，我在例6-7中对其进行了一些调整。应用程序一经运行就会开始提问，然后输出答案。它还会监听所有“命令”，也就是所有以\n（换行符）结束的行。如果监听到 `.leave` 命令，就会结束应用程序；否则，它只是重复该命令，然后继续提示用户。Ctrl-C或Ctrl-D组合键也可以终止应用程序，尽管这样做会略显粗暴。

**例6-7　使用Readline来创建一个简单的、命令驱动的用户界面**

```python
var readline = require('readline');
// create a new interface
var rl = readline.createInterface(process.stdin, process.stdout);
// ask question
rl.question(">>What is the meaning of life?  ", function(answer) {
   console.log("About the meaning of life, you said " + answer);
   rl.setPrompt(">> ");
   rl.prompt();
}); 
// function to close interface
function closeInterface() {
   rl.close(); 
   console.log('Leaving Readline');
}
// listen for .leave
rl.on('line', function(cmd) {
   if (cmd.trim() == '.leave') {
      closeInterface();
      return;
   }
   console.log("repeating command: " + cmd);
   rl.prompt();
}); 
rl.on('close', function() {
    closeInterface();
});
```

下面是一个会话示例：

```python
>>What is the meaning of life?  ===
About the meaning of life, you said ===
>>This could be a command
repeating command: This could be a command
>>We could add eval in here and actually run this thing
repeating command: We could add eval in here and actually run this thing
>>And now you know where REPL comes from
repeating command: And now you know where REPL comes from
>>And that using rlwrap replaces this Readline functionality
repeating command: And that using rlwrap replaces this Readline functionality
>>Time to go
repeating command: Time to go
>>.leave
Leaving Readline...
Leaving Readline...
```

是不是看着很眼熟？还记得第4章中我们用 `rlwrap` 重写REPL的命令行功能吗？我们用下面的命令行来激活它：

```python
env NODE_NO_READLINE=1 rlwrap node
```

现在我们知道这个参数做了什么事情——它告诉REPL不要使用Node的 `Readline` 模块进行命令行处理，而是使用 `rlwrap` 。



