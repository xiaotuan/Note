[toc]

> 注意：`scoped` 属性是 HTML5 中的新属性。

### 1. 浏览器支持

只有 Firefox属性支持 `scoped` 属性 。

### 2. 定义和用法

`scoped` 属性是一个布尔属性。

如果使用该属性，则样式仅仅应用到 `style` 元素的父元素及其子元素。

### 3. 语法

```html
<style scoped>
```

### 4. 示例

```html
<div>
    <style type="text/css" scoped>
        h1 {color:red;}
        p {color:blue;}
    </style>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
</div>
```

