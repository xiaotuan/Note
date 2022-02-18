[toc]

> 注意：
>
> 构建 AudioTrack 对象时，采样率、编码，格式、缓存大小、通道进来与录制该 pcm 文件的参数一致。

使用 AudioTrack 播放 pcm 音频文件的步骤：

+ 创建一个线程。
+ 在线程中创建 AudioTrack 对象
+ 调用 AudioTrack 对象的 play() 方法
+ 调用 AudioTrack 对象的 write() 方法将 pcm 文件的数据写入音频设备中。
+ 调用 stop() 方法停止播放
+ 调用 release() 方法是否资源。

### 1. Kotlin

```kotlin
import android.media.AudioFormat
import android.media.AudioManager
import android.media.AudioTrack
import android.media.AudioRecord
import android.util.Log
import java.io.File
import java.io.FileInputStream

private fun playPcmAudioFile(filePath: String?) {
    Thread {
        if (filePath == null) {
            Log.e(TAG, "filePath is null.")
            return@Thread
        }

        val audioFile = File(filePath)
        if (!audioFile.exists() || !audioFile.isFile) {
            Log.e(TAG, "Audio file is not exist or not a file.")
            return@Thread
        }

        val channel = AudioFormat.CHANNEL_OUT_MONO
        val sampleRate = 44100
        val encoding = AudioFormat.ENCODING_PCM_16BIT

        mPlayer = if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) {
            val format = AudioFormat.Builder()
            .setChannelMask(channel)
            .setSampleRate(sampleRate)
            .setEncoding(encoding)
            .build()
            AudioTrack.Builder()
            .setAudioFormat(format)
            .build()
        } else {
            val bufferSize = 2 * AudioRecord.getMinBufferSize(sampleRate, channel, encoding)
            AudioTrack(
                AudioManager.STREAM_MUSIC,
                sampleRate,
                channel,
                encoding,
                bufferSize,
                AudioTrack.MODE_STREAM
            )
        }

        mPlayer?.apply {
            play()

            var fis: FileInputStream? = null
            try {
                fis = FileInputStream(audioFile)
                val data = ByteArray(4096)
                var length = fis.read(data)
                while (length != -1) {
                    write(data, 0, length)
                    length = fis.read(data)
                }
            } catch (e: Exception) {
                Log.e(TAG, "Play error: ", e)
            } finally {
                try {
                    fis?.close()
                } catch (ignore: Exception) {
                }
            }
        }
    }.start()
}
```

### 2. Java

```java
import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioTrack;
import android.media.AudioRecord;
import android.util.Log;
import java.io.File;
import java.io.FileInputStream;

private void playPcmAudioFile(String filePath) {
    new Thread(() -> {
        if (filePath == null) return;

        File audioFile = new File(filePath);
        if (!audioFile.exists() || !audioFile.isFile()) {
            Log.e(TAG, "playPcmAudioFile=>Audio file is not exist or not a file.");
            return;
        }

        FileInputStream fis = null;
        AudioTrack player = null;

        int channel = AudioFormat.CHANNEL_OUT_MONO;
        int sampleRate = 44100;
        int encoding = AudioFormat.ENCODING_PCM_16BIT;

        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) {
            AudioFormat format = new AudioFormat.Builder()
                .setChannelMask(channel)
                .setSampleRate(sampleRate)
                .setEncoding(encoding)
                .build();
            player = new AudioTrack.Builder()
                .setAudioFormat(format)
                .build();
        } else {
            int bufferSize = 2 * AudioRecord.getMinBufferSize(sampleRate,
                                                              channel, encoding);
            player = new AudioTrack(AudioManager.STREAM_MUSIC, sampleRate,
                                    channel, encoding,
                                    bufferSize, AudioTrack.MODE_STREAM);
        }
        player.play();

        try {
            fis = new FileInputStream(audioFile);
            byte[] data = new byte[4096];
            int length = fis.read(data);
            while(length != -1) {
                player.write(data, 0, length);
                length = fis.read(data);
            }
        } catch (Exception e) {
            Log.e(TAG, "playPcmAudioFile=>Play error: ", e);
        } finally {
            if (fis != null) {
                try {
                    fis.close();
                } catch (Exception ignore) {}
            }
        }
    }).start();
}
```

