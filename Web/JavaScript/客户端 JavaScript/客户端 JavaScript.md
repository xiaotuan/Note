`Window` 对象是所有客户端 `JavaScript` 特性和 `API` 的主要接入点。它表示 `Web` 浏览器的一个窗口或窗体，并且可以用标识符 `window` 来引用它。`Window` 对象定义了一些属性，比如，指代 `Location` 对象的 `location` 属性，`Location` 对象指定当前显示在窗口中的 `URL`，并允许脚本往窗口里载入新的 `URL`：  

```js
// 设置 location 属性，从而跳转到新的 Web 页面
window.location = "http://www.oreilly.com/";
```

`Window` 对象还定义了一些方法，比如 `alert()`，可以弹出一个对话框用来显示一些信息。还有`setTimeout()`，可以注册一个函数，在给定的一段时间之后触发一个回调：  

```js
// 等待两秒，然后说 hello
setTimeout(function() { alert("hello world"); }, 2000);
```

> 注意：上面的代码并没有显式地使用 `window` 属性。在客户端 `JavaScript` 中，`Window` 对象也是全局对象。这意味着 `Window` 对象处于作用域链的顶部，它的属性和方法实际上是全局变量和全局函数。  

`Window` 对象中其中一个最重要的属性是 `document`，它引用 `Document` 对象，后者表示显示在窗口中的文档。`Document` 对象有一些重要方法，比如 `getElementById()`，可以基于元素 `id` 属性的值返回单一的文档元素（表示 `HTML` 标签的一对开始/结束标记，以及它们之间的所有内容）：  

```JS
// 查找 id="timestamp" 的元素
var timestamp = document.getElementById("timestamp");
```

`getElementById()` 返回的 `Element` 对象有其他重要的属性和方法，比如允许脚本获取它的内容，设置属性值等：  

```js
// 如果元素为空，往里面插入当前的日期和时间
if (timestamp.firstChild == null)
	timestamp.appendChild(document.createTextNode(new Date().toString()));
```

每个 `Element` 对象都有 `style` 和 `className` 属性，允许脚本指定文档元素的 `CSS` 样式，或修改应用到元素上的 `CSS` 类名。设置这些 `CSS` 相关的属性会改变文档元素的呈现：  

```js
// 显式修改目标元素的呈现
timestamp.style.backgroundColor = "yellow";
// 或者只改变类，让样式表指定具体内容
timestamp.className = "highlight";
```

`Window`、`Document` 和 `Element` 对象上另一个重要的属性集合是事件处理程序相关的属性。可以在脚本中为之绑定一个函数，这个函数会在某个事件发生时以异步的方式调用。事件处理程序可以让 `JavaScript` 代码修改窗口、文档和组成文档的元素的行为。事件处理程序的属性名是以单词 “on” 开始的，用法如下：  

```js
// 当用户单击timestamp元素时，更新它的内容
timestamp.onclick = function() { this.innerHTML = new Date().toString(); }
```

`Window` 对象的 `onload` 处理程序是最重要的事件处理程序之一。当显示在窗口中的文档内容稳定并可以操作时会触发它。`JavaScript` 代码通常封装在 `onload`事件处理程序里。  

```html
<!DOCTYPE html>
<html>
    <head>
        <style>
            /* 本页的css样式表 */
            .reveal * { display: none; }
            /* class="reveal"的元素的子元素都不显示 */
            .reveal *.handle { display: block;}
            /* 除了class="handle"的元素 */
        </style>
        <script>
            // 所有的页面逻辑在onload事件之后启动
            window.onload = function() {
                // 找到所有class名为"reveal"的容器元素
                var elements = document.getElementsByClassName("reveal");
                for (var i = 0; i < elements.length; i++) { // 对每个元素进行遍历
                    var elt = elements[i];
                    // 找到容器中的"handle"元素
                    var title = elt.getElementsByClassName("handle")[0];
                    // 当单击这个元素时，呈现剩下的内容
                    addRevealHandler(title,elt);}
                    function addRevealHandler(title,elt) {
                        title.onclick = function() {
                        if (elt.className == "reveal") {
                        	elt.className = "revealed";
                        } else if (elt.className == "revealed") {
                        	elt.className = "reveal";
                        }
                    }
                }
            };
        </script>
    </head>
    <body>
        <div class="reveal">
            <h1 class="handle">Click Here to Reveal Hidden Text</h1>
            <p>This paragraph is hidden. It appears when you click on the title.</p>
        </div>
    </body>
</html>
```

