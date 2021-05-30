可以通过如下方法获取 `get` 请求的参数：

```js
var name = require('url').parse(req.url, true).query.name;
```

