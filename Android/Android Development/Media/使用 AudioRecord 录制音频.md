[toc]

> 注意
>
> 录音需要 `android.permission.RECORD_AUDIO` 权限，如果需要将录音文件写入内部存储或外部存储中，还需要 `android.permission.WRITE_EXTERNAL_STORAGE`。

### 1. 录制原始音频

#### 1.1 创建 AudioRecord 对象

> 注意：
>
> 创建 AudioRecord 对象完成后需要通过 `getState()` 方法判断对象状态是否是初始化状态。

对于采样频率，应该选择一种标准值，比如 8000、16000、44100、22050 或 11025 Hz。声道配置应该从 AudioFormat 中描述的 CHANNEL* 值中选择。编码格式将为 ENCODING_PCM_8BIT 或 ENCODING_PCM_16BIT。请注意，这里的选择将影响以原始音频数据形式返回的值的类型。如果不需要 16 位的精度，可以使用 8 位。文档表明只有 44100 的采样频率可保证适用于所有设备，但模拟器仅支持 8000 Hz、CHANNEL_IN_MONO 和 ENCODING_PCM_8BIT 。

##### 1.1.1 Kotlin

```kotlin
// 采样率
val sampleRate = 44100
// 声道
val channelConfig = AudioFormat.CHANNEL_IN_MONO
// 编码格式
val audioFormat = AudioFormat.ENCODING_PCM_16BIT
// 数据缓存大小
val bufferSize =
2 * AudioRecord.getMinBufferSize(sampleRate, channelConfig, audioFormat)

val record = AudioRecord(
    MediaRecorder.AudioSource.MIC,
    sampleRate,
    channelConfig,
    audioFormat,
    bufferSize
)

if (record.state != AudioRecord.STATE_INITIALIZED) {
    Log.e(TAG, "AudioRecord is not properly initialized.")
} else {
    Log.d(TAG, "AudioRecord is initialized")
}
```

##### 1.1.2 Java

```java
// 采样率
int sampleRate = 44100;
// 声道
int channelConfig = AudioFormat.CHANNEL_IN_MONO;
// 编码格式
int audioFormat = AudioFormat.ENCODING_PCM_16BIT;
// 数据缓存大小
int bufferSize = 2 * AudioRecord.getMinBufferSize(sampleRate, channelConfig, audioFormat);

AudioRecord record = new AudioRecord(
    MediaRecorder.AudioSource.MIC,
    sampleRate,
    channelConfig,
    audioFormat,
    bufferSize
);

if (record.getState() != AudioRecord.STATE_INITIALIZED) {
    Log.e(TAG, "AudioRecord is not properly initialized.");
} else {
    Log.d(TAG, "AudioRecord is initialized");
}
```

#### 1.2 开始录制音频

> 注意：
>
> 调用 `startRecording()` 方法后需要通过 `getRecordingState()()` 方法判断当前状态是否是录音状态。

调用 `startRecording()` 方法后，通过 `AudioRecord` 对象的 `read()` 方法读取录音数据，并写入文件。

##### 1.2.1 Kotlin

```kotlin
var fos: FileOutputStream? = null
try {
    val outFile = File(outputFilePath)
    if (outFile.exists() && outFile.isFile) {
        outFile.delete()
    }
    outFile.createNewFile()
    fos = FileOutputStream(outFile, true)
    
    startRecording()
    
    if (recordingState != AudioRecord.RECORDSTATE_RECORDING) {
        Log.e(TAG, "beginRecording=>AudioRecord is not recording")
        inRecordMode = false
        return@Thread
    } else {
        Log.v(TAG, "beginRecording=>AudioRecord has started recording ...")
    }

    val audioBuffer = ByteArray(mAudioBufferSampleSize)
    while (inRecordMode) {
        val samplesRead = read(audioBuffer, 0, mAudioBufferSampleSize)
        fos.write(audioBuffer, 0, samplesRead)
    }
} catch (e: Exception) {
    Log.e(TAG, "Read record data error: ", e)
} finally {
    try {
        fos?.flush()
        fos?.close()
    } catch (ignore: Exception) {
    }
}
```

##### 1.2.2 Java

