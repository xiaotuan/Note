通常只在 DOM 完全加载之后才执行 JavaScript。实际情况是，任何 DOM 遍历和操作都要求在操作之前必须加载 DOM。如果在这种情况下使用 `window.onload` 事件，包括所有资源的整个文档完全加载之后才能触发 onload 事件，这太浪费时间了。

jQuery 提供 `ready()` 方法，通常与 DOM 的文档对象绑定。 `ready()` 方法的参数是一个函数，后者包含在 DOM 可以遍历和操纵时执行的 JavaScript 代码。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Ready</title>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            jQuery(document).ready(function(){
                // DOM not loaded, must use ready event
                alert(jQuery('p').text());
            })
        </script>
    </head>
    <body>
        <p>The DOM is ready!</p>
    </body>
</html>
```

> 建议将 `ready()` 的脚本放在样式表声明和包含文件之后，这样能够确保 `ready()` 事件执行任何 jQuery 或 JavaScript 代码之前，所有元素属性都已经正确定义。

使用jQuery 的 ready 事件的快捷方式：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Ready</title>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            jQuery(function(){
                // DOM not loaded, must use ready event
                alert(jQuery('p').text());
            })
        </script>
    </head>
    <body>
        <p>The DOM is ready!</p>
    </body>
</html>
```

jQuery 用 `ready()` 事件处理程序方法代替了 JavaScript 的 `Window.onload` 事件。使用这个定制事件时，建议将它放在样式表声明和包含文件之后，这样能够确保 `ready()` 事件执行任何 jQuery 或 JavaScript 代码之前，所有元素属性都已经正确定义。

使用 ready 事件的简洁方式：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        jQuery(function() {
            // DOM 未加载，必须使用就绪事件
            alert(jQuery('p').text());
        })
    </script>
</head>
<body>
    <p>The DOM is ready!</p>
</body>
</html>
```

ready 事件只有在 JavaScript 必须嵌入到页面顶端的文档流并封装在 \<head\> 元素里才有必要。

如果将 JavaScript 代码放到页面最后，可以不需要使用 `ready()` 事件:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>jQuery Cookbook</title>
    
</head>
<body>
    <p>The DOM is ready!</p>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        alert(jQuery('p').text());  // 提示 DOM 已经加载
    </script>
</body>
</html>
```

