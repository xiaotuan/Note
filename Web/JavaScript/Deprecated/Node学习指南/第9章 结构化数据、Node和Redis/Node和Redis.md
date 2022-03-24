> 提示：`Redis` 的网址：<https://redis.io/>。更多有关 `Memcached` 的信息：<http://memcached.org/>，以及 `Apache Cassandra` 的网址：<https://cassandra.apache.org/>。

支持 `Redis` 的模块有很多，例如 `Redback`，它提供了一个高抽象层次的接口。但在本章中，我们将关注另一个由 `Matt Ranney` 编写的 `node_redis` 模块。

> `node_redis` 的 `GitHub` 页面在 <https://github.com/mranney/node_redis>。

使用 npm 安装 redis 模块：

```console
$ npm install redis
```

我同样也建议使用 hiredis 库，因为它是非阻塞的且能提高性能。使用下面的命令安装它：

```console
$ npm install hiredis redis
```

想要在 `Node` 应用程序中使用 `node-redis` 的话，首先要包含模块：

```js
var redis = require('redis')
```

然后，使用 `createClient` 方法创建一个 `Redis` 客户端：

```js
var client = redis.createClient();
```

`createClient` 方法包含三个可选参数： port，host 和 options。host 默认值为 127.0.0.1，port 默认值为 6379。port 的默认值也是 Redis 服务器默认使用的端口号，所以如果 Redis 服务器与 Node 应用程序都托管在同一台机器上的话，就无需修改这些默认值了。

第三个参数是一个对象，它所支持的选项如下:

*parser*

`Redis` 协议 replay 解析器，默认为 hiredis。也可以使用 javascript。

*return_buffers*

默认为 false。如果为 true，所有的回复将以 Node buffer 对象返回，而不是字符串。

*detect_buffers*

默认为 false。若为 true 并且有原始操作命令被缓存起来时，回复信息将被包装在 Node buffer 对象中。

*socket_nodelay*

默认为 true，指定是否在 TCP 流中调用 setNoDelay。

*no_ready_check*

默认为 false。设置为 true 时，会阻止 "ready check" 被发送到服务器，以便准备更多的命令。

一旦建立了客户端与 `Redis` 数据存储系统的连接，你就可以发送命令给服务器直到调用 `client.quit` 方法关闭该连接。如果想强制关闭连接，你可以调用 `clent.end` 方法，该方法不会等待答复解析完毕。

在下面的代码中，我们使用 `client.hset` 方法设置哈希属性：

```js
client.hset("hashid", "propname", "propvalue", function (err, reply) {
  // do something with error or reply
})
```

`hset` 命令可设置一个值，因此没有返回数据，只返回 `Redis` 的确认信息。如果你调用了一个可以返回多个值的方法。例如 `client.hvals`，那么在回调函数的第二个参数中将会保存字符串数组或者是对象组：

```js
client.hvals(obj.member, function (err, replies) {
  if (err) {
    return console.error("error response - " + err)
  }
  
  console.log(replies.length + ' replies: ')
  replies.forEach(function (reply, i) {
    console.log(" " + i + ": " + reply)
  })
})
```

因为 `Node` 回调无所不在，但很多 `Redis` 命令的返回信息仅包含了类似于操作成功的确认回复。因此，`node_redis` 模块提供了 `node_redis.print` 方法，你可以将其作为回调函数的最后一个参数传入：

```js
client.set('somekey', 'somevalue', redis.print);
```

`redis.print` 方法会将错误信息或答复内容输出到控制台并返回。

> 注意：要使用 `Redis` 必须在电脑上安装 `Redis` 客户端，`Windows` 客户端可以从 <https://github.com/MicrosoftArchive/redis/releases> 中下载。