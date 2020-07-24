当你需要从 DOM 中选择元素时，jQuery 提供两种备选方案。这两种选项都要求使用 jQuery 函数（ `jQuery()` 或其别名 `$()` ）。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Ready</title>
    </head>
    <body>
        <a href='#'>link</a>
        <a href='#'>link</a>
        <a href='#'>link</a>
        <a href='#'>link</a>
        <a href='#'>link</a>
        <a href='#'>link</a>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            // 用警告框显示页面上有6个元素
            alert('Page contains ' + jQuery('a').length + ' <a> elements!');
        </script>
    </body>
</html>
```

jQuery 函数的第一个参数能够接受多个表达式，只要在传递给 jQuery 函数的第一个字符串参数中用逗号分隔多个选择器就行了。

```javascript
jQuery('selector1, selector2, selector3').length;
```

