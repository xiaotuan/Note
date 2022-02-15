[toc]

> 注意：
>
> 由于 `SoundPool` 设计的初衷是用于无时延地播放游戏中的短促音效，因此实际开发中应该只将长度小于 7s 的声音资源放进 `SoundPool` ，否则可能会加载失败或内存占用过大。

### 1. SoundPool 类的构造器以及方法

+ **public SoundPool(int maxStreams, int streamType, int srcQuality)**

  创建 SoundPool 对象

  + maxStreams：该参数用于设置最多同时能够播放多少个音效
  + streamType：该参数设置音频类型，在游戏中通常设置为：STREAM_MUSIC
  + srcQuality：该参数设置音频文件的质量，设置为 0（默认值）

+ **public in load(Context context, int resId, int priority)**

  加载音频文件

  + context：应用程序的上下文
  + resId：该参数为要加载的音效资源的 ID
  + priority：优先级，现在还没有作用，设置为 1 即可

+ **public final int play(int soundID, float leftVolume, float rightVolume, int priority, int loop, float rate)**

  播放音效

  + soundID：该参数为要播放音效的 ID
  + leftVolume：该参数用来控制左声道音量
  + rightVolume：该参数用来控制右声道音量
  + priority：该参数为优先级，0 为最低
  + loop：该参数为音效播放的循环次数，0 为不循环， -1 为永远循环
  + rate：该参数为音效的回放速度，该值在 0.5 ~ 2.0f，1.0f 为正常速度

+ **public final void pause(int streamID)**

  暂停音效的播放

  + streamID：要暂停音效的 ID

+ **public final void stop(int streamID)**

  停止音效的播放

  + streamID：要停止音效的ID

### 2. SoundPool 的使用

#### 2.1 创建 SoundPool 对象

> 注意
>
> `SoundPool(int maxStreams, int streamType, int srcQuality)` 构造函数中 `srcQuality` 参数的值没有效果，默认传 0。

##### 2.1.1 Kotlin

```kotlin
import android.media.AudioAttributes
import android.media.AudioManager
import android.media.SoundPool

val soundPool = if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
    val aa = AudioAttributes.Builder()
    .setLegacyStreamType(AudioManager.STREAM_MUSIC)
    .build()
    SoundPool.Builder()
    .setAudioAttributes(aa)
    .setMaxStreams(5)
    .build()
} else {
    SoundPool(5, AudioManager.STREAM_MUSIC, SRC_QUALITY)
}

// 设置播放完成监听器
soundPool.setOnLoadCompleteListener(this)

override fun onLoadComplete(soundPool: SoundPool?, sampleId: Int, status: Int) {
    TODO("Not yet implemented")
}

companion object {
    const val SRC_QUALITY = 0
}
```

##### 2.1.2 Java

```java
import android.media.AudioAttributes;
import android.media.AudioManager;
import android.media.SoundPool;

private static final int SRC_QUALITY = 0;

SoundPool soundPool = null;
if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
    AudioAttributes aa = new AudioAttributes.Builder()
        .setLegacyStreamType(AudioManager.STREAM_MUSIC)
        .build();
    soundPool = new SoundPool.Builder()
        .setMaxStreams(5)
        .setAudioAttributes(aa)
        .build();
} else {
    soundPool = new SoundPool(5, AudioManager.STREAM_MUSIC, SRC_QUALITY);
}

// 设置播放完成监听器
soundPool.setOnLoadCompleteListener(this);

@Override
public void onLoadComplete(SoundPool soundPool, int sampleId, int status) {

}
```

#### 2.2 加载音频文件

> 注意
>
> `load(FileDescriptor fd, long offset, long length, int priority)` 加载音频资源方法中 `priority` 的值没有效果，默认传 1。

##### 2.2.1 Kotlin

