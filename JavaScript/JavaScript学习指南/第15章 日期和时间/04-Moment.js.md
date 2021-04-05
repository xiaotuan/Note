### 15.3　Moment.js

虽然本书是一本关于JavaScript语言的书，而非关于类库的书，但由于日期操作非常重要而且常见，所以作者决定在这里介绍一个功能强大而且非常好用的日期类库：Moment.js。

Moment.js有两个版本：一种支持时区，一种不支持。由于支持时区的版本很大（因为它包含了全世界所有的时区信息），日常工作中可以选择不支持时区的版本。简单起见，后文中没有特殊说明的情况下，引用的都是支持时区的版本。如果想使用较小的版本，可以通过访问http://momentjs.com网站查找相关信息。

如果正在开发一个基于Web的项目，可以从像cdnjs这样的CDN中引用Moment.js：

```javascript
<script src="//cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.4.0/
moment-timezone.min.js"></script> 
```

如果在用Node，可以用 `npm install –save moment-timezone` 安装Moment.js，然后在代码中通过 `require` 引用它：

```javascript
const moment = require('moment-timezone');
```

Moment.js是一个很大的库，功能也很强大，如果需要操作日期，它几乎可以提供所有需要的功能。Moment.js还有一个非常详细的官方文档可供参考。（http:// momentjs.com/）。