```java
FileOutputStream fos = null;
try {
    File outFile = new File(outputFilePath);
    if (outFile.exists() && outFile.isFile()) {
        boolean success = outFile.delete();
        if (!success) {
            Log.e(TAG, "beginRecording=>Unable delete old audio file.");
            return;
        }
    }
    boolean success = outFile.createNewFile();
    if (!success) {
        Log.e(TAG, "beginRecording=>Unable create audio file.");
        return;
    }
    fos = new FileOutputStream(outFile, true);

    record.startRecording();

    if (record.getRecordingState() != AudioRecord.RECORDSTATE_RECORDING) {
        Log.e(TAG, "beginRecording=>AudioRecord is not recording");
        inRecordMode = false;
        return;
    } else {
        Log.v(TAG, "beginRecording=>AudioRecord has started recording ...");
    }

    byte[] audioBuffer = new byte[mAudioBufferSampleSize];
    while (inRecordMode) {
        int samplesRead = record.read(audioBuffer, 0, mAudioBufferSampleSize);
        fos.write(audioBuffer, 0, samplesRead);
    }
} catch (Exception e) {
    Log.e(TAG, "Read record data error: ", e);
} finally {
    try {
        if (fos != null) {
            fos.flush();
            fos.close();
        }
    } catch (Exception ignore) {}
}
```

### 2. 使用回调方法录制原始音频

使用回调方法录制原始音频步骤如下：

+ 创建 AudioRecord 对象

+ 调用 `setPositionNotificationPeriod()` 方法设置通知位置

  > 注意
  >
  > 通知位置的大小必须小于读取数据长度，经验证通知位置的大小是读取数据长度的一半运行正常。

+ 调用 `setRecordPositionUpdateListener()` 方法设置回调监听器

+ 调用 `startRecording()` 方法开始录制音频

+ 在监听器的 `onPeriodicNotification()` 读取音频数据并写入文件中

+ 在需要停止播放的时候调用 `setNotificationMarkerPosition()` 方法，该方法会触发监听器中的 `onMarkerReached()` 方法

+ 在监听器的 `onMarkerReached()` 方法中读取最后的音频数据，关闭输出文件和停止录制。

#### 2.1 Kotlin

