`underscore` 名称的由来是因为，它的功能都是通过下划线 (`-`) 来调用的，类似于 `jQuery` 的 `$`，如下所示：

```js
var _ = require('underscore')
_.each(['apple', 'cherry'], function (fruit) {
    console.log(fruit);
});
```

它还有一个值得一提的功能：可以使用 `mixin` 函数将你自己的工具函数集成到 `underscore` 中。

```js
var us = require('underscore')
us.mixin({
    betterWithNode: function(str) {
        return str + ' is better with Node';
    }
});
console.log(us.betterWithNode('chocolate'));
```

> 提示：
>
> `underscore` 模块的其他用法请参阅 <https://underscorejs.net/>。