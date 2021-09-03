在使用 `Kotlin` 语言开发 `Android` 应用程序时，`Android` 原生的 `PreferenceManager` 类已经标明为过时类。在 `Kotlin` 开发中推荐使用 `androidx` 框架中的 `PreferenceManager` 类。可以在 `build.gradle` 文件中引入 `preferences` 库，如下代码所示：

**Kotlin 版本**

```
dependencies {
    def preference_version = "1.1.1"
    
    // Kotlin
    implementation "androidx.preference:preference-ktx:$preference_version"
}
```

**Java 版本**

```
dependencies {
    def preference_version = "1.1.1"

    // Java language implementation
    implementation "androidx.preference:preference:$preference_version"
}
```

> 提示：`androidx.preference` 库的最新版本请查阅：<https://developer.android.google.cn/jetpack/androidx/releases/preference#kts>

