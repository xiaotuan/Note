`Optimist` 的全部功能就是解析命令中的选项参数。

```js
#!/usr/local/bin/node
var argv = require('optimist').argv
console.log(argv.o + " " + argv.t)
```

可以使用下面命令进行测试：

```console
$ ./app.js -o 1 -t 2
```

上面的方法也可以处理长选项：

```console
$ ./app.js -o='My' --t="Name"
```

> 更多关于 `Optimist` 参考： <https://github.com/substack/node-optimist>

