可以使用 `querystring` 模块解析 URL 中的参数，`querystring` 模块通常与 `url` 模块一起使用。（最新 Nodejs 已经弃用 `url` 模块中的 `parse` 方法，推荐使用 URL 类，请参考 [URL解析](./URL解析.md) ）

```js
var url = require('url')
var querystring = require('querystring')
var urlObj = url.parse('http://examples.burningbird.net:8124/?file=main');
var query = querystring.parse(urlObj.query)
console.log(query)
```

输出结果如下：

```console
[Object: null prototype] { file: 'main' }
```

使用 URL 类的方法如下：

```js
var urlObj = new URL('http://examples.burningbird.net:8124/?file=main');
console.log(urlObj.searchParams.get('file'))
```

输出结果如下：

```console
main
```

