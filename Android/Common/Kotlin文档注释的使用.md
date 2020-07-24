1. 参数 `@param text message to show`

```kotlin
/**
 * Shows toast message with given message shortly.
 * @param text message to show
 * @see .show
 */
fun showShort(context: Context, text: CharSequence): Toast {
    return show(context, text, Toast.LENGTH_SHORT)
}
```

2. 返回参数 `@return Whether the Uri authority is ExternalStoragProvider`

```kotlin
/**
 * @param uri The Uri to check.
 * @return Whether the Uri authority is ExternalStorageProvider.
 */
fun isExternalStorageDocument(uri: Uri): Boolean {
    return "com.android.externalstorage.documents" == uri.authority
}
```

3. 引用 `[KitKat][android.os.Build.VERSION_CODES.KITKAT]`

```kotlin
/**
 * @return `true` if device is running
 * [KitKat][android.os.Build.VERSION_CODES.KITKAT] or higher, `false` otherwise.
 */
fun hasKitKatApi(): Boolean {
    return Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT
}
```

4. 代码  @return \`true\` if device is running

```kotlin
/**
 * @return `true` if device is running
 * [Jelly Bean 4.3][android.os.Build.VERSION_CODES.JELLY_BEAN_MR2]
 */
fun hasJellyBeanMR2Api(): Boolean {
    return Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR2
}
```

5. 文档内引用 `@see .show`

```kotlin
/**
 * Shows toast message with given message shortly.
 * @param text message to show
 * @see .show
 */
fun showShort(context: Context, text: CharSequence): Toast {
    return show(context, text, Toast.LENGTH_SHORT)
}
```