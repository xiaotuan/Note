> 警告：`setEngineByPackageName()` 方法已经被标注为过时 API，要指定特定的 TTS 引擎，请使用下面的方法。

要指定特定的 TTS 引擎，可以在构造 TextToSpeech 对象时，传递 TTS 引擎包名进去即可，例如：

**Kotlin**

```kotlin
mTts = TextToSpeech(this, this, "com.svox.pico")
```

**Java**

```java
mTts = new TextToSpeech(this, this, "com.svox.pico");
```

