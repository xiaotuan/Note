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

在 `REPL` 中只需要使用方向键就可以找到创建正则表达式的命令，修改，回车然后继续测试；还可以使用 <kbd>Tab</kbd> 键自动补全。

**表2-1 REPL中的键盘控制**

| 键盘输入 | 功能 |
| :-: | :- |
| <kbd>Ctrl</kbd>+<kbd>C</kbd> | 终止当前命令。按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 键两次直接退出 |
| <kbd>Ctrl</kbd>+<kbd>D</kbd> | 退出 `REPL` |
| <kbd>Tab</kbd> | 自动补全全局或者局部变量 |
| 方向上键 | 查找该命令之前的输入 |
| 方向下键 | 查找该条命令之后的输入 |
| 下划线（\_） | 上一条表达式的输出 |

`.save` 命令将当前语境中的输入保存在文件中。

```console
> .save ./dir/session/save.js
```

以下是一个完整的 `REPL` 命令以及功能列表：

**.break**

如果多行输入发生混乱不知道当前位置时，使用 `.break` 会重新开始。不过会丢失之前输入的多行内容。

**.clear**

重置语境并清空所有表达式。该命令可以使你重头再来。

**.exit**

退出 `REPL`。

**.help**

显示所有可用的 `REPL` 命令。

**.save**

将当前 `REPL` 会话保存至文件。

**.load**

将文件加载到当前会话（`.load /path/to/file.js`）。
