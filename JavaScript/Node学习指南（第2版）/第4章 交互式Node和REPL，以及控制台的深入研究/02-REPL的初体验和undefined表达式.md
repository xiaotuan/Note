[toc]

### 4.1　REPL的初体验和undefined表达式

在命令行直接输入 **node** （不需要提供任何Node应用）就可以打开REPL，就像这样：

```python
$ node
```

REPL有一个默认的命令提示符——尖括号（>）。从这里输入的任何内容都会由底层的V8 JavaScript引擎处理。

REPL非常容易上手。就像使用文件一样，输入JavaScript代码就行：

```python
> a = 2; 
2
```

这个工具会打印输入的表达式。在上例中，表达式的值是 `2` 。在下面的例子中，表达式的值是一个含有3个元素的数组。

```python
> b = ['a','b','c'];
[ 'a', 'b', 'c' ]
```

使用下划线（_）这个特殊变量就可以获取上一个表达式。在下面的代码中， `a` 的值被设为 `2` ，然后 `a` 作为前表达式被加1，然后又被加1：

```python
> a = 2;
2
> ++_;
3
> ++_; 
4
```

你甚至可以用下划线表达式来访问属性或者调用函数：

```python
> ['apple','orange','lime'] 
[ 'apple', 'orange', 'lime' ] 
> _.length
3
>3 + 4
7
> _.toString();
'7'
```

在REPL中，可以用 `var` 关键字来定义表达式，以备后续访问，但可能会有想不到的错误。比如，在REPL中输出下面的代码：

```python
var a = 2;
```

这段代码并不会返回2，而是返回 `undefined` 。这是因为赋值表达式在赋值时并不会返回，所以这个表达式的结果是 `undefined` 。

再看看下面的代码，这或多或少可以代表REPL引擎的行为：

```python
console.log(eval('a = 2'));
console.log(eval('var a = 2'));
```

把上面的内容写入一个文件，用Node运行后会返回这样的结果：

```python
2 
undefined
```

第二个 `eval` 调用并没有返回结果，因此，返回值是 `undefined` 。REPL是一个“读取-求值-打印”循环，重点是求值。

像Node应用一样，你也可以在REPL中使用变量：

```python
> var a = 2;
undefined
> a++;
2
> a++; 
3
```

后面两个命令有返回值，REPL会把它们打印出来。

> <img class="my_markdown" src="../images/56.png" style="zoom:50%;" />
> 我会在4.3.3节中演示如何创建自定义的REPL——一个不会输出 `undefined` 的REPL。

若想结束REPL，你可以按两次Ctrl-C，或者一次Ctrl-D。在4.3.1节中，我们会看到结束REPL的其他方式。

