CSS 继承性是指后代元素可以继承祖先元素的样式。继承样式主要包括字体、文本等基本属性，如字体、字号、颜色、行距等，对于下面类型属性是不允许继承的：边框、边界、补白、背景、定位、布局、尺寸等。例如：

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>CSS3</title> 
		<style type="text/css">
			body {
				font-size: 12px;
			}
		</style>
	</head>
	<body>
		<div id="wrap">
			<div id="header">
				<div id="menu">
					<ul>
						<li><span>首页</span></li>
						<li>菜单项</li>
					</ul>
				</div>
			</div>
			<div id="main">
				<p>主体内容</p>
			</div>
		</div>
	</body>
</html>
```

