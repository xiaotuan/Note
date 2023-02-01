`RelativeLayout` 布局管理器实现一种策略，让容器的中控件以相对于容器或容器中的另一个控件的形式放置。

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <TextView
        android:id="@+id/userNameLbl"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Username: "
        android:layout_alignParentTop="true" />

    <EditText
        android:id="@+id/userNameText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_below="@id/userNameLbl" />

    <TextView
        android:id="@+id/pwdLbl"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_below="@id/userNameText"
        android:text="Password: " />

    <EditText
        android:id="@+id/pwdText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_below="@id/pwdLbl" />

    <TextView
        android:id="@+id/pwdCriteria"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_below="@id/pwdText"
        android:text="Password Criteria..." />

    <TextView
        android:id="@+id/disclaimerLbl"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:text="Use at your own risk..." />

</RelativeLayout>
```

将 `android:layout_alignParentTop` 设置为 true，将使控件紧靠容器的顶部。将 `android:layout_below` 设置为某个控件的 ID，该控件将放置在该 ID 控件下方。将 `android:layout_alignParentBottom` 设置为 true，控件将会紧靠容器底部。

除了这 3 个布局特性，还可以指定 `layout_above`、`layout_toRightOf`、`layout_toLeftOf` 和 `layout_centerInParent` 等属性。