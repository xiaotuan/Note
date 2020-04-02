<center><font size="5"><b>伪类选择器required与optional</b></font></center>

+ `E:required` 伪类选择器用来指定允许使用 required 属性，且已经指定了 required 属性的 input 元素、select 元素以及 textarea 元素的样式。
+ `E:optional` 伪类选择器用来指定允许使用 required 属性，且未指定 required 属性的 input 元素、select元素以及 textarea 元素的样式。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <title>伪类选择器required与optional使用示例</title>
        <style type="text/css">
        input[type="text"]:required {
            border-color: red;
            border-width: 3px;
        }
        input[type="text"]:optional {
            border-color: black;
            border-width: 1px;
        }
        </style>
    </head>
    <body>
        <form>
            姓名：<input type="text" required placeholder="必须输入姓名" /><br/>
            住址：<input type="text" />
        </form>
    </body>
</html>
```



