只需要输入 node 命令就可以运行 repl，不需要提供任何 Node 应用文件作为参数：

```console
$ node
```

可以使用下划线 "\_" 调用上一个表达式。还可以用下划线访问该对象的属性或者调用方法。

在 REPL 中也可以使用 var 关键字。可以在之后统统变量名访问表达式或者变量：

```console
var a = 2;
```

该表达式返回值并不是 2，而是 undefined。表达式结果为 undefined 的原因是变量赋值的表达式并不返回变量的值作为表达式的值。

按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 键两次或者 <kbd>Ctrl</kbd>+<kbd>D</kbd> 键一次退出 REPL。

在 REPL 中导入模块：

```console
$ node
> qs = require('querystring')
{
    unescapeBuffer: [Function],
    unescape: [Function],
    escape: [Function],
    encode: [Function],
    stringify: [Function],
    decode: [Function]
}
> val = qs.parse('file=main&file=secondary&test=one').file
['main', 'secondary']
```

为了兼容外部模块，REPL 可以处理多行表达式，提供了可以嵌套使用的文本标识符，跟在大括号 {} 之后：

```console
> var test = function (x, y) {
... var va1 = x * y
... return va1
... }
undefined
> test(3, 4)
12
```

REPL 提供重复的点 "." 符号跟在开放的大括号后面表示输入命令未完成，该符号同样可以用于不闭合的小括号：

```console
> test(4
... 5)
20
```

