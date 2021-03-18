[toc]

### 4.3.3　自定义REPL

Node提供了一个可以创建自定义REPL的API。在创建之前，需要引入REPL模块（ `repl` ）：

```python
var repl = require("repl");
```

为了创建一个新的REPL，我们在 `repl` 对象上调用 `start` 方法。语法如下：

```python
repl.start(options);
```

`options` 对象会接收一些参数，我想详细说明的是下面这些参数。

+ `prompt` ，默认是>。
+ `input` ，可读流，默认是 `process.stdin` 。
+ `output` ，可写流，默认是 `process.stdout` 。
+ `eval` ，默认是 `eval` 的异步封装。
+ `useGlobal` ，默认是 `false` ，表示使用一个新的上下文而非 `global` 对象。
+ `useColors` ，表示 `writer` 函数是否有颜色，默认值是REPL的 `terminal` 的颜色。
+ `ignoreUndefined` ，默认是 `false` ，不忽略 `undefined` 结果。
+ `terminal` ，将其设为 `true` 时， `stream` 被当成 `tty` （即来自 `terminal` 的输入）来处理，它只支持ANSI/VT100转义码。
+ `writer` ，计算每个命令并返回格式化后的结果，默认情况下会调用 `util. inspect` 。
+ `replMode` ，REPL运行时是用严格（strict）模式、默认（default）模式，还是混合（hybrid）模式。

> <img class="my_markdown" src="../images/58.png" style="zoom:50%;" />
> 从Node 5.8.0以后， `repl.start()` 就不再需要 `options` 对象了。

我发现REPL中 `undefined` 这样的表达式结果没有意义，所以定义了自己的REPL。同时我也重新定义了提示符，并将REPL设为严格模式，也就是说我输入的每一行都将在严格模式下执行。

```python
var repl = require('repl');
repl.start( {
  prompt: 'my repl> ',
  replMode: repl.REPL_MODE_STRICT,
  ignoreUndefined: true, 
});
```

用Node运行repl.js文件：

```python
node repl
```

接下来我就能使用自定义的REPL了，就像使用原生的REPL一样，除了提示符不同外，再也不用在第一个变量赋值后就看到烦人的 `undefined` 了。我们会得到一个非 `undefined` 的结果：

```python
my repl> let ct = 0;
my repl> ct++;
0
my repl> console.log(ct);
1
my repl> ++ct;
2
my repl> console.log(ct);
2
```

在我的代码中，除了我列出的属性之外，其他的全部使用默认值。对于 `options` 对象的属性，只要没有被列出，就会使用默认值。

可以将 `eval` 函数替换成自定义的REPL。唯一需要注意的是特殊格式：

```python
function eval(cmd, callback) {
   callback(null, result);
}
```

`input` 和 `output` 比较有意思。你可以同时运行多个版本的REPL，并同时从标准输入（默认方式）和套接字中获得 `input` 。Node.js官网上有REPL的文档，其中有一个使用REPL监听TCP套接字的例子，代码如下：

```python
var net = require("net"),
    repl = require("repl");
connections = 0;
repl.start({
  prompt: "node via stdin> ",
  input: process.stdin,
  output: process.stdout
}); 
net.createServer(function (socket) {
  connections += 1;
  repl.start({
    prompt: "node via UNIX socket> ",
    input: socket,
    output: socket
  }).on('exit', function() {
    socket.end();
  })
}).listen("/tmp/node-repl-sock");
net.createServer(function (socket) {
  connections += 1;
  repl.start({
    prompt: "node via TCP socket> ",
    input: socket,
    output: socket
  }).on('exit', function() {
    socket.end();
  });
}).listen(5001);
```

运行这个应用之后，你就可以在运行Node应用的地方看到标准输入提示符了。你也可以通过TCP访问REPL。我用PuTTY作为Telnet客户端来访问可以使用TCP的REPL，在某种程度上，它是可以实现的。它的缺点是，我必须先执行一次 `.clear` 命令，它没有格式化，另外也无法使用下划线来引用上一个表达式。我也试过用Windows Telnet客户端，结果更糟。但是，用Linux Telnet客户端却很顺利。

你可能已经猜到问题所在了，是Telnet客户端的设置。不过我并不打算深究这个问题，因为我不打算也不推荐在一个Telnet套接字中运行REPL，毕竟它没有足够的安全性。这就好像在客户端代码中使用 `eval()` ，却并不传入用户输入来运行程序（在套接字中运行REPL的安全性更差）。

你可以使用GNU Netcat来运行REPL并使用UNIX套接字进行通信：

```python
nc -U /tmp/node-repl-sock
```

你可以像使用 `stdin` 一样输入命令。但是，要注意的是，如果你在用TCP或者UNIX套接字，那么任何从 `console.log` 输出的内容都会打印到服务端，而不是客户端：

```python
console.log(someVariable); // actually printed out to server
```

我觉得对于应用程序来说，创建一个REPL来提前加载模块会更有用。在例4-1的应用中，REPL开始后， `Request` （一个强大的HTTP客户端）、 `Underscore` （工具类库），和 `Q` （promise管理）中的第三方模板会被加载并被赋值给属性 `context` 。

**例4-1　创建一个可以提前加载模块的自定义REPL**

```python
var repl = require('repl');
var context = repl.start({prompt: '>> ',
                          ignoreUndefined: true,
                          replMode: repl.REPL_MODE_STRICT}).context;
// preload in modules
context.request = require('request');
context.underscore = require('underscore');
context.q = require('q');
```

在Node中运行应用将会启动一个REPL命令行，我们可以在这里访问那些模块：

```python
>> request('http://blipdebit.com/phoenix5a.png')
.pipe(fs.createWriteStream('bird.png'))
```

Node的核心模块不需要专门引入，你可以直接通过模块名来访问这些模块。

如果你希望像Linux的可执行程序一样运行REPL应用，那么把下面这行代码加到应用的第一行：

```python
#!/usr/local/bin/node
```

将文件修改成可执行的形式，然后运行它：

```python
$ chmod u+x replcontext.js
$ ./replcontext.js
>>
```

