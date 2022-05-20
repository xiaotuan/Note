`<header>` 元素描述了文档的头部区域，用于定义内容的介绍展示区域。在页面中用户可以使用多个 `<header>` 元素。例如：

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Header 元素</title>
    </head>
    <body>
        <header>
            <h1>《琵琶行》</h1>
        </header>
        <article>
            <header>
                <h1>千呼万唤始出来，犹抱琵琶半遮面。</h1>
            </header>
            <h1>嘈嘈切切错杂弹，大珠小珠落玉盘。</h1>
        </article>
    </body>
</html>
```

> 提示：在 HTML 5 中，一个 `<header>` 元素通常包括至少一个（h1 ~ h6）元素，也可以包括 `hgroup` 元素、`nav` 元素，还可以包括其他元素。但是 `<header>` 标签不能被放在 `<footer>`、`<address>` 或者另一个 `<header>` 元素内部。