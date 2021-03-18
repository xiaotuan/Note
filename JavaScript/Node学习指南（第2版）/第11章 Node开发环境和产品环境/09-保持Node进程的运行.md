

### 11.3　保持Node进程的运行

要写就写最好的程序。我们现在已经写了完整的测试，而且还加入了错误处理，这样出错时就不会影响到用户的使用。但是，还会有别的问题——程序可能会因为一些无法预料的意外而无法运行。如果这种情况发生了，就需要确保即使你不做任何事情，程序在这种情况下也可以自动重启。

Forever就是这样一个工具——确保你的程序在崩溃时自动重启。它也是通过daemon模式启动程序（这样程序可以在当前的终端会话之外运行）的一种方法。Forever既可以在命令行中使用，也可以集成在程序中。如果要在命令行中使用，需要将它安装在全局环境中：

```python
npm install forever –g
```

然后就不要直接使用Node启动程序了，要用Forever启动它：

```python
forever start -a -l forever.log -o out.log -e err.log finalserver.js
```

其中的两个参数是有默认值的： `minUpTime` （默认为1 000ms）和 `spin SleepTime` （默认为1 000ms）。

这个命令会启动脚本finalserver.js，并指定了Forever日志、输入日志和错误日志。如果日志文件已经存在，它会告诉程序追加日志。

如果程序崩溃了，Forever就会重启它。如果你关闭了所运行程序的终端窗口，Forever还会确保程序的运行。

Forever既有参数，也有命令。刚刚命令行中的 `start` 就是命令的一个例子。全部的命令如下所示：

+ `start` ，启动一个脚本；
+ `stop` ，终止一个脚本；
+ `stopall` ，终止所有脚本；
+ `restart` ，重启一个脚本；
+ `restartall` ，重启所有正在运行的脚本；
+ `cleanlogs` ，删除所有的日志记录；
+ `logs` ，列出所有Forever进程的日志文件；
+ `list` ，列出所有在运行的脚本；
+ `config` ，列出用户配置；
+ `set <` `key` `> <` `val` `>` ，增加一项配置；
+ `clear <` `key` `>` ，删除项配置；
+ `logs <` `script` `|` `index` `>` ，对 `<` `script` `/` `index` `>` 的日志运行 `tail` 命令；
+ `columns add <` `col` `>` ，向Forever的输出列表中添加一列数据；
+ `columns rm <` `col` `>` ，从Forever的输出列表中删除一列数据；
+ `columns set <` `cols` `>` ，设置Forever的输出列表的数据显示格式。

下面是在httpserver.js脚本以Forever的daemon模式启动之后， `list` 命令输出的一个例子：

```python
info:    Forever processes running
data:       uid command           script         forever pid    id
logfile                             uptime
data:    [0] _gEN /usr/bin/nodejs serverfinal.js 10216   10225
/home/name/.forever/forever.log STOPPED
```

用 `logs` 命令列出所有的日志文件：

```python
info:   Logs for running Forever processes
data:       script         logfile
data:   [0] serverfinal.js /home/name/.forever/forever.log
```

除此之外，还有很多可以用的参数，包括刚刚展示过的日志文件设置，运行脚本的相关参数（ `-s` 或者 `--silent` ），打开Forever的日志模式（ `-v` 或者 `--verbose` ），以及设置脚本的源代码目录（ `--sourceDir` ），还有一些其他的参数。输入下面的命令就能看到：

```python
forever ––help
```

你也可以使用Forever的兄弟模块——forever-monitor，来将它集成到你的代码中。这个模块的文档介绍了如何进行集成：

```python
var forever = require('forever-monitor');
   var child = new (forever.Monitor)('serverfinal.js', {
     max: 3,
     silent: true,
     args: [] 
   }); 
   child.on('exit', function () {
     console.log('serverfinal.js has exited after 3 restarts');
   });
     child.start();
```

另外，你还可以将Forever和Nodemon结合使用。这样就不仅可以在程序崩溃之后进行重启，还可以在源代码更新时进行刷新。

使用下面的命令全局安装Nodemon：

```python
npm install -g nodemon
```

Nodemon会封装你的程序。所以请使用Nodemon替代Node来启动：

```python
nodemon app.js
```

Nodemon会默默地监控程序所在的目录（以及其中的子目录），并检查文件的修改。如果发现了文件的变化，它就会重启你的程序，这样最新的修改就能生效了。

你可以这样给Nodemon传递参数：

```python
nodemon app.js param1 param2
```

这个模块还可以配合CoffeeScript使用：

```python
nodemon someapp.coffee
```

如果你想监控应用所在目录之外的目录，可以使用 `--watch` 参数：

```python
nodemon --watch dir1 --watch libs app.js
```

关于其他的参数，请查阅模块的文档。

如果要搭配Nodemon来使用Forever，你需要将Nodemon封装到Forever中，并且给出 `--exitcrash` 参数，来确保如果应用崩溃了，Nodemon会完全退出，并将程序的控制权交给Forever：

```python
forever start nodemon --exitcrash serverfinal.js
```

如果出现报错，提示Forever找不到Nodemon，那么试试使用完整路径：

```python
forever start /usr/bin/nodemon --exitcrash serverfinal.js
```

这样一来，如果程序真的崩溃了，Forever会启动Nodemon，而Nodemon会启动Node脚本，这样就可以确保在修改代码时，不仅可以实时刷新，还可以确保发生不可预知的错误后你的程序可以重启。

