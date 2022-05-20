[toc]

> 注意：`formenctype` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 支持 `formenctype` 属性。

> **注意：**Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `formenctype` 属性。

### 2. 定义和用法

`formenctype` 属性规定当表单数据提交到服务器时如何编码（仅适用于 `method="post"` 的表单）。

`formenctype` 属性覆盖 `<form>` 元素的 `enctype` 属性。

> **注释：**`formenctype` 属性与 `type="submit"` 和 `type="image"` 配合使用。

### 3. 语法

```html
<input formenctype="value">
```

### 4. 属性值

| 值                                | 描述                                                         |
| :-------------------------------- | :----------------------------------------------------------- |
| application/x-www-form-urlencoded | 默认。在发送前对所有字符进行编码。将空格转换为 "+" 符号，特殊字符转换为 ASCII HEX 值。 |
| multipart/form-data               | 不对字符编码。当使用有文件上传控件的表单时，该值是必需的。   |
| text/plain                        | 将空格转换为 "+" 符号，但不编码特殊字符。                    |

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
          First name: <input type="text" name="fname"><br>
          <input type="submit" value="提交">
          <input type="submit" formenctype="multipart/form-data" value="以Multipart/form-data提交">
        </form>

        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本不支持input标签的 formenctype 属性。</p>

    </body>
</html>
```

