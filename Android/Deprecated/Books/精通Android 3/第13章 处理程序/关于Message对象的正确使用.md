当调用 `sendMessage()` 和 `sendMessageDelayed()` 时，将需要 `Message` 对象的一个实例。最好使用 `obtainMessage()` 方法获取 `Message` 对象，这样就可以确保当处理完此消息时，它将会被回收。

**Java**

```java
Message m = mHandler.obtainMessage();
```

**Kotlin**

```kotlin
val m = mHandler.obtainMessage()
```

