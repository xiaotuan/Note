**1. 在代码中修改**

**Kotlin**

```kotlin
supportActionBar?.setBackgroundDrawable(ColorDrawable(getColor(R.color.white)))
```

**Java**

```java
getSupportActionBar().setBackgroundDrawable(new ColorDrawable(getColor(R.color.white)));
```

**2. 在主题文件中修改**

通过创建一个样式继承至主题中对应的 `actionBarStyle` 的样式，然后修改 `<item name="background">@color/white</item>` 的值为需要的颜色即可，最后再将该样式设置到主题中的 `actionBarStyle` 属性中即可。

```xml
<style name="Base.Theme.ApkViewer" parent="Theme.Material3.DayNight">
    <item name="actionBarStyle">@style/ApkViewerActionBar</item>
</style>

<style name="ApkViewerActionBar" parent="Widget.Material3.ActionBar.Solid">
    <item name="background">@color/white</item>
</style>
```