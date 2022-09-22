### 1. 原生设置

添加要设置的颜色：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="checkbox_normal">#424242</color>
    <color name="checkbox_activated">#64891F</color>
</resources>
```

添加 `CheckBox` 样式：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="CheckBox"  parent="android:Widget.Material.Light.CompoundButton.CheckBox">
        <item name="colorControlNormal">@color/checkbox_normal</item>
        <item name="android:colorAccent">@color/checkbox_activated</item>
    </style>
</resources>
```

设置 `CheckBox` 样式：

```xml
<CheckBox
          android:id="@+id/enabled_legal"
          android:theme="@style/CheckBox"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:layout_marginStart="16dp"
          android:layout_marginEnd="16dp"
          android:layout_marginBottom="8dp"
          android:textColor="#424242"
          android:textSize="16sp"
          android:text="(REQUIRED) I understand and agree to the terms and conditions above." />
```

### 2. 兼容包设置

添加要设置的颜色：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="checkbox_normal">#424242</color>
    <color name="checkbox_activated">#64891F</color>
</resources>
```

添加 `CheckBox` 样式：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="CheckBox"  parent="Theme.AppCompat.Light">
        <item name="colorControlNormal">@color/checkbox_normal</item>
        <item name="android:colorControlActivated">@color/checkbox_activated</item>
    </style>
</resources>
```

设置 `CheckBox` 样式：

```xml
<CheckBox
          android:id="@+id/enabled_legal"
          android:theme="@style/CheckBox"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:layout_marginStart="16dp"
          android:layout_marginEnd="16dp"
          android:layout_marginBottom="8dp"
          android:textColor="#424242"
          android:textSize="16sp"
          android:text="(REQUIRED) I understand and agree to the terms and conditions above." />
```