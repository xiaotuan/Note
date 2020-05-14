```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Example02</title>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>
        <div>old content</div>
        <div>old content</div>
        <div>old content</div>
        <div>old content</div>
        <script>
            // 隐藏页面上的所有div
            // 更新所有div中包含的文本
            // 为所有 div 添加值为 updatedContent 的 class 属性
            // 显示页面上的所有div
            jQuery('div').hide().text('new content').addClass("updatedContent").show();
        </script>
    </body>
</html>
```

jQuery 扫描网页，将所有 \<div\> 元素放在包装器集中，这样在后续方法中都会对包装器集中的每一个元素上执行该方法。

> 某些情况下只有第一个元素（而不是包装器集中的所有元素）受到 jQuery 方法（例如，`attr()`）的影响。

