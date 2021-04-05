### 20.10　Web服务器

虽然现在很多应用都在使用Node，但是它最初的目的其实是提供一个Web服务器。要是连这个用法都漏掉的话，那也太大意了。

如果读者曾经配置过Apache、IIS或者其他Web服务器，可能会惊讶于用Node创建一个可运行Web服务器是如此简单。http模块（以及它的安全版本，https模块）暴露了一个createServer方法，它可以创建一个基本的Web服务器。开发人员要做的仅仅是提供一个处理request的回调函数。在使用时，调用server的listen方法并指定一个端口，就能启动服务器。

```javascript
const http = require('http');
const server = http.createServer(function(req, res) {
    console.log(`${req.method} ${req.url}`);
    res.end('Hello world!');
}); 
const port = 8080;
server.listen(port, function() {
    // 可以传入一个callback来监听server的启动
    console.log(`server startd on port ${port}`);
}); 
```

> <img class="my_markdown" src="../images/2.png" style="width:116px;  height: 151px; " width="10%"/>
> 出于安全因素，大多数浏览器都不会让开发人员在没有权限的情况下监听默认的HTTP端口（80）。事实上，如果需要监听任何1024以下的端口，都需要相应的权限。当然获取权限也很容易：如果有sudo权限，可以直接用sudo来运行server，从而得到较高的权限，然后监听80端口（只要80端口没有被其他进程占用）。出于开发和测试的目的，一般来说，监听1024以上的端口比较常见。比如，3000、8000、3030或者8080都是常见的端口，之所以常用是因为这些端口很容易记住。

运行这段代码，然后在浏览器访问<a class="my_markdown" href="['http://localhost:8080']">http://localhost:8080</a> ，就能看到Hello world!。在console中打出了所有的request，它们是由一个方法（有时候也称为动作）和一个URL路径构成。大家可能会觉得奇怪，为什么每次访问那个URL都会出现两个request：

```javascript
GET /
GET /favicon.ico
```

大多数浏览器在访问URL的时候都会请求一个icon，用来显示在URL输出框或者浏览器标签中。浏览器会隐式地做这件事，所以才能在console中看到这条log。

Node web服务器的核心是开发人员提供的callback函数，它会处理所有服务器接收到的request。它接收两个参数，一个IncomingRequest对象（经常简写为req）和一个ServerRequest对象（经常简写为res）。IncomingRequest对象包含了所有与HTTP request相关的信息：请求的URL，以及可能存在的headers、body中发送的数据，等等。ServerRequest对象包含了会被发送到客户端（通常是浏览器）的response中的属性和方法。这里调用了req.end，如果想知道req是否为写入流，看看class头部就行了。ServerResponse对象实现了一个写入流的接口，用来定义如何向客户端写数据。由于ServerResponse对象是一个写入流，所以用它来发送文件很简单，可以直接创建一个文件读取流，然后通过管道把它传输到HTTP response中。比如，如果有可以让网页变得更好看的favicon.ico文件，那么就能察觉到这个request，并且直接发送对应的文件：

```javascript
const server = http.createServer(function(req, res) {
    if(req.method === 'GET' && req.url === '/favicon.ico') {
        const fs = require('fs');
        fs.createReadStream('favicon.ico');
        fs.pipe(res);       // 这行代码代替了调用‘end’
    } else {
        console.log('${req.method} ${req.url}');
        res.end('Hello world!');
    }
}); 
```

这是一个最小的web服务器，虽然看起来很无聊。通过 `IncomingRequest` 中的信息，可以扩展这个模型，从而创建任何想要的网站。

如果在用Node为网站提供服务，可能想了解一些有用的框架，比如，Express（http://expressjs.com/）或Koa（http://koajs.com/），从而避免从头搭建web服务器这种苦差事。

> <img class="my_markdown" src="../images/1.png" style="width:128px;  height: 170px; " width="10%"/>
> Express是一个非常流行的框架，Koa是它的继承者，这不是巧合：因为他们都是由TJ Holowaychuk编写的。如果读者已经熟悉了Express，那么使用Koa时就会得心应手。除此之外，还会享受到更趋近于ES6的web开发过程。

