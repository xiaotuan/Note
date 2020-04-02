<center><font size="5"><b>伪类选择器read-only与read-write</b></font></center>

+ `E:read-only` 伪类选择器用来指定当元素处于只读状态时的样式。
+ `E:read-write` 伪类选择器用来指定当元素处于非只读状态时的样式。

```css
input[type="text"]:read-only {
    background-color: gray;
}
input[type="text"]:read-write {
    background-color:greenyellow;
}
input[type="text"]:-moz-read-only {
    background-color: gray;
}
input[type="text"]:-moz-read-write {
    background-color: greenyellow;
}
```

