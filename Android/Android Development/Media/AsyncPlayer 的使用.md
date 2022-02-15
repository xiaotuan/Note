[toc]

如果只是希望播放某种音频，而不希望绑定到当前线程，`AsyncPlayer` 可能正是你想要的。音频源以 Uri 的形式传递给此类，所以音频文件可以位于本地或位于网络上的其他位置。此类自动创建一个后台线程来处理音频的获取和回放的启动。因为它是异步的，所以无法知道音频开始的准确时间。也不会知道它何时结束，或者甚至它是否仍在播放。但是，可以调用 stop() 获取音频以停止播放。如果在上一个音频完成播放之前再次调用 play()，上一个音频将立即停止，新音频将在未来设置并获取了所有内容时开始播放。

### 1. Kotlin

```kotlin
import android.media.AsyncPlayer
import android.media.AudioAttributes
import android.media.AudioManager
import android.net.Uri
import android.os.Build
import android.os.Environment
import java.io.File

val dir = Environment.getExternalStorageDirectory()
val audioFile = File(dir, "左宏元 张慧清 - 渡情.mp3")
val mPlayer = AsyncPlayer("AsyncPlayerDemo")
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    val aa = AudioAttributes.Builder()
    .setLegacyStreamType(AudioManager.STREAM_MUSIC)
    .build()
    mPlayer.play(
        this,
        Uri.parse("file://${audioFile.absolutePath}"),
        false,
        aa
    )
} else {
    mPlayer.play(
        this,
        Uri.parse("file://${audioFile.absolutePath}"),
        false,
        AudioManager.STREAM_MUSIC
    )
}
```

### 2. Java

```java
import android.media.AsyncPlayer;
import android.media.AudioManager;
import android.media.AudioAttributes;
import android.net.Uri;
import android.os.Environment;
import android.os.Build;
import java.io.File;

File dir = Environment.getExternalStorageDirectory();
File audioFile = new File(dir, "左宏元 张慧清 - 渡情.mp3");
AsyncPlayer mPlayer = new AsyncPlayer("AsyncPlayerDemo");
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    AudioAttributes aa = new AudioAttributes.Builder()
        .setLegacyStreamType(AudioManager.STREAM_MUSIC)
        .build();
    mPlayer.play(
        this,
        Uri.parse("file://" + audioFile.getAbsolutePath()),
        false,
        aa);
} else {
    mPlayer.play(
        this, 
        Uri.parse("file://" + audioFile.getAbsolutePath()),
        false, 
        AudioManager.STREAM_MUSIC);
}
```

