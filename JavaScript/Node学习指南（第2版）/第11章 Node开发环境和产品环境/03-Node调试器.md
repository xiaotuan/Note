

### 11.1.1　Node调试器

只要可以，我总会使用原生的实现，而不是用第三方工具。幸运的是，对于调试需求，Node提供了内置的调试支持。它并不复杂，且十分实用。

你可以使用 `debugger` 命令直接向代码中插入断点：

```python
for (var i = 0; i <= test; i++) {
   debugger;
   second+=i; 
}
```

启动程序时加上 `debug` 参数，就可以开始调试程序了：

```python
node debug application
```

我创建了一个嵌入了两个 `debugger` 断点的程序，来演示调试器如何使用：

```python
var fs = require('fs');
var concat = require('./external.js').concatArray;
var test = 10;
var second = 'test';
for (var i = 0; i <= test; i++) {
 debugger; 
 second+=i; 
} 
setTimeout(function() {
 debugger; 
 test = 1000; 
 console.log(second);
}, 1000);
fs.readFile('./log.txt', 'utf8', function (err,data) {
 if (err) {
 return console.log(err);
 }
 var arry = ['apple','orange','strawberry'];
 var arry2 = concat(data,arry);
 console.log(arry2);
});
```

使用下面的命令启动程序：

```python
node debug debugtest
```

如果你用 `--debug` 命令行参数来启动Node程序，那么也可以通过 `pid` 连接到这个进程，进行调试（debug）：

```python
node debug -p 3383
```

当然也可以通过URI连接到运行中的进程进行调试：

```python
node debug http://localhost:3000
```

调试器运行起来之后，程序会停在第一行，并且列出最前面的几行代码：

```python
< Debugger listening on port 5858
debug> . ok
break in debugtest.js:1
> 1 var fs = require('fs');
  2 var concat = require('./external.js').concatArray;
  3
```

你可以使用 `list` 命令来列出上下文中的源代码。比如， `list(10)` 会列出前面10行代码和后面10行代码。在本例中，输入 `list(25)` 则会将程序中的所有代码以及行号都打印出来。你可以使用 `setBreakpoint` 命令来添加额外的断点，也可以使用它的快捷命令： `sb` 。让我们给测试程序的第19行设置一个断点，也就是在 `fs.readFile()` 方法的回调函数中设置断点。同时我们直接在自定义模块的第三行设置一个断点：

```python
debug> sb(19)
debug> sb('external.js',3)
```

你会看到一个提示说external.js尚未加载，但是这并不影响调试功能。

你也可以使用 `watch('expression')` 命令，在变量或者表达式上设置监视器。我们会监视 `test` 变量和 `second` 变量，以及 `data` 参数和 `arry2` 数组：

```python
debug> watch('test');
debug> watch('second');
debug> watch('data');
debug> watch('arry2');
```

现在，万事俱备，只欠“调试”了。输入 `cont` 或者 `c` ，可以让程序执行到第一个断点。在输出信息中，可以看到程序已经运行到第一个断点，也可以看到所监视的那4个对象的值。其中两个—— `test` 和 `second` ——已经有了实际的值，而另外两个的值是 `<error>` 。这是因为程序目前并没有进入这个参数（ `data` ）和变量（ `arry2` ）所定义的函数的作用域中。忽略这个错误，继续调试。

```python
debug> c
break in debugtest.js:8
Watchers:
  0: test = 10
  1: second = "test"
  2: data = "<error>"
  3: arry2 = "<error>"
  6
  7 for (var i = 0; i <= test; i++) {
> 8 debugger; 
  9 second+=i; 
 10 } 
```

还有一些不常用的命令，你可以在运行到下一个断点之前尝试一下。 `scripts` 命令会列出已经被加载的脚本：

```python
debug> scripts
* 57: debugtest.js
  58: external.js
debug>
```

而 `version` 命令会打印出V8这个版本号。下面我们再次输入 `c` 来运行至下一个断点：

