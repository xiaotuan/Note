`rlwrap` 能够监听键盘输入并提供更多的功能，比如增强行编辑以及提供命令历史浏览功能。

安装 `rlwrap` ：

```console
$ apt-get install rlwrap
```

使用 `rlwrap` 将 `REPL` 的提示改为紫色：

```console
env NODE_NO_READLINE=1 rlwrap -p purple node
```

如果希望 `REPL` 的提示符一直是紫色的，可以在 bashrc 文件中添加别名（alias）：

```
alias node="env NODE_NO_READLINE=1 rlwrap -p purple node"
```

同时改变提示符和颜色：

```console
env NODE_NO_READLINE=1 rlwrap -p purple -s ":: >" node
```

现在 `node`的提示为：

```console
:: >
```