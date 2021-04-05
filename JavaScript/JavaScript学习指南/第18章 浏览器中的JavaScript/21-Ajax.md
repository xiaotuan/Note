### 18.12　Ajax

Ajax（它来源于“Asynchronous JavaScript and XML”的首字母缩写）允许客户端与服务端进行异步通信：页面上的元素在不加载整个页面的情况下刷新服务器（server）端的数据。在本世纪初引入 `XMLHttpRequest` 对象之后，这个创新才得以实现，从而开启了众所周知的“Web 2.0”时代。

Ajax的核心概念很简单：运行在浏览器端的JavaScript以可编程的的方式将HTTP request发送到server，server再返回所请求的数据，这种数据通常以JSON格式传输（在JavaScript中，JSON格式比XML格式更容易使用）。这些数据可以在浏览器上实现更多的功能。Ajax是基于HTTP的（像不使用Ajax的页面一样），这样一来，就降低了渲染和传输页面的开销，从而提高了Web应用的性能，至少从用户角度来看是这样的。

使用Ajax之前，必须得先有一个服务器（server）。这里用Node.js（先预习一下20章的内容）写一个最简单的服务器，它会暴露一个Ajax的endpoint（一个被其他服务或应用使用的特殊service）。创建一个叫作ajaxServer.js的文件：

```javascript
const http = require('http');
const server = http.createServer(function(req, res) {
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.end(JSON.stringify({
        platform: process.platform,
        nodeVersion: process.version,
        uptime: Math.round(process.uptime()),
    }));
}); 
const port = 7070;
server.listen(port, function() {
    console.log(`Ajax server started on port ${port}`);
});
```

这段代码创建了一个非常简单的server，它可以说明当前使用的操作系统（“linux”“darwin”“win32”等）、Node.js的版本和server的启动时间。

> <img class="my_markdown" src="../images/2.png" style="width:116px;  height: 151px; " width="10%"/>
> Ajax引入了一个叫作跨资源共享（CORS- cross-origin resource sharing）的安全漏洞。在本例中，在header中将Access-Control-Allow-Origin的值设为*，这告诉客户端不要因为安全问题而阻止调用。在产品环境上，一般不会使用跟本地环境一样的网络协议、域名和端口号（默认允许访问任何端口），或指明可以访问endpoint的协议、域名和端口号。这里为了演示功能，禁用了CORS的检查。

运行下面这行命令可以启动server：

```javascript
$ babel-node ajaxServer.js
```

在浏览器中打开<a class="my_markdown" href="['http://localhost:7070']">http://localhost:7070</a> ，就可以看到server的输出。有了一个server之后，就可以在HTML页面（可以继续沿用本章中一直使用的那个页面）中编写Ajax代码了。首先在body中添加一个占位符，用来接收信息：

```javascript
<div class="serverInfo">
    Server is running on <span data-replace="platform">???</span>
    with Node <span data-replace="nodeVersion">???</span>.  It has
    been up for <span data-replace="uptime">???</span> seconds.
</div> 
```

这样就有了存放从server端获取到的数据的地方了，然后就可以使用XMLHttpRequest执行Ajax调用。在HMTL文件的最下面（在闭合标签</body>的前面），添加如下代码：

```javascript
<script type="application/javascript;version=1.8">
    function refreshServerInfo() {
        const req = new XMLHttpRequest();
        req.addEventListener('load', function() {
            // TODO: 将这些值放在HTML中
            console.log(this.responseText);
        });
        req.open('GET', 'http://localhost:7070', true);
        req.send();
    }
    refreshServerInfo();
</script>
```

这段脚本执行了一个基本的Ajax调用。首先，它创建了一个新的XMLHttpRequest对象，接下来添加一个监听器来监听load事件（在Ajax调用成功的时候会被调用）。现在只是把server端的response（在this.responseText中）打印到console中。接下来调用open，才真正建立了跟server端的连接。调用open的时候明确指明这是一个HTTP GET请求，这种方式与在浏览器地址栏上输入网址来打开页面是一样的（还有POST、DELETE等方法），open方法还接收一个server端的URL。最后，调用send，这才是真正执行request的地方。在本例中，并没有显式地向server端发送任何数据，虽然可以这么做。

运行这个例子，就能在console中看到server端返回的数据了。下一个目标是把这些数据插入到HTML中。此时需要构建一个HTML，这样就可以查找那些具有replace这个数据属性的元素了，然后将元素中的内容替换成server端返回的数据。为了实现这个，将server端返回的数据进行迭代（使用Object.keys），如果其中的内容可以匹配replace的数据属性，就执行替换操作：

```javascript
req.addEventListener('load', function() {
    // this.responseText 是一个包含JSON的字符串; 
    //使用JSON.parse 将它转换成对象
    const data = JSON.parse(this.responseText);
    // 在本例中，我们只想替换<div>中含有“serverInfo“这个class的元素的文本
    const serverInfo = document.querySelector('.serverInfo');
    // 迭代从server端返回的对象中的key
    // ("platform", "nodeVersion", and "uptime"):
    Object.keys(data).forEach(p => {
        // 查找替换属性的元素（如果有的话）
        const replacements =
            serverInfo.querySelectorAll(`[data-replace="${p}"]`);
        // 将所有元素中的内容替换成从server返回的数据
        for(let r of replacements) {
            r.textContent = data[p];
        }
    }); 
}); 
```

因为refreshServerInfo是一个函数，所以可以在任何时候调用它。特别是需要定期更新server端信息（这也是为什么这里添加了一个uptime的字段）的时候。比如，希望每秒更新5次server端的信息（也就是200毫秒一次），以下是具体的代码实现：

```javascript
setInterval(refreshServerInfo, 200);
```

通过这段代码，可以在浏览器中看到server的启动时间在动态增加！

> <img class="my_markdown" src="../images/2.png" style="width:116px;  height: 151px; " width="10%"/>
> 在这个例子中，页面最开始加载的时候，<div class=“.serverInfo”>包含了一个用问号表示的占位符。在网速很慢的时候，用户可能会在内容被替换成server端的数据之前看到这些问号一闪而过。这是“闪现未加载样式内容（FOUC）”问题的变种。一种解决方案是在页面初次加载的时候就把server端的数据渲染到页面上。另一种解决方案是在内容被更新前先把元素隐藏起来；这可能还是会让用户觉得不快，但这比出现无意义的问号更容易让用户接受。

这里只介绍了关于发送Ajax请求的基本概念，想了解更多的话，可以参考MDN的文档“使用XMLHttpRequest”。

