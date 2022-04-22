[toc]

> 注意：`formtarget` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 支持 `formtarget` 属性。

> **注意：**Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `formtarget` 属性。

### 2. 定义和用法

`formtarget` 属性规定表示提交表单后在哪里显示接收到响应的名称或关键词。

`formtarget` 属性覆盖 `<form>` 元素的 `target` 属性。

> **注意：**`formtarget` 属性可以与 `type="submit"` 和 `type="image"` 配合使用。

### 3. 语法

```html
<input formtarget="_blank|_self|_parent|_top|framename">
```

### 4. 属性值

| 值        | 描述                           |
| :-------- | :----------------------------- |
| _blank    | 在新窗口/选项卡中显示响应。    |
| _self     | 在同一框架中显示响应（默认）。 |
| _parent   | 在父框架中显示响应。           |
| _top      | 在整个窗口中显示响应。         |
| framename | 在指定的 iframe 中显示响应。   |

### 5. 示例代码

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php">
          First name: <input type="text" name="fname"><br>
          Last name: <input type="text" name="lname"><br>
          <input type="submit" value="正常提交">
          <input type="submit" formtarget="_blank" value="提交到一个新的页面上">
        </form>

        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本不支持 input 标签的 formtarget 属性。</p>

    </body>
</html>
```

