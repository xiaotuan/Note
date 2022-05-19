[toc]

> 注意：`formmethod` 属性是 HTML 5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10, Firefox, Opera, Chrome, 和 Safari 支持 `formmethod` 属性。

> **注意：**Internet Explorer 9 及更早IE版本不支持 `formmethod` 属性。

### 2. 定义和用法

`formmethod` 属性制定发送表单数据使用的 HTTP 方法。`formmethod` 属性覆盖 `form` 元素的 `method` 属性。

`formmethod` 属性需与 `type="submit"` 配合使用。

可以通过以下方式发送 form-data ：

- 以 URL 变量 (使用 `method="get"`) 的形式来发送
- 以 HTTP post (使用 `method="post"`) 的形式来发送

使用 "get" 方法:

- 表单数据在URL中以 name/value 对出现。
- get传送的数据量较小，不能大于2KB，这主要是因为受URL长度限制。
- 不要使用 "get" 方法传送敏感信息！(密码或者敏感信息会出现在浏览器的地址栏中)

使用 "post" 方法:

- 以 HTTP post 形式发送表单数据。
- 比 "get" 方法更强大更安全。
- 没有大小限制

### 3. 语法

```html
<button type="submit" formmethod="get|post">
```

### 4. 属性值

| 值   | 描述                                                        |
| :--- | :---------------------------------------------------------- |
| get  | 向 URL 追加表单数据（form-data）：URL?name=value&name=value |
| post | 以 HTTP post 事务的形式发送表单数据（form-data）            |

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
        <button type="submit" formmethod="post" formaction="/statics/demosource/demo-post.php">使用 POST 提交</button>
        </form>

        <p><strong>注意：</strong> Internet Explorer 9 及更早IE版本不支持 formmethod 属性。</p>

    </body>
</html>
```

