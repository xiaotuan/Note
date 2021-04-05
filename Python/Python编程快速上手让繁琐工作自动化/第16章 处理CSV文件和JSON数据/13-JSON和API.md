### 16.3　JSON和API

JavaScript对象表示法是一种流行的方式，可将数据格式化为人可读的字符串。JSON是JavaScript程序编写数据结构的原生方式，类似于Python的 `pprint()` 函数产生的结果。不需要了解JavaScript，你也能处理JSON格式的数据。

下面是JSON格式数据的一个例子：

```javascript
{"name": "Zophie", "isCat": true,
 "miceCaught": 0, "napsTaken": 37.5,
 "felineIQ":  null}
```

了解JSON是很有用的，因为很多网站都提供JSON格式的内容作为程序与网站交互的方式。这就是所谓的提供“应用程序编程接口”（Application Programming Interface，API）。访问API和通过URL访问任何其他网页是一样的。不同的是，API返回的数据是针对机器格式化的（例如用JSON），API不是人容易阅读的。

许多网站用JSON格式提供数据。Facebook、Twitter、Yahoo、Google、Tumblr、Wikipedia、Flickr、Data.gov、Reddit、IMDb、Rotten Tomatoes、LinkedIn和许多其他流行的网站，都提供API让程序使用。有些网站需要注册，这几乎是免费的。你必须找到文档，了解程序需要请求什么 URL 才能获得想要的数据，以及返回的JSON数据结构的一般格式。这些文档应在提供API的网站上获取，如果它们有“Developers”页面，就去那里找找。

利用API，可以编程完成下列任务。

+ 从网站抓取原始数据（访问API通常比下载网页并用Beautiful Soup解析HTML更方便）。
+ 自动从一个社交网络账户下载新的帖子，并发布到另一个账户。例如，可以把Tumblr的帖子上传到Facebook。
+ 从IMDb、Rotten Tomatoes和维基百科提取数据，将其放到计算机的一个文本文件中，以为你个人的电影收藏创建一个“电影百科全书”。

JSON并不是将数据格式化为人类可读字符串的唯一方式。还有许多其他的格式，包括XML（eXtensible Markup Language）、TOML（Tom's Obvious, Minimal Language）、YML（Yet another Markup Language）、INI（Initialization），甚至是过时的 ASN.1（Abstract Syntax Notation One）格式，这些格式都提供了一种结构，可将数据重新表示为人可读的文本。本书不会涉及这些格式，因为JSON已经迅速成为广泛使用的替代格式，但有一些第三方的Python模块可以轻松处理这些格式。

