[toc]

### 4.3.2　REPL和rlwrap

Node.js的官方文档中关于REPL的部分提到要设置环境变量，这样就可以将 `rlwrap` 和REPL一起用了。什么是 `rlwrap` ，为什么要把它跟REPL一起用呢？

`rlwrap` 工具对GNU中 `readline` 库的功能进行了封装，可以让你通过键盘输入来提高灵活性。它会拦截键盘输入并提供额外的功能，比如增强行内编辑功能和记录历史命令。

要在REPL中使用这个功能，首先需要安装 `rlwrap` 和 `readline` ，大多数UNIX的操作系统都提供了方便的安装包。比如，在我的Ubuntu系统中，安装 `rlwrap` 就很简单：

```python
apt-get install rlwrap
```

使用Mac的用户应该找一个适合的安装工具来安装这些应用。而Windows用户就需要用一个UNIX环境模拟器，比如Cygwin。

下面这个例子快速且直观地展示了如何在REPL中使用 `rlwrap` 将REPL的命令行提示符改成紫色：

```python
NODE_NO_READLINE=1 rlwrap -ppurple node
```

如果希望REPL的提示符一直是紫色，可以在bashrc文件中加入 `alias` ：

```python
alias node="NODE_NO_READLINE=1 rlwrap -ppurple node"
```

如果要同时修改提示符和颜色，可以用如下命令：

```python
NODE_NO_READLINE=1 rlwrap -ppurple -S "::> " node
```

现在我的提示符应该变成：

```python
::>
```

而且是紫色的。

`rlwrap` 中有一个功能特别好用，它可以跨会话保存REPL的历史记录。一般我们只能访问一个REPL会话中的历史命令。而使用 `rlwrap` 后，下一次访问REPL时，不仅能访问当前会话中的历史命令，而且还能访问过往会话中的历史命令（以及其他命令行）。下面是我_退出_REPL并重新进入后的会话，这里的命令并不是用键盘输入的，而是使用向上键从历史记录中找出来的。

```python
::> e = ['a','b'];
[ 'a', 'b' ]
::> 3 > 2 > 1;
false
```

即使 `rlwrap` 这么有用，它依旧会在每次输入一个没有返回值的表达式时返回一个 `undefined` 。不过，我们可以进行改进，接下来要讨论的另一个功能就是创建自定义的REPL。

