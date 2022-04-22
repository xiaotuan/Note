[toc]

> 注意：`formenctype` 属性是 HTML 5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10, Firefox, Opera, Chrome, 和 Safari 支持 formenctype属性。

> **注意：** Internet Explorer 9 及更早IE版本不支持 `formenctype`属性。

### 2. 定义和用法

`formenctype` 属性覆盖 `form` 元素的 `enctype` 属性。

该属性与 `type="submit"` 配合使用。

### 3. 语法

```html
<button type="submit" formenctype="value">
```

### 4. 属性值

| 值                                | 描述                                                       |
| :-------------------------------- | :--------------------------------------------------------- |
| application/x-www-form-urlencoded | 在发送前对所有字符进行编码（默认）。                       |
| multipart/form-data               | 不对字符编码。当使用有文件上传控件的表单时，该值是必需的。 |
| text/plain                        | 将空格转换为 "+" 符号，但不编码特殊字符。                  |

### 5. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo_post_enctype.php" method="post">
        Name: <input type="text" name="fname" value="Ståle Refsnes" /><br>
        <button type="submit" >使用默认编码提交</button>
        <button type="submit" formenctype="multipart/form-data">使用multipart/form-data编码提交</button>
        </form>

        <p><strong>注意：</strong> Internet Explorer 9 及更早 IE 版本不支持 formenctype 属性。</p>

    </body>
</html>
```

