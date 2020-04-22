按照惯例，所有 `<script>` 元素都应该放在页面的 `<head>` 元素中，例如：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Example HTML Page</title>
        <script type="text/javascript" src="example1.js"></script>
        <script type="text/javascript" src="example2.js"></script>
    </head>
    <body>
        <!-- 这里放内容 -->
    </body>
<html>
```

在文档的 `<head>` 元素中包含所有 `JavaScript` 文件，意味着必须等到全部 `JavaScript` 代码都被下载、解析和执行完成以后，才能开始呈现页面的内容。为了避免这个问题，现代 `Web` 应用程序一般都把全部 `JavaScript` 引用放在 `<body>`元素中，放在页面的内容后面，例如：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Example HTML Page</title>
    </head>
    <body>
        <!-- 这里放内容 -->
        <script type="text/javascript" src="example1.js"></script>
        <script type="text/javascript" src="example2.js"></script>
    </body>
</html>
```

