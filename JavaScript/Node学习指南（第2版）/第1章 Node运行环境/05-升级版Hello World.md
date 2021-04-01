[toc]

### 1.2.2　升级版 Hello World

上面的程序成功打印了一段静态文本，这说明：第一，程序是可以正常工作的；第二，它向我们展示了如何创建一个简单的 Web 服务。这个最基本的例子也展示了 `Node` 程序的几个关键元素。但是如果把它稍微丰富一下，它就会变得更有趣。我做了一点升级，写了第二个程序，加入了一些可变因素。

升级后的代码如例 1-2 所示。在新的代码中，我对传入的 Web 请求进行解析，然后查找一个参数，将参数中的名字（name）取出来，以便确定响应的内容。几乎所有的 `name` 都会有一个个性化的响应，除非你在参数中加入 `name=burningbird` ，此时服务器端将会返回一张图片。如果 `name` 参数没有被指定，那 `name` 参数就被设为“ `world` ”。

**例1-2　升级版Hello World**

```python
var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
   var name = require('url').parse(req.url, true).query.name;
   if (name === undefined) name = 'world';
   if (name == 'burningbird') {
      var file = 'phoenix5a.png';
      fs.stat(file, function (err, stat) {
         if (err) {
            console.error(err);
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.end("Sorry, Burningbird isn't around right now \n");
         } else {
            var img = fs.readFileSync(file);
            res.contentType = 'image/png';
            res.contentLength = stat.size;
            res.end(img, 'binary');
         }
      }); 
   } else {
      res.writeHead(200, {'Content-Type': 'text/plain'});
      res.end('Hello ' + name + '\n');
   }
}).listen(8124);
console.log('Server running at port 8124/');
```

使用 `?name=burningbird` 作为参数来访问我们的Web应用，将会得到下面的图片，如图1-3所示。

![17.png](../images/17.png)
<center class="my_markdown"><b class="my_markdown">图1-3　Hello, Burningbird</b></center>

升级后的 Hello World 程序并没有比原版增加多少代码，但还是有些区别。一开始，程序中就引入了一个名叫 `fs` 的新模块，即文件系统模块。在未来的几章里，你将对这个模块非常熟悉。另外还有一个模块，它的引入方式就不太一样了：

```python
var name = require('url').parse(req.url, true).query.name;
```

模块暴露的属性可以被链式调用，因此我们可以把模块的引入和模块中方法的调用放在同一行。我们通常会在使用URL这个模块的时候用到这种方式，这个模块就是一个URL的工具集。

`response` 和 `request` 参数的变量名可以缩写为 `res` 和 `req` ，以便于日后使用。当我们解析完 `request` ，就得到了 `name` 的值，首先检测一下这个值是不是 `undefined` 。如果是，这个值就会被赋值为默认值 `world` ；而如果 `name` 不是 `undefined` ，我们会再检测它是否等于 `burningbird` 。如果不等于，那么程序的结果和我们在初级版程序中看到的很像，只不过返回的字符串中加入了我们提供的名字。

但是，如果 `name` 等于 `burningbird` ，我们就需要处理一张图片，而不是一段文字了。 `fs.stat()` 方法不但会验证文件是否存在，而且也会返回一个包含文件信息的对象，包括它的大小。这个值会被用来创建响应内容的头（content header）。

如果文件不存在，程序也会很优雅地处理这个情况：它会展示出一个友好的信息，告诉你这只鸟已经从笼子里飞走了，同时也会使用 `console.error()` 方法在控制台输出错误信息：

```python
{ [Error: ENOENT: no such file or directory, stat 'phoenix5a.png']
  errno: -2,
  code: 'ENOENT',
  syscall: 'stat',
  path: 'phoenix5a.png' }
```

如果文件存在，那么我们就将图片读取出来并赋值给一个变量，然后在响应中返回，同时相应地调整头（header）的值。

`fs.stats()` 方法使用标准的Node回调函数模式，即把错误值作为第一个参数——通常被称为 `errback` 。但是，读取图片部分的代码可能会让你搞不清楚。它看起来有点奇怪，和你在本章中看到的其他Node函数不太一样（很可能跟你在其他在线示例中看到的也不一样）。它的不同之处在于，我使用了一个同步函数 `readFileSync()` ，而不是它的异步版本 `readFile ()` 。

对于大多数文件系统功能，Node 同时提供同步和异步两个版本的函数。通常，在 Node 中的 Web 请求中使用同步操作是一种忌讳，但是 Node 确实提供了这样的功能。例1-3是同样一段代码的异步实现。

**例1-3**

```python
fs.readFile(file, function(err,data) {
                res.contentType = 'image/png';
                res.contentLength = stat.size;
                res.end(data, 'binary');
              });
```

那什么时候应该用同步函数，什么时候又该用异步函数呢？在某些情况下，无论你使用哪种类型的函数，文件 I/O 都不会影响性能，同步函数可以让代码干净，也更易于使用。它还可以减少代码嵌套——代码嵌套是 Node 回调系统的一个特殊问题，我将在第2章更详细地介绍。

此外，虽然我没有在例子中使用异常处理，但是你可以将 `try … catch` 与同步函数结合使用。你不能将这种传统的错误处理方式与异步函数结合使用（因为匿名回调函数的第一个参数就是错误值）。

所以从第二个例子中，我们学到的重点是，Node 中的 I/O 并不都是异步的。

> <img class="my_markdown" src="../images/18.png" style="zoom:50%;" />
> **文件系统和 URL 模块，缓冲器（buffer）以及异步 I/O**
> 我将在第 5 章更详细地介绍 URL 模块，在第 6 章讲解文件系统。但是请注意，文件系统的使用会贯穿整本书。缓冲器和异步处理的内容会在第 2 章中介绍。

