1. 下面代码演示逐个获取数组中的元素的示例（until）：

```kotlin
for (i in 0 until thisChunk.length) {
    result = thisChunk.get(i) - thatChunk.get(i)
    if (result != 0) {
        return result
    }
}
```

