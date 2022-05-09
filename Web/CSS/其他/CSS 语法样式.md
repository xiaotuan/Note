CSS3 语法样式包含两部分内容：选择器和声明。例如：

```
 选择器   样式分隔符	    声明           声明        样式分隔符
   p		{      font-size: 14px;	color: #000;      }
网页标签名               属性    属性值  属性   属性值
```

+ 选择器：指定样式用于哪些对象，这些对象可以是某个标签、指定 Class 或 ID 值的元素等。
+ 声明：指定浏览器如何渲染选择器匹配的对象。声明包括属性和属性值，并用分号来标识一个声明的结束，在一个样式中最后一个声明可以省略分号。
+ 属性：CSS 预设的样式选项。
+ 属性值：定义显示效果的值，包括值和单位；或者仅定义一个关键字。

例如：

```css
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>CSS3</title> 
		<style type="text/css">
			body {	/* 页面基本属性 */
				font-size: 12px;
				color: #CCCCCC;
			}
			/* 段落文本基础属性 */
			p {
				background-color: #FF00FF;
			}
		</style>
	</head>
	<body>
		<p>At first glance, it may appear that some listings are missing—Because working examples requires both HTML and CSS, I have put most listings in an HTML file, using <style> tags for the CSS. This means that both an HTML listing and CSS listing are combined in one file in the repository.</p>
	</body>
</html>
```

