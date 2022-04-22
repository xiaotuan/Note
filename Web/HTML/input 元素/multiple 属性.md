[toc]

> 注意：`multiple` 属性是 HTML5 中的新属性。

### 1. 支持浏览器

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 支持 `multiple` 属性。

**注意：**Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `multiple` 属性。

### 2. 定义和用法

`multiple` 属性是一个布尔属性。

`multiple` 属性规定允许用户输入到 `<input>` 元素的多个值。

**注意：**`multiple` 属性适用于以下 `input` 类型：email 和 file。

### 3. 语法

```html
<input multiple>
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

        <form action="/statics/demosource/demo-form.php">
          选择图片: <input type="file" name="img" multiple>
          <input type="submit">
        </form>

        <p>尝试选取一张或者多种图片。</p>

        <p><strong>注意:</strong>  Internet Explorer 9及更早IE版本不支持input标签的 multiple 属性。</p>

    </body>
</html>
```

