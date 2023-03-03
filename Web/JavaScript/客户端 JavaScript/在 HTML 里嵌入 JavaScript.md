[toc]

在 `HTML` 文档里嵌入客户端 `JavaScript` 代码有4种方法：

+ 内联，放置在 `<script>` 和 `</script>` 标签对之间。  

+ 放置在由 `<script>` 标签的 `src` 属性指定的外部文件中。

+ 放置在 `HTML` 事件处理程序中，该事件处理程序由 `onclick` 或 `onmouseover` 这样的 `HTML` 属性值指定。

+ 放在一个 `URL` 里，这个 `URL` 使用特殊的 `javascript：` 协议。  

> 注意：`HTML` 事件处理程序属性和 `javascript：URL` 这两种方式在现代 `JavaScript` 代码里已经很少使用（它们在 `Web` 早期多少有点通用）。  

### 1. `<script>` 元素

`JavaScript` 代码可以以内联的形式出现在 `HTML` 文件里的 `<script>` 和 `</script>` 标签之间：  

```html
<script>
	// 这里是你的JavaScript代码
</script>
```

在 `XHTML` 中，`<script>` 标签中的内容被当做其他内容一样对待。如果 `JavaScript` 代码包含了 `<` 或 `&` 字符，那么这些字符就被解释成为 `XML` 标记。因此，如果要使用 `XHTML`，最好把所有的 `JavaScript` 代码放入到一个 `CDATA` 部分里：  

```html
<script><![CDATA[
	// 这里是你的JavaScript代码
]]></script>
```

**示例代码：实现一个简单的JavaScript数字时钟程序**

```html
<!DOCTYPE html> <!-- 这是一个 HTML5 文件 -->
<html> <!-- 根节点 -->
    <head> <!-- 标题、脚本和样式都放在这里 -->
        <title>Digital Clock</title>
        <script> // js代码
            // 定义一个函数用以显示当前时间
            function displayTime() {
            var elt = document.getElementById("clock"); // 通过id= "clock"找到元素
            var now = new Date(); // 得到当前时间
            elt.innerHTML = now.toLocaleTimeString(); // 让elt来显示它
                setTimeout(displayTime, 1000); // 在1秒后再次执行
            }
            window.onload = displayTime; // 当onload事件发生时开始显示时间
        </script>
        <style> /* 钟表的样式 */
            #clock { /* 定义 id="clock"的元素的样式 */
                font: bold 24pt sans; /* 使用粗体大号字 */
                background: #ddf; /* 定义蓝灰色背景 */
                padding: 10px; /* 周围有一圈空白 */
                border: solid black 2px; /* 定义纯黑色边框 */
                border-radius: 10px; /* 定义圆角（如果浏览器支持的话） */
            }
        </style>
    </head>
    <body> <!-- body部分是用来显示文档的 -->
        <h1>Digital Clock</h1> <!-- 显示标题 -->
        <span id="clock"></span> <!-- 输出时钟 -->
    </body>
</html>
```

### 2. 外部文件中的脚本

`<script>` 标签支持 `src` 属性，这个属性指定包含 `JavaScript` 代码的文件的 `URL`。它的用法如下： 

```html
<script src="../../scripts/util.js"></script>
```

> 注意：即便指定了 `src` 属性并且 `<script>` 和 `</script>` 标签之间没有 `JavaScript` 代码，结束的 `</script>`标签也是不能丢的。在 `XHTML` 中，在此处可以使用简短的 `<script/>` 标签。  

使用 `src` 属性时，`<script>` 和 `</script>` 标签之间的任何内容都会忽略。如果需要，可以在 `<script>` 标签之间添加代码的补充说明文档或版权信息。但是要注意，如果有任何非空格或 `JavaScript` 注释的文本出现在 `<script src="">` 和 `</script>` 之间，`HTML5` 校验器将会报错（注：有时我们会看到诸如这种代码：  

```html
<script src="core.js">
config = {...};
</script>
```

看起来这段代码定义了一些配置项，由 `core.js` 来读取，这是一种将页面参数传入库文件的方法，在 `JavaScript` 库的开发中非常常见，其中 `<script>` 和 `</script>` 之间的代码是一段纯文本，在 `core.js` 执行时读取这段文本然后动态执行一次，浏览器不会自动执行 `<script>` 标签之间的代码。）。  

### 3. 脚本类型

`JavaScript` 是 `Web` 的原始脚本语言，而在默认情况下，假定 `<script>` 元素包含或引用 `JavaScript` 代码。如果要使用不标准的脚本语言，如 `Microsoft` 的 `VBScript`（只有 `IE` 支持），就必须用 `type` 属性指定脚本的 `MIME` 类型：  

