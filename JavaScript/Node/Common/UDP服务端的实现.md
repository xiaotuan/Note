UDP 服务端实现代码如下所示：

```js
var dgram = require('dgram')

var server = dgram.createSocket('udp4')

server.on('message', function (msg, rinfo) {
   console.log("Message: " + msg + " from " + rinfo.address + ":" + rinfo.port)
})

server.bind(8124)
```

