[toc]

> 注意：`srcdoc` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

只有 Chrome 和 Safari 6 支持 `<iframe>` 标签的 `srcdoc` 属性。

### 2. 定义和用法

`srcdoc` 属性规定要显示在内联框架中的页面的 HTML 内容。

> **提示：**该属性应该与 `sandbox` 和 `seamless` 属性一起使用。
>
> 如果浏览器支持 `srcdoc` 属性，且指定了 `srcdoc` 属性，它将覆盖在 `src` 属性中规定的内容。
>
> 如果浏览器不支持 `srcdoc` 属性，且指定了 `srcdoc` 属性，它将显示在 `src` 属性中规定的文件。

###  3. 语法

```html
<iframe srcdoc="HTML_code">
```

### 4. 属性值

| 值        | 描述                                                     |
| :-------- | :------------------------------------------------------- |
| HTML_code | 要显示在 iframe 中的 HTML 内容。必需是有效的 HTML 语法。 |

### 5. 示例

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>W3Cschool(w3cschool.cn)</title> 
</head>
<body>

<iframe srcdoc="<p>Hello world!</p>" src="demo-iframe_srcdoc.htm">
  <p>您的浏览器不支持  iframe 标签。</p>
</iframe>

<p><strong>注意：</strong> 只有 Chrome 和 Safari 6 支持 <iframe> 标签的 srcdoc 属性。</p>

</body>
</html>
```

