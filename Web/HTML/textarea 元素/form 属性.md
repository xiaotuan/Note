HTML 5 为 `textarea` 元素增加 `form` 属性，该属性用于声明元素属于哪个表单，而并不关心元素具体在页面的哪个位置，甚至是表单之外都可以。

语法：

```html
<textarea form="form_id">
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

        <form action="demo-form.php" id="usrform">
          Name: <input type="text" name="usrname">
          <input type="submit">
        </form>
        <br>
        <textarea rows="4" cols="50" name="comment" form="usrform">输入内容...</textarea>

        <p>以上的表单在文本框之外，但是它仍是表单中的一部分。</p>

        <p><b>注意：</b> IE 不支持 form 属性。</p>

    </body>
</html>
```

