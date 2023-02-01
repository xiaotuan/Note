`android:gravity` 设置供视图使用，而 `android:layout_gravity` 设置供容器（`android.view.ViewGroup` ）使用。例如，可以将 `android:gravity` 设置为 center，以将 EditText 中的文本在控件中居中。类似地，通过设置 `android:layout_gravity="right"` ，可以将 EditText 在 `LinearLayout` （容器）中右对齐。

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:orientation="vertical">
		
  	<EditText
              android:layout_width="wrap_content"
              android:layout_height="wrap_content"
              android:layout_gravity="right"
              android:gravity="center"
              android:text="one" />
              
</LinearLayout>
```

