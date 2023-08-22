假如定义有如下 `Java` 方法：

```java
public static boolean hasPermissions(@NonNull Context context,
                                         @Size(min = 1) @NonNull String... perms) {
    ...
}
```

在 `Kotlin` 中可以使用如下代码将 `Array` 类型变量传递给改函数作为参数，在 `Array` 类型变量名前需要添加 `*` 符号，例如：

```kotlin
val permissions = arrayOf(
        Manifest.permission.WRITE_EXTERNAL_STORAGE,
        Manifest.permission.READ_EXTERNAL_STORAGE
    )

hasPermissions(this, *permissions);
```

