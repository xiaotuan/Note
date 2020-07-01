[toc]

### 1. XML属性说明

| 属性名 | 参数类型 | 功能 | 示例 |
| :- | :- | :- | :- | :- |
| text | 字符串类型 | 按钮的名字 | android:text="Run" |
| onClick | 字符串类型 | 按钮点击事件的方法名称 | android:onclick="runAnimation" |

### 2. 在布局文件中使用 onClick 属性设置点击事件

```xml
<Button
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_weight=".4"
    android:id="@+id/runButton"
    android:text="Run"
    android:onClick="runAnimation"/>
```