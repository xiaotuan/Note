[toc]

在网页中，有 3 种方法可以正确引入 CSS 样式，让浏览器能够识别和解析：

### 1. 行内样式

把 CSS 样式代码置于标签的 style 属性中，例如：

```html
<span style="color:red;">红色字体</span>
<div style="border:solid 1px blue; width: 200px; height: 200px;"></div>
```

这种用法没有真正把 HTML 结构与 CSS 样式分离，一般不建议大规模使用。除非为页面中某个元素临时设置特定样式。

### 2. 内部样式

把 CSS 样式代码放在 `<style>` 标签内。例如：

```css
<style type="text/css">
    body {	/* 页面基本属性 */
        font-size: 12px;
        color: #CCCCCC;
    }
    /* 段落文本基础属性 */
    p {
        background-color: #FF00FF;
    }
</style>
```

这种用法也称为网页内部样式，适合单页面定义 CSS 样式，不适合为一个网站或多个页面定义样式。

内部样式一般位于网页的头部区域，目的是让 CSS 源代码早于页面源代码下载并被解析，避免当网页下载之后还无法正常显示。

### 3. 外部样式

把样式放在独立的文件中，然后使用 `<link>` 标签或者 `@import` 关键字导入。一般网站都采用这种方法来设计样式。例如：

```html
<link href="001.css" rel="stylesheet" type="text/css" />
```

`link` 标签必须设置的属性说明如下：

+ `href`：定义样式表文件 URL。
+ `type`：定义导入文件类型，同 `style` 元素一样。
+ `rel`：用于定义文档关联，这里表示关联样式表。

或者：

```html
<style type="text/css">
	@import url("001.css");
</style>
```

在 `@import` 关键字后面，利用 `url()` 函数包含具体的外部样式表文件的地址。