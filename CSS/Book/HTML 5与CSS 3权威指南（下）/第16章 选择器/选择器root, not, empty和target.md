<center><font size="5"><b>选择器root, not, empty和target</b></font></center>

##### 1. root选择器

root 选择器将样式绑定到页面的根元素中。根元素是指定位于文档树中最顶层结构的元素。

```css
:root {
    background-color: yellow;
}
```

##### 2. not选择器

如果想对某个结构元素使用样式，但是想排除这个结构元素下面的子结构元素，让它不使用这个样式时，可以使用not选择器。

```css
body *:not(h1) {
    background-color: yellow;
}
```

##### 3. empty选择器

使用 `empty` 选择器来指定当元素中内容为空白时使用的样式

```css
:empty {
    background-color: yellow;
}
```

##### 4. target选择器

使用 `target` 选择器来对页面中某个 `target` 元素（该元素的 `id` 被当做页面中的超链接来使用）指定样式，该样式只在用户点击了页面中的超链接，并且跳转到 `target` 元素后起作用。

```css
:target {
    background-color: yellow;
}
```