```kotlin
import android.media.*
import android.os.Bundle
import android.os.Environment
import android.util.Log
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream

class MainActivity : AppCompatActivity() {

    private var mPlayer: AudioTrack? = null
    private var mRecorder: AudioRecord? = null
    private var mOutputStream: FileOutputStream? = null
    private val mOutputFile =
        Environment.getExternalStorageDirectory().absolutePath + "/recordaudio3.pcm"

    private var mAudioBufferSize = 0
    private var mAudioBufferSampleSize = 0
    private var inRecordMode = false
    private var inPlaying = false
    private var inStoping = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onDestroy() {
        killMediaRecorder()
        killMediaPlayer()
        super.onDestroy()
    }

    fun doClick(view: View) {
        when (view.id) {
            R.id.beginBtn -> {
                try {
                    beginRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
            R.id.stopBtn -> {
                try {
                    stopRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
            R.id.playRecordingBtn -> {
                try {
                    playRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
            R.id.stopPlayingRecordingBtn -> {
                try {
                    stopPlayingRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
        }
    }

    private fun beginRecording() {
        killMediaRecorder()

        if (inRecordMode) {
            return
        }

        inRecordMode = true

        val sampleRate = 44100
        val channelConfig = AudioFormat.CHANNEL_IN_MONO
        val audioFormat = AudioFormat.ENCODING_PCM_16BIT
        mAudioBufferSize =
            2 * AudioRecord.getMinBufferSize(sampleRate, channelConfig, audioFormat)

        mRecorder = AudioRecord(
            MediaRecorder.AudioSource.MIC,
            sampleRate,
            channelConfig,
            audioFormat,
            mAudioBufferSize
        )
        Log.v(TAG, "beginRecording=>Setup of audioRecord okay. Buffer size = $mAudioBufferSize")
        Log.v(TAG, "beginRecording=>Sample buffer size = $mAudioBufferSampleSize")

        try {
            val outFile = File(mOutputFile)
            if (outFile.exists() && outFile.isFile) {
                outFile.delete()
            }
            outFile.createNewFile()
            mOutputStream = FileOutputStream(outFile, true)

            mRecorder?.apply {
                if (state != AudioRecord.STATE_INITIALIZED) {
                    Log.e(TAG, "beginRecording=>initAudioRecord=>AudioRecord is not properly initialized.")
                    inRecordMode = false
                    return
                } else {
                    Log.d(TAG, "beginRecording=>initAudioRecord=>AudioRecord is initialized")
                }

                mAudioBufferSampleSize = mAudioBufferSize / 2
                val notifyPosition = mAudioBufferSampleSize / 2
                val audioBuffer = ByteArray(mAudioBufferSampleSize)

                val pResult = setPositionNotificationPeriod(notifyPosition)
                Log.d(TAG, "pResult=$pResult")
                setRecordPositionUpdateListener(object: AudioRecord.OnRecordPositionUpdateListener {
                    /** 到达标志点 */
                    override fun onMarkerReached(recorder: AudioRecord?) {
                        Log.d(TAG, "onMarkerReached()...")
                        val samplesRead = read(audioBuffer, 0, mAudioBufferSampleSize)
                        Log.d(TAG, "onMarkerReached=>samplesRead: $samplesRead")
                        if (samplesRead > 0) {
                            mOutputStream?.write(audioBuffer, 0, samplesRead)
                        }
                        try {
                            mOutputStream?.flush()
                            mOutputStream?.close()
                        } catch (ignore: Exception) {
                        }
                        stop()
                        release()
                        mRecorder = null
                        inRecordMode = false
                        inStoping = false
                    }

                    /**定期通知 */
                    override fun onPeriodicNotification(recorder: AudioRecord?) {
                        val samplesRead = read(audioBuffer, 0, mAudioBufferSampleSize)
                        Log.d(TAG, "onPeriodicNotification=>samplesRead: $samplesRead")
                        if (samplesRead > 0) {
                            Log.d(TAG, "onPeriodicNotification=>write")
                            mOutputStream?.write(audioBuffer, 0, samplesRead)
                        }
                    }

                })

                startRecording()

                if (recordingState != AudioRecord.RECORDSTATE_RECORDING) {
                    Log.e(TAG, "beginRecording=>AudioRecord is not recording")
                    inRecordMode = false
                    return
                } else {
                    Log.v(TAG, "beginRecording=>AudioRecord has started recording ...")
                }
            }
        } catch (e: Exception) {
            Log.e(TAG, "Read record data error: ", e)
            inRecordMode = false
            try {
                mOutputStream?.flush()
                mOutputStream?.close()
            } catch (ignore: Exception) {
            }
        }
    }

    private fun stopRecording() {
        if (inRecordMode && !inStoping) {
            inStoping = true
            mRecorder?.notificationMarkerPosition = mAudioBufferSampleSize / 2
        }
    }

    private fun killMediaRecorder() {
        mRecorder?.release()
    }

    private fun killMediaPlayer() {
        mPlayer?.release()
    }

    private fun playRecording() {
        killMediaPlayer()

        Thread {
            inPlaying = true

            val audioFile = File(mOutputFile)
            if (!audioFile.exists() || !audioFile.isFile) {
                Log.e(TAG, "Audio file is not exist or not a file.")
                inPlaying = false
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
                    fis = FileInputStream(mOutputFile)
                    val data = ByteArray(4096)
                    var length = fis.read(data)
                    while (length != -1 && inPlaying) {
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

            inPlaying = false
        }.start()
    }

    private fun stopPlayingRecording() {
        inPlaying = false
        mPlayer?.stop()
    }

    companion object {
        const val TAG = "qty"
    }
}
```

#### 2.2 Java

