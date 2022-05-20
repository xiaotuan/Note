HTML 5 为 `fieldset` 元素增加 `form` 属性，该属性用于声明元素属于哪个表单，而并不关心元素具体在页面的哪个位置，甚至是表单之外都可以。

语法：

```html
<fieldset form="form_id">
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

        <form action="/statics/demosource/demo-form.php" method="get" id="form1">
你喜欢的颜色是什么？<input type="text" name="fav_color"><br>
        <input type="submit">
        </form>

        <p>下面的自定义字段在表单外,但仍是表单的一部分。</p>

        <fieldset form="form1">
          <legend>个人信息:</legend>
          姓名: <input type="text" name="username"><br>
          邮箱: <input type="text" name="usermail"><br>
        </fieldset>

        <p><b>注意：</b>目前，只有 Opera 支持 form 属性。</p>

    </body>
</html>
```

