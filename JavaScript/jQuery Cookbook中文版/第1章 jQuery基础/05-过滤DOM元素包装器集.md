[toc]

### 1. 问题

在 jQuery 包装器集中有一组选中的 DOM 元素，但是打算从集合中删除不匹配新指定表达式的元素，以创建一个新的操作元素集合。

### 2. 解决方案

可以使用 `filter()` 方法过滤当前的元素集。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>jQuery Cookbook</title>
    
</head>
<body>
    <a href="#" class="external">link</a>
    <a href="#" class="external">link</a>
    <a href="#">link</a>
    <a href="#" class="external">link</a>
    <a href="#" class="external">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        // 在警告框中显示集合中还有 4 个元素
        alert(jQuery('a').filter('.external').length + " external links");
    </script>
</body>
</html>
```

### 3. 讨论

向 `filter()` 方法传递一个用于过滤包装器集的函数也是可行的。

```js
alert(jQuery('a').filter(function(index) {
    return $(this).hasClass('external');
}).length + " external links");
```

调用这个函数的上下文与当前元素相同，也就是说当在函数中使用 `$(this)` 时，实际应用的是包装器集中的每个 DOM 元素。

这里向函数传递了一个名为 index 的参数，在必要的时候，这个参数可用来以数字像是指出 jQuery 包装器集中元素的索引