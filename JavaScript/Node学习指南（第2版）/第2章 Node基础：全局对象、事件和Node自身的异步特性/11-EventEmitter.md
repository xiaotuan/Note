[toc]

### 2.3.3　EventEmitter

对于很多Node核心模块，如果你翻开表面，去看它们的源码，会发现它们都使用了 `EventEmitter` 。只要看见一个对象触发事件，或者一个事件被 `on` 函数捕获，那一定就是 `EventEmitter` 在起作用。理解 `EventEmitter` 的工作方式和掌握它的使用方法，是Node开发中的两个重要组成部分。

`EventEmitter` 激活了Node中的异步事件处理。为了演示其核心功能，我们来快速创建一个用于测试的应用程序。

首先，引入 `Events` 模块：

```python
var events = require('events');
```

接着，创建一个 `EventEmitter` 的实例：

```python
var em = new events.EventEmitter();
```

下面使用新创建的 `EventEmitter` 来执行两个简单的任务：设置事件处理函数来监听事件，然后触发该事件。在触发特定事件时， `EventEmitter.on()` 的事件处理器会被调用。该方法的第一个参数是事件的名称；第二个参数是一个回调函数，用于执行一些功能：

```python
em.on('someevent', function(data) { ... });
```

当满足特定条件时，事件会通过 `EventEmitter.emit()` 方法从对象上发出：

```python
if (somecriteria) { 
   en.emit('data'); 
}
```

在例2-6中，我们会创建一个 `EventEmitter` 例子，每3s发出一个定时事件。它的事件处理函数会将带有计数器的消息输出到控制台。请注意 `EventEmitter.emit()` 中的 `counter` 参数与处理事件的 `EventEmitter.on()` 中的对应数据之间的关联性。

**例2-6　EventEmitter功能的基础测试**

```python
var eventEmitter = require('events').EventEmitter;
var counter = 0;
var em = new eventEmitter();
setInterval(function() { em.emit('timed', counter++); }, 3000);
em.on('timed', function(data) {
  console.log('timed ' + data);
});
```

运行应用程序，定时事件消息就会不断地输出到控制台，直到应用程序终止。从这个简单应用程序中，我们可以看到事件是通过 `EventEmitter.emit ()` 函数触发的，而 `EventEmitter.on ()` 函数则可以捕获该事件并进行处理。

这是一个有意思的例子，但并不是非常有用。我们需要的是可以将 `EventEmitter` 的功能添加到现有对象中的能力，而不是在整个应用程序中使用 `EventEmitter` 的例子。而这正是 `http.Server` 和Node中大多数基于事件的类所需要的能力。

`EventEmitter` 的功能是继承而来的，所以我们必须用另一个Node对象 `Util` 来启用继承功能。Util模块可以通过下面的方式被引入到应用程序中：

```python
var util = require('util');
```

`Util` 模块非常有用。我将在第11章介绍调试Node应用时，介绍它的大部分功能。它有一个函数 `util.inherits()` ，我们现在就要用到。

`util.inherits ()` 函数是使一个构造函数能够继承另一个构造函数（也就是父构造函数）的原型方法。 `util.inherits ()` 的厉害之处在于，你还可以直接在构造函数中访问父构造函数。

`util.inherits ()` 函数能够让我们在任何类中继承Node的事件队列功能，同样也可以继承 `EventEmitter` ：

```python
util.inherits(Someobj, EventEmitter);
```

通过在对象中使用 `util.inherits ()` ，我们可以调用对象方法中的 `emit` 函数，并在对象实例上调用添加事件处理函数：

```python
Someobj.prototype.someMethod = function() { this.emit('event'); };
...
Someobjinstance.on('event', function() { });
```

与其煞费苦心地去破译 `EventEmitter` 在抽象层面的工作原理，不如来看看例2-7，我在这个例子中创建了一个类—— `inputchecker` ，该类的作用就是继承 `EventEmitter` 的功能。构造器接收两个参数，一个人名和一个文件名。它的作用就是把人名分配到物品上，并用文件系统模块的 `createWriteStream` 方法创建了一个可写流的引用。

