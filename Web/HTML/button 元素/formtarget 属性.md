[toc]

> 注意：`formtarget` 属性是 HTML 5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10, Firefox, Opera, Chrome, 和 Safari 支持 `formtarget` 属性。

> **注意：** Internet Explorer 9 及更早IE版本不支持 `formtarget` 属性。

### 2. 定义和用法

`formtarget` 属性指定在提交表单后在哪里显示响应。`formtarget` 属性覆盖表单元素的 `target` 属性。

该属性与 `type="submit"` 配合使用。

### 3. 语法

```html
<button type="submit" formtarget="_blank|_self|_parent|_top|framename">
```

### 4. 属性值

| 值        | 描述                                   |
| :-------- | :------------------------------------- |
| _blank    | 在新窗口/选项卡中将表单提交到文档。    |
| _self     | 在同一框架中将表单提交到文档。（默认） |
| _parent   | 在父框架中将表单提交到文档。           |
| _top      | 在整个窗口中将表单提交到文档。         |
| framename | 在指定的框架中将表单提交到文档。       |

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
        <button type="submit" >提交</button>
        <button type="submit" formtarget="_blank">提交到一个新窗口或选项卡</button>
        </form>

        <p><strong>注意：</strong> Internet Explorer 9 及更早 IE 版本不支持 formtarget 属性。</p>

    </body>
</html>
```

