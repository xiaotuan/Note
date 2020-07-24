<center><font size="5"><b>LinearLayout的measureWithLargestChild属性说明</b></font></center>

> 摘自：[android/storage-samples/ActionOpenDocument](https://github.com/android/storage-samples/tree/master/ActionOpenDocument)

```
android:measureWithLargestChild=true
```

`android:measureWithLargestChild` 的作用：该属性为 true 的时候，所有带权重的子元素都会具有最大子元素的最小尺寸，且只有当父 view 布局方向上的宽度或高度为 wrap_content 才有效。

例如，当 `LinearLayout` 的布局方向为水平方向（`android:orientation="horizontal"`），则其宽度必须设置为 `wrap_content`，这样 `android:measureWithLargestChild=true` 才有效。如果该 `LinearLayout` 内有两个子元素（比如 Button），一个 `Button` 的按钮文字是 ButtonPress，且该 `Button` 的权重（ weight）为 2；另一个 `Button` 的按钮文字是 Next，且权重为 1。虽然它们设置的权重不同，但是最后显示的宽度都是一样的，且宽度为刚好容纳第一个 `Button` 内容的宽度（因为它的文字比 Next 长，为了完全显示且不换行，则其需要更宽的宽度）