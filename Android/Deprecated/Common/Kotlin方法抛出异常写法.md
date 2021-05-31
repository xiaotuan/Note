<center><font size="5"><b>Kotlin方法抛出异常写法</b></font></center>

```kotlin
// 抛出单个异常的写法
@Throws(IOException::class)
private fun openRenderer(context: Context?, documentUri: Uri) {
    ......
}

// 抛出多个异常的写法
@Throws(IOException::class, ArrayIndexOutOfBoundsException::class)
private fun openRenderer(context: Context?, documentUri: Uri) {
    ......
}
```

