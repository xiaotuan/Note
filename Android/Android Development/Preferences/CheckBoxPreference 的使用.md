`CheckBoxPreference` 首选项显示了一个复选框部件作为它的 UI 元素。在 XML 文件中使用 `CheckBoxPreference` 首选项的代码如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<PreferenceScreen xmlns:android="http://schemas.android.com/apk/res/android"
    android:key="flight_columns_pref"
    android:title="Flight Search Preferences"
    android:summary="Set Columns for Search Results">

    <CheckBoxPreference
        android:key="show_airline_column_pref"
        android:defaultValue="true"
        android:title="Airline"
        android:summary="Show Airline column" />

</PreferenceScreen>
```

通过设置 `android:defaultValue` 属性值来设置 `CheckBoxPreference` 是否默认勾选。

`CheckBoxPreference` 可以根据是否选中了复选框来设置不同的摘要文本。它的两个特性是 `summaryOn` 和 `summaryOff`。

