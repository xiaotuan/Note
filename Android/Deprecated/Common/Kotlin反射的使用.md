```kotlin
try {
    val clazz = Class.forName("android.view.View$AttachInfo");
    var field = clazz.getDeclaredField("mWindowLeft")
    field.isAccessible = true
    position[0] = field.getInt(info)

    field = clazz.getDeclaredField("mWindowTop")
    field.isAccessible = true
    position[1] = field.getInt(info)
} catch (e: Exception) {
    Log.e(TAG, "Failed to get window\'s position from AttachInfo.")
    return null
}
```

```kotlin
try {
    val field = View::class.java.getDeclaredField("mAttachInfo")
    field.isAccessible = true
    info = field.get(view)
} catch (e: Exception) {
    info = null
    Log.e(TAG, "Failed to get AttachInfo.")
}
```

