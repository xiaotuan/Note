### 3.5 域名解析和 URL 处理

使用 `dns.lookup` 方法可以解析并得到一个域名的 IP 地址，在下面的代码中，我们会将解析到的 IP 地址输出到终端：

```js
var dns = require('dns');
dns.lookup('burningbird.net', function(err, ip) {
    if (err) throw err;
    console.log(ip);
});
```

使用 `dns.reverse` 方法则会根据给定的 IP 地址返回一组域名：

```js
dns.reverse('173.255.206.103', function(err, domains) {
    domains.forEach(function(domain) {
        console.log(domain);
    });
});
```

`dns.resolve` 方法会根据指定的记录类型返回一组记录，常见的记录类型有 A、MX、NS 等。下面的代码描述了如何查找出解析域名 "burningbird.net"  所用的域名服务器：

```js
var dns = require('dns');
dns.resolve('burningbird.net', 'NS', function(err, domains) {
    if (err) throw err;
    domains.forEach(function(domain) {
        console.log(domain);
    });
});
```

URL 模块可以提供 URL 解析功能，并能返回一个对象来描述 URL 中的所有信息。如下代码所示：

```js
var url = require('url')
var urlObj = url.parse('http://examples.burningbird.net:8124/?file=main');
console.log(urlObj)
```

返回值为一个 JavaScript 对象：

```json
Url {
  protocol: 'http:',
  slashes: true,
  auth: null,
  host: 'examples.burningbird.net:8124',
  port: '8124',
  hostname: 'examples.burningbird.net',
  hash: null,
  search: '?file=main',
  query: 'file=main',
  pathname: '/',
  path: '/?file=main',
  href: 'http://examples.burningbird.net:8124/?file=main' }
```

对象中的每个属性可以被分别访问，像这样：

```js
var qs = urlObj.query;	// 获得查询字符串
```

调用 `URL.format` 方法可以执行相反的操作：

```js
console.log(url.format(urlObj));	// 返回原始 URL
```

URL 模块常常与 Query String 模块一并使用。可以使用 `querystring.parse` 方法取得查询字符串中的键值对。如下所示：

```js
var vals = querystring.parse('file=main&file=secondary&type=html');
```

你同意可以使用一个保存有键值对的对象转换为查询字符串，使用 `querystring.stringify` 方法即可：

```js
var qryString = querystring.stringify(vals);
```