该对象还有一个方法—— `check` ，它会检查特定命令的输入数据。一个命令（ `wr :` ）用来触发写事件，另一个（ `en:` ）则用来触发结束事件。如果没有任何命令，则触发 `echo` 事件。该对象的实例对这3种事件都提供了事件处理器。捕获到写事件时，它会把内容写入一个文件；捕获到非命令的输入内容时，它会进行回显；捕获到结束事件时，它会使用 `process.exit` 来终止程序运行。

所有输入都来自标准输入（ `process.stdin` ）。输出使用了可写流，用这种方式可以在后台创建新的输出源，未来的写操作都会排队等待。如果你在这个程序中需要进行频繁的文件写入操作，那么这个方法更有效率。需要回显的输入内容则会被输出到 `process.stdout` 。

**例2-7　创建一个继承 `EventEmitter` 的基于事件的对象**

```python
"use strict";
var util = require('util');
var eventEmitter = require('events').EventEmitter;
var fs = require('fs');
function InputChecker (name, file) {
   this.name = name;
   this.writeStream = fs.createWriteStream('./' + file + '.txt',
      {'flags' : 'a',
      'encoding' : 'utf8',
      'mode' : 0o666});
};
util.inherits(InputChecker,eventEmitter);
InputChecker.prototype.check = function check(input) {
  // trim extraneous white space
  let command = input.trim().substr(0,3);
  // process command
  // if wr, write input to file
  if (command == 'wr:') {
     this.emit('write',input.substr(3,input.length));
  // if en, end process
  } else if (command == 'en:') {
     this.emit('end');
  // just echo back to standard output
  } else {
     this.emit('echo',input);
  }
}; 
// testing new object and event handling
let ic = new InputChecker('Shelley','output');
ic.on('write', function(data) {
   this.writeStream.write(data, 'utf8');
}); 
ic.on('echo', function( data) {
   process.stdout.write(ic.name + ' wrote ' + data);
}); 
ic.on('end', function() {
   process.exit();
}); 
// capture input after setting encoding
process.stdin.setEncoding('utf8');
process.stdin.on('readable', function() {
   let input = process.stdin.read();
   if (input !== null)
      ic.check(input);
});
```

注意，该代码还调用了 `process.stdin.on` 方法，因为 `process.stdin` 是继承自 `EventEmitter` 的众多Node对象之一。

> <img class="my_markdown" src="../images/36.png" style="zoom:50%;" />
> **严格模式下不存在八进制字面量**
> 在例2-7中，因为要使用ES6的 `let` 语法，所以我用了严格（strict）模式。而正是由于使用了严格模式，所以不能在写入流文件描述标识符中使用八进制字面量（比如0666）。因此我用了符号0o666，这是一个ES6风格的字面量。

`on()` 函数其实是 `EventEmitter.addListener` 的缩写，所以它们接收的参数是一样的，所以这段代码：

```python
ic.addListener('echo', function( data) {
    console.log(this.name + ' wrote ' + data);
});
```

和这段代码是完全相等的：

```python
ic.on('echo', function( data) {
   console.log(this.name + ' wrote ' + data);
});
```

你可以用 `EventEmitter.once()` 来监听下一个事件：

```python
ic.once(event, function);
```

如果有超过10个监听器在监听同一个事件，就会产生一个警告（warning）。可以用 `setMaxListeners` 方法传入一个数字，来修改监听器的数量。数字0表示不限数量的监听器。

也可以用 `EventEmitter.removeListener()` 来移除监听器：

```python
ic.on('echo', callback); 
ic.removeListener('echo',callback);
```

这段代码会从事件监听器数组中删除一个监听器，并保持原来的顺序。不过，如果因为某些原因使用 `EventEmitter.listeners()` 复制了事件监听器数组，那么一旦删除了某个监听器，就需要重新创建这个监听器数组。

