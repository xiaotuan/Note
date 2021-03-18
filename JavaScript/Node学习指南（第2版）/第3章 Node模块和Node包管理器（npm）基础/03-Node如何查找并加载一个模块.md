[toc]

### 3.1.1　Node如何查找并加载一个模块

当你需要引用一个Node模块时，不管这个模块是核心模块还是独立安装于Node之外的，都需要用require语句：

```python
var http = require('http');
```

你也可以访问所引用模块的某个属性。比如，在使用URL模块时，常常只会用到其中的parse()函数：

```python
var name = require('url').parse(req.url, true).query.name;
```

你也可以引用某个模块中的对象，并在整个应用程序中使用它：

```python
var spawn = require('child_process').spawn;
```

当程序引用一个模块时，会发生这样几件事。首先，Node会检查模块是否有缓存。Node在首次加载一个模块之后，会将它缓存起来，而不是每次引用都重新加载。这种做法可以减少因系统对文件的查找而引起的延迟。

> <img class="my_markdown" src="../images/38.png" style="zoom:50%;" />
> **从文件到模块：一对一的映射**
> 每个文件只能定义一个模块。

如果模块没有缓存，Node会检查这个模块是不是一个原生模块。原生模块指的是那些预编译过的二进制文件，比如第1章说过的C++插件。如果这个模块是一个原生模块，Node会使用一个专用的函数来加载它，并返回模块所提供的功能。

如果模块没有缓存，也不是原生模块，那么Node会为它创建一个新的模块对象，并返回模块的exports属性。我们会在第3.3节中详细讲解模块的输出，现在只需要知道它会将公共接口返回给应用程序即可。

然后这个模块会被缓存。如果出于某种原因你想从缓存中删除一个模块，可以调用下面这个函数：

```python
delete require('./circle.js');
```

这样，应用程序会在下次请求这个模块的时候重新加载它。

要加载模块，Node 必须先找到模块所处的位置。它有自己的一套查找模块文件的优先级。

首先，核心模块的优先级最高。你可以将自己的模块命名为http，但是当你想要加载它的时候，Node实际上加载的是核心模块中的http模块。想要使用http这个名字加载你自己的模块的唯一方法是，提供模块路径，将它和核心模块中的http模块区分开来。

```python
var http = require ('/home/mylogin/public/modules/http.js');
```

正如本例所示，如果你提供绝对路径或者相对路径加文件名，Node就会使用这个路径。下例就使用了当前目录下的文件：

```python
var someModule = require('./somemodule.js');
```

加载模块的时候我为模块文件加上了扩展名，但是这一步并非必须。Node会先查找目录下符合模块名称的 js 文件，如果找到了，就直接加载，如果没有，就回去找符合名称的JSON文件。如果扩展名为json的文件被找到，模块内容就会以JSON格式来加载。如果这两种文件都没有找到，Node会查找符合模块名称的.node文件。这意味着这个模块是一个预编译的Node插件，Node会进行相应的处理。

> <img class="my_markdown" src="../images/39.png" style="zoom:50%;" />
> JSON文件不需要一个显式的exports声明，只要是格式正确的JSON即可。

你还可以用一个复杂点的相对路径：

```python
var someModule = require('./somedir/someotherdir/somemodule.js');
```

如果你确信这个程序不会被移动，你也可以使用一个绝对路径。它会是一个平台特定的路径，而不是一个URL：

```python
var someModule = require('/home/myname/public/modules/somemodule.js');
```

如果模块是使用npm安装的，你就不需要提供路径，只要列出模块名称即可：

```python
var async = require('async');
```

Node会在一个叫作node_modules的目录下面按照层级结构来搜索这个模块，搜索的优先级如下所示：

（1）应用程序目录内的node_modules子目录；

（2）当前应用程序的父目录中的node_modules目录；

（3）继续向父目录中寻找node_modules目录，直到根目录；

（4）最后，在全局安装的模块中进行寻找（下面会详细说明）。

Node使用这样的层级结构是为了优先访问当前目录下安装的模块，然后才去访问全局安装的模块。因此，如果你正在测试某个模块的新版本，并且已经在应用程序目录中安装了模块：

```python
npm install somemodule
```

那么它将被优先加载，而不是优先加载全局模块：

```python
npm install -g somemodule
```

通过require.resolve()函数可以知道加载的是哪个模块：

```python
console.log(require.resolve('async'));
```

返回的结果就是解析出的模块路径。

如果你提供的是一个目录名，那么Node会搜索目录下的package.json文件。文件中包含一个main字段，它指明了要加载的模块文件：

```python
{ "name" : "somemodule", 
  "main" : "./lib/somemodule.js" }
```

如果Node在目录中没有找到package.json文件，就会寻找index.js或者index.node文件来加载。以上文件都没有的话，Node就会报错。

> <img class="my_markdown" src="../images/40.png" style="zoom:50%;" />
> **缓存是基于文件名的**
> 请注意，缓存是基于加载模块的文件名和路径的。如果你已经缓存了全局版本的模块，然后又去加载本地版本，那么本地版本也会被缓存起来。

既然Module对象是基于JavaScript的，那么我们就可以深入地研究一下Node源代码，看看背后都发生了些什么。

每一个使用Module对象封装的模块都有一个require函数，我们所使用的全局require会调用Module对象中的相应函数。而Module.require()函数又会调用另外一个内部函数：Module._load()。这个函数会执行前面所讲的加载模块的功能。唯一不同的是，如果请求的是REPL模块，这样的模块有自己独立的处理逻辑。这部分内容我们会在下一章介绍。

如果一个模块被当作主模块使用，主模块也就是在命令行中被调用的模块（即我们所说的应用程序），那么它会作为一个属性被赋值给全局对象require（require.main）。新建一个文件，将其命名为test.js，然后在文件中加入以下代码，并使用Node来运行：

```python
console.log(require);
```

你将会看到main对象，其内容就是封装了我们的应用程序代码的Module对象。其中，Module对象的文件名正是应用程序的文件名加路径。你还可以看到Node用来查找模块的路径和程序的缓存，虽然其中只包含当前这一个应用程序。

> <img class="my_markdown" src="../images/41.png" style="zoom:50%;" />
> **查找Node源代码**
> 如果下载了源代码，你就能看到Node的所有功能实现。不需要用源代码来构建Node，只把它作为课后练习就好。JavaScript部分的功能在/lib子目录中，实际的C++代码在/src子目录中。

这让我再一次重新认识了Node的全局对象。在第2章中，我讲过Node的全局对象，也说明了它和浏览器全局对象的区别。我注意到，和浏览器不一样的是，顶层的变量会被限制在它们所处的上下文中，这意味着一个模块中定义的变量不会和应用程序或者其他模块中定义的变量冲突。这是因为Node会将所有的脚本封装在下面代码中：

```python
function (module, exports, __filename, ...) {}
```

换句话说，Node将模块（不论主模块还是其他模块）封装在一个匿名函数中，只对外暴露开发者需要暴露的部分。而且，由于这些模块属性都有模块名作为前缀，所以也不会与本地定义的变量有冲突。

说到上下文，下一节我们来详细了解一下。

