[toc]

> 注意
>
> 录音需要 `android.permission.RECORD_AUDIO` 权限，如果需要将录音文件写入内部存储或外部存储中，还需要 `android.permission.WRITE_EXTERNAL_STORAGE`。

### 1. 创建 MediaRecorder 对象

`MediaRecorder` 的常用方法如下：

+ `setAudioSource()`：设置音频来源，其值可以是：
  + MediaRecorder.AudioSource.MIC：主麦克风
  + MediaRecorder.AudioSource.VOICE_UPLINK：通话的上行端音频（即电话用户的声音）
  + MediaRecorder.AudioSource.VOICE_DOWNLINK：通话的下行端音频（即来自电话另一头的声音）
  + MediaRecorder.AudioSource.VOICE_CALL：通话音频源
  + MediaRecorder.AudioSource.CAMCORDER：相机麦克风，没有则使用主麦克风
  + MediaRecorder.AudioSource.VOICE_RECOGNITION：语音识别麦克风，没有则使用主麦克风
  + MediaRecorder.AudioSource.VOICE_COMMUNICATION：用于语音通信（如 VoIP）的麦克风音频源
+ `setOutputFormat()`：设置输出格式，其值可以是如下值：
  + MediaRecorder.OutputFormat.THREE_GPP：.3gpp
  + MediaRecorder.OutputFormat.MPEG_4：
  + MediaRecorder.OutputFormat.RAW_AMR：.amr
  + MediaRecorder.OutputFormat.AMR_NB：.amr
  + MediaRecorder.OutputFormat.AMR_WB：.amr
  + MediaRecorder.OutputFormat.AAC_ADIF：.acc
  + MediaRecorder.OutputFormat.AAC_ADTS：.acc
  + MediaRecorder.OutputFormat.OUTPUT_FORMAT_RTP_AVP
  + MediaRecorder.OutputFormat.MPEG_2_TS
  + MediaRecorder.OutputFormat.WEBM：.webm
  + MediaRecorder.OutputFormat.HEIF
  + MediaRecorder.OutputFormat.OGG：.ogg
+ `setAudioEncoder()`：设置音频编码格式，其值有：
  + MediaRecorder.AudioEncoder.AMR_NB
  + MediaRecorder.AudioEncoder.AMR_WB
  + MediaRecorder.AudioEncoder.AAC
  + MediaRecorder.AudioEncoder.HE_AAC
  + MediaRecorder.AudioEncoder.AAC_ELD
  + MediaRecorder.AudioEncoder.VORBIS
  + MediaRecorder.AudioEncoder.OPUS
+ `setOutputFile()`：设置音频输出文件
+ `setMaxDuration()`：设置最大录制时长，该方法需要在 setOutputFormat() 方法之后，prepare() 方法之前调用，时间单位为 ms，0 或者负数不限制录制时长
+ `setMaxFileSize()`：设置录制音频文件的最大大小，该方法需要在 setOutputFormat() 方法之后，prepare() 方法之前调用，单位为：byte，0 或者负数不限制文件大小

#### 1.1 Kotlin

```kotlin
import android.media.*
import android.os.Environment
import java.io.File
import java.lang.Exception

val outPutFilePath = Environment.getExternalStorageDirectory().absolutePath + "/recordaudio3.3gpp"
val recorder = MediaRecorder()
recorder.apply { 
    setAudioSource(MediaRecorder.AudioSource.MIC)
    setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP)
    setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB)
    setOutputFile(OUTPUT_FILE)
    prepare()
}
```

#### 1.2 Java

```java
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.Environment;
import java.io.File;

String outputFile = Environment.getExternalStorageDirectory().getAbsolutePath() + "/recordaudio3.3gpp";
File outFile = new File(outputFile);

if (outFile.exists()) {
    outFile.delete();
}

outFile.createNewFile();

MediaRecorder recorder = new MediaRecorder();
recorder.setAudioSource(MediaRecorder.AudioSource.MIC);
recorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
recorder.setOutputFile(mOutputFile);
recorder.prepare();
```

### 2. 开始录制

#### 2.1 Kotlin

```kotlin
recorder.start()
```

#### 2.2 Java

```java
recorder.start();
```

### 3. 停止录制

#### 3.1 Kotlin

```kotlin
recorder.stop()
```

#### 3.2 Java

```java
recorder.stop();
```

### 4. 释放资源

> 注意
>
> 录制结束后需要是否录制资源，避免内存泄漏。

#### 4.1 Kotlin

```kotin
recorder.release()
```

#### 4.2 Java

```java
recorder.release();
```

### 5. 一个完整示例

#### 5.1 Kotlin

```kotlin
import android.media.*
import android.os.Bundle
import android.os.Environment
import android.view.View

import androidx.appcompat.app.AppCompatActivity
import java.io.File
import java.lang.Exception

class MainActivity : AppCompatActivity() {

    private var mMediaPlayer: MediaPlayer? = null
    private var mRecorder: MediaRecorder? =null
    private var OUTPUT_FILE = Environment.getExternalStorageDirectory().absolutePath + "/recordaudio3.3gpp"

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

        val outFile = File(OUTPUT_FILE)

        if (outFile.exists()) {
            outFile.delete()
        }

        outFile.createNewFile()

        mRecorder = MediaRecorder()
        mRecorder?.apply {
            setAudioSource(MediaRecorder.AudioSource.MIC)
            setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP)
            setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB)
            setOutputFile(OUTPUT_FILE)
            prepare()
            start()
        }
    }

    private fun stopRecording() {
        mRecorder?.stop()
    }

    private fun killMediaRecorder() {
        mRecorder?.release()
    }

    private fun killMediaPlayer() {
        mMediaPlayer?.release()
    }

    private fun playRecording() {
        killMediaPlayer()

        mMediaPlayer = MediaPlayer()
        mMediaPlayer?.apply {
            setDataSource(OUTPUT_FILE)
            prepare()
            start()
        }
    }

    private fun stopPlayingRecording() {
        mMediaPlayer?.stop()
    }

    companion object {
        const val TAG = "qty"
    }
}
```

#### 5.2 Java

```java
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Environment;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private MediaPlayer mPlayer;
    private MediaRecorder mRecorder;
    private String mOutputFile;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mOutputFile = Environment.getExternalStorageDirectory().getAbsolutePath() + "/recordaudio3.3gpp";
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

    private void beginRecording() throws Exception {
        killMediaRecorder();

        File outFile = new File(mOutputFile);

        if (outFile.exists()) {
            outFile.delete();
        }

        outFile.createNewFile();

        mRecorder = new MediaRecorder();
        mRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
        mRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
        mRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
        mRecorder.setOutputFile(mOutputFile);
        mRecorder.prepare();
        mRecorder.start();
    }

    private void stopRecording() {
        if (mRecorder != null) {
            mRecorder.stop();
        }
    }

    private void killMediaRecorder() {
        if (mRecorder != null) {
            mRecorder.release();
        }
    }

    private void killMediaPlayer() {
        if (mPlayer != null) {
            mPlayer.release();
        }
    }

    private void playRecording() throws Exception {
        killMediaPlayer();

        mPlayer = new MediaPlayer();
        mPlayer.setDataSource(mOutputFile);
        mPlayer.prepare();
        mPlayer.start();
    }

    private void stopPlayingRecording() {
        if (mPlayer != null) {
            mPlayer.stop();
        }
    }
}
```

#### 5.3 Layout

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

