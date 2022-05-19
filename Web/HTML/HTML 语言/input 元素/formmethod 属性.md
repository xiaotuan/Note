[toc]

> 注意：`formmethod` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 支持 `formmethod` 属性。

> **注意：**Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `formmethod` 属性。

### 2. 定义和用法

`formmethod` 属性定义发送表单数据到 action URL 的 HTTP 方法。

`formmethod` 属性覆盖 `<form>` 元素的 `method` 属性。

**注意：**`formmethod` 属性与 `type="submit"` 和 `type="image"` 配合使用。

表单数据可被作为 URL 变量的形式来发送（`method="get"`）或者作为 HTTP post 事务的形式来发送（`method="post"`）。

**关于 "get" 方法的注释：**

- 该方法将表单数据以名称/值对的形式附加到 URL 中
- 该方法对于用户希望加入书签的表单提交很有用
- URL 的长度是有限的（不同浏览器限制不一样），因此，您不能确定是否所有的表单数据都能被正确传输
- 绝不要使用 "get" 方法来发送敏感数据！（比如密码或者其他敏感信息，在浏览器的地址栏中是可见的）、

**关于 "post" 方法的注释：**

- 该方法将表单数据以 HTTP post 事务的形式发送
- 通过 "post" 方法提交的表单不能加入书签
- "post" 方法比 "get" 更安全，且 "post" 没有长度限制

### 3. 语法

```html
<input formmethod="get|post">
```

### 4. 属性值

| 值   | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| get  | 默认。将表单数据（form-data）以名称/值对的形式附加到 URL：URL?name=value&name=value。 |
| post | 以 HTTP post 事务的形式发送表单数据（form-data）。           |

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
          First name: <input type="text" name="fname"><br>
          Last name: <input type="text" name="lname"><br>
          <input type="submit" value="提交">
          <input type="submit" formmethod="post" formaction="/statics/demosource/demo-post.php" value="使用 POST 提交">
        </form>

        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本不支持 input 标签的 formmethod 属性。</p>

    </body>
</html>
```

