使用 require 语句引入模块：

```js
var http = require('http')
```

还可以引入模块中的特定对象，而不是整个模块：

```js
var spawn = require('child_process').spawn
```

对于非 Node 原生支持和不在 node_modules 文件夹里的模块，需要在字符串之前加上相对路径。

```js
require('./mymodule.js')
require('/home/myname/myapp/mymodule.js')
```

模块文件的扩展名可以为 .js，.node 或者 .json。

Node 核心模块的优先级要高于外部模块。当你尝试加载一个自定义的 http 模块，Node 会首先加载内部核心 HTTP 模块，除非换个模块名字或者提供绝对路径。

require 还有两种形式：require.resolve 和 require.cache。require.resolve 方法负责查找给定的模块但是并不加载该模块，只返回文件名。require.cache 对象包含所有加载模块的缓存版本。如果有需要强制重新加载某个 cache 中的模块，先从 cache 中删除该模块然后重新加载。

删除模块：

```
var circle = require('./circle.js')

delete require.cache('./circle.js')
```
