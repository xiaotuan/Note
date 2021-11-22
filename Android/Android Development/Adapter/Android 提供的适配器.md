以下列表汇总了 Android 提供的适配器：

+   `ArrayAdapter<T>`：这个适配器位于一般的任意对象数组的顶部，需要在 `ListView` 中使用。
+   `CursorAdapter`：这个适配器也需要在 `ListView` 中使用，通过游标向列表提供数据。
+   `SimpleAdapter`：从名称可以看出，这个适配器是一个简单适配器，它通常用于使用静态数据（可能来自资源）填充列表。
+   `ResourceCursorAdapter`：这个适配器扩展了 `CursorAdapter`，知道如何从资源创建视图。
+   `SimpleCursorAdapter`：这个适配器扩展了 `ResourceCursorAdapter`，从游标中的列创建 `TextView/ImageView` 视图。这些视图在资源中定义。
+   `BaseAdapter`：经常用于自定义适配器。