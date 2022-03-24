可以通过如下代码来获取 GET 的请求参数：

```js
var name = require('url').parse(req.url, true).query.name;
```

上面的代码将获取 name 的参数，比如请求网址为: http://127.0.0.1:8124/?name=burningbird，则 name 的值为 burningbird。