```kotlin
import android.os.Environment
import java.io.File
import java.io.IOException

// 方法一
var audioId = soundPool.load(this, R.raw.test, PRIORITY)

// 方法二
try {
    val afd = assets.openFd("test.mp3")
    audioId = soundPool.load(afd.fileDescriptor, afd.startOffset, afd.length, PRIORITY)
    afd.close()
} catch (e : IOException) {
    e.printStackTrace()
}
      
// 方法三
val dir = Environment.getExternalStorageDirectory()
val file = File(dir, "test.mp3")
if (file.exists() && file.isFile) {
    audioId = soundPool.load(file.absolutePath, PRIORITY)
}
```

##### 2.2.2 Java

```java
import android.content.res.AssetFileDescriptor;
import android.os.Environment;
import java.io.File;
import java.io.IOException;

int audioId = soundPool.load(this, R.raw.test, PRIORITY);
        
try {
    AssetFileDescriptor afd = getAssets().openFd("test.mp3");
    audioId = soundPool.load(afd.getFileDescriptor(), afd.getStartOffset(), afd.getLength(), PRIORITY);
    afd.close();
} catch (IOException e) {
    e.printStackTrace();
}

File dir = Environment.getExternalStorageDirectory();
File audioFile = new File(dir, "test.mp3");
if (audioFile.exists() && audioFile.isFile()) {
    audioId = soundPool.load(audioFile.getAbsolutePath(), PRIORITY);
}
```

####  2.4 播放

`play(int soundID, float leftVolume, float rightVolume, int priority, int loop, float rate)` 方法的参数说明：

+ soundID：音频资源ID，通过 load() 方法获取
+ leftVolume：左声道音量大小，取值范围：0.0 ~ 1.0
+ rightVolume：右声道音量大小，取值范围：0.0 ~ 1.0
+ priority：优先级， 0 表示最低优先级
+ loop：是否循环播放， 0 表示不循环，-1 表示循环播放
+ rate：播放速率， 1.0f 表示正常播放，取值范围为 0.5 ~ 2.0

##### 2.4.1 Kotlin

```kotlin
import android.media.AudioManager

val am = getSystemService(AUDIO_SERVICE) as AudioManager
val currentVolume =
am.getStreamVolume(AudioManager.STREAM_MUSIC).toFloat() / am.getStreamMaxVolume(
    AudioManager.STREAM_MUSIC
).toFloat()
val result = soundPool.play(audioId, currentVolume, currentVolume, PRIORITY, -1, 1.0f)
if (result == 0) {
    Log.e(TAG, "Failed to start sound")
}
```

##### 2.4.2 Java

```java
import android.media.AudioManager;
import android.util.Log;

AudioManager am = (AudioManager) getSystemService(AUDIO_SERVICE);
final float currentVolume = ((float) am.getStreamVolume(AudioManager.STREAM_MUSIC)) / ((float) am.getStreamMaxVolume(AudioManager.STREAM_MUSIC));
int result = soundPool.play(audioId, currentVolume, currentVolume, PRIORITY, -1, 1.0f);
if (result == 0) {
    Log.e(TAG, "Failed to start sound");
}
```

#### 2.5 全部恢复播放或全部暂停

##### 2.5.1 Kotlin

```kotlin
// 全部播放
soundPool.autoResume()
// 全部暂停
soundPool.autoPause()
```

##### 2.5.2 Java

```java
// 全部播放
soundPool.autoResume();
// 全部暂停
soundPool.autoPause();
```

#### 2.6 完整示例

##### 2.6.1 Kotlin 版本

