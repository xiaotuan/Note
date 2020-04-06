<center><font size="5"><b>Guideline的使用</b></font></center>

> 摘自：[android/storage-samples/ActionOpenDocument](https://github.com/android/storage-samples/tree/master/ActionOpenDocument)

`androidx.constraintlayout.widget.Guideline` 是配合 `androidx.constraintlayout.widget.ConstraintLayout` 布局一起使用的。从其名字可以知道，它是一种布局指导线，在界面中不会显示。其主要属性有：

+ android:oriention：指定那个方向上的指导线。
+ app:layout_constraintGuide_begin：指定距版面左侧或顶部的固定距离
+ app:layout_constraintGuide_end：指定距版面右侧或底部的固定距离
+ app:layout_constraintGuide_percent：指定布局的宽度或高度的百分比

> 添加指导线后，根据指导线进行布局，应用将会尽可能的将内容显示在指导线的范围内，但是如果内容过大，而指导线限制的范围过小，这时指导线的意义可能会无效。