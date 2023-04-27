[toc]

`<iframe>` 标签，又叫浮动帧标签，可以利用 `<iframe>` 标签将一个 HTML 文档嵌入在一个 HTML 中显示。使用 `<iframe>` 标签，能够拖入外部文件。这样可以更好地管理内容，并且提供了一种在不同位置包含内容的机制。

#### 1. \<iframe> 标签

#### 1.1 语法

```html
<iframe>
    ......
</iframe>
```

### 2. \<iframe> 标签的属性

#### 2.1 语法

```html
<iframe src="文件" height="数值" width="数值" name="框架名称" scrolling="值" frameborder="值">
    ......
</iframe>
```

<center><b>&lt;iframe&gt; 标签的属性</b></center>

| 属性         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| align        | 用于对齐包含在 `<iframe>` 标签中的数据，并且可以取 `left`、`right`、`center` 以及 `justify` 值。因支持使用 CSS 对齐元素而过时 |
| class        | 一个以逗号分隔的样式类别表，这些样式类将标签实例化为已定义的类的一个实例 |
| frameborder  | 取一个 0 或者 1 值以判断是否应该在帧四周画一个框             |
| height       | 指定 `<iframe>` 的高度                                       |
| id           | 通常由样式单来定义应该被应用于标签中的数据的样式类型         |
| logndesc     | 到一个标签内容的一个较长描述的链接                           |
| marginheight | 帧的内容与边框的上、下边间的像素数                           |
| marginwidth  | 帧的内容与边框的左、右边之间的像素数                         |
| name         | 用于给块命名。它可以由 JavaScript 来对层进行操作             |
| noresize     | 当出现时，阻止用户重新调整帧的大小                           |
| scrolling    | 取 auto、yes 或者 no 值为判断滚动条是否显示                  |
| src          | 指定包含 `<iframe>` 内容的 URL                               |
| style        | 允许在标签内指定一个样式定义，而不是在一个样式表内指定       |
| title        | 允许为标签提供一个比 `<iframe>` 标签更有信息量的标题，它应用于整个文档 |
| width        | 指定 `<iframe>` 的宽度                                       |

> 注意：`<iframe>` 标签只适用于 IE 浏览器。它的作用是在网页中插入一个框架窗口以显示另一个文件。