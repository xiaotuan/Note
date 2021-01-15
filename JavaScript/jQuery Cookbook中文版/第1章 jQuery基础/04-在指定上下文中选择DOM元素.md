[toc]

### 1. 问题

你需要引用在另一个 DOM 元素或者文档上下文中的单个 DOM 元素或者一组 DOM 元素，以便用 jQuery 方法操作这些元素。

### 2. 解决方案

jQuery 函数还有第二个参数，这个参数告诉 jQuery 函数应该在那个上下文中根据表达式搜索 DOM 元素。在这种情况下，第二个参数可以是一个 DOM 引用、jQuery 包装器或者文档。在下面代码中有12个 `<input>` 元素，仅选择特定的 `<input>` 元素：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>jQuery Cookbook</title>
    
</head>
<body>
    <form>
        <input name="" type="checkbox" />
        <input name="" type="radio" />
        <input name="" type="text" />
        <input name="" type="button" />
    </form>
    <form>
        <input name="" type="checkbox" />
        <input name="" type="radio" />
        <input name="" type="text" />
        <input name="" type="button" />
    </form>
    <input name="" type="checkbox" />
    <input name="" type="radio" />
    <input name="" type="text" />
    <input name="" type="button" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        // 使用上下文包装器在所有表单元素中搜索，警告框中显示 "selected 8 inputs"
        alert('selected ' + jQuery('input', $('form')).length + " inputs");
        // 用 DOM 引用作为上下文，在第一个表单元素中搜索，警告框中显示 "selected 4 inputs"
        alert('selected ' + jQuery('input', document.forms[0]).length + ' inputs');
        // 用表达式搜索 body 元素中的所有输入元素，警告框中显示 "selected 12 inputs"
        alert('selected ' + jQuery('input', 'body').length + ' inputs');
    </script>
</body>
</html>
```

### 3. 讨论

也可以将文档作为搜索的上下文。