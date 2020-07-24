**示例1-1 Node版Hello, World**

helloword.js

```js
// load http module
var http = require('http')

// create http server
http.createServer(function (req, res) {
    // content header
    res.writeHead(200, {'content-type': 'text/plain'})
    
    // write message and signal communication is complete
    res.end("Hello, World!\n")
}).listen(8124)

console.log('Server running on 8124')
```

可以在 `Linux` 系统中使用命令行，或在 `Mac OS` 中使用终端窗口，或在 `Windows` 中使用命令窗口，运行如下命令来启动示例程序：

```console
node hellowrld.js
```

现在可以在浏览器中输入 `localhost:8124` 地址访问站点。

> 警告：
> 如果是在 `Fedora` 系统中安装 `Node` 环境，需要留意 `Node` 会被重命名，以避免与系统中现有功能的冲突。

如果想在后台运行应用程序，在 `Linux` 系统中可以使用如下命令：

```console
node helloworld.js &
```

之后，你需要通过 "ps -ef" 命令找到进程对应的 ID，然后使用 kill 命令手动关闭该进程：

```console
ps -ef | grep node
kill 3747
```

> 警告
> `WebMatrix` 会覆盖 `Node` 程序中使用的端口号。当你运行应用程序后，你只能通过项目中定义好的端口访问站点，而不能使用在 `http.Server.listen` 方法中指定的端口。

`end` 方法有两个参数：

+ 一个数据块，可以是一个字符串或者 buffer 对象；
+ 如果数据库是字符串对象，第二个参数用于指定编码方式。

这两个参数都是可选的，而且只有在字符串是非 utf-8 编码的情况下才需要指定第二个参数，因为其默认值是 utf-8。

我们也可以不在 end 方法中传递数据块，而使用另一个 write 方法：

```js
res.write("Hello, World!\n")
res.end()
```

`http.Server.listen` 方法紧接在 `createServer` 之后调用，用于在指定端口监听接入的客户端连接。它的可选参数是一个 hostname 和一个回调函数。如果指定了 hostname，客户端将能通过 Web 地址的形式访问服务端，比如：http://oreilly.com 。
