[toc]

### 1. 浏览器支持

除了 Internet Explorer 和 Safari，其他主流浏览器都支持 `required` 属性。

### 2. 定义和用法

`required` 属性是一个布尔属性。

`required` 属性规定一个文本区域是必需的或必须填写（以提交表单）。

### 3. HTML可用版本

HTML 5

### 4. 语法

```html
<textarea required>
```

### 5. 示例

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="demo-form.php">
            <textarea rows="4" cols="50" name="comment" required></textarea>
            <input type="submit">
        </form>

        <p><b>注意：</b> IE 9 及更早 IE 版本，Safari浏览器不支持 required 属性。</p>

    </body>
</html>
```

