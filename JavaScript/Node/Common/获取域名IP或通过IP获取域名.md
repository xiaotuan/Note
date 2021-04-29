获取域名 IP 的代码如下所示：

```js
var dns = require('dns')

dns.lookup('www.baidu.com', function (err, ip) {
  if (err) throw err
  console.log(ip)
})

dns.reverse('173.255.206.103', function (err, domains) {
  domains.forEach( function (domain) {
    console.log(domain)
  })
})

dns.resolve('burningbird.net', 'NS', function (err, domains) {
  domains.forEach(function (domain) {
    console.log(domain)
  })
})
```