```java
package com.android.androidtest;

import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioRecord;
import android.media.AudioTrack;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private AudioTrack mPlayer;
    private AudioRecord mRecorder;
    private FileOutputStream mOutputStream;
    private String mOutputFile;

    private int mAudioBufferSize;
    private int mAudioBufferSampleSize;
    private boolean inRecordMode = false;
    private boolean inPlaying = false;
    private boolean inStoping = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mOutputFile = Environment.getExternalStorageDirectory().getAbsolutePath() + "/recordaudio3.pcm";
    }

    @Override
    protected void onDestroy() {
        killMediaRecorder();
        killMediaPlayer();
        super.onDestroy();
    }

    public void doClick(View view) {
        try {
            switch (view.getId()) {
                case R.id.beginBtn:
                    beginRecording();
                    break;

                case R.id.stopBtn:
                    stopRecording();
                    break;

                case R.id.playRecordingBtn:
                    playRecording();
                    break;

                case R.id.stopPlayingRecordingBtn:
                    stopPlayingRecording();
                    break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void beginRecording() {
        killMediaRecorder();

        if (inRecordMode) {
            return;
        }
        inRecordMode = true;

        int sampleRate = 44100;
        int channelConfig = AudioFormat.CHANNEL_IN_MONO;
        int audioFormat = AudioFormat.ENCODING_PCM_16BIT;
        mAudioBufferSize = 2 * AudioRecord.getMinBufferSize(sampleRate, channelConfig, audioFormat);
        mAudioBufferSampleSize = mAudioBufferSize / 2;

        mRecorder = new AudioRecord(
                MediaRecorder.AudioSource.MIC,
                sampleRate,
                channelConfig,
                audioFormat,
                mAudioBufferSize
        );
        Log.v(TAG, "beginRecording=>Setup of audioRecord okay. Buffer size = " + mAudioBufferSize);
        Log.v(TAG, "beginRecording=>Sample buffer size = " + mAudioBufferSampleSize);

        try {
            File outFile = new File(mOutputFile);
            if (outFile.exists() && outFile.isFile()) {
                boolean success = outFile.delete();
                if (!success) {
                    Log.e(TAG, "beginRecording=>Unable delete old audio file.");
                    return;
                }
            }
            boolean success = outFile.createNewFile();
            if (!success) {
                Log.e(TAG, "beginRecording=>Unable create audio file.");
                return;
            }
            mOutputStream = new FileOutputStream(outFile, true);

            if (mRecorder.getState() != AudioRecord.STATE_INITIALIZED) {
                Log.e(TAG, "beginRecording=>initAudioRecord=>AudioRecord is not properly initialized.");
                inRecordMode = false;
                return;
            } else {
                Log.d(TAG, "beginRecording=>initAudioRecord=>AudioRecord is initialized");
            }

            byte[] audioBuffer = new byte[mAudioBufferSampleSize];
            int notifyPosition = mAudioBufferSampleSize / 2;

            mRecorder.setPositionNotificationPeriod(notifyPosition);
            mRecorder.setRecordPositionUpdateListener(new AudioRecord.OnRecordPositionUpdateListener() {
                @Override
                public void onMarkerReached(AudioRecord recorder) {
                    if (mOutputStream != null) {
                        int samplesRead = mRecorder.read(audioBuffer, 0, mAudioBufferSampleSize);
                        if (samplesRead > 0) {
                            try {
                                mOutputStream.write(audioBuffer, 0, samplesRead);
                            } catch (IOException e) {
                                Log.e(TAG, "onPeriodicNotification=>error: ", e);
                            }
                        }
                        try {
                            mOutputStream.flush();
                            mOutputStream.close();
                        } catch (Exception ignore) {
                        }
                    }
                    mRecorder.stop();
                    mRecorder.release();
                    mRecorder = null;
                    mOutputStream = null;
                    inRecordMode = false;
                    inStoping = false;
                }

                @Override
                public void onPeriodicNotification(AudioRecord recorder) {
                    if (mOutputStream != null) {
                        int samplesRead = mRecorder.read(audioBuffer, 0, mAudioBufferSampleSize);
                        Log.d(TAG, "onPeriodicNotification=>samplesRead: " + samplesRead);
                        if (samplesRead > 0) {
                            try {
                                mOutputStream.write(audioBuffer, 0, samplesRead);
                            } catch (IOException e) {
                                Log.e(TAG, "onPeriodicNotification=>error: ", e);
                                stopRecording();
                            }
                        }
                    }
                }
            });

            mRecorder.startRecording();

            if (mRecorder.getRecordingState() != AudioRecord.RECORDSTATE_RECORDING) {
                Log.e(TAG, "beginRecording=>AudioRecord is not recording");
                inRecordMode = false;
            } else {
                Log.v(TAG, "beginRecording=>AudioRecord has started recording ...");
            }
        } catch (Exception e) {
            Log.e(TAG, "Read record data error: ", e);
            stopRecording();
            try {
                if (mOutputStream != null) {
                    mOutputStream.flush();
                    mOutputStream.close();
                }
            } catch (Exception ignore) {}
        }
    }

    private void stopRecording() {
        if (inRecordMode && !inStoping) {
            if (mRecorder != null) {
                inStoping = true;
                mRecorder.setNotificationMarkerPosition(mAudioBufferSampleSize / 2);
            }
        }
    }

    private void killMediaRecorder() {
        if (mRecorder != null) {
            mRecorder.stop();
            mRecorder.release();
        }
    }

    private void killMediaPlayer() {
        if (mPlayer != null) {
            mPlayer.stop();
            mPlayer.release();
        }
    }

    private void playRecording() {
        killMediaPlayer();

        new Thread(() -> {
            inPlaying = true;

            int sampleRate = 44100;
            int channelConfig = AudioFormat.CHANNEL_OUT_MONO;
            int audioFormat = AudioFormat.ENCODING_PCM_16BIT;

            FileInputStream fis = null;

            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) {
                AudioFormat format = new AudioFormat.Builder()
                        .setChannelMask(channelConfig)
                        .setSampleRate(sampleRate)
                        .setEncoding(audioFormat)
                        .build();
                mPlayer = new AudioTrack.Builder()
                        .setAudioFormat(format)
                        .build();
            } else {
                int bufferSize = 2 * AudioRecord.getMinBufferSize(sampleRate,
                        channelConfig, audioFormat);
                mPlayer = new AudioTrack(AudioManager.STREAM_MUSIC, sampleRate,
                        channelConfig, audioFormat,
                        bufferSize, AudioTrack.MODE_STREAM);
            }
            mPlayer.play();

            try {
                fis = new FileInputStream(mOutputFile);
                byte[] data = new byte[4096];
                int length = fis.read(data);
                while(inPlaying && length != -1) {
                    mPlayer.write(data, 0, length);
                    length = fis.read(data);
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (fis != null) {
                    try {
                        fis.close();
                    } catch (Exception ignore) {}
                }
            }
            inPlaying = false;
        }).start();
    }

    private void stopPlayingRecording() {
        if (mPlayer != null) {
            inPlaying = false;
            mPlayer.stop();
        }
    }

}
```

