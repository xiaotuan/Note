[toc]

`JavaScript` 程序的执行有两个阶段。在第一阶段，载入文档内容，并执行 `<script>` 元素里的代码（包括内联脚本和外部脚本）。脚本通常（但不总是，参见13.3.1节）会按它们在文档里的出现顺序执行。所有脚本里的 `JavaScript` 代码都是从上往下，按照它在条件、循环以及其他控制语句中的出现顺序执行。  

当文档载入完成，并且所有脚本执行完成后，`JavaScript` 执行就进入它的第二阶段。这个阶段是异步的，而且由事件驱动的。在事件驱动阶段，`Web` 浏览器调用事件处理程序函数（由第一阶段里执行的脚本指定的 `HTML` 事件处理程序，或之前调用的事件处理程序来定义），来响应异步发生的事件。  

### 1. 同步、异步和延迟的脚步

`JavaScript` 第一次添加到Web浏览器时，还没有 `API` 可以用来遍历和操作文档的结构和内容。当文档还在载入时，`JavaScript` 影响文档内容的唯一方法是快速生成内容。它使用`document.write()` 方法完成上述任务。  

```html
<h1>Table of Factorials</h1>
<script>
    function factorial(n) { // 用来计算阶乘的函数
        if (n <= 1) return n;
        else return n*factorial(n-1);
    }
    document.write("<table>"); // 开始创建HTML表
    document.write("<tr><th>n</th><th>n!</th></tr>"); // 输出表头
    for(var i = 1; i <= 10; i++) { // 输出10行
        document.write("<tr><td>" + i + "</td><td>" + factorial(i) + "</td></tr>");
    }
    document.write("</table>"); // 表格结束
    document.write("Generated at " + new Date()); // 输出时间戳
</script>
```

当脚本把文本传递给 `document.write()` 时，这个文本被添加到文档输入流中，`HTML` 解析器会在当前位置创建一个文本节点，将文本插入这个文本节点后面。我们并不推荐使用`document.write()`，但在某些场景下它有着重要的用途。当HTML解析器遇到 `<script>` 元素时，它默认必须先执行脚本，然后再恢复文档的解析和渲染。  

脚本的执行只在默认情况下是同步和阻塞的。`<script>` 标签可以有 `defer` 和 `async` 属性，这（在支持它们的浏览器里）可以改变脚本的执行方式。这些都是布尔属性，没有值；只需要出现在 `<script>` 标签里即可。`HTML5` 说这些属性只在和 `src` 属性联合使用时才有效，但有些浏览器还支持延迟的内联脚本：  

```html
<script defer src="deferred.js"></script>
<script async src="async.js"></script>
```

`defer` 属性使得浏览器延迟脚本的执行，直到文档的载入和解析完成，并可以操作。`async` 属性使得浏览器可以尽快地执行脚本，而不用在下载脚本时阻塞文档解析。如果`<script>` 标签同时有两个属性，同时支持两者的浏览器会遵从 `async` 属性并忽略 `defer` 属性。  

> 注意：延迟的脚本会按它们在文档里的出现顺序执行。而异步脚本在它们载入后执行，这意味着它们可能会无序执行。  

甚至可以在不支持 `async` 属性的浏览器里，通过动态创建 `<script>` 元素并把它插入到文档中，来实现脚本的异步载入和执行。  

```js
// 异步载入并执行一个指定 URL 中的脚本
function loadasync(url) {
    var head = document.getElementsByTagName("head")[0]; // 找到<head>元素
    var s = document.createElement("script"); // 创建一个<script>元素
    s.src = url; // 设置其src属性
    head.appendChild(s); // 将script元素插入head标签中
}
```

### 2. 事件驱动的 JavaScript

注册事件处理程序最简单的方法是把 `JavaScript` 函数赋值给目标对象的属性，类似这样的代码：  

```js
window.onload = function() { ... };
document.getElementById("button1").onclick = function() { ... };
function handleResponse() { ... }
request.onreadystatechange = handleResponse;
```

> 注意，按照约定，事件处理程序的属性的名字是以 “on” 开始，后面跟着事件的名字。还要注意在上面的任何代码里没有函数调用：只是把函数本身赋值给这些属性。  

如果需要为一个事件注册多个事件处理程序函数，或者如果想要写一个可以安全注册事件处理程序的代码模块，就算另一个模块已经为相同的目标上的相同的事件注册了一个处理程序，也需要用到另一种事件处理程序注册技术。大部分可以成为事件目标的对象都有一个叫做 `addEventListaner()` 的方法，允许注册多个监听器：  

```js
window.addEventListener("load", function() {...}, false);
request.addEventListener("readystatechange", function() {...}, false);
```

> 注意：这个函数的第一个参数是事件的名称。  

在 IE8 以及之前的浏览器中，必须使用一个相似的方法，叫做 `attachEvent()`：  

```js
window.attachEvent("onload", function() {...});
```

客户端 `JavaScript` 程序还使用异步通知类型，这些类型往往不是事件。如果设置`Window` 对象的 `onerror` 属性为一个函数，会在发生 `JavaScript` 错误（或其他未捕获的异常）时调用函数。  

```js
// 注册函数f，当文档载入完成时执行这个函数f
// 如果文档已经载入完成，尽快以异步方式执行它
function onLoad(f) {
    if (onLoad.loaded) // 如果文档已经载入完成
    	window.setTimeout(f, 0); // 将f放入异步队列，并尽快执行它
    else if (window.addEventListener) // 注册事件的标准方法
    	window.addEventListener("load", f, false);
    else if (window.attachEvent) // IE8以及更早的IE版本浏览器注册事件的方法
    	window.attachEvent("onload", f);
}
// 给onLoad设置一个标志，用来指示文档是否载入完成
onLoad.loaded = false;
// 注册一个函数，当文档载入完成时设置这个标志
onLoad(function() { onLoad.loaded = true; });
```

### 3. 客户端 JavaScript 线程模型

`JavaScript` 语言核心并不包含任何线程机制，并且客户端 `JavaScript` 传统上也没有定义任何线程机制。`HTML5` 定义了一种作为后台线程的 “WebWorker”，但是客户端 `JavaScript` 还像严格的单线程一样工作。甚至当可能并发执行的时候，客户端 `JavaScript` 也不会知晓是否真的有并行逻辑的执行。  

单线程执行意味着浏览器必须在脚本和事件句处理程序执行的时候停止响应用户输入。这为 `JavaScript` 程序员带来了负担，它意味着 `JavaScript` 脚本和事件处理程序不能运行太长时间。如果一个脚本执行计算密集的任务，它将会给文档载入带来延迟，而用户无法在脚本完成前看到文档内容。如果事件处理程序执行计算密集的任务，浏览器可能变得无法响应，可能会导致用户认为浏览器崩溃了。  

如果应用程序不得不执行太多的计算而导致明显的延迟，应该允许文档在执行这个计算之前完全载入，并确保能够告知用户计算正在进行并且浏览器没有挂起。如果可能将计算分解为离散的子任务，可以使用 `setTimeout()` 和 `setInterval()` 方法在后台运行子任务，同时更新一个进度指示器向用户显示反馈。

HTML5 定义了一种并发的控制方式，叫做 “Web worker”。Web worker 是一个用来执行计算密集任务而不冻结用户界面的后台线程。运行在 Web worker 线程里的代码不能访问文档内容，不能和主线程或其他worker共享状态，只可以和主线程和其他worker通过异步事件进行通信，所以主线程不能检测并发性，并且 Web worker 不能修改 JavaScript 程序的基础单线程执行模型。