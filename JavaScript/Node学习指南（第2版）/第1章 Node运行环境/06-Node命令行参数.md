[toc]

### 1.2.3　Node命令行参数

在前面两节中，Node 都是在命令行中调用的，而且不带任何参数。在继续下面的内容之前，我想简要介绍一些命令行参数。其他的参数会在需要时再介绍。

使用help参数（ `-h` 或 `--help` ），可以展示出所有可以使用的选项和参数：

```python
$ node --help
```

这个参数会列出 Node 的所有参数，同时展示使用语法：

```python
Usage: node [options] [ -e script | script.js ] [arguments]
       node debug script.js [arguments]
```

要知道 Node 的版本信息，可以使用下面这个命令：

```python
$ node -v or –-version
```

要查看某个 Node 应用的语法，可以使用 `-c` 参数。这个参数可以在不运行应用的情况下查看运行语法：

```python
$ node -c or --check script.js
```

要查看V8参数，请输入：

```python
$ node --v8-options
```

这个命令会返回几个不同的参数，包括 `--harmony` 参数。这个参数用于开启所有已完成的 Harmony JavaScript 功能。这包括已经实现但尚未纳入 LTS 或当前 Node 版本的所有 ES6 功能。

我最喜欢的Node参数是 `-p` 或 `--print` ，它可以运行一行 Node 脚本并打印结果。如果你正在使用进程的环境变量（我们将在第2章进行更全面的讨论），那么这一参数将尤其有用。下面是一个例子，这个例子会打印出 `process.env` 属性的所有值：

```python
$ node -p "process.env"
```

