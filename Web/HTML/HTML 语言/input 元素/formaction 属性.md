[toc]

> 注意：`formaction` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 都支持 `formaction` 属性。

> **注意：**Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `formaction` 属性。

### 2. 定义和用法

`formaction` 属性规定当表单提交时处理输入控件的文件的 URL。

`formaction` 属性覆盖 `<form>` 元素的 `action` 属性。

> **注释：**`formaction` 属性适用于 `type="submit"` 和 `type="image"`。

### 3. 语法

```html
<input formaction="URL">
```

### 4. 属性值

| 值   | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| URL  | 规定当表单提交时处理输入控件的文件的 URL。可能的值：绝对 URL - 某个页面的完整地址（比如 href="http://www.example.com/formresult.html"）相对 URL - 指向当前站点内的一个文件（比如 href="formresult.html"） |

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
          First name: <input type="text" name="fname"><br>
          Last name: <input type="text" name="lname"><br>
          <input type="submit" value="提交"><br>
          <input type="submit" formaction="/statics/demosource/demo-admin.php" value="以管理员提交">
        </form>
        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本不支持 input 标签的 formaction 属性。</p>

    </body>
</html>
```

