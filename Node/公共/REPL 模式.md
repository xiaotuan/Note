[toc]

### 1. 启动 Node REPL

REPL 是 Read-Eval-Print-Loop 的缩写。如果需要启动 Node REPL（Node Shell），可以在任何 shell 中输入 `node`：

```shell
$ node
> 
```

你可以在 `>` 符号后输入 Node 代码，然后按 <kbd>Enter</kbd> 键，将会看到该代码的执行结果。例如：

```shell
$ node
> console.log("Hello World!");
Hello World!
undefined
> 
```

如果你在 Node REPL 中看到三个点（...），这就意味着你需要输入更多的代码去完成当前的表达式、语句或函数。例如：

```shell
$ node
> function sayHello() {
... console.log("Hello");
... }
undefined
> sayHello();
Hello
undefined
> 
```

如果需要终止输入更多代码，可以输入 `.break` 来终止当前更多代码输入（即已经输入的需要更多的代码的代码将会被清除）。例如：

```shell
$ node
> function sayHello() {
... .break
>
```

### 2. 退出 REPL

1. 只需按下 <kbd>Ctrl</kbd> + <kbd>D</kbd> （Windows）组合键就可以退出 REPL。

2. 也可以按下 <kbd>Ctrl</kbd> + <kbd>C</kbd> 组合键两次即可退出 REPL。