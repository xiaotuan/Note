[toc]

> 注意：`list` 属性是 HTML5 中的新属性。

### 1. 支持浏览器

Internet Explorer 10、Firefox、Opera 和 Chrome 支持 `list` 属性。

> **注意：**Safari 或者 Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `list` 属性。

### 2. 定义和用法

`list` 属性引用 `<datalist>` 元素，其中包含 `<input>` 元素的预定义选项。

### 3. 语法

```html
<input list="datalist_id">
```

### 4. 属性值

| 值          | 描述                                       |
| :---------- | :----------------------------------------- |
| datalist_id | 规定绑定到 <input> 元素的 datalist 的 id。 |

### 5. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php" method="get">
        <input list="browsers" name="browser">
        <datalist id="browsers">
          <option value="Internet Explorer">
          <option value="Firefox">
          <option value="Chrome">
          <option value="Opera">
          <option value="Safari">
        </datalist>
        <input type="submit">
        </form>

        <p><strong>注意:</strong> Internet Explorer 9（更早IE版本），Safari不支持 datalist 标签。</p>

    </body>
</html>
```

