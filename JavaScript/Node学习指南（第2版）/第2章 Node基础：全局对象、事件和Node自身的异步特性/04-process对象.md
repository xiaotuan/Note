[toc]

### 2.1.2　process对象

`process` 对象是Node环境中的基础组件，它提供了当前运行环境的信息。而且，通过 `process` 你可以操作标准输入/输出（I/O），可以终止一个Node程序，也可以在Node的事件循环（将在2.3.1节中讲到）结束的时候发信号。

`process` 对象在本书的很多应用中都有涉及，你可以查看 `process` 的索引，以便找到所有使用了 `process` 的例子。现在，我们将深入研究 `process` 对象关于运行环境的内容，以及在任何时候都很重要的标准I/O。

`process` 对象提供了对Node环境和其运行环境的信息的访问。要知道它都提供了哪些信息，我们可以使用 `-p` 参数来运行Node，它会执行一段脚本并立即返回结果。比如，想知道 `process.versions` 属性的值，可以在控制台（console）中输入：

```python
$ node -p "process.versions"
{ http_parser: '2.5.0',
  node: '4.2.1',
  v8: '4.5.103.35',
  uv: '1.7.5',
  zlib: '1.2.8',
  ares: '1.10.1-DEV',
  icu: '56.1',
  modules: '46',
  openssl: '1.0.2d' }
```

> <img class="my_markdown" src="../images/28.png" style="zoom:50%;" />
> **命令行中的单引号和双引号**
> 注意双引号的使用：在Windows的命令行窗口中必须使用双引号。由于双引号可以在任何环境下使用，所以请在所有脚本中都使用双引号。

各种Node组件和依赖的版本号都被列出来了，其中包括V8、OpenSSL（用来进行安全通信的库）、Node本身以及其他相关组件的版本。

`process.env` 属性提供了超多信息，它告诉我们Node当前所处的开发/生产环境中的环境变量：

```python
$ node -p "process.env"
```

这个运行结果在不同计算机架构中（比如Linux和Windows）的区别尤为有趣。

想知道 `process.release` 的值，可以运行下面的命令：

```python
$ node -p "process.release"
```

这条命令的输出取决于你安装的Node版本。在长期维护版本和当前最新版本环境下，你都能获取到应用的名字和源代码的URL。但是在长期维护版本的环境下，你还能看到一个额外的属性：

```python
$ node -p "process.release.lts"
'Argon'
```

不过，如果你在最新发布版本中访问同样的值，比如V6，你会看到一个不一样的输出：

```python
$ node -p "process.release.lts"
undefined
```

这些运行环境的信息可以帮助开发人员理解在开发前和开发中，Node能看到什么变量。不过，这些信息中的大部分的数据是不能在应用中直接引用的，原因显而易见。因为在不同的Node版本中，它们的值可能并不一致。但是花点时间研究一下这些信息还是值得的。

而在应用程序中广泛使用的一些基本对象和函数，在Node的不同版本中应该保持一致。其中包括能否访问标准I/O的对象，以及用来正常关闭Node应用的函数。

标准流是一些预先建立的，用于应用和环境之间沟通的通道。标准流由标准输入（stdin）、标准输出（stdout）和标准错误（stderr）组成。在一个Node应用中，这些通道可以帮助Node应用和控制台之间进行通信。这也是一个可以让你和应用进行通信的方式。

Node通过以下3个 `process` 函数来支持这些通道。

+ `process.stdin` :  `stdin` 的可读流。
+ `process.stdout` :  `stdout` 的可写流。
+ `process.stderr` :  `stderr` 的可写流。

这些流是无法在应用中关闭或者结束的，不过你可以从 `stdin` 输入流中获取输入，并写入 `stdout` 输出流和 `stderr` 错误流中。

`process` 的I/O函数继承自 `EventEmitter` ，这部分我们将在2.3.3节介绍。顾名思义，它可以触发事件，相应地你也可以捕获事件并且处理数据。为了从 `process` . `stdin` 中读取数据，我们首先要为这些流设置编码，否则你将读取到缓冲器而不是字符串：

```python
process.stdin.setEncoding('utf8');
```

接下来就可以监听 `readable` 事件了。当有很多数据可以读取时，该事件会通知我们。然后可以用 `process.stdin.read()` 函数读取数据，如果数据不为 `null` ，就用 `process.stdout.write()` 函数把数据打印到 `process.stdout` ：

```python
process.stdin.on('readable', function() {
   var input = process.stdin.read();
   if (input !== null) {
      // 打印文本
      process.stdout.write(input);
   }
});
```

其实不用设置编码也可以得到相同的结果——只要读取缓冲器，再原封不动地将其写入输出流即可。但是对于用户来说，这看上去是在操作文本（字符串），实际上并不是。接下来要介绍的 `process` 函数会演示其中的不同。

在第1章中，我们创建了一个非常基础的Web服务器来监听一个请求并打印信息。如果要结束这个程序，你需要通过信号（signal）来终止进程，或者用组合键Ctrl-C。现在有了 `process` ，你也可以通过在应用中调用 `process.exit()` 来结束它。你还可以在应用正常结束或者出错的时候发出不同的信号。

我们来修改一下这个简单的I/O应用，让它“监听”一个退出字符串，监听到之后就退出程序。例2-1中包含了应用的全部代码。

**例2-1　演示Node中的标准输入/输出和退出程序**

```python
process.stdin.setEncoding('utf8');
process.stdin.on('readable', function() {
   var input = process.stdin.read();
   if (input !== null) {
      // edho the text
      process.stdout.write(input);
      var command = input.trim();
      if (command == 'exit')
         process.exit(0);
   }
});
```

当我们运行这个应用时，所有敲出来的内容都会被立刻输出。这时如果输入 **exit** ，程序会立刻结束，不需要使用组合键Ctrl-C。

如果删除程序前面的 `processs.stdin.setEncoding()` 的函数调用，应用就会出错。原因在于在缓冲器中没有 `trim()` 函数。我们可以先将缓冲器转换成字符串，然后执行 `trim` ：

```python
var command = input.toString().trim();
```

其实更好的做法是加上encoding，并去掉所有不需要的副作用。

> <img class="my_markdown" src="../images/29.png" style="zoom:50%;" />
> **流接口**
> `process` 中的I/O对象是流接口的一种实现，我会在第6章中跟其他系统模块一起介绍。

顾名思义， `process.stderr` 对象可以让你写入错误。那为什么不直接用 `process.stdout` 呢？其中的原因跟创建 `stderr` 对象的原因一样：用来区分那些我们期望的输出和用来记录错误的输出。在一些系统里，你甚至可以用不同的方式来处理 `stderr` 和 `stdout` 的输出（比如将 `stdout` 中的内容输出到 `log` 文件中，而 `stderr` 的内容则输出到控制台）。

前面提到过，在Node中，还有很多对象和有用的函数都跟 `process` 相关，在本书会看到很多相关的内容。

