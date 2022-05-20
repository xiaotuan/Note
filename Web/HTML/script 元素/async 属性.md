[toc]

> 注意：`async` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 支持 async 属性。

> **注意：**Internet Explorer 9 及之前的版本不支持 `<script>` 标签的 `async` 属性。

### 2. 定义和用法

`async` 属性是一个布尔属性。

`async` 属性一旦脚本可用，则会异步执行。

> **注意：**`async` 属性仅适用于外部脚本（只有在使用 src 属性时）。

> **注意：**有多种执行外部脚本的方法：
>
> - 如果 `async="async"`：脚本相对于页面的其余部分异步地执行（当页面继续进行解析时，脚本将被执行）
> - 如果不使用 `async` 且 `defer="defer"`：脚本将在页面完成解析时执行
> - 如果既不使用 `async` 也不使用 `defer`：在浏览器继续解析页面之前，立即读取并执行脚本

### 3. 语法

```html
<script async>
```

### 4. 示例

```html
<script src="demo_async.js" async></script>
```

