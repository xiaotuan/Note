HTML 5 为 `input` 元素增加 `form` 属性，该属性用于声明元素属于哪个表单，而并不关心元素具体在页面的哪个位置，甚至是表单之外都可以。

语法：

```html
<input form="form_id">
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
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php" id="form1">
        First name: <input type="text" name="fname"><br>
        <input type="submit" value="提交">
        </form>

        <p> "Last name" 字段没有在form表单之内，但它也是form表单的一部分。</p>

        Last name: <input type="text" name="lname" form="form1">

        <p><b>注意:</b> IE不支持form属性</p>

    </body>
</html>
```

