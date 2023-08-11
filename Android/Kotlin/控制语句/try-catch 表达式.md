Kotlin 把 `try-catch` 视为一个表示式。如果没有异常，则 `try` 部分中的最后一个表达式将作为结果返回。否则，`catch` 中的最后一条语句将作为结果返回。

```kotlin
fun tryExpr(blowup: Boolean): Int {
    return try {
        if (blowup) {
            throw RuntimeException("fail")
        }
        2
    } catch(ex: Exception) {
        4
    } finally {
        // ...
    }
}

println(tryExpr(false)) // 2
println(tryExpr(true))  // 4
```

