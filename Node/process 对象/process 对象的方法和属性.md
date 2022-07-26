`process` 对象中的许多方法和属性能提供关于应用程序身份标识和当前运行环境的信息。调用 `process.exeecPath` 方法可以返回当前 `Node` 应用程序的执行路径，`process.version` 提供了 `Node` 版本信息，`process.platform` 提供服务器平台信息：

```js
console.log(process.execPath);
console.log(process.version);
console.log(process.platform);
```

`process` 对象对一些标准输入输出流也进行了封装，包括标准输入 `stdin`，标准输出 `stdout` 和标准错误输出 `stderr`。`stdin` 和 `stdout` 支持异步操作，前者可读，后者可写。然而，要注意的是 `stderr` 是一个同步可阻塞流。

`stdin` 流默认情况下是不允许直接操作的，所以在发送数据之前，我们必须先调用 `resume`：

```js
process.stdin.resume();

process.stdin.on('data', function(chunk) {
    process.stdout.write('data: ' + chunk);
});
```

`process` 对象中另一个常用的方法是 `memoryUsage`，通过它可以查询当前 Node 应用程序的内存使用量：

```js
> process.memoryUsage();
{
  rss: 26906624,
  heapTotal: 6512640,
  heapUsed: 4924992,
  external: 964098,
  arrayBuffers: 141511
}
```

其中 `heapTotal` 和 `heapUsed` 属性指示了 V8 引擎的内存使用情况。

`process` 对象的 `nextTick` 方法可以将一个回调函数挂载到 `Node` 程序的事件循环机制中，并在下一个事件循环发生时调用该函数。如果由于某种原因，你想延迟并且异步的执行某个函数调用，那么你可以使用 `process.nextTick`。下面的代码是一个演示：

```js
var asynchFunction = function(data, callback) {
    process.nextTick(function() {
        callback(data);
    });
};
```

虽然你也可以使用 `setTimeout` 方法并传入一个（0）毫秒的延迟来达到同样的目的，而不采用 `process.nextTick` 方法，例如：

```js
setTimeout(function() {
    callback(val);
}, 0);
```

然而，`setTimeout` 方法并不像 `process.nextTick` 方法那样高效。

