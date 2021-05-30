[toc]

### 1. 创建事件循环

`setInterval()` 方法的第一个参数是一个回调函数，第二个参数是延迟时间（以 ms 为单位），同时还有一些可选的参数：

```js
setInterval(function(name) {
    console.log('Hello' + name);
}, 3000, 'Shelley');
```

执行后输出如下：

```console
$ node hello.js
HelloShelley
HelloShelley
HelloShelley
```

### 2. 取消事件循环

调用 `setInterval()` 方法后会返回一个代表这个定时器的 ID，通过将这个 ID 传递给 `clearInterval()` 方法取消该定时器。

```js
var intervalId = setInterval(function(name) {
    console.log('Hello' + name);
}, 3000, 'Shelley');
console.log("set interval");
clearInterval(intervalId);
```

