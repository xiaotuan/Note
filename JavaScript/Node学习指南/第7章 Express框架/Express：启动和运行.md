安装：

```console
npm install express
```

使用 express 命令创建应用程序：

```console
$ npm install express-generator -g // 安装 Express 应用生成器
$ express site // site 为应用程序的名字
$ cd site
$ npm install
$ node bin/www
```

> 可能需要在 www 文件中修改端口号。

手动创建 Express 应用程序：

1. 创建应用程序目录

```
$ mkdir mySite
```

2. 通过 npm init 命令为应用程序创建一个 package.json 文件

```
$ npm init
```

该命令将要求你输入几个参数，例如名称版本。直接回车接受默认即可，但是下面这个除外:

```
entry point: (index.js)
```

这里输入项目的入口文件：app.js（默认是 index.js）

3. 安装 Express

```
npm install express --save
```

4. 创建 app.js

```
var express = require('express')
var app = express()

app.get('/', function (req, res) {
    res.send('Hello World!')
})

var server = app.listen(3000, function () {
    console.log('Example app listening on port 3000!')
})
```

5. 运行应用程序

```
node app.js
```

当无法找到页面时，或者用户视图访问一个受限的子目录时，可以使用一个自定义匿名函数作为中间件，并将该中间件设置为处理序列中的最后一个中间件。
