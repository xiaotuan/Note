假如有如下接口：

```kotlin
interface RequestPermissionCallback {
    fun onResult(graint: Boolean)
}
```

有如下方法定义：

```kotlin
fun requstAllPermissions(context: AppCompatActivity, callback: RequestPermissionCallback) {
    ...
}
```

如果希望像下面的代码调用该方法：

```kotlin
requstAllPermissions(this) { graint ->
    Log.d(TAG, "onCreate=>graint: $graint")
}
```

则需要将接口的定义修改成如下：

```kotlin
fun interface RequestPermissionCallback {
    fun onResult(graint: Boolean)
}
```

即在 `interface` 前面加上 `fun` 关键字。