```kotlin
package com.qty.kotlintest

import android.media.AudioAttributes
import android.media.AudioManager
import android.media.SoundPool
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import java.util.*
import kotlin.collections.HashMap

class MainActivity : AppCompatActivity(), View.OnClickListener {

    private var mStartBtn: Button? = null
    private var mPauseBtn: Button? = null
    private var mStopBtn: Button? = null

    private var mSoundPool: SoundPool? = null
    private var mStreamIDs: HashMap<Int, Int>? = null
    private var mCurrStreamId = -1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initSoundPool()

        mStartBtn = findViewById(R.id.start)
        mPauseBtn = findViewById(R.id.pause)
        mStopBtn = findViewById(R.id.stop);

        mStartBtn?.setOnClickListener(this)
        mPauseBtn?.setOnClickListener(this)
        mStopBtn?.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        when (v?.id) {
            R.id.start -> {
                if (mCurrStreamId == -1) {
                    playSound(1, 0)
                } else {
                    resumeSound()
                }
                mStartBtn?.isEnabled = false
                mPauseBtn?.isEnabled = true
                mStopBtn?.isEnabled = true
                Toast.makeText(this@MainActivity, "播放即时音效", Toast.LENGTH_SHORT).show()
            }
            R.id.pause -> {
                pauseSound()
                mStartBtn?.isEnabled = true
                mPauseBtn?.isEnabled = false
                mStopBtn?.isEnabled = true
                Toast.makeText(this@MainActivity, "暂停播放即时音效", Toast.LENGTH_SHORT).show()
            }
            R.id.stop -> {
                stopSound()
                mStartBtn?.isEnabled = true
                mPauseBtn?.isEnabled = false
                mStopBtn?.isEnabled = false
                Toast.makeText(this@MainActivity, "停止播放即时音效", Toast.LENGTH_SHORT).show()
            }
        }
    }

    // 初始化声音池的方法
    fun initSoundPool() {
        // 创建 SoundPool 对象
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            val attr = AudioAttributes.Builder()
                .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                .setUsage(AudioAttributes.USAGE_MEDIA)
                .setLegacyStreamType(AudioManager.STREAM_MUSIC)
                .build()
            mSoundPool = SoundPool.Builder()
                .setMaxStreams(4)
                .setAudioAttributes(attr)
                .build()
        } else {
            mSoundPool = SoundPool(4, AudioManager.STREAM_MUSIC, 0);
        }
        // 创建 HashMap 对象
        mStreamIDs = HashMap()
        mSoundPool?.let {
            // 加载声音文件 musictest 并且设置为 1 号声音放入 mStreamIDs 中
            mStreamIDs?.put(1, it.load(this@MainActivity, R.raw.musictest, 1))
        }
    }

    // 播放声音的方法
    fun playSound(sound: Int, loop: Int) {
        // 获取 AudioManager 引用
        val am = getSystemService(AUDIO_SERVICE) as AudioManager
        // 获取当前音量
        val streamVolumeCurrent = am.getStreamVolume(AudioManager.STREAM_MUSIC).toFloat()
        // 获取系统最大音量
        val streamVolumeMax = am.getStreamMaxVolume(AudioManager.STREAM_MUSIC).toFloat()
        // 计算得到播放音量
        val volume = streamVolumeCurrent / streamVolumeMax
        // 调用 SoundPool 的 play 方法来播放声音文件
        mSoundPool?.apply {
            mStreamIDs?.let {
                mCurrStreamId = play(it.get(sound)!!.toInt(), volume, volume, 1, loop, 1.0f)
            }
        }
    }

    // 暂停播放音效的方法
    fun pauseSound() {
        mSoundPool?.pause(mCurrStreamId)
    }

    // 恢复播放音效的方法
    fun resumeSound() {
        mSoundPool?.resume(mCurrStreamId)
    }

    // 停止播放音效的方法
    fun stopSound() {
        mSoundPool?.stop(mCurrStreamId)
        mCurrStreamId = -1
    }
}
```

##### 2.6.2 Java 版本

