<center><font size="5"><b>伪类选择器in-range与out-of-range</b></font></center>

+ `E:in-range` 伪类选择器用来指定当元素的有效值被限定在一段范围之内（通常通过 min 属性值与 max 属性值来限定），且实际输入值在该范围内时使用的样式。
+ `E:out-of-range` 伪类选择器用来指定当元素的有效值被限制在一段范围之内（通常通过 min 属性值与 max 属性值来限定），且实际输入值在该范围之外时使用的样式。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <title>伪类选择器in-range与out-of-range使用示例</title>
        <style type="text/css">
        inpt[type="number"]:in-range {
            background-color: white;
        }
        input[type="number"]:out-of-range {
            background-color: red;
        }
        </style>
    </head>
    <body>
        <form>
            请输入1到100之内的数值：<input type="number" min="0" max="100"/>
        </form>
    </body>
</html>
```

