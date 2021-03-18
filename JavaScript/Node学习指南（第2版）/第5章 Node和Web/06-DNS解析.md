[toc]

### 5.5　DNS解析

你的大多数程序可能都不会直接使用DNS服务，但是如果用到了，核心的DNS模块会提供此类功能。

我们来看看DNS模块中的两个函数： `dns.lookup()` 和 `dns.resolve()` 。 `dns. lookup()` 函数可以获取一个域名的第一个IP地址。在下面的代码中，返回的结果是找到的第一个epubit.com的IP地址：

```python
dns.lookup('epubit.com', function(err,address,family) {
     if (err) return console.log(err);
     console.log(address);
     console.log(family);
});
```

Address就是返回的IP地址，而 `family` 的值是4还是6，取决于这个地址是IPv4还是IPv6。你可以指定一个 `option` 对象。

+ `family` ，一个数字，4或者6，代表你想要的地址类型（IPv4或者IPv6）。
+ `hints` ，支持 `getaddrinfo` 参数，一个数字。
+ `all` ，如果为true，返回所有的地址（默认为false）。

我想得到所有的IP地址，所以我修改了代码，让它能返回所有的IP地址。同时，我又去掉了 `family` 参数，所以在获取所有的地址时，它就是 `undefined` 。运行这段代码，我得到了一个可用的IP地址对象列表，包含IP地址和类型（ `family` ）：

```python
dns.lookup('epubit.com', {all: true}, function(err,family) {
     if (err) return console.log(err);
     console.log(family);
});
```

返回值是：

```python
[ { address: '209.204.146.71', family: 4 },
  { address: '209.204.146.70', family: 4 } ]
```

`dns.resolve()` 函数则用于解析一个主机名的记录类型。可能的类型（字符串格式）如下：

+ A，默认的IPv4地址；
+ AAAA，IPv6地址；
+ MX，邮件交换记录；
+ TXT，文本记录；
+ SRV，SRV记录；
+ PTR，用于反向IP查找；
+ NS，名字服务器；
+ CNAME，别名记录；
+ SOA，SOA记录。

在下面的例子中，我使用 `dns.resolve()` 来获取epubit.com的MX记录：

```python
dns.resolve('epubit.com','MX', function(err,addresses) {
   if (err) return err;
   console.log(addresses);
});
```

返回值为：

```python
[ { exchange: 'aspmx.l.google.com', priority: 1 },
  { exchange: 'alt1.aspmx.l.google.com', priority: 5 },
  { exchange: 'aspmx2.googlemail.com', priority: 10 },
  { exchange: 'alt2.aspmx.l.google.com', priority: 5 },
  { exchange: 'aspmx3.googlemail.com', priority: 10 } ]
```



