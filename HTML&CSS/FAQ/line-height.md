<center><font size="5"><b>line-height</b></font></center>

## 属性含义

行间距

## CSS line-height 属性



## 实例

Set the line height in percent:

p.small {line-height:90%}
p.big {line-height:200%}


[尝试一下 »](https://www.w3cschool.cn/tryrun/showhtml/trycss_line-height)

在此页底部有更多的例子。

------

## 属性定义及使用说明

设置以百分比计的行高：.

**注意：** 负值是不允许的

| 默认值：          | normal                        |
| :---------------- | ----------------------------- |
| 继承：            | yes                           |
| 版本：            | CSS1                          |
| JavaScript 语法： | *object*.style.lineHeight="2" |



------

## 浏览器支持

表格中的数字表示支持该属性的第一个浏览器版本号。

| 属性        | Chrome |  IE  | Firefox | Safari | Opera |
| :---------- | :----: | :--: | :-----: | :----: | :---: |
| line-height |  1.0   | 4.0  |   1.0   |  1.0   |  7.0  |

------

## 属性值

| 值       | 描述                                                 |
| :------- | :--------------------------------------------------- |
| normal   | 默认。设置合理的行间距。                             |
| *number* | 设置数字，此数字会与当前的字体尺寸相乘来设置行间距。 |
| *length* | 设置固定的行间距。                                   |
| *%*      | 基于当前字体尺寸的百分比行间距。                     |
| inherit  | 规定应该从父元素继承 line-height 属性的值。          |