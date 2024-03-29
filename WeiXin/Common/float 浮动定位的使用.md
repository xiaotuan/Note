<center><font size="5"><b>float 浮动定位的使用</b></font></center>

`float` 是相对定位的，会随着浏览器的大小和分辨率的变化而改变。`float` 浮动属性是元素定位中非常重要的属性，常常通过对 Div 元素应用 `float` 浮动来进行定位。 

语法： float: none| left| right 

说明： `none` 是默认值，表示对象不浮动；`left` 表示对象浮在左边；`right` 表示对象浮在右边。 

CSS 允许任何元素浮动，不论是图像、段落，还是列表。无论先前元素是什么状态，浮动后都成为 块元素。 浮动元素的宽度默认为 `auto`。如果 `float` 取值为 `none` 或没有设置 `float` 时，不会发生任何浮动， 块元素独占一行，紧随其后的块元素将在新行中显示.

`clear` 属性定义了元素的哪些边上不允许出现浮动元素。在CSS1和CSS2中，这是通过自动为清除元素（ 即设置了 `clear` 属性的元素）增加上外边距来实现的。在 CSS2. 1 中，会在元素上外边距 之上增加清除空间，而外边距本身并不改变。不论哪一种改变，最终结果都是一样的，如果声明为 左边或右边清除，会使元素的上外边框边界刚好在该边上浮动元素的下外边距边界之下。 

语法：

``` text
Clear： none | left | right | both 
```

说明： `none` 表示允许两边都可以有浮动对象，是默认值。 `left` 表示不允许左边有浮动对象。 `right` 表示不允许右边有浮动对象。 `both` 表示不允许有浮动对象。