[toc]

> 注意：`formaction` 属性是 HTML 5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10, Firefox, Opera, Chrome, 和 Safari 支持 `formaction` 属性。

> **注意：** Internet Explorer 9 及更早IE版本不支持 `formaction` 属性。

### 2. 定义和用法

`formaction` 属性覆盖 `form` 元素的 `action` 属性。

该属性与 `type="submit"` 配合使用。

### 3. 语法

```html
<button type="submit" formaction="URL">
```

### 4. 属性值

| 值   | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| URL  | 规定将表单数据发送到的地址。可能值：绝对 URL - 完整的页面URL地址(如：href="http://www.example.com/formresult.html" rel="external nofollow" target="_blank" )相对 URL 地址 -指向当前网站的一个文件(如：href="formresult.html") |

### 5. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php" method="get">
        First name: <input type="text" name="fname" /><br>
        Last name: <input type="text" name="lname" /><br>
        <button type="submit">提交</button><br>
        <button type="submit" formaction="/statics/demosource/demo-admin.php" method="get">提交</button>
        </form>

        <p><strong>注意：</strong> Internet Explorer 9 及更早 IE 版本不支持 formaction 属性。</p>
    </body>
</html>
```

