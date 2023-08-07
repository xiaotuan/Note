`selector` 图片资源文件内容大致如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">

    <item android:state_selected="true" android:drawable="@drawable/ic_btn_update_selected" />
    <item android:state_pressed="true" android:drawable="@drawable/ic_btn_update_selected" />
    <item android:state_enabled="false" android:drawable="@drawable/ic_btn_update_disabled" />
    <item android:drawable="@drawable/ic_btn_update_normal" />

</selector>
```

关于文件中 `item` 的顺序问题如下：

+ 应用在使用 `selector` 图片资源时，会从上到下匹配图片，只要匹配到某些，就不会继续匹配。
+ `<item android:drawable="@drawable/ic_btn_update_normal" />` 项匹配任何情况，因此该项要放在所有项的最后。如果放在第一位，应用将用于都使用该项的图片。