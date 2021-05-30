使用 `<script>` 元素的方式有两种：直接在页面中嵌入 `JavaScript` 代码和包含外部 `JavaScript` 文件。
1. 在使用 `<script>` 元素嵌入 `JavaScript` 代码时， 只须为 `<script>` 指定 type 属性。然后，像下面这样把 `JavaScript` 代码直接放在元素内部即可：

```html
<script type="text/javascript">
    function sayHi() {
        alert("Hi!")
    }
</script>
```
在使用 `<script>` 嵌入 `JavaScript` 代码时，记住不要在代码中的任何地方出现 "\</script\>" 字符串。

```html
<script type="text/javascript">
    function sayScript() {
        alert("</script>")
    }
</script>
```

通过把这个字符串分割为两部分可以解决这个问题，例如：

```html
<script type="text/javascript">
    function sayScript() {
        alert("\</script\>")
    }
</script>
```

2. 通过 `<script>` 元素来包含外部 `JavaScript` 文件，那么 `src` 属性就是必需的。这个属性的值是一个指向外部 `JavaScritp` 文件的链接，例如：

```html
<script type="text/javascript" src="example.js"></script>
```

与解析嵌入式 `JavaScript` 代码一样，在解析外部 `JavaScript` 文件（包括下载该文件）时，页面的处理也会暂时停止。

需要注意的是，带有 `srcd` 属性的 `<script>` 元素不应该在其 `<script>` 和 `</script>` 标签之间再包含额外的 `JavaScript` 代码。如果包含了嵌入的代码，则只会下载并执行脚本文件，嵌入的代码会被忽略。

`<script>` 的 `src` 属性可以是指向当前的 HTML 页面所在域之外的某个域中的 URL，例如：

```html
<script type="text/javascript" src="http://www.somewhere.com/afile.js"></script>
```

无论如何包含代码，只要不存在 `defer` 和 `async` 属性，浏览器都会按照 `<script>` 元素在页面中出现的先后顺序对它们依次进行解析。