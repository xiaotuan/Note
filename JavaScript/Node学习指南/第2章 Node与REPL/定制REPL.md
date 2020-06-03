首先需要引入 REPL 模块（repl）：

```js
var repl = require('repl')
```

通过在 repl 对象上调用 start 方法创建新的 REPL：

```js
repl.start([prompt], [stream], [eval], [useGlobl], [ignoreUndefined])
```

所有参赛都是可选的。如果不传入参数，将会使用各参数的默认值，参数列表如下：

| 参数 | 描述 |
| :-: | :- |
| prompt | 默认值为 >。 |
| stream | 默认值为 process.stdin。 |
| eval | 默认值为 async。 |
| useGlobal | 默认值为 false，新建一个语境而不是使用全局对象。 |
| ignoreUndefined | 默认值为 false。不要忽略 undefined 的返回值。 |

不输出 undefined的解决方法：创建 repl.js 文件，文件内容如下：

```
repl = require('repl')
// 设置 ignoreUndefined 为 true，启动 REPL
repl.start("node via stdin> ", null, null, null, true)
```

在 Node 中运行 repl.js 文件：

```console
$ node repl.js
```

使用 `REPL` 监听 TCP socket 的例子：

```js
var repl = require('repl'), net = require('net')
// 设置 ignoreUndefined 为 true，启动 REPL
repl.start("node via stdin> ", null, null, null, true)
net.createServer((socket) => {
    repl.start("node via TCP socket> ", socket)
}).listen(8124)
```

创建可以预加载模块的自定义 `REPL`：

```js
var repl = require('repl')
var context = repl.start(">>", null, null, null, true)
// 预加载模块
context.http = require('http')
context.util = require('util')
context.os = require('os')
```

> `REPL` 在 `Node 0.8` 中有较大修改，输入内建的模块名称，比如 fs，就可以加载该模块了。
