[toc]

> 注意：`formnovalidate` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera 和 Chrome 支持 `formnovalidate` 属性。

> **注意：**Safari 或者 Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `formnovalidate` 属性。

### 2. 定义和用法

`novalidate` 属性是一个布尔属性。

`novalidate` 属性规定当表单提交时 `<input>` 元素不进行验证。

`formnovalidate` 属性覆盖 `<form>` 元素的 `novalidate` 属性。

> **注意：**`formnovalidate` 属性可与 `type="submit"` 配合使用。

### 3. 语法

```html
<input formnovalidate="formnovalidate">
```

> **注意：**`formnovalidate` 属性是一个布尔属性，且可通过下面的方式进行设置：
>
> - `<input formnovalidate>`
> - `<input formnovalidate="formnovalidate">`
> - `<input formnovalidate="">`

### 4. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php">
          E-mail: <input type="email" name="userid"><br>
          <input type="submit" value="提交"><br>
          <input type="submit" formnovalidate="formnovalidate" value="不验证提交">
        </form>

        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本,或Safari不支持 input 标签的 formnovalidate 属性。</p>

    </body>
</html>
```

