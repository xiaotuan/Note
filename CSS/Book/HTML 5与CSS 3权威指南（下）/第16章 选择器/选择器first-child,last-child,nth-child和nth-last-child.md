<center><font size="5"><b>选择器first-child,last-child,nth-child和nth-last-child</b></font></center>

##### 1. first-child

指定第一个子元素的样式。

##### 2. last-child

指定最后一个子元素的样式。

> 如果使用 `first-child` 选择器与 `last-child` 选择器，就不需要设置 `class` 属性值了。

```css
li:first-child {
    background-color: yellow;
}
li:last-child {
    background-color: skyblue;
}
```

> `first-child` 选择器在 `CSS 2` 就已经存在，而 `last-child` 从 `CSS 3` 开始被提供。

##### 3. nth-child

对指定序号（正序）的子元素使用样式

##### 4. nth-last-child

对指定序号（倒序）的子元素使用样式。

```css
li:nth-child(2) {
    background-color: yellow;
}
li:nth-last-child(2) {
    background-color: skyblue;
}
```

除了对指定序号的子元素使用样式以外，`nth-child` 选择器与 `nth-last-child` 选择器还可以用来对某个父元素中所有第奇数个子元素或第偶数个子元素使用样式。

```css
// 所有正数下来的第偶数个子元素
<子元素>:nth-child(even) {
    // 指定样式
}
// 所有倒数上去的第奇数个子元素
<子元素>:nth-last-child(odd) {
    // 指定样式
}
// 所有倒数上去的第偶数个子元素
<子元素>:nth-last-child(event) {
    // 指定样式
}
```

> 使用 `nth-child` 选择器与 `nth-last-child` 选择器时，虽然在对列表项目使用时没有问题，但是当用于其他元素时，还是会出现问题。