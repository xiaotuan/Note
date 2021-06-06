可以通过如下方法获取 `get` 请求的参数：

```js
var name = require('url').parse(req.url, true).query.name;
```

> 提示：`url` 模块的很多方法已经过期，文档中推荐使用 `URL` 类来代替。具体使用方法请参阅 [URL类的使用](./URL类的使用.md) 。

