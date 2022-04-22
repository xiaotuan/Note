[toc]

> 注意：`seamless` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

只有 Chrome 和 Safari 6 支持 `<iframe>` 标签的 `seamless` 属性。

### 2. 定义和用法

`seamless` 属性是一个布尔属性。

`seamless` 属性规定 `<iframe>` 看起来像是包含的文档的一部分（没有边框和滚动条）。

### 3. 语法

```html
<iframe seamless>
```

### 4. 示例

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>W3Cschool(w3cschool.cn)</title> 
</head>
<body>

<p>这是一个段落。</p>

<iframe src="/statics/demosource/demo_iframe.htm" seamless></iframe>

<p><strong>注意：</strong> 有 Chrome 和 Safari 6 支持 iframe 标签的 seamless 属性。</p>

</body>
</html>
```

