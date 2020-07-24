可以使用 `TextClock` 控件显示日期、时间、星期等信息。

显示时间:

```xml
<TextClock
    android:id="@+id/timeView"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_centerVertical="true"
    android:layout_gravity="center"
    android:layout_toStartOf="@+id/dataView"
    android:format24Hour ="HH:mm"
    android:format12Hour ="hh:mm"
    android:textColor="@color/material_white"
    android:textSize="@dimen/w_56" />
```

显示日期：

```xml
<TextClock
    android:id="@+id/timeView"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_centerVertical="true"
    android:layout_gravity="center"
    android:layout_toStartOf="@+id/dataView"
    android:format24Hour ="yyyy-MM-dd"
    android:format12Hour ="yyyy-MM-dd"
    android:textColor="@color/material_white"
    android:textSize="@dimen/w_56" />
```

显示星期：

```xml
<TextClock
    android:id="@+id/timeView"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_centerVertical="true"
    android:layout_gravity="center"
    android:layout_toStartOf="@+id/dataView"
    android:format24Hour ="EEEE"
    android:format12Hour ="EEEE"
    android:textColor="@color/material_white"
    android:textSize="@dimen/w_56" />
```

> 其实 `TextClock`中是使用 `DateFormat` 来格式化时间的，因此 `android:format12Hour` 和 `android:format12Hour` 的值可以是 `DateFormat` 用于格式化时间的任何字符。

> 注意： 如果希望 `TextClock` 显示 24 小时制，则需要同时设置 `android:format12Hour` 和 `android:format12Hour` 属性。