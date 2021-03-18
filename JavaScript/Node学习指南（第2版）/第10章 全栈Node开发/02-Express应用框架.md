

### 10.1　Express应用框架

> <img class="my_markdown" src="../images/98.png" style="zoom:50%;" />
> **Jade现在已经更名为Pug**
> 由于商标冲突，Jade的创始者无法再使用“Jade”作为Express和其他应用程序所使用的模板引擎的名称了。但是，从Jade到Pug的转换还在进行中。在生产环境，Express生成器仍将生成Jade文件，但是尝试安装Jade依赖的话则会产生一个错误信息：
> Pug的网站保留了Jade的名字，但是文档和功能都是Pug的。

在第5章中，我讲了如何简单地使用Node来构建一个Web应用程序。使用Node来创建Web应用很困难，所以像Express这样的框架才会变得非常流行：它提供了我们需要的绝大部分功能，使我们的工作变得非常简单。

有Node的地方，几乎都有Express，所以一定要熟悉这个框架。我们在本章中会介绍最简单的Express程序，但完成这些之后还需要进一步的训练。

> <img class="my_markdown" src="../images/97.png" style="zoom:50%;" />
> **Express现在已经成为Node.js的基础组件**
> Express一开始很不稳定，但现在已经是Node.js基础组件之一。未来的开发应该会变得更稳定，功能也会更可靠。

```python
Jade has been renamed to pug, please install the latest version of pug instead of jade
```

Express有很好的文档支持，包括如何启动一个程序。我们会跟着文档大纲一步一步来，然后扩展我们的基本程序。一开始，我们要为应用程序创建一个子目录，起什么名字无所谓。然后使用npm来创建一个package.json文件，并将app.js作为程序入口。最后，键入以下命令，安装Express并保存到package.json的依赖中：

```python
npm install express --save
```

Express的文档包含了一个基本的Hello World程序，将下面的代码放入app.js文件中：

```python
var express = require('express');
var app = express();
app.get('/', function (req, res) {
  res.send('Hello World!');
}); 
app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
```

`app.get()` 函数会处理所有的GET请求，传入我们在前面几章已经很熟悉的 `request` 和 `response` 对象。按照惯例，Express程序会使用缩写形式，也就是 `req` 和 `res` 。它们在默认的 `request` 和 `response` 对象的功能基础上还加入了Express的功能。比如说，你可以调用 `res.write()` 和 `res.end()` 来为Web请求提供响应，如我们在前几章中做过的一样。但是有了Express，你就可以用 `res.send()` ，只需一行就能实现同样的功能。

我们还可以使用Express的生成器来生成程序框架，而不是手动创建。下面就会用到这个功能，它会提供一个功能更详尽、可读性更高的Express程序。

首先，全局安装Express程序生成器：

```python
sudo npm install express-generator –g
```

下一步，运行这个程序，后面跟上你想要创建的程序的名称。此处我以 `bookapp` 为例：

```python
express bookapp
```

Express程序生成器会创建所需的子目录。然后进入bookapp子目录安装依赖：

```python
npm install
```

好了，到此为止你的第一个Express程序框架就生成好了。如果你用的是OS X或者Linux环境，那么可以使用下面的命令来运行程序：

```python
DEBUG=bookapp:* npm start
```

如果是Windows则需要在命令行中运行下面的命令：

```python
set DEBUG=bookapp:* & npm start
```

如果不需要调试的话，直接使用 `npm start` 也可以启动程序。

程序启动之后会在默认的3000端口上监听请求。在浏览器中访问程序，你会得到一个简单的Web页面，页面上有一条欢迎语“Welcome to Express”。

程序会自动生成几个子目录和文件：

```python
├── app.js
├── bin
│   └── www
├── package.json
├── public
│   ├── images 
│   ├── javascripts
│   └── stylesheets
│       └── style.css
├── routes
│   ├── index.js
│   └── users.js
└── views
    ├── error.jade
    ├── index.jade
    └── layout.jade
```

其中的很多组件我们都会讲到，但是能够公开访问的文件都放在public子目录中。你会注意到，图片文件和CSS文件都在这个目录中。动态内容的模板文件都在views目录中。routes目录包含了程序的Web接口，它们可以监听Web请求和显示Web页面。

bin目录下的www文件是程序的启动脚本。它是一个被转化为命令行程序的Node文件。如果查看生成的package.json文件，你会发现它出现在程序的启动脚本中。

```python
{
  "name": "bookapp",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "node ./bin/www"
  },
  "dependencies": {
    "body-parser": "~1.13.2",
    "cookie-parser": "~1.3.5",
    "debug": "~2.2.0",
    "express": "~4.13.1",
    "jade": "~1.11.0",
    "morgan": "~1.6.1",
    "serve-favicon": "~2.3.0"
  }
}
```

你需要在bin目录下安装别的脚本，来对应用程序进行测试、重启或其他控制。

现在让我们来深入了解一下这个程序，就从程序的入口——app.js文件开始吧。

当你打开app.js文件时，你会看到里面的代码比我们之前看到的简单程序还要多。代码中引入了更多的模块，其中大多数是为面向Web的应用程序提供中间件。被引入的模块也会包含程序特定的引用，也就是routes目录下的文件：

```python
var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var routes = require('./routes/index');
var users = require('./routes/users');
var app = express();
```

其中所涉及的模块以及它们的功能如下：

