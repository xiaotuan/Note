`transparent` 属性值用来指定全透明色彩，等效于 `rgba(0,0,0,0)` 值。

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			#demo {
				width: 0;
				height: 0;
				border-left: 50px solid transparent;
				border-right: 50px solid transparent;
				border-bottom: 100px solid red;
			}
			#demo1 {
				width: 0;
				height: 0;
				border-left: 50px solid transparent;
				border-right: 50px solid transparent;
				border-top: 100px solid red;
			}
			#demo2 {
				width: 0;
				height: 0;
				border-top: 50px solid transparent;
				border-right: 100px solid red;
				border-bottom: 50px solid transparent;
			}
			#demo3 {
				width: 0;
				height: 0;
				border-top: 50px solid transparent;
				border-left: 100px solid red;
				border-bottom: 50px solid transparent;
			}
			#demo4 {
				width: 0;
				height: 0;

				border-top: 100px solid red;
				border-right: 100px solid transparent;
			}
			#demo5 {
				width: 0;
				height: 0;

				border-top: 100px solid red;
				border-left: 100px solid transparent; 
			}
			#demo6 {
				height: 0;
				width: 120px;
				border-bottom: 120px solid #ec3504;
				border-left: 60px solid transparent;
				border-right: 60px solid transparent;

			}
		</style>
	</head>

	<body>
		<div id="demo"></div>
		<br />
		<div id="demo1"></div>
		<br />
		<div id="demo2"></div>
		<br />
		<div id="demo3"></div>
		<br />
		<div id="demo4"></div>
		<br />
		<div id="demo5"></div>
		<br />
		<div id="demo6"></div>
	</body>
</html>
```

运行效果如下：

![05](./images/05.png)