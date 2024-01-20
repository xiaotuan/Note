`CSS` 变形的原点默认为对象的中心点（50%，50%），使用 `transform-origin` 属性可以重新设置变形原点。语法格式如下：

```
transform-origin: [<percentage> | <length> | left | center① | right] [<percentage> | <length> | top | center② | bottom]?
```

取值简单说明如下：

+ `<percentage>`：用百分比指定坐标值。可以为负值。
+ `<length>`：用长度值指定坐标值。可以为负值。
+ `left`：指定原点的横坐标为 `left`；
+ `center①`：指定原点的横坐标为 `center`。
+ `right`：指定原点的横坐标为 `right`。
+ `top`：指定原点的纵坐标为 `top`。
+ `center②`：指定原点的纵坐标为 `center`。
+ `bottom`：指定原点的纵坐标为 `bottom`。

示例代码：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>设置变形的原点</title>
        <style>
            img {
                position: absolute;
                left: 20px;
                top: 10px;
                width: 250px;
            }
            img.bg {
                opacity: 0.3;
                border: dashed 1px red;
            }
            img.change {
                border: solid 1px red;
                -moz-transform-origin: top right;
                -webkit-transform-origin: top right;
                -o-transform-origin: top right;
                transform-origin: top right;
                -webkit-transform: rotate(-45deg);
                -moz-transform: rotate(-45deg);
                -o-transform: rotate(-45deg);
                transform: rotate(-45deg);
            }
        </style>
    </head>
    <body>
        <img class="bg" src="images/1.jpg" />
        <img class="change" src="images/1.jpg" />
    </body>
</html>
```

效果如下：

![01](./images/01.png)