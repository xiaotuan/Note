`opacity` 属性定义元素对象的不透明度。其语法格式如下：

```css
opacity: <alphavalue> | inherit;
```

取值简单说明如下：

+ `<alphavalue>`：由浮点数字和单位标识符组成的长度值。不可为负值，默认值为1。opacity 取值为 1 时，元素是完全不透明的；取值为 0 时，元素是完全透明、不可见的；介于 1 到 0 之间的任何值都表示该元素的不透明程度。
+ inherit：表示继承父辈元素的不透明性。

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style type="text/css">
            body {
                margin: 0;
                padding: 0;
            }
            div { position: absolute; }
            .bg {
                width: 100%;
                height: 100%;
                background: #000;
                opacity: 0.7;
                filter: alpha(opacity=70);
            }
            .login {
                text-align:center;
                width:100%;
                top: 20%;
            }
    	</style>
    </head>
    <body>
        <div class="web"><img src="images/bg.png" /></div>
        <div class="bg"></div>
        <div class="login"><img src="images/login.png"  /></div>
    </body>
</html>
```

运行效果如下：

![04](./images/04.png)