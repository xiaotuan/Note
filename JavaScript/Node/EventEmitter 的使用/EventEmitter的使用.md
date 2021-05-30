[toc]

> 提示：实例代码请参阅 [EventEmitter功能的基础测试](./Simple/EventEmitter功能的基础测试.md) 。

`EventEmitter` 使用自定义的模块支持 `on` 的函数模式。使用 `EventEmitter` 的步骤如下：

### 1. 引入 `Events` 模块

```js
var events = require('events');
```

### 2. 创建一个 `EventEmitter` 的实例

```js
var em = new events.EventMitter();
```

### 3. 创建 `on` 事件

```js
em.on('someevent', function(data) { ... });
```

### 4. 触发 `on` 事件

```js
em.emit('someevent', 'data');
```

