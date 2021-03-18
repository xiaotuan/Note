

### 10.2.2　Redis中的key/value存储

数据库有两种，一种是关系型数据库，另一种是非关系型数据库，而非关系型数据库，就是我们所说的NoSQL。在所有的NoSQL数据库中，有一种基于键/值（key/value）的数据结构，通常存储在内存中，从而能够提供极快的访问速度。3种最流行的基于内存的key/value存储分别是Memcached、Cassandra和Redis。Node开发人员应该感到高兴，因为Node对这3种存储都提供了支持。

Memcached主要用于缓存数据查询从而能快速访问内存中的数据。将它用于分布式计算也是一个不错的选择，只是它对复杂数据的支持有限。对于需要执行大量查询的应用程序，Memcached非常有用，但对于有大量数据写入和读取的应用程序来说则略逊一筹。对于后一种应用程序，Redis则是一个超棒的选择。Redis可以持久化，此外，它比Memcached提供了更多的灵活性，特别是在支持不同类型的数据时。美中不足的是，与Memcached不同，Redis只能在一台机器上工作。

Redis和Cassandra则比较相似。和Memcached一样的是，Cassandra支持集群。不一样的是，它对数据结构的支持有限。Cassandra对于ad hoc查询非常有用，Redis则不然。不过Redis使用简单，不复杂，而且要比Cassandra快很多。出于各种各样的原因，Redis在Node开发人员中获得了更多的关注。

> <img class="my_markdown" src="../images/103.png" style="zoom:50%;" />
> **EARN**
> EARN（Express、AngularJS、Redis和Node）这个缩写让人读起来很有感觉。在The EARN Stack中有一个关于EARN的例子。

我推荐使用Node中的Redis模块，用npm就可以安装：

```python
npm install redis
```

如果你打算在Redis上进行一些大型操作，我还建议安装Node模块支持hiredis，因为它是非阻塞的，可以提高性能：

```python
npm install hiredis redis
```

Redis模块只对Redis进行了一层简单的封装。因此，你需要自己花时间学习Redis命令以及Redis数据存储的工作原理。

在Node应用中使用Redis时，要先引入模块：

```python
var redis = require('redis');
```

接着需要使用 `createClient` 方法创建一个Redis客户端：

```python
var client = redis.createClient();
```

`createClient` 方法有3个可选的参数： `port、host` 和 `options` （稍后讲解）。默认的 `host` 是127.0.0.1， `port` 是6379。这个端口就是Redis服务器的默认端口，所以如果Redis服务器与Node应用运行在同一台机器上，那么使用默认设置就可以工作。

第3个参数是一个对象，它支持一些选项，Redis模块的文档中有详细介绍。在熟悉Node和Redis前，使用默认设置就可以了。

一旦客户端连接到Redis数据库，你就可以给服务器发送命令了，直到调用 `client.quit()` 方法关闭应用程序与Redis服务的连接。如果想要强制关闭，可以使用client.end()方法。不过，后一种方法并不会等所有的返回值都被解析才断开。如果应用程序无响应或者你想重新开始运行程序，就可以使用 `client.end()` 。

通过客户端连接发送Redis命令是一个相当直观的过程。所有命令都作为客户端对象上的方法暴露出来，而所有命令的参数都可以作为方法的参数传递。由于这是Node，所以最后一个参数是一个回调函数，回调函数的参数是一个错误对象和Redis命令的返回结果。

在下面的代码中，我们用 `client.hset()` 方法设置了一个 `hash` 属性。在Redis中， `hash` 是字符串格式的字段和值的映射（mapping），比如“lastname”对应姓氏，而“firstname”对应名字，以此类推：

```python
client.hset("hashid", "propname", "propvalue", function(err, reply) {
   // do something with error or reply
});
```

`hset` 命令是用来设置值的，没有返回数据，因为存在Redis里面了。如果调用一个能获取多个值的方法，如 `client.hvals` ，则回调函数中的第二个参数将是一个数组——可以是字符串数组或对象数组：

```python
client.hvals(obj.member, function (err, replies) {
   if (err) {
      return console.error("error response - " + err);
   }
   console.log(replies.length + " replies:");
   replies.forEach(function (reply, i) {
     console.log("    " + i + ": " + reply);
   });
});
```

由于Node的回调函数很普及，且很多Redis命令都是返回成功确认的操作，因此Redis模块提供了 `redis.print` 方法，该方法可以作为回调函数的最后一个参数传入：

```python
client.set("somekey", "somevalue", redis.print);
```

