[toc]

> 注意：`formnovalidate` 属性是 HTML 5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10, Firefox, Opera, Chrome支持 `formmethod` 属性。

> **注意：** Safari、Internet Explorer 9 及更早IE版本不支持 `formmethod` 属性。

### 2. 定义和用法

`formnovalidate` 属性是一个 boolean（布尔） 属性。

如果使用该属性，则提交表单时按钮不会执行验证过程。`formnovalidate` 属性覆盖表单的 `novalidate` 属性。

该属性与 `type="submit"` 配合使用。

### 3. 语法

```html
<button type="submit" formnovalidate>
```

### 4. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php" method="get">
        E-mail: <input type="email" name="userid" /><br>
        <button type="submit" >提交</button><br>
        <button type="submit" formnovalidate>不验证提交</button>
        </form>

        <p><strong>注意：</strong> Safari、Internet Explorer 9 及更早IE版本不支持 formmethod 属性。</p>

    </body>
</html>
```

