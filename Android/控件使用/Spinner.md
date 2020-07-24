[toc]

### 1. XML属性说明

| 属性名 | 参数类型 | 功能 | 示例 |
| :- | :- | :- | :- | :- |
| entries | 数组资源 | 设置下拉列表数据 | android:entries="@array/interpolators" |

### 2. 在布局文件中使用 entries 属性设置下拉列表数据

```xml
<Spinner
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_weight=".6"
    android:id="@+id/spinner"
    android:entries="@array/interpolators"
    android:layout_margin="4dp"
    />
```