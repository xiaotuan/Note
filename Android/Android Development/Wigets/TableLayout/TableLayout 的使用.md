`TableLayout` 布局管理器是 `LinearLayout` 的扩展。这个布局管理器以行和列的形式组织其子控件。

```xml
<?xml version="1.0" encoding="utf-8"?>
<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TableRow>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="First Name:" />

        <EditText
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Edgar" />

    </TableRow>

    <TableRow>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Last Name:" />

        <EditText
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Poe" />
        
    </TableRow>

</TableLayout>
```

由于 `TableLayout` 的内容是使用行来定义的，而不是使用列，所以 Android 通过查找包含最多单元格的行来确定表格中的列数。

```xml
<?xml version="1.0" encoding="utf-8"?>
<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TableRow>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="First Name:" />

        <EditText
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Edgar" />

    </TableRow>

    <TableRow>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Last Name:" />

        <EditText
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Allen" />

        <EditText
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Poe" />

    </TableRow>

</TableLayout>
```

通常我们使用 `TableRow` 元素来填充 `TableLayout`，但可以放置任何 `android.widget.View` 作为表格的子控件。

```xml
<?xml version="1.0" encoding="utf-8"?>
<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:stretchColumns="0,1,2">

    <EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Fullname:" />

    <TableRow>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Last Name:" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Allen" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Poe" />

    </TableRow>

</TableLayout>
```

将 `TableLayout` 的 `android:stretchColumns` 属性设置为 "0,1,2"。这将提示 `TableLayout`，列 0、1 和 2 可以根据表格内容进行拉伸。如果未在上面代码中使用 `stretchColumns`，将会看到 "EdgarAllenPoe" 都挤压在一起。从技术上讲，第二行会占据整个宽度，但第三个 TextView 不会拉伸。

如果其他列需要更多空间，可以设置 `android:shrinkColumns` 来包装一列或多列内容。也可以设置 `android:collapseColumns` 来使列不可见。请注意，列使用以 0 开始的索引方式进行标识。

`TableLayout` 还提供了 `android:layout_span`，可以使用此属性让一个单元格跨越多列。

