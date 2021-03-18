[toc]

### 4.3　更复杂的多行JavaScript

在REPL可以输入跟文件中一样的JavaScript代码，包括用 `require` 语句来引入模块。下面的代码重复使用了 `Query String(qs)` 模块：

```python
$ node
> qs = require('querystring');
{ unescapeBuffer: [Function],
  unescape: [Function],
  escape: [Function],
  encode: [Function],
  stringify: [Function],
  decode: [Function],
  parse: [Function] }
> val = qs.parse('file=main&file=secondary&test=one').file;
[ 'main', 'secondary' ]
```

由于没有使用 `var` 关键字，所以表达式的结果会打印出来。在本例中，会打印 `querystring` 这个对象的接口。这真是个意外之喜！因为你不仅可以访问对象，而且可以学到更多关于对象接口的内容。不过，如果你不想让输出太冗长，就用 `var` 关键字：

```python
> var qs = require('querystring');
```

通过上述方法，你可以使用 `qs` 变量访问 `querystring` 对象。

为了能够集成外部模块，REPL提供了一个代码的文本标识符（用花括号({}包起来的）来支持多行表达式：

```python
> var test = function (x, y) {
... var val = x * y;
.. return val;
.. };
undefined
> test(3,4);
12
```

REPL中的3个点表示所有在这之后的代码都在花括号中，命令并没有结束。这对于圆括号来讲也同样适用：

```python
> test(4,
... 5);
20
```

圆点的数量随着嵌套深度的增加而增加。这在交互式环境中很重要，因为你可能在输入代码的时候不知道进行到哪里了：

```python
> var test = function (x, y) {
... var test2 = function (x, y) {
..... return x * y;
..... }
... return test2(x,y);
... }
undefined
> test(3,4);
12
>
```

在REPL中，你可以直接输入代码，也可以复制粘贴整个Node应用，然后运行。我把服务（Server）端的显示内容缩减和加粗，因为它们太长了，而且当你读到这段代码的时候这些内容很可能会变。

```python
> var http = require('http');
undefined
> http.createServer(function (req, res) {
...
...   // content header
...   res.writeHead(200, {'Content-Type': 'text/plain'});
...
...   res.end("Hello person\n");
... }).listen(8124);
{ domain: 
 { domain: null,
 _events: { error: [Function] },
 _maxListeners: undefined,
 members: [] },
 _
 ... 
 httpAllowHalfOpen: false,
 timeout: 120000,
 _pendingResponseData: 0,
 _connectionKey: '6:null:8124' }
> console.log('Server running at http://127.0.0.1:8124/');
Server running at http://127.0.0.1:8124/
Undefined
```

你可以从浏览器访问这个应用，这跟用文件写代码然后用Node运行没什么不同。

不将表达式赋值给变量的“缺点”是，应用中可能会显示一个很长的对象。不过，我最喜欢的REPL的特性之一就是能够快速查看对象。例如，在Node网站中，Node核心对象 `global` 的介绍非常分散。为了更好地了解 `global` 对象，可以打开一个REPL会话，并将该对象传给 `console.log` 方法，如下：

```python
> console.log(global)
```

也可以用一个 `gl` 变量来达到同样的效果（为了省地方，把 `global` 缩写成 `gl` ）：

```python
> gl = global;
...
_: [Circular],
  gl: [Circular] }
```

直接打印 `global` 也可以输出相同的信息：

```python
> global
```

我就不在这里复制REPL打印出的内容了。因为 `global` 的接口太大了，所以这些内容就留给你们在自己的计算机上尝试吧。在这个练习中需要掌握的是，在REPL中，我们可以在任何时间快速、轻易地查看一个对象的接口，这可以让我们很方便地知道哪些方法被调用了，哪些属性是可用的。

> <img class="my_markdown" src="../images/57.png" style="zoom:50%;" />
> 在第2章中有很多关于 `global` 的介绍。

在REPL中，我们可以用上下键来切换之前输入过的命令。这样即使在受限的条件下，也能很方便地查看和修改前面写的代码。

请阅读以下REPL会话：

```python
> var myFruit = function(fruitArray,pickOne) {
... return fruitArray[pickOne - 1];
... }
undefined
> fruit = ['apples','oranges','limes','cherries'];
[ 'apples',  'oranges', 'limes',  'cherries' ]
> myFruit(fruit,2);
'oranges'
> myFruit(fruit,0);
undefined
> var myFruit = function(fruitArray,pickOne) {
... if (pickOne <= 0) return 'invalid number';
... return fruitArray[pickOne - 1];
... };
undefined
> myFruit(fruit,0);
'invalid number'
> myFruit(fruit,1);
'apples'
```

有一些内容在这个输出中没有体现出来，那就是当我需要修改函数来检查输入值时，实际上是按向上键回到函数声明的起始部分，然后按回车键重新启动该函数。我添加了新行，然后再次使用上下键重复前面输出的内容，直到写完函数。我也用了向上键重复函数调用从而导致出现 `undefined` 。

说了这么多，好像都是为了不重复输入一些简单的内容。现在考虑一下需要输入正则表达式的场景，比如下面这个例子：

```python
> var ssRe = /^\d{3}-\d{2}-\d{4}$/;
undefined
> ssRe.test('555-55-5555');
true
> var decRe = /^\s*(\+|-)?((\d+(\.\d+)?)|(\.\d+))\s*$/;
undefined
> decRe.test(56.5);
true
```

碰到正则表达式我就没有办法了，每次都需要调整好多次，表达式才能正确。使用REPL来测试正则表达式很有吸引力。不过，重复输入过长的正则表达式依旧会带来很大的工作量。

幸运的是，在REPL中，我们需要做的仅仅是用上下键找到含有正则表达式的那一行，修改它，按回车键，然后继续测试。

除了上下键以外，还能用Tab键进行自动补全，当然，必须很清楚需要补全的内容才能使用它。举个例子，在命令行输入 **va** 然后按Tab键，REPL会列出 `var` 和 `valueOf` ，它们都能补全当前的命令。不过，输入 **querys** 再按Tab键则只有一个选择： `querysting` 。你也可以用Tab键自动补全任何全局或本地变量。表4-1提供了在REPL中可用的键盘命令的快速汇总。

<center class="my_markdown"><b class="my_markdown">表4-1 　REPL中的键盘控制</b></center>

| 键盘输入 | 作用 |
| :-----  | :-----  | :-----  | :-----  |
| Ctrl-C | 终止当前命令。按两遍Ctrl-C键会强制退出REPL |
| Ctrl-D | 退出REPL |
| Tab | 自动补全全局或本地变量 |
| 向上键 | 上一条历史命令 |
| 向下键 | 下一条历史命令 |
| 下划线（_） | 引用上一个表达式的结果 |

如果你担心在REPL中写代码花了很多时间，但却没办法展示写过的代码，别担心，你可以在当前上下文中用 `.save` 命令来保存结果。在下一小节中我将介绍这个命令和其他一些命令。

