[toc]

可以使用如下形式表示 `raw` 资源的 `uri`：

```
android.resource:// + 包名 + "/" + raw 资源 ID
```

### 1. kotlin

```kotlin
val uriStr = "android.resource://" + getPackageName() + "/" + R.raw.hd1080p
mVideoView.setVideoURI(Uri.parse(uriStr))
mVideoView.start()
mVideoView.setOnCompletionListener {
    Log.d(TAG, "onResume=>Video play completed.")
}
```

### 2. Java

```java
String uri = "android.resource://" + getPackageName() + "/" + R.raw.hd1080p;
mVideoView.setVideoURI(Uri.parse(uri));
mVideoView.start();
mVideoView.setOnCompletionListener(mp -> {
    Log.d(TAG, "onCreate=>play completed.");
});
```

