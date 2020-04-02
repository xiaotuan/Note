<center><font size="5"><b>only-child 选择器</b></font></center>

可以使用下面的方法指定当某个父元素中只有一个子元素时才使用的样式。

```css
<子元素>:nth-child(1):nth-last-child(1) {
    // 指定样式
}
```

也可以使用 `only-child` 选择器来代替。

```css
li:only-child {
    background-color: yellow;
}
```

也可以使用 `only-of-type` 选择器来替代 `nth-of-type(1):nth-last-of-type(1)` 。