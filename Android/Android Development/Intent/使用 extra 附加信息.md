Intent 可以包括名为 extra 的附加特性，extra 可以向收到 Intent 的组件提供更多信息。可以使用许多方法来向包添加基本类型：

+   `putExtra(String name, boolean value)`
+   `putExtra(String name, int value)`
+   `putExtra(String name, double value)`
+   `putExtra(String name, String value)`

以下是一些稍微复杂的 extra 数据：

+   `putExtra(String name, int[] values)`
+   `putExtra(String name, float[] values)`
+   `putExtra(String name, Serializable value)`
+   `putExtra(String name, Parcelable value)`
+   `putExtra(String name, Bundle value)`
+   `putExtra(String name, Intent anotherIntent)`
+   `putIntegerArrayListExtra(String name, ArrayList arrayList)`
+   `putParcelableArrayListExtra(String name, ArrayList arrayList)`
+   `putStringArrayListExtra(String name, ArrayList arrayList)`

在 <https://developer.android.google.cn/reference/android/content/Intent.html#EXTRA_ALARM_COUNT> 上可以看到大量 extra 信息键常量。