+ `express` ，Express程序；
+ `path` ，用来调用文件路径的Node核心模块；
+ `serve-favicon` ，用来从给定的路径或缓冲器提供favicon.ico文件的中间件；
+ `morgon` ，一个HTTP请求日志记录工具；
+ `cookie-parser` ，解析 `cookie` 头，并将结果填充到 `req.cookies` ；
+ `body-parser` ，提供4种不同类型的请求内容解析器（除了multi-part类型的内容）。

每个中间件模块都同时兼容普通的HTTP服务和Express服务。

> <img class="my_markdown" src="../images/99.png" style="zoom:50%;" />
> **什么是中间件**
> 中间件是我们的应用程序和系统、操作系统以及数据库之间的桥梁。使用Express时，中间件就是应用程序链中的一部分，而每一部分都在完成与HTTP请求相关的特定功能——处理请求，或者对请求进行一些修改以便后面的中间件使用。Express所使用的中间件集合非常容易理解。

app.js中的下一段代码，通过 `app.use()` 函数和给定的路径加载中间件（也就是让它们在程序中可用）。加载的顺序同样重要，所以如果你还需要加载别的中间件，一定要根据开发人员建议的顺序进行添加。

这段代码还包含了视图引擎初始化的代码，我稍后会讲到。

```python
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
```

对 `app.use()` 的最后一次调用引用了为数不多的Express内建的中间件之一 ——  `express.static` ，它的作用是处理所有的静态文件。如果一个Web用户请求一个HTML、JPEG或者其他的静态文件，这个请求就会由 `expess.static` 来处理。这个中间件加载之后，所有处于某个子目录的相对路径下的静态文件都可供使用，在本例中，这个子目录就是public。

回到 `app.set()` 函数调用，这个函数是用来定义视图引擎的，你需要用一个模板引擎来帮你将数据展现给用户。最流行的模板引擎之一 —— Jade会被默认加载，当然Mustache或者EJS也很好用。引擎的设置中会定义模板文件（视图）所在的子目录的位置，以及应该使用哪个视图引擎（Jade）。

> <img class="my_markdown" src="../images/100.png" style="zoom:50%;" />
> **再次提醒：Jade现在叫Pug了**
> 正如前面提到的，Jade现在叫Pug。Express文档和Pug文档你都需要查看一下，以便了解如何使用重新命名的模板引擎。
> 在本书付印之时，我修改了生成的package.json文件，将Jade替换为Pug：

```python
<p>"pug": "2.0.0-alpha8",</p>
```

> 然后在app.js文件中，将 `jade` 引用替换为 `pug` ：

```python
app.set('view engine', 'pug');
```

> 修改完成后整个应用程序运行起来没有任何问题。

在views子目录中，你会发现3个文件：error.jade、index.jade和layout.jade。这3个文件可以帮你初始化，当然还需要将数据集成到程序中。你需要做的远不止这些。下面是生成的index.jade文件的内容：

```python
extends layout
block content
  h1= title
  p Welcome to #{title}
```

`extends layout` 这一行会将layout.jade文件中的Jade语法集成进来。下面是HTML中的标题（ `h1` ）和段落（ `p` ）元素。 `h1` 标题被赋值为 `title` ，也就是被传入模板的 `title` 变量，而 `title` 在段落元素中也用到了。这些值在模板中显示的方式，决定了我们必须回到app.js文件并加入下面的代码：

```python
app.use('/', routes);
app.use('/users', users);
```

这些都是程序特定的入口，也就是响应客户请求的功能入口。根目录的请求 `('/')` 会被routes子目录中的index.js文件处理。 `users` 请求会被users.js文件处理。

在index.js文件中，我们会接触到Express路由（router），它提供了响应处理功能。Express文档提到，路由的行为需要使用下面的模式来定义：

```python
app.METHOD(PATH, HANDLER)
```

METHOD指的是HTTP方法，Express支持很多种方法，包括常见的 `get` 、 `post` 、 `put` 和 `delete` ，还有一些不常见的方法，比如 `search` 、 `head` 、 `options` 等。 `path` 指的是Web路径，而 `handler` 指的是处理这个请求的函数。在index.js中，方法是 `get，path` 是程序的根路径，而 `handler` 是一个传递请求和响应的回调函数：

```python
var express = require('express');
var router = express.Router();
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
module.exports = router;
```

在 `res.render()` 函数中，数据（局部变量）和视图将会被组合起来。这里使用的视图是我们前面看过的index.jade文件，你会发现模板中使用的 `title` 属性的值，被作为数据传递给 `render` 函数。你可以在本地代码中把Express改为任何你喜欢的内容，然后刷新页面看看修改结果。

app.js文件中剩下的部分就都是错误处理了，这部分留给读者自己分析理解。这是一个非常简单和快速的Express示例，幸运的是麻雀虽小，五脏俱全，你可以从这个例子中了解一个Express程序的基本结构是什么样的。

> <img class="my_markdown" src="../images/101.png" style="zoom:50%;" />
> **数据整合**
> 如果你想要了解如何在Express程序中进行数据整合，那么我就抛砖引玉推荐一下我自己的书——《JavaScript经典实例》（译版，中国电力出版社，2012年出版）。第14章展示了如何扩展一个现有的Express程序来集成MongoDB数据库和控制器，从而实现一个完整的MVC架构。

