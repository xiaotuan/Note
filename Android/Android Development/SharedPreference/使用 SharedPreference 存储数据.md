使用 `SharedPreferences` 可以存储如下类型的数据：`String`、`Set<String>`、`Int`、`Long`、`Float`、`Boolean` 。例如：

**Kotlin 版本**

```kotlin
val prefs = PreferenceManager.getDefaultSharedPreferences(context)
val ed = prefs.edit()
ed.apply {
    putString("hostname", "smtp.gmail.com")
    putInt("port", 587)
    putBoolean("ssl", true)
}
ed.commit()
```

**Java 版本**

```java
SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
SharedPreferences.Editor ed = prefs.edit();
ed.putString("hostname", "smtp.gmail.com");
ed.putInt("port", 587);
ed.putBoolean("ssl", true);
ed.commit();
```

> 注意：在执行完写入操作后，必须调用 `SharedPreferences.Editor` 类的 `commit()`  或 `apply()` 方法，将修改写入到磁盘中。

> 提示：尽量使用 `commit()` 方法提交修改，因为这个方法是同步的。

