[toc]

### 3.4.3　无所不在的Underscore

使用下面的命令安装Underscore：

```python
npm install underscore
```

对于开发者而言，Underscore是一个Node的实用工具库。它提供了很多我们已经习惯在第三方框架（如jQuery和Prototype.js）中使用的JavaScript扩展功能。

Underscore名称的由来是因为，它的功能都是通过下划线（）来调用的，类似于jQuery的$，如下所示：

```python
var _ = require('underscore');
_.each(['apple','cherry'], function (fruit) { console.log(fruit); });
```

当然，使用下划线也有问题，因为它在REPL中有特殊的含义，下一章会介绍。不过不用担心，我们还可以用另一个变量——us：

```python
var us = require('underscore');
us.each(['apple','cherry'], function(fruit) { console.log(fruit); });
```

Underscore提供了很多扩展功能，涵盖了数组、集合、函数、对象、调用链以及通用工具。幸运的是，它也提供了所有功能的优秀文档，在它的网站上就可以看到，这里就不赘述了。

它还有一个值得一提的功能：可以使用mix函数将你自己的工具函数集成到Underscore中。我们可以在REPL会话中快速地体验这个方法：

```python
> var us = require('underscore');
> us.mixin({
... betterWithNode: function(str) {
..... return str + ' is better with Node';
..... }
... });
> console.log(us.betterWithNode('chocolate'));
chocolate is better with Node
```

> <img class="my_markdown" src="../images/55.png" style="zoom:50%;" />
> 你会发现很多Node模块中都是用了mixin这个概念。这种做法是基于这样一种模式的，即一个对象中的属性被加入（“mixed in”）到另一个对象中。

Underscore并非唯一的高分工具模块，另一个叫lodash，也是一个很实用的工具。除非你已经安装了其中一种了，否则我推荐同时安装这两个工具。lodash的网站上包含这个模块的完整文档。



