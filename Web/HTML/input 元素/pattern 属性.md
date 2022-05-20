[toc]

> 注意：`pattern` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera 和 Chrome 支持 `pattern` 属性。

> **注意：**Safari 或者 Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `pattern` 属性。

### 2. 定义和用法

`pattern` 属性规定用于验证 `<input>` 元素的值的正则表达式。

> **注意：**`pattern` 属性适用于下面的 `input` 类型：text、search、url、tel、email 和 password。

> **提示：**请使用全局的 [title](https://www.w3cschool.cn/htmltags/att-global-title.html) 属性来描述模式以帮助用户。

> **提示：**可以在我们的 JavaScript 教程中学习更多有关 [正则表达式](https://www.w3cschool.cn/javascript/js-obj-regexp.html) 的知识。

### 3. 语法

```html
<input pattern="regexp">
```

### 4. 属性值

| 值     | 描述                                        |
| :----- | :------------------------------------------ |
| regexp | 规定用于验证 <input> 元素的值的正则表达式。 |

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
          Country code: <input type="text" name="country_code" pattern="[A-Za-z]{3}" title="Three letter country code">
          <input type="submit">
        </form>

        <p><strong>注意:</strong>  Internet Explorer 9及更早IE版本，或Safari不支持input标签的 pattern 属性。</p>

    </body>
</html>
```

