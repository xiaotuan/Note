[toc]

### 1. 问题

你需要选择一个 DOM 元素或者一组 DOM 元素，以便用 jQuery 方法用于这些元素。

### 2. 解决方案

当你需要从 DOM 中选择元素时，jQuery 提供两种备选方案：`jQuery()` 或 `$()`。下面的代码是一个例子，选择 HTML 文档中的所有 `<a>` 元素：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>jQuery Cookbook</title>
    
</head>
<body>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        // 用警告框显示页面上有 6 个元素
        alert('Page contains ' + jQuery('a').length + ' <a> elements!');
    </script>
</body>
</html>
```

jQuery 函数的第一个参数能够接受多个表达式，只要在传递给 jQuery 函数的第一个字符串参数中用逗号分隔多个选择器就行了。

```js
jQuery('selector1, selector2, selector3').length;
```

选择 DOM 元素的第二种选项是向 jQuery 函数传递 DOM 元素的实际 JavaScript 引用。下面的代码将选择 HTML 文档中的所有 `<a>` 元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>jQuery Cookbook</title>
    
</head>
<body style="background-color: yellow;">
    <!-- yes the attribute is depreciated, I know, roll with it -->
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        // 用警告框显示页面上有 6 个元素
        alert('Page contains ' + jQuery(document.getElementsByName('a')).length 
            + ' <a> elements, And has a ' + jQuery(document.body).css("background-color") + " backgroudColor.");
    </script>
</body>
</html>
```

### 3. 讨论

jQuery 能够胜任繁重的工作，这在某种程度上是因为选择器引擎 Sizzle（<https://github.com/jquery/sizzle/wiki>），该引擎能够从 HTML 文档中选择 DOM 元素。

