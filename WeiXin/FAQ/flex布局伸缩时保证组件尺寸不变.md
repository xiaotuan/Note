<center><font size="5"><b>flex布局伸缩时保证组件尺寸不变</b></font></center>

在使用 `flex` 布局时，设置 `flex-grow` 或 `flex-shrink` 或 `flex` 属性后，`flex` 布局中的元素会根据设置的比例进行伸缩。如果需要设置某个元素始终保持当前的尺寸，可以将给该元素设置 `flex-shrink` 属性设置为 0，如下：

```css
flex-shrink: 0;
```

