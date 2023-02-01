[toc]

### 1. 在 xml 中定义 TextView 的样式

```xml
<style name="ErrorText">
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_height">wrap_content</item>
    <item name="android:textColor">#FF0000</item>
    <item name="android:typeface">monospace</item>
</style>
```

### 2. 在布局文件中应用样式

```xml
<TextView
        android:id="@+id/errors"
        style="@style/ErrorText"
        android:text="There's trouble down at the mill." />
```