```html
<script type="text/vbscript">
	' 这里是VBScript 代码
</script>
```

> 提示：`type` 属性的默认值是 `text/javascript`。  

老的浏览器在 `<script>` 标记上用 `language` 属性代替 `type` 属性，这种情况现在也会经常看到：  

```html
<script language="javascript">
	// 这里是JavaScript代码……
</script>
```

> 警告：`language` 属性已经废弃，不应该再使用了。  

### 4. HTML 中的事件处理程序

类似 `onclick` 的事件处理程序属性，用相同的名字对应到 `HTML` 属性，并且还可以通过 `JavaScript` 代码放置在 `HTML` 属性里来定义事件 处理程序。例如，要定义用户切换表单中的复选框时调用的事件处理程序，可以作为表示复选框的 `HTML` 元素的属性指定处理程序代码：  

```html
<input type="checkbox" name="options" value="giftwrap" onchange="order.options.giftwrap = this.checked;">
```

> 提示： `HTML` 中定义的事件处理程序的属性可以包含任意条 `JavaScript` 语句，相互之间用逗号分隔。  

### 5. URL 中的 JavaScript

在 `URL` 后面跟一个 `javascript：` 协议限定符，是另一种嵌入` JavaScript` 代码到客户端的方式。这种特殊的协议类型指定  `URL` 内容为任意字符串，这个字符串是会被 `JavaScript` 解释器运行的 `JavaScript` 代 码。它被当做单独的一行代码对待，这意味着语句之间必须用分号隔开，而 `//` 注释必须用 `/**/` 注释代替。`javascript：URL` 能识别的“资源”是转换成字符串的执行代码的返回值。如果代码返回 `undefined`，那么这个资源是没有内容的。  

`javascript：URL` 可以用在可以使用常规 `URL` 的任意地方：比如 `<a>` 标记的 `href` 属性，`<form>` 的 `action` 属性，甚至 `window.open()` 方法的参数。超链接里的 `JavaScript URL` 可以是这样：  

```html
<a href="javascript:new Date().toLocaleTimeString();">What time is it?</a>
```

其他浏览器（比如 `Chrome` 和 `Safari` ）不允许 `URL` 像上面一样覆盖当前文档，它们会忽略代码的返回值。但是，类似这样的 `URL` 还是支持的：  

```html
<a href="javascript:alert(new Date().toLocaleTimeString());">检查时间，而不必覆盖整个文档</a>
```

当浏览器载入这种类型的 `URL` 时，它会执行 `JavaScript` 代码，但是由于没有返回值（`alert()` 方法返回 `undefined` ）作为新文档的显示内容，类似 `Firefox` 的浏览器并不会替换当前显示的文档。  如果要确保 `javascript：URL` 不会覆盖当前文档，可以用`void` 操作符强制函数调用或给表达式赋予 `undefined` 值：  

```html
<a href="javascript:void window.open('about:blank');">打开一个窗口</a>
```

> 提示：如果要测试一小段 `JavaScript` 代码，那么可以在浏览器地址栏里直接输入`javascript：URL` 。  

### 6. 书签

在 `Web` 浏览器中，“书签”就是一个保存起来的 `URL` 。如果书签是 `javascript：URL`，那么保存的就是一小段脚本，叫做 `bookmarklet`。  

考虑下面 `<a>` 标签里的 `javascript：URL` 。单击链接会打开一个简单的 `JavaScript` 表达式计算器，它允许在页面环境中计算表达式和执行语句：  

```html
<a href='javascript:
var e = "", r = ""; /* 需要计算的表达式和结果 */
do {
/* 输出表达式和结果，并要求输入新的表达式 */
e = prompt("Expression: " + e + "\n" + r + "\n", e);
try { r = "Result: " + eval(e); } /* 尝试计算这个表达式 */
catch(ex) { r = ex; } /* 否则记住这个错误 */
} while(e); /* 直到没有输入表达式或者单击了Cancel按钮才会停止，否则一直循环执行*/
void 0; /*这句代码用以防止当前文档被覆盖 */
'>
JavaScript Evaluator
</a>
```

> 注意：即便这个 `JavaScript URL` 是写成多行的，`HTML` 解析器仍将它作为单独的一行对待，并且其中的单行 `//` 注释也是无效的。还有，要记住代码是单引号中的 `HTML` 属性的一部分，所以代码不可以包含任何单引号。  