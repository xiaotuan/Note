`ID` 选择器以井号 `#` 为前缀，后面是一个 `ID` 名。应用方法：在标签中定义 `id` 属性，然后设置属性值为 `ID` 选择器的名称。

+ 优点：精准匹配。
+ 缺点：需要为标签定义 `id` 属性，影响文档结构，相对于类选择器，缺乏灵活性。

> 提示：不管是类选择器，还是 `ID` 选择器，都可以指定一个限定标签名，用于限定它们的应用范围。例如，针对上面示例，在 `ID` 选择器前面增加一个 `<div>` 标签，这样 `div#box` 选择器的优先级会高于 `#box` 选择器的优先级。在同等条件下，浏览器会优先解析 `div#box` 选择器定义的样式。对于类选择器，也可以使用这种方式限制其应用范围，并增加其优先级。

例如：

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>类选择器</title> 
		<style type="text/css">
			/* ID 样式 */
			#box {
				background: url(images/1.png) center bottom;	/* 定义背景图片并让其居中、底部对齐 */
				height: 200px;	/* 固定盒子的高度 */
				width: 400px;	/* 固定盒子的宽度 */
				border:solid 2px red;	/* 边框 */
				padding: 100px;	/* 增加内边距 */
			}
		</style>
	</head>
	<body>
		<div id="box">问君有几多愁，恰似一江春水向东流。</div>
	</body>
</html>
```

效果如下：

![01](./images/01.png)