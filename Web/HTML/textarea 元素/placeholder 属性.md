HTML 5 为 `textarea` 元素新增 `placeholder` 属性，该属性可以在用户输入时进行提示。例如：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        您是谁？
        <textarea rows="4" cols="50" placeholder="描述信息..."></textarea>

        <p><strong>注意：</strong>Internet Explorer 9 及更早 IE 版本不支持 textarea 标签的  placeholder 属性。</p>

    </body>
</html>
```

> 注意
>
> 上面的例子中，如果 `textarea` 标签写成如下形式：
>
> ```html
> <textarea rows="4" cols="50" placeholder="描述信息...">
> </textarea>
> ```
>
> 将会导致 `placeholder` 属性失效。