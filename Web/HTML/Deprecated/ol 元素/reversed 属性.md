[toc]

> 注意：`reversed` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

目前只有 Chrome 和 Safari 6 支持 `reversed` 属性。

### 2. 定义和用法

`reversed` 属性是一个布尔属性。

`reversed` 属性规定列表顺序为降序 (9, 8, 7...)，而不是升序 (1, 2, 3...)。

### 3. 语法

```html
<ol reversed>
```

### 4. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <ol reversed>
            <li>咖啡</li>
            <li>茶</li>
            <li>牛奶</li>
        </ol>

        <p><strong>注意：</strong>目前只有 Chrome 和 Safari 6 支持 reversed 属性。</p>

    </body>
</html>
```

