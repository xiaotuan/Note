只需要输入 node 命令就可以运行 repl，不需要提供任何 Node 应用文件作参数：

```shell
$ node
```

REPL 默认尖括号 `>` 为命令行提示符。在该符号之后输入的任何内容都由底层的 V8 JavaScript 引擎进行处理。

```shell
C:\Users\xiaotuan>node
Welcome to Node.js v16.16.0.
Type ".help" for more information.
>
```

REPL 的使用很简单，就像在文件中编写 JavaScript 一样：

```shell
> a = 2;
2
```

REPL 可以即时打印输入的任何表达式的结果。在上面例子中，表达式的结果是 2。

可以使用下划线 `_` 调用上一个表达式。本例中，a 为 2，结果表达式两次自增 1：

```shell
> a = 2;
2
> _++;
3
> _++;
4
```

还可以用下划线访问该对象的属性或者调用方法：

```shell
> ['apple', 'orange', 'lime']
[ 'apple', 'orange', 'lime' ]
> _.length
3
> 3 + 4
7
> _.toString()
'7'
```

在 REPL 中也可以使用 `var` 关键字。可以在之后通过变量名访问表达式或者变量。但是这样可能会得到意料之外的结果。比如，在 REPL 中输入以下命令行：

```shell
var a = 2;
```

该表达式返回值并不是 2，而是 undefined。表达式结果为 undefined 的原因是变量赋值的表达式并不返回变量的值作为表达式的值。

但是，在 REPL 中你仍旧可以使用该变量，像在 Node 应用中一样：

```shell
> var a = 2;
undefined
> a++;
2
> a++;
3
```

