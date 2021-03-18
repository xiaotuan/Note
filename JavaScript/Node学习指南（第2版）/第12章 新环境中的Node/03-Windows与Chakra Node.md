

### 12.2　Windows与Chakra Node

在2016年1月9日，微软提交了一个pull request（PR），使得Node可以在微软的ChakraCore（JavaScript）引擎中运行。同时微软创建了一个可实现大部分V8核心API的适配器，允许Node在ChakraCore上无障碍地运行。

让Node运行在除了V8之外的引擎上，是一件很有意思、也很有吸引力的事情。虽然V8似乎在主导着Node的开发，至少对Node目前的版本来说是这样的，但从技术上来说，并没有硬性需求说Node必须基于V8开发。毕竟，最新的Node版本更侧重于增强Node API，并结合新的ECMAScript来创新。

微软已经将ChakraCore开源了，这是一个好的开始。微软公司的新浏览器Edge就使用了该引擎。同时，微软声称该引擎优于V8。

虽然关于这个PR的讨论和测试还在进行，但实际上你已经可以自己在ChakraCore上测试Node了，只需要一台装有Python（2.6或2.7）和Visual Studio（如Visual Studio 2015社区版，可免费下载）的Windows计算机。也可以下载预编译的二进制可执行文件来测试。Microsoft为ARM（适用于黑莓派）以及更传统的x86和x64架构提供二进制文件。当我将其安装在我的Windows计算机中时，它创建了与非ChakraCore Node一致的命令窗口。最重要的是，它可以安装在装有Node的计算机上，且二者可以同时使用。

我运行了一些本书中的代码，都没有问题。我也尝试了一些能够体现Node最新修改的代码，比如允许child_process.spawn()函数指定一个shell选项（在第8章讲过）。这个例子在4.x LTS的版本中不生效，但是在最新的版本中却是生效的（编写本书的时候Node的最新版本是6.0.0）。同时它在基于ChakraCore的Node的二进制版本中也是生效的。虽然最新版Node的发布只过了几天，微软却已经将其功能包含进了他们的ChakraCore编译版本中。

当我尝试了一下这个用ES6写的反射和代理的例子时，我发现更有意思了：

```python
'use strict' 
// example, courtesy of Dr. Axel Rauschmayer
// http://www.2ality.com/2014/12/es6-proxies.html
let target = {};
    let handler = {
        get(target, propKey, receiver) {
            console.log('get ' + propKey);
            return 123;
        } 
    }; 
let proxy = new Proxy(target, handler);
console.log(proxy.foo);
proxy.bar = 'abc';
console.log(target.bar);
```

它在ChakraCore Node中是生效的，但在V8 Node中却不生效（即使是最新版本的V8）。ChakraCore开发人员声称它的另一个优势是优美地实现了最新ECMAScript中的增强功能。

> <img class="my_markdown" src="../images/117.png" style="zoom:50%;" />
> 这个功能在V5的稳定版本中不能使用，但却能够兼容最新的V6版本。

目前，ChakraCore仅适用于Windows，并提供了树莓派二进制文件。同时开发者承诺Linux版本将很快出现。

