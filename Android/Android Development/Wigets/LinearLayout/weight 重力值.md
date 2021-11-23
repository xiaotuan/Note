`android:layout_weight` 的值为浮点值，表明该控件占据容器的比例。默认的 `android:layout_weight` 的值为 0.0。通过将中间组件的重力特性设置为 1.0，将其他两个组件的重力特性保留为 0.0，我们可以指定中间组件应该占用容器中剩余的所有空白空间，其他两个组件应该保持它们的理想大小。

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:orientation="vertical">
		<EditText
              android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:layout_weight="0.0"
              android:gravity="left"
              android:text="one" />
  
  <EditText
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_weight="1.0"
            android:gravity="center"
            android:text="two" />
  
  <EditText
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_weight="0.0"
            android:gravity="right"
            android:text="three" />
  
</LinearLayout>
```

