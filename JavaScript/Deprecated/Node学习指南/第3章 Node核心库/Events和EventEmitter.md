### 3.7 Events 和 EventEmitter

对于可以产生事件并能通过 on 方法绑定事件处理函数的对象来说，几乎无一例外都是通过继承 EventEmitter 来实现的。

首先，包含 `Events` 模块：

```js
var events = require('events');
```

接下来，创建一个 EventEmitter 的实例：

```js
var em = new events.EventEmitter();
```

使用新创建的 EventEmitter 实例来完成两个基本任务：为指定事件添加事件处理程序，激发并产生事件。当一个特定的事件产生时，名为 `on` 的事件处理函数将被触发。该方法的第一个参数是事件名称，第二个参数为事件处理函数：

```js
em.on('someevent', function(data) { ... });
```

当某些条件满足之后，我们可以通过 emit 方法来激发对象上的事件：

```js
if (somecriteria) {
    en.emit('data');
}
```

**示例3-12 EventEmitter 基本功能示例**

```js
var eventEmitter = require('events').EventEmitter;
var counter = 0;

var em = new eventEmitter();

setInterval(function() {
    em.emit('timed', counter++);
}, 3000);

em.on('timed', function(data) {
    console.log('timed ' + data);
});
```

我们需要的往往是将 EventEmitter 功能添加到代码的现有对象中，而不仅仅是在整个应用中直接使用 EventEmitter 的示例，可以使用 `util.inherits` 方法实现：

```js
util.inherits(someobj, EventEmitter);

someobj.prototype.somemethod = function() {
    this.emit('event');
};
...
someobjinstance.on('event', function() {});
```

> **可读写流**
>
> 使用 Node 的文件系统模块（fs）可以打开文件并进行读写操作，或者监视指定文件是否有新的活动，还可以对文件系统的目录结构进行维护。同时它还未我们提供可读流和可写流来操作文件内容。
>
> 你可以使用 `fs.createReadStream` 方法并传入文件名称、文件路径或其他可选来创建一个可读流。也可以使用 `fs.createWriteStream`  方法并传入文件名称和路径来创建一个可写流。
>
> 如果你期望通过事件驱动方式来操作文件，并且需要频繁读写文件内容时，使用可读写流是一个好的选择。程序后台会打开流并将所有读写操作放入队列然后按序进行处理。

**示例3-13 通过继承 EventEmitter 创建支持事件功能的对象**

```js
```



