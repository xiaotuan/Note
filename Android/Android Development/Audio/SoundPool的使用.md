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

2.1 将音频文件 `musictest.ogg` 文件复制到 `app/src/main/res/raw` 文件夹下。

2.2 实现代码：

**Kotlin 版本**

```kotlin
```

**Java 版本**

```java
package com.qty.test;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.media.AudioManager;
import android.media.SoundPool;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.File;
import java.util.HashMap;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button mStartBtn;
    private Button mPauseBtn;
    private Button mStopBtn;

    private SoundPool mSoundPool;
    private HashMap<Integer, Integer> mStreamIDs;
    private int currStreamId = -1;

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
                playSound(1, 0);
                mStartBtn.setEnabled(false);
                mPauseBtn.setEnabled(true);
                mStopBtn.setEnabled(true);
                Toast.makeText(this, "播放即时音效", Toast.LENGTH_SHORT).show();
                break;

            case R.id.pause:
                pauseSound();
                mStartBtn.setEnabled(true);
                mPauseBtn.setEnabled(true);
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
        mSoundPool = new SoundPool(4, AudioManager.STREAM_MUSIC, 0);    // 创建 SoundPool 对象
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
        currStreamId = mSoundPool.play(mStreamIDs.get(sound), volume, volume, 1, loop, 1.0f);
    }

    // 暂停播放音效的方法
    private void pauseSound() {
        mSoundPool.pause(currStreamId);
    }

    // 停止播放音效的方法
    private void stopSound() {
        mSoundPool.stop(currStreamId);
        currStreamId = -1;
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



