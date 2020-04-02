<center><font size="5"><b>伪类选择器hover, active和focus</b></font></center>

+ `E:enabled` 伪类选择器用来指定当元素处于可用状态时的样式。
+ `E:disabled` 伪类选择器用来指定当元素处于不可用状态时的样式。

```css
input[type="text"]:enabled {
    background-color: yellow;
}
input[type="text"]:disabled {
    background-color: purple;
}
```

