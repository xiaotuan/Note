可以使用 `Handler` 的 `obtainMessage()` 方法获取 `Message` 对象，该方法不会创建新消息，而是从一个全局消息池获取一个。在以后的某个时刻，当处理完此消息后，它将被回收。

**Kotlin**

```kotlin
val mHandler = Handler()
val msg = mHandler.obtainMessage()
```

**Java**

```java
Handler mHandler = new Handler();
Message msg = mHandler.obtainMessage();
```

