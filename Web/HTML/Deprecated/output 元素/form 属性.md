HTML 5 为 `output` 元素增加 `form` 属性，该属性用于声明元素属于哪个表单，而并不关心元素具体在页面的哪个位置，甚至是表单之外都可以。

语法：

```html
<output form="form_id">
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

        <form action="/statics/demosource/demo-form.php" id="numform" oninput="x.value=parseInt(a.value)+parseInt(b.value)">0
        <input type="range" id="a" name="a" value="50">100
        +<input type="number" id="b" name="b" value="50">
        <br><br>
        <input type="submit">
        </form>

        <p> element 元素在表单之外,但它仍属于该表单的一部分。</p>
        <output form="numform" name="x" for="a b"></output>

        <p><b>注意:</b>几乎所有的主流浏览器都不支持 form 属性。</p>

    </body>
</html>
```

