[toc]

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera 和 Chrome 支持 required 属性。

> **注意：**Safari 或者 Internet Explorer 9 及之前的版本不支持 `<input>` 属性的 required 属性。

### 2. 定义和用法

`required` 属性是一个布尔属性。

`required` 属性规定必需在提交表单之前填写输入字段。

> 注意
>
> `required` 属性适用于下面的 `input` 类型：`text`、`search`、`url`、`tel`、`email`、`password`、`date pickers`、`number`、`checkbox`、`radio` 和 `file`。

### 3. 支持版本

`required` 属性是 HTML5 中的新属性。

### 4. 语法

```html
<input required>
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

        <form action="/statics/demosource/demo-form.php">
          Username: <input type="text" name="usrname" required>
          <input type="submit">
        </form>

        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本，或Safari不支持input标签的 required 属性。</p>

    </body>
</html>
```