`redis.print` 函数会将错误信息或者控制台中返回的内容打印出来，然后返回。

为了在Node中演示Redis，我创建了一个消息队列（message queue）。消息队列是一种应用程序，它将某种形式的通信作为输入，然后存储到队列中。消息一直存储在队列中，直到被接收方取走，此时消息会被移出队列，发送给接收方（每次一条或者批量进行）。通信是异步的，因为存储消息的应用不要求接收器保持连接，接收器也不要求消息存储应用保持连接。

Redis是这种应用的理想存储介质。当消息被存储它们的应用程序接收时，它们被添加到队尾。当消息被接收它们的应用程序取出时，它们将从队首取出。

> <img class="my_markdown" src="../images/104.png" style="zoom:50%;" />
> **了解一些TCP、HTTP和子进程相关的知识**
> 这个Redis的例子由一个TCP服务器（因此使用了Node的Net模块）、一个HTTP服务器和一个子进程组成。第5章介绍了HTTP，第7章介绍了Net，第8章介绍了子进程。

在演示消息队列时，我创建了一个Node应用程序来访问几个不同子域名下的Web日志文件。应用程序用了Node子进程和UNIX的 `tail-f` 命令来访问不同日志文件的最新记录。

在访问这些日志记录时，应用程序使用了两个正则表达式对象：第一个用来提取访问到的资源的内容，第二个用来检测资源是否为图片文件。如果被访问的资源是图片文件，应用程序就把该资源的URL通过TCP消息发送到消息队列的应用程序中。

消息队列程序所做的事情就是在3000端口监听消息，然后将接收到的所有内容都发送到Redis数据库进行存储。

示例程序的第三部分是一个在8124端口监听请求的Web服务器。对于每个请求，它都会访问Redis数据库并取出图像数据库中靠前的记录，通过响应对象返回这条记录。如果Redis数据库在请求图片资源时返回 `null` ，则会打印出一条消息，表明应用程序已到达消息队列的末尾。

程序的第一部分在处理Web日志记录，如例10-2所示。UNIX的 `tail` 命令可以显示文本文件（或管道中的数据）的最后几行。当加上 `-f` 参数时，将会显示文件中几行然后暂停，并监听新的日志记录。一旦有新的记录，它就会将其打印出来。 `tail –f` 也可以用于需要同时监听多个文件的情况，它可以通过给数据打标签（标出其来源）的方式来管理这些内容。这个命令并不关心最新的记录来自哪个文件——它只关心日志本身。

一旦程序拿到了日志（log），它就会对数据进行正则表达式匹配，从而发现可以访问的图片资源（文件扩展名为.jpg、.gif、.svg或者.png）。如果匹配成功，就把资源URL发送到消息队列程序（一个TCP服务器）。程序很简单，它不会去检查字符串到底是文件后缀名还是嵌入在文件名中，比如this.jpg.html。对于这样的文件名，你会得到一个假阳性（false positive）结果。不过只要它能演示Redis的用法就够了。

**例10-2　处理Web日志并将图片资源请求发送到消息队列的Node程序**

```python
var spawn = require('child_process').spawn;
var net = require('net');
var client = new net.Socket();
client.setEncoding('utf8');
// connect to TCP server
client.connect ('3000','examples.burningbird.net', function() {
    console.log('connected to server');
});
// start child process
var logs = spawn('tail', ['-f',
        '/home/main/logs/access.log',
        '/home/tech/logs/access.log',
        '/home/shelleypowers/logs/access.log',
        '/home/green/logs/access.log',
        '/home/puppies/logs/access.log']);
// process child process data
logs.stdout.setEncoding('utf8');
logs.stdout.on('data', function(data) {
   // resource URL
   var re = /GET\s(\S+)\sHTTP/g;
   // graphics test
   var re2 = /\.gif|\.png|\.jpg|\.svg/;
   // extract URL
   var parts = re.exec(data);
   console.log(parts[1]);
   // look for image and if found, store
   var tst = re2.test(parts[1]);
   if (tst) {
      client.write(parts[1]);
   }
});
logs.stderr.on('data', function(data) {
   console.log('stderr: ' + data);
});
logs.on('exit', function(code) {
   console.log('child process exited with code ' + code);
   client.end();
});
```

这个程序会输出如下所示的典型的控制台日志记录，需要关注的部分（图片文件访问）已用粗体标出：

```python
/robots.txt
/weblog
/writings/fiction?page=10
/images/kite.jpg
/node/145
/culture/book-reviews/silkworm
/feed/atom/
/images/visitmologo.jpg
/images/canvas.png
/sites/default/files/paws.png
/feeds/atom.xml
```

