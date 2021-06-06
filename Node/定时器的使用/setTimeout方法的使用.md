[toc]

### 1. 设置定时器

`setTimeout()` 方法的第一个参数是一个回调函数，第二个参数是延迟时间（以 ms 为单位），同时还有一些可选的参数：

```js
setTimeout(function(name) {
    console.log('Hello' + name);
}, 3000, 'Shelley');
```

执行后输出如下：

```console
$ node hello.js
HelloShelley
```

### 2. 取消定时器

调用 `setTimeout()` 方法后会返回一个代表这个定时器的 ID，通过将这个 ID 传递给 `clearTimeout()` 方法取消该定时器。

```js
var timeoutId = setTimeout(function(name) {
    console.log('Hello' + name);
}, 3000, 'Shelley');
console.log("set timeout")
clearTimeout(timeoutId)
```

