安装 `Underscore` 模块：

```console
$ npm install underscore
```

用下划线（ \_ ）可以访问 `Underscore` 库函数，`Underscore` 因此而得名。例如：

```js
var _ = require('underscore')
_.each(['apple', 'cherry'], function (fruit) { console.log(fruit) })
```

可以通过 `mixin` 方法用你自己的函数扩展 `Underscore` 的功能。

```js
var _ = require('underscore')
_.mixin({
  betterWithNode: function (str) {
    return str + ' is better with node'
  }
})

console.log(_.betterWithNode('chocolate'))
```

