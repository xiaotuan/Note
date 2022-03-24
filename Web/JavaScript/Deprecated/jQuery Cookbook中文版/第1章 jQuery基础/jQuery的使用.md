```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Example01</title>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>
        <div>old content</div>
        <script>
            // 隐藏页面上的所有div
            jQuery('div').hide();
            // 更新所有div中包含的文本
            jQuery('div').text('new content');
            // 为所有 div 添加值为 updatedContent 的 class 属性
            jQuery('div').addClass("updatedContent");
            // 显示页面上的所有div
            jQuery('div').show();
        </script>
    </body>
</html>
```

