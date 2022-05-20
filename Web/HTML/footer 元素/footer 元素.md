`<footer>` 元素可以作为其上层父级内容区块或是一个根区块的脚注。`<footer>` 通常包括其相关区块的脚注信息，如作者相关阅读链接及版权信息等。

> 提示：与 `<header>` 元素一样，一个页面中也未限制 `<footer>` 元素的个数。同时，可以为 `<article>` 元素或 `<section>` 元素添加 `<footer>` 元素。

例如：

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>元素的应用</title> 
	</head>
	<body>
		<footer>
			<ul>
				<li>版权信息</li>
				<li>站点地图</li>
				<li>联系方式</li>
			</ul>
		</footer>
	</body>
</html>
```

效果如下：

<footer>
    <ul>
        <li>版权信息</li>
        <li>站点地图</li>
        <li>联系方式</li>
    </ul>
</footer>