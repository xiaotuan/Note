[toc]

### 1. 通过 \<script> 元素向 HTML 页面插入 JavaScript

HTML 4.01 为 `<script>` 定义了下列 6 个属性：

+ `async`：可选。表示应该立即下载脚本，但不应妨碍页面中的其他操作，比如下载其他资源或等待加载其他脚本。只对外部脚本文件有效。
+ `charset`：可选。表示通过 `src` 属性指定的代码的字符集。由于大多数浏览器会忽略它的值，因此这个属性很少使用。
+ `defer`：可选。表示脚本可以延迟到文档完全被解析和显示之后再执行。只对外部脚本文件有效。IE 7 及更早版本对嵌入脚本也支持这个属性。
+ `language`：已废弃。原来用于表示编写代码使用的脚本语言（如 JavaScript、VBScript）。
+ `src`：可选。表示包含要执行代码的外部文件。
+ `type`：可选。可以看成是 `language` 的替代属性：表示编写代码使用的脚本语言的内容类型（也称为 MIME类型）。默认值为 `text/javascript`。

使用 `<script>` 元素的方式有两种：

#### 1.1 直接在页面中嵌入 JavaScript 代码

只须为 `<script>` 指定 `type` 属性，然后，像下面这样把 `JavaScript` 代码直接放在元素内部即可：

```html
<script type="text/javascript">
	function sayHi() {
        alert("Hi!");
    }
</script>
```

> 注意
>
> 1. 包含在 `<script>` 元素内部的 `JavaScript` 代码将被从上至下依次解释。
> 2. 不要在代码中任何地方出现 `</script>` 字符串，例如，浏览器在加载下面所示的代码时就会产生一个错误。

#### 1.2 包含外部 JavaScript 文件



