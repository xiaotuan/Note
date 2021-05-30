+ global 对象，也是 Node 的全局命名空间；
+ process 对象，它提供了一些关键功能，例如对三种标准 I/O 流的封装，以及将同步函数转换为异步回调的功能；
+ Buffer 类，它提供了存储和操作原始数据的功能，同样它也是全局可见的；
+ 子进程；
+ 用于域名解析和 URL 处理的模块。

**global**

如果在 Node 模块中创建一个顶层变量（在函数之外的变量），它仅仅在该模块中是全局的，而在其他模块中是不可见的。

当 `Node` 开发人员谈及 context 时， 一般是指 global 对象。

mod1.js

```js
var globalValue

exports.setGlobal = function(val) {
    globalValue = val
}

exports.returnGlobal = function() 
    console.log(global)
    return globalValue
}
```

使用 mod1.js 模块

```console
> var mod1 = require('./mod1.js')
> mod1.setGlobal(34)
> var va1 = mod1.returnGlobal()
```

**process**

每个 `Node` 应用程序都是一个 process 对象实例，process 对象中的许多方法和属性能提供关于应用程序身份标识和当前运行环境的信息。调用 `process.execPath` 方法可以返回当前 `Node` 应用程序的执行路径， `process.version` 提供了 `Node` 版本信息， `process.platform` 提供服务器平台信息：

```console
console.log(process.execPath)
console.log(process.version)
console.log(process.platform)
```

process 对象包括 stdin、stdout 和 stderr。stdin 和 stdout 支持异步操作，stderr是一个同步可阻塞流。

**示例3-1 使用 stdin 和 stdout 来读取和写入数据**

```js
process.stdin.resume()

process.stdin.on('data', (chunk) => {
    process.stdout.write('data: ' + chunk)
})
```

可以通过 process 对象的 memoryUsage 方法查询当前 `Node` 应用程序的内存使用量。process 对象的 nextTick 方法可以将一个回调函数挂载到 `Node` 程序的事件循环机制中，并在下一个事件循环发生时调用该函数。

```js
function asynchFunction = function (data, callback) {
    process.nextTick(function() {
        callback(val)
    })
}
```

可以使用 `setTimeout` 方法并传入一个 (0) 毫秒的延迟来达到同样的目的：

```js
setTimeout(function() {
    callback(val)
}, 0)
```

然而， `setTimeout` 方法并不像 `process.nextTick` 方法那样高效。

**Buffer**

Buffer 是 `Node` 中的另一个全局对象，是用于处理二进制数据的一种方式。为了将二进制数据转换为字符串，需要调用流套接字的 `setEncoding` 函数来改变当前使用的数据编码方式。

**支持的编码方式**

| 编码方式 | 说明 |
| :-: | :- |
| ascii | 七位 ASCII |
| utf8 | 多字节编码的 Unicode 字符 |
| usc2 | 两字节， little endian 方式编码的 Unicode 字符 |
| base64 | Base64 编码 |
| hex | 每个字节编码为两个十六进制字符 |

可以将字符串写入到一个现有的 buffer 对象中，并指定该写入操作的偏移，数据长度和编码方式：

```js
// 写入的默认偏移为 0，默认数据长度为 buffer.length - offset，编码默认采用 utf8
buf.write(string)
```


