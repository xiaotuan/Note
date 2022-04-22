HTML 5 为 `base` 元素新增 `target` 属性，规定页面中所有的超链接和表单在何处打开。该属性会被每个链接中的 `target` 属性覆盖。可用值如下：

| _blank | _parent   | _self |
| ------ | --------- | ----- |
| _top   | framename |       |

例如：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title>
        <base target="_blank">
    </head>
    <body>

    	<p><a href="http://www.w3cschool.cn/">w3cschool.cn</a> - 注意这个链接会在新窗口打开，即便它没有 target="_blank" 属性。因为在 base 标签里我们已经设置了 target 属性的值为 "_blank"。</p>

    </body>
</html>
```

