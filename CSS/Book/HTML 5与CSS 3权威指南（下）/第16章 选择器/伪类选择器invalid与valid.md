<center><font size="5"><b>伪类选择器invalid与valid</b></font></center>

+ `E:invalid` 伪类选择器用来指定，当元素内容不能通过 `HTML 5` 通过使用元素的诸如 required、pattern 等属性所指定的检查或元素内容不符合元素的规定规格（例如通过使用 type 属性值为 Email 的 input 元素来限定元素内容必须为有效的 Email 格式）时的样式。
+ `E:valid` 伪类选择器用来指定，当元素内容通过 `HTML 5` 通过使用元素的诸如 required、pattern 等属性所指定的检查或元素内容符合元素的规定规格（例如通过使用 type 属性值为 Email 的 input 元素来限定元素内容必须为有效的 Email 格式）时的样式。

```css
input[type="text"]:invalid {
    background-color: red;
}
input[type="text"].valid {
    background-color: white;
}
```

