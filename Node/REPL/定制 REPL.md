Node 提供了定制 REPL 的功能。为了实现该功能，首先需要引入 REPL 模块：

```shell
var repl = require("repl");
```

通过在 repl 对象上调用 start 方法创建新的 REPL。调用该方法的语法是：

```shell
repl.start([prompt], [stream], [eval], [useGlobal], [ignoreUndefined]);
```

所有参数都是可选择的。如果不传入参数，将会使用各参数的默认值，参数列表如下：

+ `prompt`

  默认值为 `>`。

+ `stream`

  默认值为 `process.stdin`。
  
+ `eval`

  eval 的默认值为 async。

+ `useGlobal`

  默认值为 false，新建一个语境而不是使用全局对象。

+ `ignoreUndefined`

  默认值为 false。不要忽略 undefined 的返回值。

事实上只需要两行代码就可以实现：

```shell
repl = require("repl");
// 设置 ignoreUndefined 为 true，启动 REPL
repl.start("node via stdin> ", null, null, null, true);
```

在 Node 中运行 repl.js 文件：

```shell
$ node repl.js
```

可以用自定义的 REPL 替代 eval 方法。唯一的要求是有具体的格式：

```shell
function eval(cmd, callback) {
	callbaack(null, result);
}
```

stream 选项比较有意思。可以运行多个版本的 REPL，从标准输入（默认）或者 socket 中获取输入内容。Node.js 网站提供的 REPL 文档中给出了 REPL 监听 TCP socket 的例子，代码与下面这个例子类似：

```js
var repl = require("repl"),
    net = require("net");
// 设置 ignoreUndefined 为 true，启动 REPL
repl.start("node via stdin> ", null, null, null, true);
net.createServer(function(socket) {
    repl.start("node via TCP socket> ", socket);
}).listen(8124);
```

在 REPL 启动之后，可以预加载模块并赋值给当前语境的对应属性：

```js
var repl = require('repl');
var context = repl.start(">>", null, null, null, true).context;
// 预加载模块
context.http = require('http');
context.util = require('util');
context.os = require('os');
```

用 Node 运行该程序，显示 REPL 的提示符，可以访问之前加载的那些模块：

```shell
$ node repl.js
>>os.hostname();
'DESKTOP-KLNJ9T2'
>>util.log('message');
23 Jul 19:45:28 - message
>>
```

如果希望像 Linux 中的可执行程序一样运行 REPL 程序，将下面代码加入应用程序开头：

```js
#!/usr/local/bin/node
```

修改文件权限为可执行并运行：

```shell
# chmod u+x replcontext.js
# ./replcontext.js
>>
```

> 提示：REPL 在 Node 0.8 中有较大修改，输入内建的模块名称，比如 fs，就可以加载该模块了。其他一些改进标注在 Node.js 官网提供的新的 REPL 文档中。