例10-3包含了消息队列的代码。这个简单的程序会启动一个TCP服务器然后监听发送来的消息。当它接收到消息时，会抽取其中的数据存储到Redis数据库中。这个程序用Redis的 `rpush` 命令将数据存入图片列表的末尾（在代码中加粗标出）。

**例10-3　接收消息并将它存入Redis列表的消息队列**

```python
var net = require('net');
var redis = require('redis');
var server = net.createServer(function(conn) {
   console.log('connected');
   // create Redis client
   var client = redis.createClient();
   client.on('error', function(err) {
     console.log('Error ' + err);
   }); 
   // sixth database is image queue
   client.select(6);
   // listen for incoming data
   conn.on('data', function(data) {
      console.log(data + ' from ' + conn.remoteAddress + ' ' +
        conn.remotePort);
      // store data 
      client.rpush('images',data);
   }); 
}).listen(3000);
server.on('close', function(err) {
   client.quit();
}); 
console.log('listening on port 3000');

```

下面是消息队列程序的控制台日志：

```python
listening on port 3000
connected
/images/venus.png from 173.255.206.103 39519
/images/kite.jpg from 173.255.206.103 39519
/images/visitmologo.jpg from 173.255.206.103 39519
/images/canvas.png from 173.255.206.103 39519
/sites/default/files/paws.png from 173.255.206.103 39519
```

消息队列程序的最后一个需要演示的功能是监听8124端口的HTTP服务器，如例10-4所示。每当HTTP服务器接收到一个请求，它都会访问Redis数据库，取出图片列表中的下一条记录，并打印到响应（response）中。如果队列中没有内容了（例如，Redis返回 `null` ），则返回一条消息说消息队列为空。

**例10-4　从Redis列表中取出信息并将它返回给HTTP服务器**

```python
var redis = require("redis"),
    http = require('http');
var messageServer = http.createServer();
// listen for incoming request
messageServer.on('request', function (req, res) {
   // first filter out icon request
   if (req.url === '/favicon.ico') {
      res.writeHead(200, {'Content-Type': 'image/x-icon'} );
      res.end();
      return;
   } 
   // create Redis client
   var client = redis.createClient();
   client.on('error', function (err) {
     console.log('Error ' + err);
   }); 
   // set database to 6, the image queue
   client.select(6);
   client.lpop('images', function(err, reply) {
      if(err) { 
        return console.error('error response ' + err);
      }
      // if data
      if (reply) {
         res.write(reply + '\n');
      } else {
         res.write('End of queue\n');
      }
      res.end();
   });
   client.quit();
});
messageServer.listen(8124);
console.log('listening on 8124');
```

通过浏览器访问HTTP服务器时，每个请求都会返回一个图片资源URL，直到消息队列为空。

这个例子涉及的数据很简单，但可能非常多，这也是它适合使用Redis的原因。Redis是一个快速、简单的数据库，而且不用花费太多精力就能将它集成到Node程序中。

> **何时创建Redis客户端**
> 当我使用Redis时，有时候会创建一个Redis客户端让它始终存在于程序中，而有时则在Redis命令结束后就释放之前创建的Redis客户端。那么什么时候应该创建一个持久的Redis连接？什么时候又该建立连接并在结束使用后立即释放呢？
> 好问题。
> 为了测试这两种不同的策略，我创建了一个TCP服务器，用来监听请求（request）并一个将简单的散列值存入Redis数据库。接着我创建了另一个应用程序作为TCP客户端，它只负责将对象搭载在TCP消息中发送给服务器。
> 我用ApacheBench程序并发运行一些客户端，并重复这个过程，每次运行后测试其运行时间。首先运行那些使用了持久Redis连接的程序，接着运行那些为每个请求建立数据库连接、但使用之后就立即释放连接的程序。
> 我期望的测试结果是拥有持久化客户端连接的程序运行较快，结果证明在某种程度上，我是对的。大约在测试到一半的时候，建立持久连接的应用程序在一段很短的时间内处理速度急剧降低，然后恢复了相对较快的速度。
> 当然，最可能发生的情况是，在队列中等待的Redis数据库请求最终会（至少是短暂的）阻塞Node程序，直到队列被清空。而每一次请求都需要打开和关闭连接时，并不会发生类似的情况，因为这个过程所需的额外开销会减慢应用程序的运行速度，刚好没有达到数据库并发访问的上限。