```java
package com.qty.test;

import androidx.appcompat.app.AppCompatActivity;

import android.media.AudioAttributes;
import android.media.AudioManager;
import android.media.SoundPool;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.HashMap;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private static final String TAG = MainActivity.class.getSimpleName();

    private Button mStartBtn;
    private Button mPauseBtn;
    private Button mStopBtn;

    private SoundPool mSoundPool;
    private HashMap<Integer, Integer> mStreamIDs;
    private int mCurrStreamId = -1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initSoundPool();

        mStartBtn = findViewById(R.id.start);
        mPauseBtn = findViewById(R.id.pause);
        mStopBtn = findViewById(R.id.stop);

        mStartBtn.setOnClickListener(this);
        mPauseBtn.setOnClickListener(this);
        mStopBtn.setOnClickListener(this);


    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.start:
                if (mCurrStreamId == -1) {
                    playSound(1, 0);
                } else {
                    resumeSound();
                }
                mStartBtn.setEnabled(false);
                mPauseBtn.setEnabled(true);
                mStopBtn.setEnabled(true);
                Toast.makeText(this, "播放即时音效", Toast.LENGTH_SHORT).show();
                break;

            case R.id.pause:
                pauseSound();
                mStartBtn.setEnabled(true);
                mPauseBtn.setEnabled(false);
                mStopBtn.setEnabled(true);
                Toast.makeText(this, "暂停播放即时音效", Toast.LENGTH_SHORT).show();
                break;

            case R.id.stop:
                stopSound();
                mStartBtn.setEnabled(true);
                mPauseBtn.setEnabled(false);
                mStopBtn.setEnabled(false);
                Toast.makeText(this, "停止播放即时音效", Toast.LENGTH_SHORT).show();
                break;
        }
    }

    // 初始化声音池的方法
    private void initSoundPool() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            AudioAttributes attr = new AudioAttributes.Builder()
                    .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                    .setUsage(AudioAttributes.USAGE_MEDIA)
                    .setLegacyStreamType(AudioManager.STREAM_MUSIC)
                    .build();
            mSoundPool = new SoundPool.Builder()
                    .setMaxStreams(4)
                    .setAudioAttributes(attr)
                    .build();
        } else {
            mSoundPool = new SoundPool(4, AudioManager.STREAM_MUSIC, 0);    // 创建 SoundPool 对象
        }
            mStreamIDs = new HashMap<>();   // 创建 HashMap 对象
        // 加载声音文件 musictest 并且设置为 1 号声音放入 mStreamIDs 中
        mStreamIDs.put(1, mSoundPool.load(this, R.raw.musictest, 1));
    }

    // 播放声音的方法
    private void playSound(int sound, int loop) {
        // 获取 AudioManager 引用
        AudioManager am = (AudioManager) getSystemService(AUDIO_SERVICE);
        // 获取当前音量
        float streamVolumeCurrent = am.getStreamVolume(AudioManager.STREAM_MUSIC);
        // 获取系统最大音量
        float streamVolumeMax = am.getStreamMaxVolume(AudioManager.STREAM_MUSIC);
        // 计算得到播放音量
        float volume = streamVolumeCurrent / streamVolumeMax;
        // 调用 SoundPool 的 play 方法来播放声音文件
        mCurrStreamId = mSoundPool.play(mStreamIDs.get(sound), volume, volume, 1, loop, 1.0f);
    }

    // 暂停播放音效的方法
    private void pauseSound() {
        mSoundPool.pause(mCurrStreamId);
    }

    // 恢复播放音效的方法
    private void resumeSound() {
        mSoundPool.resume(mCurrStreamId);
    }

    // 停止播放音效的方法
    private void stopSound() {
        mSoundPool.stop(mCurrStreamId);
        mCurrStreamId = -1;
    }
}
```

2.3 布局文件

**activity_main.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    >

    <Button
        android:id="@+id/start"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textAllCaps="false"
        android:text="播放音效" />

    <Button
        android:id="@+id/pause"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textAllCaps="false"
        android:enabled="false"
        android:text="暂停音效" />

    <Button
        android:id="@+id/stop"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textAllCaps="false"
        android:enabled="false"
        android:text="停止音效" />

</LinearLayout>
```



