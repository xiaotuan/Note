<center><font size="5"><b>ConstraintLayout子元素的constraintDimensionRatio属性说明</b></font></center>

> 摘自：[android/storage-samples/ActionOpenDocument](https://github.com/android/storage-samples/tree/master/ActionOpenDocument)

```
app:layout_constraintDimensionRatio="1:1"
app:layout_constraintDimensionRatio="h,1:1"
app:layout_constraintDimensionRatio="w,1:1"
```
`app:layout_constraintDimensionRatio` 的作用是设置控件的宽高比。如果要使用该属性，则该控件的宽或高至少有一个设置为 "match_constraints" `0dp`。
`1:1` ：表示宽和高的比值。
`h,2:1` ：表示以高为基准设置宽度，宽为 2，高为 1。
`w,2:4` ：表示以宽为基准设置高度，宽为2，高为 4。