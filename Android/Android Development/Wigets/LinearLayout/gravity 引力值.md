`android:gravity` 可以有许多可能的值，包括 `left`、`center`、`right`、`top`、`bottom`、`center_vertical` 和 `clip_horizontal` 等。`android:gravity` 可以同时设置多个值，各个值之间使用 `|` 连接，例如：`android:gravity="left|center_vertical"`。

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:orientation="vertical">
		<EditText
              android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:gravity="left"
              android:text="one" />
</LinearLayout>
```

