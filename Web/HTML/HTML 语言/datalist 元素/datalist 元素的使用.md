[toc]

> 注意：`<datalist>` 标签是 HTML5 中的新标签。

### 1. 浏览器支持

IE 10、Firefox、Opera 和 Chrome 支持 `<datalist>` 标签。

> **注释：**IE 9 和更早版本的 IE 浏览器 以及 Safari 不支持 `<datalist>` 标签。

### 2. 标签定义及使用说明

`<datalist>` 标签规定了 `<input>` 元素可能的选项列表。

`<datalist>` 标签被用来在为 `<input>` 元素提供"自动完成"的特性。用户能看到一个下拉列表，里边的选项是预先定义好的，将作为用户的输入数据。

请使用 `<input>` 元素的 `list` 属性来绑定 `<datalist>` 元素。

**提示：**不能控制 `datalist` 的位置，并且不能将其与服务器的数据进行绑定。

### 3. 示例

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

