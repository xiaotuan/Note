`EditTextPreference` 首选项可用于捕获原始文本，点击该首选项会弹出输入对话框，接受用户的输入。例如：

```xml
<?xml version="1.0" encoding="utf-8"?>
<PreferenceScreen xmlns:android="http://schemas.android.com/apk/res/android"
    android:key="package_name_screen"
    android:title="Package Name"
    android:summary="Set package name">

    <EditTextPreference
        android:key="package_name_preference"
        android:title="Set Package Name"
        android:summary="Set the package name for generated code"
        android:dialogTitle="Package Name" />

</PreferenceScreen>
```

可以通过 `getEditText()` 来操作实际的 `EditText`。要获得 `EditTextPreference` 的文本，只需使用 `getText()` 方法。

可以通过 `android:dialogLayout` 属性设置自定义对话框布局文件，只需要在布局文件中添加 ID 为 `@android:id/edit` 的 `EditText` 控件即可。

