[toc]

### 第2章　Node基础：全局对象、事件和Node自身的异步特性

虽然说基于浏览器的应用和Node应用都是在JavaScript的基础上构建的，但它们的环境却不同。Node和基于浏览器的JavaScript之间有一个本质的区别，就是二进制数据的缓存。的确，Node现在可以操作ES6的 `ArrayBuffer` 和类型化数组了。不过Node中大部分跟二进制有关的功能还是用 `Buffer` 类来实现的。

`buffer` 是Node中的一个全局对象。另一个全局对象是 `global` 本身，不过Node中的 `global` 对象跟我们在浏览器中所用的 `global` 对象有着本质的不同。Node开发人员还能访问另一个全局变量—— `process` ，它帮我们在Node应用和其运行环境之间架起了桥梁。

Node中总算有一个东西是前端开发人员所熟悉的，那就是它的事件驱动的异步特性。但是Node与浏览器不同的是，我们要等待文件打开，而非等待用户单击按钮。

事件驱动也意味着，我们可以在Node中使用那些我们所熟悉的计数器函数。

> <img class="my_markdown" src="../images/27.png" style="zoom:50%;" />
> **模块和控制台**
> 至于其他全局组件—— `require` 、 `exports` 、 `module` 和 `console` ，我会在本书后面的章节中介绍。 `require` 、 `exports` 和 `module` 这些全局组件会在第3章中介绍， `console` 会在第4章中介绍。

