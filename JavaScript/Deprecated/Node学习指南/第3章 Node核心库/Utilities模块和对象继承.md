### 3.6 Utilities 模块和对象继承

`Utilities` 模块提供了一些非常实用的功能。你可以通过 `util` 来包含这个模块：

```js
var util = require('util');
```

你可以使用 Utilities 模块来测试一个对象是否是数组（`util.isArray`）或正则表达式（`util.isRegExp` ），或者将其格式化成一个字符串（`util.format` ）。最近还增加了一个新的实验性功能，用于将可读流的数据输出到可写流（`util.pump`）：

```js
util.pump(process.stdin, process.stdout);
```

我经常使用 `util.inspect` 来获得一个对象的描述信息。当你想了解某个对象的更多信息时，这是一个很好的方法。`inspect` 方法的第一参数是必选的，传入你想查看的对象即可；第二个参数是可选的，决定了是否需要查看对象中的不可枚举属性；第三个指定了递归次数，即所能查看的对象信息的深度；第四个参数也是可选的，指定是否使用 ANSI 颜色输出信息。如果第三个参数是一个空值 null，则表示无限递归（默认为 2）。

```js
var util = require('util');
var jsdom = require('url');
console.log(util.inspect(jsdom, true, null, true));
```

Utilities 模块还提供了另外一些方法，util.inherits 是比较常用的一个。它需要两个参数，constructor 和 superConstructor。方法的执行结果是 constructor 将继承 superConstructor 的功能。

**示例3-11 使用 util.inherits 方法实现继承**

```js
var util = require('util');

// define original object
function first() {
    var self = this;
    this.name = 'first';
    this.test = function() {
        console.log(self.name);
    };
}

first.prototype.output = function() {
    console.log(this.name);
}

// inherit from first
function second() {
    second.super_.call(this);
    this.name = 'second';
}

util.inherits(second, first);

var two = new second();

function third(func) {
    this.name = 'third';
    this.callMethod = func;
}

var three = new third(two.test);

// all three should output 'second'
two.output();
two.test();
three.callMethod();
```

在 util.inherits 的实现中，我们可以看到有关 `super_` 的定义：

```js
exports.inherits = function(ctor, superCtor) {
    ctor.super_ = superCtor;
    ctor.prototype = Object.create(superCtor.prototype, {
        constructor: {
            value: ctor,
            enumerable: false,
            writable: true,
            configurable: true
        }
    });
};
```

在 JavaScript 中，this 用于描述一个对象的上下文，当一个函数被作为参数传递时（比如传递给事件处理程序），this 将会发生切换。如果期望此函数仍然使用所属对象的数据的话，唯一方法是将 this 赋值给一个对象内变量 （self），然后再函数定义中使用该对象变量。