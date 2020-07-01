[toc]

### 1. XML 属性

| 属性名 | 参数类型 | 功能 | 示例 |
| :- | :- | :- | :- | :- |
| max | int类型 | 设置拖动条的最大值 | android:max="100" |
| progress | int类型 | 设置拖动条的当前值 | android:progress="50" |

### 2. 在布局中使用 max 和 progress 属性设置拖动条的最大值和当前值

```xml
<SeekBar
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_weight=".5"
    android:max="2000"
    android:progress="300"
    android:layout_gravity="center_vertical"
    android:id="@+id/durationSeeker"/>
```

