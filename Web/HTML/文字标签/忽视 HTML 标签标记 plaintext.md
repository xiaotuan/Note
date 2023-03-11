忽视 HTML 标签标记主要是用来使 HTML 标签失去作用，而直接显示在页面中。这一标记在实际中应用并不多。

### 1. 语法

```html
<plaintext>内容</plaintext>
或
<xmp>内容</xmp>
```

> 警告：使用 `plaintext` 或 `xmp` 标记后，其标记后面的所有内容都将忽视 HTML 标签，没有结束标记。

### 2. 示例代码

```html
<html>
    <head>
    	<title>忽视HTML 标签标记</title>
    </head>
    <body>
        <plaintext>
            <!--作者管于-->
            <p>一年之计,莫如树谷;十年之计,莫如树木;百年之计,莫如树人。</p>
        </plaintext>
    </body>
</html>
```

