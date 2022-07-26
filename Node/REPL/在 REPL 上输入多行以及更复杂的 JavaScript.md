你可以像写文件一样在 REPL 中输入 JavaScript，包括导入 module 的 require 语句。以下代码显示了如何使用 Query String module：

```shell
C:\Users\xiaotuan>node
Welcome to Node.js v16.16.0.
Type ".help" for more information.
> qs = require('querystring');
{
  unescapeBuffer: [Function: unescapeBuffer],
  unescape: [Function: qsUnescape],
  escape: [Function: qsEscape],
  stringify: [Function: stringify],
  encode: [Function: stringify],
  parse: [Function: parse],
  decode: [Function: parse]
}
> val = qs.parse('file=main&file=secondary&test=one').file;
[ 'main', 'secondary' ]
>
```

如果不想看到可能出现的长文本输出，请使用 var 关键字：

```shell
> var qs = require('querystring');
```

REPL 提供重复的点 `.` 符号跟在开放的大括号后面表示输入命令未完成，该符号同样可以用于不闭合的小括号：

```shell
> var test = function(x, y) {
... var val = x * y;
... return val;
... };
undefined
> test(3, 4);
12
```

