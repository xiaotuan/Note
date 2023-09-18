取得布尔值（Boolean）的属性，例如disabled和readonly等，通过省略属性的值来表达“值为true”。如果要表达“值为false”，则直接省略属性本身即可。此外，在写明属性值来表达“值为true”时，可以将属性值设为属性名称本身，也可以将值设为空字符串。代码如下：

```html    
<!-- 以下的checked 属性值皆为true -->
<input type="checkbox" checked>
<input type="checkbox" checked="checked">
<input type="checkbox" checked="">
```

下表列出了 `HTML5` 中允许省略属性值的属性：

| HTML5 属性 | XHTML 语法          |
| ---------- | ------------------- |
| checked    | checked="checked"   |
| readonly   | readonly="readonly" |
| disabled   | disabled="disabled" |
| selected   | selected="selected" |
| defer      | defer="defer"       |
| ismap      | ismap="ismap"       |
| nohref     | nohref="nohref"     |
| noshade    | noshade="noshade"   |
| nowrap     | nowrap="nowrap"     |
| multiple   | multiple="multiple" |
| noresize   | noresize="noresize" |

取得布尔值（Boolean）的属性，在设置属性值时，可以使用双引号或单引号来引用。`HTML5` 语法则更进一步，只要属性值不包含空格、`<`、`>`、`'`、`"`、\`、`=` 等字符，都可以省略属性的引用符。代码如下：

```html
<!--请注意type 属性的引用符-->
<input type="text">
<input type='text'>
<input type=text>
```

