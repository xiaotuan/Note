**表7-1 widget对象的 REST / route / CRUD 映射**

| HTTP verb | Path | Action | Usedfor |
| :-: | :- | :- | :- |
| GET | /widgets | index | 显示所有 widgets |
| GET | /widgets/new | new | 返回创建新 widget 的 HTML 表单 |
| POST | /widgets | create | 创建一个新的 widget |
| GET | /widgets/:id | show | 显示特定的 widget |
| GET | /widgets/:id/edit | edit | 返回用于修改指定的 widget 的 HTML |
| PUT | /widgets/:id | update | 更新一个指定的 widget |
| DELETE | /widgets/id | destroy | 删除指定的 widget |

**示例7-6 widget控制器 (widgets.js) **

```js
var widgets = [
    {
        id: 1,
        name: "The Great Widget",
        price: 1000.0
    }
];

// index listing of widgets at /widgets/
exports.index = function (req, res) {
    res.send(widgets);
};

// display new widget form
exports.new = function (req, res) {
    res.send('displaying new widget form');
};

// add a widget 
exports.create = function (req, res) {
    var index = widgets.length + 1;
    widgets[widgets.length] = {
        id: index,
        name: req.body.widgetname,
        price: parseFloat(req.body.widgetprice)
    };
    console.log(widgets[index - 1]);
    res.send('Widget ' + req.body.widgetname + ' added with id ' + index);
};

// show a widget
exports.show = function (req, res) {
    var index = parseInt(req.params.id) - 1;
    if (!widgets[index]) {
        res.send('There is no widget with id of ' + req.params.id);
    } else {
        res.send(widgets[index]);
    }
};

// delete a widget
exports.destroy = function (req, res) {
    var index = req.params.id - 1;
    delete widgets[index];

    console.log('deleted ' + req.params.id);
    res.send('deleted ' + req.params.id);
};

// display edit form
exports.edit = function (req, res) {
    res.send('displaying edit form');
};

// update a widget
exports.update = function (req, res) {
    var index = parseInt(req.params.id) - 1;
    widgets[index] = {
        id: index,
        name: req.body.widgetname,
        price: parseFloat(req.body.widgetprice)
    };
    console.log(widgets[index]);
    res.send('Updated ' + req.params.id);
};
```

**示例7-7 将路由映射到控制器方法 (maproutecontroller.js)**

```js
exports.mapRoute = function (app, prefix) {
    prefix = '/' + prefix;

    var prefixObj = require('./controllers/' + prefix);

    console.log("prefix: " + prefix)
    console.log("prefixObj: ", prefixObj)

    // index
    app.get(prefix, prefixObj.index);

    // add 
    app.get(prefix + '/new', prefixObj.new);

    // show 
    app.get(prefix + '/:id', prefixObj.show);

    // create
    app.post(prefix + '/create', prefixObj.create);

    // edit
    app.get(prefix + '/:id/edit', prefixObj.edit);

    // update
    app.put(prefix + '/:id', prefixObj.update);

    // destroy
    app.delete(prefix + '/:id', prefixObj.destroy);
    
}
```

**示例7-8 使用了 MVC 架构的 widget 应用程序 (app.js) **

```js
var express = require('express')
var http = require('http')
var logger = require('morgan')
var path = require('path')
var favicon = require('serve-favicon')
var bodyParser = require('body-parser')
var methodOverride = require('method-override')
var map = require('./maproutecontroller')
var indexRouter = require('./routes/index')

var app = express()

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')))
app.use(logger('dev'))
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: false }))
app.use(methodOverride(function (req, res) {
    if (req.body && typeof req.body === 'object' && '_method' in req.body) {
        // look in urlencoded POST bodies and delete it
        var method = req.body._method
        delete req.body._method
        return method
    }
}))
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);

var prefixes = ['widgets']

// map route to controller
prefixes.forEach(function (prefix) {
    map.mapRoute(app, prefix)
})

app.use(function (req, res, next) {
    throw new Error(req.url + ' not found')
})
app.use(function (err, req, res, next) {
    console.log(err)
    res.send(err.message)
})

http.createServer(app).listen(8000)

console.log('Express server listening on port 8000')
```

其他相关文件:

**[favicon.ico](https://www.baidu.com/favicon.ico)**

**index.js**

```js
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' }, function (err, stuff) {
    if (!err) {
      console.log(stuff);
      res.write(stuff);
      res.end();
    }
  });
});

module.exports = router;
```

**error.jade**

```
extends layout

block content
  h1= message
  h2= error.status
  pre #{error.stack}
```

**index.jade**

```
extends layout

block content
  h1= title
  p Welcome to #{title}
```

**layout.jade**

```
doctype html
html
  head
    title= title
    link(rel='stylesheet', href='/stylesheets/style.css')
  body
    block content
```

**目录结构：**

```
|_controllers
    |_widgets.js
|_public
    |_favicon.ico
|_routes
    |_index.js
|_views
    |_error.jade
    |_index.jade
    |_layout.jade
|_app.js
|_maproutecontroller.js
|_package.json
```

**运行应用程序方法：**

1. 进入应用程序根目录，执行下面的命令生成 package.json 文件：

```console
$ npm init
```

2. 在 package.json 文件中添加依赖（主要是添加 jade 的依赖）：

```json
{
  "name": "mvcsite",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cookie-parser": "~1.4.4",
    "debug": "~2.6.9",
    "express": "~4.16.1",
    "http-errors": "~1.6.3",
    "jade": "~1.11.0",
    "morgan": "~1.9.1",
    "serve-favicon": "^2.5.0"
  }
}
```

3. 运行应用程序：

```console
$ node app.js
```

**测试应用程序**

```console
$ curl --request GET http://localhost:8000/widgets	// 查看所有widget
$ curl --request GET http://localhost:8000/widgets/new	// 发出创建 widget 的请求
$ curl --request POST http://localhost:8000/widgets/create --data 'widgetname=Smallwidget&widgetprice=10.00'	// 创建 widget
$ curl --request PUT http://localhost:8000/widgets/2 --data 'widgetname=Smallwidget&widgetprice=75.00'	// 更新 widget
$ curl --request DELETE http://localhost:8000/widgets/2	// 删除 widget
```

> **其他框架**
> 虽然 Express 是一个框架，但它却是一个非常简单和基本的框架。如果你想用它来做更多的事，还是需要相当多的工作量。
> 因此，有一些以 Express 为基础的第三方应用程序能够为我们提供更多功能。Calipso 就是一个建立在 Express 之上完整的内容管理系统，它使用 MongoDB 做持久性存储。
> 而 Express-Resource 是一个小型框架，它为 Express 提供了简化的 MVC 功能，这样你就不自己写了。
> Tower.js 是另一个能够支持完整 MVC 的 Web 框架，它提供了一个更高层次的抽象，并且以 Ruby on Rails 为原型。RailwayJS 也是一个 MVC 框架，基于 Express 并仿照 Ruby on Rails。
> 还有一个名为 Strata 的框架，它采取了与 Tower.js 和 RailwayJS 不同的策略。它遵循由 WSGI (Python) 和 Rack (Ruby) 建立的模型，而不是 Rails 模型。这是一个低级别的抽象，如果你没有 Ruby 和 Rails 编程工作经验，使用它会更简单些。