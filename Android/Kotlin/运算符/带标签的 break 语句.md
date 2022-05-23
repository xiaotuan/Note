使用 `break` 语句可以跳出循环，默认情况下只跳出最近一层的循环。如果需要跳出多层循环，需要使用带标签的 `break` 语句，例如：

```kotlin
override fun onRestoreInstanceState(savedInstanceState: Bundle) {
    super.onRestoreInstanceState(savedInstanceState)

    val id = savedInstanceState.getLong(GESTURES_INFO_ID, -1L)
    if (id != -1L) {
        sStore?.let {
            out@ for (name in it.gestureEntries) {
                for (gesture in it.getGestures(name)) {
                    if (gesture.id == id) {
                        mCurrentRenameGesture = NamedGesture(name, gesture)
                        break@out
                    }
                }
            }
        }
    }
}
```

