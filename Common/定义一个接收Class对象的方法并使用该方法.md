比如有如下的 `Java` 方法：

```java
public static void showDialog(Activity activity, Class clazz, String tag) {
	// ....
}
```

将其转换为 `Kotlin` 版本为：

```kotlin
fun showDialog(activity: Activity, clazz: Class<*>, tag: String) {
    // ...
}
```

使用 `Kotlin` 版本的 `showDialog` 方法：

```kotlin
showDialog(activity, AboutDialog::class.java, TAG_FRAGMENT_ABOUT)
```

