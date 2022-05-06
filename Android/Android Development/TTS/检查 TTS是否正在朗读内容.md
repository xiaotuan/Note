`isSpeaking()` 方法用于检查 TTS 引擎当前是否正在朗读任何内容，此方法返回 true 或 false。例如：

**Kotlin**

```kotlin
mTts?.isSpeaking()
```

**Java**

```java
mTts.isSpeaking()
```

> 提示：如果需要在 TTS 完成对队列内容的朗读之后获得通知，可以为 `ACTION_TTS_QUEUE_PROCESSING_COMPLETED` 广播实现一个 `BroadcastReceiver`。