#### 2.3 Layout

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:padding="16dp"
    android:orientation="vertical">

    <Button
        android:id="@+id/beginBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Begin Recording"
        android:onClick="doClick" />

    <Button
        android:id="@+id/stopBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Stop Recording"
        android:onClick="doClick" />

    <Button
        android:id="@+id/playRecordingBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Play Recording"
        android:onClick="doClick" />

    <Button
        android:id="@+id/stopPlayingRecordingBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Stop Playing Recording"
        android:onClick="doClick" />

</LinearLayout>
```

### 3. 完整示例代码

#### 3.1 Kotlin

```kotlin
import android.media.*
import android.os.Bundle
import android.os.Environment
import android.util.Log
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream

class MainActivity : AppCompatActivity() {

    private var mPlayer: AudioTrack? = null
    private var mRecorder: AudioRecord? = null
    private val mOutputFile =
        Environment.getExternalStorageDirectory().absolutePath + "/recordaudio3.pcm"

    private var mAudioBufferSize = 0
    private var mAudioBufferSampleSize = 0
    private var inRecordMode = false
    private var inPlaying = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onDestroy() {
        killMediaRecorder()
        killMediaPlayer()
        super.onDestroy()
    }

    fun doClick(view: View) {
        when (view.id) {
            R.id.beginBtn -> {
                try {
                    beginRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
            R.id.stopBtn -> {
                try {
                    stopRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
            R.id.playRecordingBtn -> {
                try {
                    playRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
            R.id.stopPlayingRecordingBtn -> {
                try {
                    stopPlayingRecording()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
        }
    }

    private fun beginRecording() {
        killMediaRecorder()
        Thread {
            inRecordMode = true

            val sampleRate = 44100
            val channelConfig = AudioFormat.CHANNEL_IN_MONO
            val audioFormat = AudioFormat.ENCODING_PCM_16BIT
            mAudioBufferSize =
                2 * AudioRecord.getMinBufferSize(sampleRate, channelConfig, audioFormat)
            mAudioBufferSampleSize = mAudioBufferSize / 2

            mRecorder = AudioRecord(
                MediaRecorder.AudioSource.MIC,
                sampleRate,
                channelConfig,
                audioFormat,
                mAudioBufferSize
            )
            Log.v(TAG, "beginRecording=>Setup of audioRecord okay. Buffer size = $mAudioBufferSize")
            Log.v(TAG, "beginRecording=>Sample buffer size = $mAudioBufferSampleSize")

            var fos: FileOutputStream? = null
            try {
                val outFile = File(mOutputFile)
                if (outFile.exists() && outFile.isFile) {
                    outFile.delete()
                }
                outFile.createNewFile()
                fos = FileOutputStream(outFile, true)

                mRecorder?.apply {
                    if (state != AudioRecord.STATE_INITIALIZED) {
                        Log.e(TAG, "beginRecording=>AudioRecord is not properly initialized.")
                        inRecordMode = false
                        return@Thread
                    } else {
                        Log.d(TAG, "beginRecording=>AudioRecord is initialized")
                    }

                    startRecording()

                    if (recordingState != AudioRecord.RECORDSTATE_RECORDING) {
                        Log.e(TAG, "beginRecording=>AudioRecord is not recording")
                        inRecordMode = false
                        return@Thread
                    } else {
                        Log.v(TAG, "beginRecording=>AudioRecord has started recording ...")
                    }

                    val audioBuffer = ByteArray(mAudioBufferSampleSize)
                    while (inRecordMode) {
                        val samplesRead = read(audioBuffer, 0, mAudioBufferSampleSize)
                        fos.write(audioBuffer, 0, samplesRead)
                    }

                }
            } catch (e: Exception) {
                Log.e(TAG, "Read record data error: ", e)
            } finally {
                try {
                    fos?.flush()
                    fos?.close()
                } catch (ignore: Exception) {
                }
            }

            inRecordMode = false
        }.start()
    }

    private fun stopRecording() {
        inRecordMode = false
        mRecorder?.stop()
    }

    private fun killMediaRecorder() {
        mRecorder?.release()
    }

    private fun killMediaPlayer() {
        mPlayer?.release()
    }

    private fun playRecording() {
        killMediaPlayer()

        Thread {
            inPlaying = true

            val audioFile = File(mOutputFile)
            if (!audioFile.exists() || !audioFile.isFile) {
                Log.e(TAG, "Audio file is not exist or not a file.")
                inPlaying = false
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
                    fis = FileInputStream(mOutputFile)
                    val data = ByteArray(4096)
                    var length = fis.read(data)
                    while (length != -1 && inPlaying) {
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

            inPlaying = false
        }.start()
    }

    private fun stopPlayingRecording() {
        inPlaying = false
        mPlayer?.stop()
    }

    companion object {
        const val TAG = "qty"
    }
}
```

#### 3.2 Java

```java
import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioRecord;
import android.media.AudioTrack;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private AudioTrack mPlayer;
    private AudioRecord mRecorder;
    private String mOutputFile;

    private int mAudioBufferSize;
    private int mAudioBufferSampleSize;
    private boolean inRecordMode = false;
    private boolean inPlaying = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mOutputFile = Environment.getExternalStorageDirectory().getAbsolutePath() + "/recordaudio3.pcm";
    }

    @Override
    protected void onDestroy() {
        killMediaRecorder();
        killMediaPlayer();
        super.onDestroy();
    }

    public void doClick(View view) {
        try {
            switch (view.getId()) {
                case R.id.beginBtn:
                    beginRecording();
                    break;

                case R.id.stopBtn:
                    stopRecording();
                    break;

                case R.id.playRecordingBtn:
                    playRecording();
                    break;

                case R.id.stopPlayingRecordingBtn:
                    stopPlayingRecording();
                    break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void beginRecording() {
        killMediaRecorder();
        new Thread(() -> {
            inRecordMode = true;

            int sampleRate = 44100;
            int channelConfig = AudioFormat.CHANNEL_IN_MONO;
            int audioFormat = AudioFormat.ENCODING_PCM_16BIT;
            mAudioBufferSize = 2 * AudioRecord.getMinBufferSize(sampleRate, channelConfig, audioFormat);
            mAudioBufferSampleSize = mAudioBufferSize / 2;

            mRecorder = new AudioRecord(
                    MediaRecorder.AudioSource.MIC,
                    sampleRate,
                    channelConfig,
                    audioFormat,
                    mAudioBufferSize
            );
            Log.v(TAG, "beginRecording=>Setup of audioRecord okay. Buffer size = " + mAudioBufferSize);
            Log.v(TAG, "beginRecording=>Sample buffer size = " + mAudioBufferSampleSize);

            FileOutputStream fos = null;
            try {
                File outFile = new File(mOutputFile);
                if (outFile.exists() && outFile.isFile()) {
                    boolean success = outFile.delete();
                    if (!success) {
                        Log.e(TAG, "beginRecording=>Unable delete old audio file.");
                        return;
                    }
                }
                boolean success = outFile.createNewFile();
                if (!success) {
                    Log.e(TAG, "beginRecording=>Unable create audio file.");
                    return;
                }
                fos = new FileOutputStream(outFile, true);

                if (mRecorder.getState() != AudioRecord.STATE_INITIALIZED) {
                    Log.e(TAG, "beginRecording=>AudioRecord is not properly initialized.");
                    inRecordMode = false;
                    return;
                } else {
                    Log.d(TAG, "beginRecording=>AudioRecord is initialized");
                }

                mRecorder.startRecording();

                if (mRecorder.getRecordingState() != AudioRecord.RECORDSTATE_RECORDING) {
                    Log.e(TAG, "beginRecording=>AudioRecord is not recording");
                    inRecordMode = false;
                    return;
                } else {
                    Log.v(TAG, "beginRecording=>AudioRecord has started recording ...");
                }

                byte[] audioBuffer = new byte[mAudioBufferSampleSize];
                while (inRecordMode) {
                    int samplesRead = mRecorder.read(audioBuffer, 0, mAudioBufferSampleSize);
                    fos.write(audioBuffer, 0, samplesRead);
                }
            } catch (Exception e) {
                Log.e(TAG, "Read record data error: ", e);
            } finally {
                try {
                    if (fos != null) {
                        fos.flush();
                        fos.close();
                    }
                } catch (Exception ignore) {}
            }
            inRecordMode = false;
        }).start();
    }

    private void stopRecording() {
        inRecordMode = false;
    }

    private void killMediaRecorder() {
        if (mRecorder != null) {
            mRecorder.stop();
            mRecorder.release();
        }
    }

    private void killMediaPlayer() {
        if (mPlayer != null) {
            mPlayer.stop();
            mPlayer.release();
        }
    }

    private void playRecording() {
        killMediaPlayer();

        new Thread(() -> {
            inPlaying = true;

            int sampleRate = 44100;
            int channelConfig = AudioFormat.CHANNEL_OUT_MONO;
            int audioFormat = AudioFormat.ENCODING_PCM_16BIT;

            FileInputStream fis = null;

            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) {
                AudioFormat format = new AudioFormat.Builder()
                        .setChannelMask(channelConfig)
                        .setSampleRate(sampleRate)
                        .setEncoding(audioFormat)
                        .build();
                mPlayer = new AudioTrack.Builder()
                        .setAudioFormat(format)
                        .build();
            } else {
                int bufferSize = 2 * AudioRecord.getMinBufferSize(sampleRate,
                        channelConfig, audioFormat);
                mPlayer = new AudioTrack(AudioManager.STREAM_MUSIC, sampleRate,
                        channelConfig, audioFormat,
                        bufferSize, AudioTrack.MODE_STREAM);
            }
            mPlayer.play();

            try {
                fis = new FileInputStream(mOutputFile);
                byte[] data = new byte[4096];
                int length = fis.read(data);
                while(inPlaying && length != -1) {
                    mPlayer.write(data, 0, length);
                    length = fis.read(data);
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (fis != null) {
                    try {
                        fis.close();
                    } catch (Exception ignore) {}
                }
            }
            inPlaying = false;
        }).start();
    }

    private void stopPlayingRecording() {
        if (mPlayer != null) {
            inPlaying = false;
            mPlayer.stop();
        }
    }

}
```

#### 3.3 Layout

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:padding="16dp"
    android:orientation="vertical">

    <Button
        android:id="@+id/beginBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Begin Recording"
        android:onClick="doClick" />

    <Button
        android:id="@+id/stopBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Stop Recording"
        android:onClick="doClick" />

    <Button
        android:id="@+id/playRecordingBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Play Recording"
        android:onClick="doClick" />

    <Button
        android:id="@+id/stopPlayingRecordingBtn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Stop Playing Recording"
        android:onClick="doClick" />

</LinearLayout>
```

