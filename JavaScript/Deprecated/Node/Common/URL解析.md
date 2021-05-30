可以使用 URL 模块对 URL 的各个部分进行解析：

```js
var url = require('url')
var urlObj = url.parse('http://examples.burningbird.net:8124/?file=main');
console.log(urlObj)
```

输出结果如下：

```console
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

可以通过 `url.format(urlObj)` 方法将解析后的对象重新生成 URL。

```js
url.format(urlObj)
```

> 警告：`url` 模块中的 `parse` 方法已经标注为过时，建议使用 URL 类进行替换。URL 类的使用方法如下：
>
> ```js
> const myURL =
>   new URL('https://user:pass@sub.host.com:8080/p/a/t/h?query=string#hash');
> console.log(myURL)
> ```
>
> 输出结果如下所示：
>
> ```console
> URL {
>   href: 'https://user:pass@sub.host.com:8080/p/a/t/h?query=string#hash',
>   origin: 'https://sub.host.com:8080',
>   protocol: 'https:',
>   username: 'user',
>   password: 'pass',
>   host: 'sub.host.com:8080',
>   hostname: 'sub.host.com',
>   port: '8080',
>   pathname: '/p/a/t/h',
>   search: '?query=string',
>   searchParams: URLSearchParams { 'query' => 'string' },
>   hash: '#hash'
> }
> ```
>
> 依旧可以使用 `url.format()` 方法将 myURL 转换成 URL 字符串。
> 
> ```js
> var url = require('url')
> url.format(myURL)
> ```

