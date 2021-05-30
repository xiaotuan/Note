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

