`Kotlin` 通过 `class` 启动 `Activity` 方法如下：

```kotlin
private fun invokeLibActivity(mid: Int) {
    val intent = Intent(this, TestLibActivity::class.java)
    intent.putExtra("com.ai.menuid", mid)
    startActivity(intent)
}
```

