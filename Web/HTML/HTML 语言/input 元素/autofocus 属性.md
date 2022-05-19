HTML 5 为 `input` 元素增加了 `autofocus` 属性，该属性表示在打开页面时使元素自动获得焦点。例如：

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>

    <body>

        <form action="/statics/demosource/demo-form.php">
          First name: <input type="text" name="fname" autofocus><br>
          Last name: <input type="text" name="lname"><br>
          <input type="submit">
        </form>
        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本不支持input标签的 autofocus 属性。</p>

    </body>
</html>
```

