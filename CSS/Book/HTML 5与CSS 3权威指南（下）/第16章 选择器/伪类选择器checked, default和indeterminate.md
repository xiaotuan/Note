<center><font size="5"><b>伪类选择器checked, default和indeterminate</b></font></center>

+ `E:checked` 伪类选择器用来指定当表单中的 `radio` 单选框或 `checkbox` 复选框处于选取状态时的样式。

```css
input[type="checkbox"]:checked {
    outline: 2px solid blue;
}
```

+ `E:default` 选择器用来指定当页面打开时默认处于选取状态的单选框或复选框控件的样式。需要注意的是，即使用户将该单选框或复选框控件的选取状态设定为非选取状态， `E:default` 选择器中指定的样式仍然有效。

```css
input[type="checkbox"]:default {
    outline: 2px solid blue;
}
```

+ `E:indeterminate` 伪类选择器用来指定当页面打开时，一组单选框中没有任何一个单选框被设定为选取状态时整组单选框的样式。到目前为止，只有 `Opera`  浏览器对这个选择器提供支持。

```css
input[type="radio"]:indeterminate {
    outline: solid 3px blue;
}
```