```python
debug> c
break in debugtest.js:8
Watchers:
  0: test = 10
  1: second = "test0"
  2: data = "<error>"
  3: arry2 = "<error>"
  6 
  7 for (var i = 0; i <= test; i++) {
> 8    debugger;
  9    second+=i;
 10 }
```

请注意， `second` 变量的值已经发生了变化。这是因为 `debugger` 所在的 `for` 循环中， `second` 的值被改变了。输入几次 `c` 命令，循环就会执行几次，同时 `second` 变量的值发生了连续的变化。不幸的是，用 `debugger` 语句生成的断点无法删除，但是使用 `setBreakpoint` 或者 `sb` 生成的断点是可以删除的。调用 `clearBreakpoint` 或者 `cb` 时，需要提供断点的脚本名称和行号。

```python
cb('debugtest.js',19)
```

监视器也可以通过 `unwatch` 来关闭：

```python
debug> unwatch('second')
```

直接调用 `sb` 而不输入任何参数，这会在当前行设置断点：

```python
debug> sb();
```

在程序中，调试器会一直运行程序，直到遇到我们在 `fs.readFile( )` 的回调函数中设置的断点。这时你会发现， `data` 参数的值发生了变化：

```python
debug> c
break in debugtest.js:19
Watchers:
  0: test = 10
  1: second = "test012345678910"
  2: data = "test"
  3: arry2 = undefined
 17 
 18 fs.readFile('./log.txt', 'utf8', function (err,data) {
>19   if (err) {
 20     return console.log(err)
21   }
```

此时 `arry2` 的值不再是一个错误，而是 `undefined` 。

我们需要一行一行地运行代码，所以就不能使用 `c` 命令了，而需要使用 `next` 或者 `n` 命令。当执行到第23行时，调试器会加载外部的模块，并且停留在第三行，因为我们之前对这个模块设置了断点：

```python
debug> n
break in external.js:3
Watchers:
  0: test = "<error>"
  1: second = "<error>"
  2: data = "<error>"
  3: arry2 = "<error>"
  1
  2 var concatArray = function(str, arry) {
> 3   return arry.map(function(element) {
  4        return str + ' ' + element;
  5   });
```

我们可以直接跳过函数的执行，来到程序的第23行，也可以使用 `stop` 或者 `s` 命令来进入模块函数的内部：

```python
debug> s
break in external.js:3
Watchers:
  0: test = "<error>"
  1: second = "<error>"
  2: arry2 = "<error>"
  3: data = "<error>"
  1 
  2 var concatArray = function(str, arry) {
> 3   return arry.map(function(element) {
  4        return str + ‘’ + element;
  5   });
```

请注意，所有被监视的变量，现在都显示了一个错误信息。此时，我们已经跳出了父程序的执行上下文。在函数或者外部模块执行期间重新添加监视器，就可以避免这样的错误出现。或者，如果同一个变量在程序运行上下文和外部模块中都有定义，那么也不会出现这个错误。

> <img class="my_markdown" src="../images/106.png" style="zoom:50%;" />
> **继续执行命令的bug**
> 如果你在程序执行结束之后输入 `c` 或者 `cont` ，调试器就会卡住，而且无法恢复。这是一个已知的bug。

`backtrace` 或者 `bt` 命令提供了一个当前执行上下文的回溯（backtrace）。当前调试状态下的返回值会被显示为代码块：

```python
debug> bt
#0 concatArray external.js:3:3
#1 debugtest.js:23:15
```

我们看到两行内容，第一行是我们在加载的模块中所处的位置，第二行是我们目前在程序中所处的位置。

使用 `out` 或者 `o` 命令，可以帮助我们跳过外部函数，或者回到程序主文件。这个命令会在函数执行过程中帮助你回到主程序中（不论这个函数是在主文件中还是在一个外部模块中）。

Node调试器是基于REPL的，我们也确实可以在调试器中使用 `repl` 来调出REPL。如果要停止正在执行脚本，可以使用 `kill` 命令，而使用 `restart` 命令则可以重启脚本。但是要注意，重启脚本会清空所有的断点和监视器。

既然调试器是运行是在REPL中的，那么按下Ctrl-C键或者输入 `.exit` 都可以直接终止程序的运行。

