HTML 5 为 `button` 元素增加 `form` 属性，该属性用于声明元素属于哪个表单，而并不关心元素具体在页面的哪个位置，甚至是表单之外都可以。

语法：

```html
<button form="form_id">
```

属性值：

| 值      | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| form_id | 规定 `<input>` 元素所属的一个或多个表单的 id 列表，以空格分隔。 |

例如：

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php" method="get" id="nameform">
        First name: <input type="text" name="fname" /><br>
        Last name: <input type="text" name="lname" /><br>
        </form>

        <p>下面的按钮是在表单元素外,但仍是表单的一部分。</p>

        <button type="submit" form="nameform" value="提交">提交</button>

        <p><b>注意：</b>除了 Internet Explorer 浏览器，其他主流浏览器都支持 form 属性。</p>

    </body>
</html>
```

