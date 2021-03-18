[toc]

### 4.5.1　控制台消息类型、Console类以及阻塞

在本书的大多数例子中我们都用了 `console.log()` ，因为我们在探索Node的时候只对输出感兴趣。这个函数会把结果输出到 `stdout` ，通常是终端。当你把Node应用部署到产品环境上时，就会用到其他的控制台消息函数。

`console.info()` 函数跟 `console.log()` 是等价的。它们都会输出到控制台，也都会在消息前面加上一个换行符。而 `console.error()` 跟它们不同的地方的是，它会把消息输出到 `stderr` ，而非 `stdout` ：

```python
console.error("An error occurred...");
```

`console.warn()` 也会进行一样的操作。

这些消息都会出现在终端中，你可能好奇它们的区别是什么。实际上，这些消息并没有什么不同。为了理解这一点，我们需要仔细研究一下 `console` 对象。

> <img class="my_markdown" src="../images/59.png" style="zoom:50%;" />
> **使用Logging模块**
> 能用来打印日志的不只是 `console` 对象，还有一些更复杂的日志工具，比如 `Bunyan` 模块和 `Winston` 模块。

首先， `console` 对象是 `Console` 类的一个全局化的实例。如果需要，我们可以用这个类创建自己的控制台，而且可以用两种方式来创建。

要创建一个 `Console` 实例，可以通过引入 `Console` 类，也可以通过使用全局的 `console` 对象。下面两个都是新的 `console` 对象：

```python
// using require
var Console = require('console').Console;
var cons = new Console(process.stdout, process.stderr);
cons.log('testing');
// using existing console object
var cons2 = new console.Console(process.stdout, process.stderr);
cons2.error('test');
```

注意，在这两个实例中， `process.stdout` 和 `process.stderr` 属性都被作为可写流的实例参数传入，分别用来写入 `log` 和 `error` 信息。实际上全局 `console` 对象就是这样创建的。

我在第2章中介绍过 `process.stdout` 和 `process.stderror` 。我们知道它们会分别映射到环境中的 `stdout` 和 `stderr` 文件描述符，而且它们和Node中大多数流不同，因为它们通常会被阻塞——毕竟它们是同步的，唯一不同步的时候是当流指向管道（pipe）时。所以在大多数情况下， `console` 对象会阻塞 `console.log()` 和 `console.error()` 。但是，除非你在流中注入了大量数据，否则不会出现这样的问题。

为什么在出错的时候用 `console.error()` 呢？因为在两个具有不同流的环境中，我们想要保证在 `stdont` 和 `stderr` 使用了不同的流的情况下也能得到我们想要的结果。如果在某种环境中， `log` 信息不会被阻塞但是 `error` 会，那么你就要确保Node中的错误信息也被阻塞。同时，在运行Node应用时，你可以直接用命令行指定 `console.log()` 和 `console.error()` 分别输出到不同的文件中。下面的代码会把 `console.log()` 的信息输出到日志文件中，而错误信息输出到error文件中：

```python
node app.js 1> app.log 2> error.log
```

下面的Node应用：

```python
// log messages
console.log('this is informative');
console.info('this is more information');
// error messages
console.error('this is an error');
console.warn('but this is only a warning');
```

会把前两行输出到app.log，剩下两行输出到error.log。

回到 `Console` 类，如果给 `Console` 类传递 `process.stdout` 和 `process.stderr` 这两个参数，就可以实现和全局 `console` 对象一样的功能。你也可以创建一个新的类似于 `console` 的对象，来把内容输出到不同的流（比如log和error文件）中。Node官方提供的控制台文档中有这样一个例子：

```python
var output = fs.createWriteStream('./stdout.log');
var errorOutput = fs.createWriteStream('./stderr.log');
// custom simple logger
var logger = new Console(output, errorOutput);
// use it like console
var count = 5;
logger.log('count: %d', count);
// in stdout.log: count 5
```

使用这种类型对象的好处是，可以用全局 `console` 来获取一些常见的反馈，而新创建的 `console` 对象则用于打印正式的日志。

> <img class="my_markdown" src="../images/60.png" style="zoom:50%;" />
> **Process和Stream**
> 大家可能注意到了， `process` 对象在第2章中介绍过了，流（stream）则会在第6章中介绍。

