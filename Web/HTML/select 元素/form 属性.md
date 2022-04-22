HTML 5 为 `select` 元素增加 `form` 属性，该属性用于声明元素属于哪个表单，而并不关心元素具体在页面的哪个位置，甚至是表单之外都可以。

语法：

```html
<select form="form_id">
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

        <form action="/statics/demosource/demo-form.php" id="carform">
          Firstname:<input type="text" name="fname">
          <input type="submit">
        </form>
        <br>
        <select name="carlist" form="carform">
          <option value="volvo">Volvo</option>
          <option value="saab">Saab</option>
          <option value="opel">Opel</option>
          <option value="audi">Audi</option>
        </select>

        <p>下拉列表超出了表单元素,但仍是表单的一部分。</p>
        <p><b>注意:</b> Internet Explorer 不支持 select 标签的 form 属性。</p>

    </body>
</html>
```

