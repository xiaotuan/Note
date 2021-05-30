`<noscript>` 元素用以在不支持 `JavaScript` 的浏览器中显示替代的内容。这个元素可以包含能够出现在文档 `<body>` 中的任何 `HTML` 元素——`<script>` 元素除外。包含在 `<noscript>` 元素中的内容只有在下列情况下才会显示出来：

+ 浏览器不支持脚本；
+ 浏览器支持脚本，但脚本被禁用。

例如：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Example HTML Page</title>
        <script type="text/javascript" defer="defer" src="example1.js"></script>
        <script type="text/javascript" defer="defer" src="example2.js"></script>
    </head>
    <body>
        <noscript>
            <p>本页面需要浏览器支持（启用）JavaScript。</p>
        </noscript>
    </body>
</html>
```

