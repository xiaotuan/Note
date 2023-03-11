使用 `<blockquote>` 标记可以实现页面文字的段落缩进。这一标记也是每使用一次，段落就缩进一次，可以嵌套使用，以达到不同的缩进效果。

### 1. 语法

```html
<blockquote>文字</blockquote>
```

### 2. 示例代码

```html
<html>
	<head>
    <title>段落的缩进效果</title>
    </head>
    <body>
        《荀子》
        <blockquote>不登高山</blockquote>
        <blockquote><blockquote>不知天之高也</blockquote></blockquote>
        <blockquote><blockquote><blockquote>不临深溪</blockquote></blockquote></blockquote>
        <blockquote><blockquote><blockquote><blockquote>
        不知地之厚也</blockquote></blockquote></blockquote></blockquote>
    </body>
</html>
```

