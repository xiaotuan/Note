**1. 在代码中修改**

**kotlin**

```kotlin
supportActionBar?.elevation = 0.0f
```

**Java**

```java
getSupportActionBar().setElevation(0.0f);
```

**2. 在主题中修改**

通过创建一个样式继承至主题中对应的 `actionBarStyle` 的样式，然后修改 `<item name="elevation">0dp</item>` 的值为 0dp，最后再将该样式设置到主题中的 `actionBarStyle` 属性中即可。

```xml
<style name="Base.Theme.ApkViewer" parent="Theme.Material3.DayNight">
    <item name="actionBarStyle">@style/ApkViewerActionBar</item>
</style>

<style name="ApkViewerActionBar" parent="Widget.Material3.ActionBar.Solid">
    <item name="elevation">0dp</item>
</style>
```

