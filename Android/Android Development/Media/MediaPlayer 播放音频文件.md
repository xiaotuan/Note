[toc]

### 1. MediaPlayer 常用方法

+ `setDataSource()`：设置音频源
+ `prepare()`：为播放做准备
+ `start()`：开始播放
+ `pause()`：暂停播放，再次播放无需再调用 `prepare()` 方法
+ `getCurrentPosition()`：获取当前播放位置
+ `seekTo()`：设置播放位置
+ `stop()`：停止播放，再次播放前需要调用 `prepare()` 方法
+ `reset()`：重置播放状态
+ `release()`：释放资源

### 2. 播放网络音频文件

> 注意
>
> 需要 `android.permission.INTERNET` 权限。

#### 2.1 Kotlin

```kotlin
import android.media.MediaPlayer
import android.os.Bundle
import android.util.Log

import androidx.appcompat.app.AppCompatActivity
import java.io.IOException

class MainActivity : AppCompatActivity() {

    private var mPlayer: MediaPlayer? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onResume() {
        super.onResume()
        playAudio()
    }

    override fun onPause() {
        super.onPause()
        stopPlayAudio()
    }

    private fun playAudio() {
        if (mPlayer == null) {
            val urlStr = "https://xact02.baidupcs.com/file/4035e8f76n42fb8a27ebd55733b8ce71?bkt=en-cf7b18a7c51d9078e6fbbb7233909aee6dfc7291cdfc1bdbf4fb3e6bfc922ede93f15d9c1bddf3ec&fid=3157217601-250528-486160312351565&time=1644826052&sign=FDTAXUbGERQlBHSKfWqiu-DCb740ccc5511e5e8fedcff06b081203-UVA9AE%2BqO6B2QljvoXeVKGLdig8%3D&to=126&size=7908442&sta_dx=7908442&sta_cs=1&sta_ft=mp3&sta_ct=0&sta_mt=0&fm2=MH%2CXian%2CAnywhere%2C%2Cguangdong%2Cct&ctime=1644825990&mtime=1644825990&resv0=-1&resv1=0&resv2=rlim&resv3=5&resv4=7908442&vuk=3157217601&iv=2&htype=&randtype=&tkbind_id=0&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=en-e3ae8b5593a01abf50680336f74f518536c813b3e8c69e822701214bffc30ba1b96bbf3181097560&expires=8h&rt=sh&r=769032726&vbdid=967595916&fin=%E5%B7%A6%E5%AE%8F%E5%85%83+%E5%BC%A0%E6%85%A7%E6%B8%85+-+%E6%B8%A1%E6%83%85.mp3&fn=%E5%B7%A6%E5%AE%8F%E5%85%83+%E5%BC%A0%E6%85%A7%E6%B8%85+-+%E6%B8%A1%E6%83%85.mp3&rtype=1&clienttype=0&dp-logid=9106518173687161476&dp-callid=0.1&hps=1&tsl=0&csl=0&fsl=-1&csign=%2ButfmhhyTK4LE5EsK1S2wRD0P%2Bk%3D&so=0&ut=1&uter=4&serv=0&uc=3721604516&ti=c77e04c9862927e5e612fecec356e054dbd4f2d4e3edfd58305a5e1275657320&hflag=30&from_type=1&adg=c_d679289db92225aff9cdf5f67b08b693&reqlabel=250528_f_3a9e3094924f9e391e03069401c417ef_-1_b1866a87779e1669f3ab2ff6c7ca6297&by=themis&resvsflag=1-0-0-1-1-1"
            try {
                mPlayer = MediaPlayer()
                mPlayer?.let {
                    it.setDataSource(urlStr)
                    it.prepare()
                    it.start()
                }
            } catch (e : IOException) {
                Log.e(TAG, "playAudio=>error: ", e)
                mPlayer?.let {
                    it.stop()
                    it.reset()
                    it.release()
                }
                mPlayer = null
            }
        }
    }

    private fun stopPlayAudio() {
        mPlayer?.let {
            it.stop()
            it.reset()
            it.release()
        }
        mPlayer = null
    }

    companion object {
        const val TAG = "qty"
    }
}
```

#### 2.2 Java

```java
import android.media.MediaPlayer;
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private MediaPlayer mPlayer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onResume() {
        super.onResume();
        playAudio();
    }

    @Override
    protected void onPause() {
        super.onPause();
        stopPlayAudio();
    }

    private void playAudio() {
        if (mPlayer == null) {
            String urlStr = "https://xact02.baidupcs.com/file/4035e8f76n42fb8a27ebd55733b8ce71?bkt=en-cf7b18a7c51d9078e6fbbb7233909aee6dfc7291cdfc1bdbf4fb3e6bfc922ede93f15d9c1bddf3ec&fid=3157217601-250528-486160312351565&time=1644826052&sign=FDTAXUbGERQlBHSKfWqiu-DCb740ccc5511e5e8fedcff06b081203-UVA9AE%2BqO6B2QljvoXeVKGLdig8%3D&to=126&size=7908442&sta_dx=7908442&sta_cs=1&sta_ft=mp3&sta_ct=0&sta_mt=0&fm2=MH%2CXian%2CAnywhere%2C%2Cguangdong%2Cct&ctime=1644825990&mtime=1644825990&resv0=-1&resv1=0&resv2=rlim&resv3=5&resv4=7908442&vuk=3157217601&iv=2&htype=&randtype=&tkbind_id=0&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=en-e3ae8b5593a01abf50680336f74f518536c813b3e8c69e822701214bffc30ba1b96bbf3181097560&expires=8h&rt=sh&r=769032726&vbdid=967595916&fin=%E5%B7%A6%E5%AE%8F%E5%85%83+%E5%BC%A0%E6%85%A7%E6%B8%85+-+%E6%B8%A1%E6%83%85.mp3&fn=%E5%B7%A6%E5%AE%8F%E5%85%83+%E5%BC%A0%E6%85%A7%E6%B8%85+-+%E6%B8%A1%E6%83%85.mp3&rtype=1&clienttype=0&dp-logid=9106518173687161476&dp-callid=0.1&hps=1&tsl=0&csl=0&fsl=-1&csign=%2ButfmhhyTK4LE5EsK1S2wRD0P%2Bk%3D&so=0&ut=1&uter=4&serv=0&uc=3721604516&ti=c77e04c9862927e5e612fecec356e054dbd4f2d4e3edfd58305a5e1275657320&hflag=30&from_type=1&adg=c_d679289db92225aff9cdf5f67b08b693&reqlabel=250528_f_3a9e3094924f9e391e03069401c417ef_-1_b1866a87779e1669f3ab2ff6c7ca6297&by=themis&resvsflag=1-0-0-1-1-1";
            try {
                mPlayer = new MediaPlayer();
                mPlayer.setDataSource(urlStr);
                mPlayer.prepare();
                mPlayer.start();
            } catch (IOException e) {
                Log.e(TAG, "playAudio=>error: ", e);
                if (mPlayer != null) {
                    mPlayer.stop();
                    mPlayer.reset();
                    mPlayer.release();
                    mPlayer = null;
                }
            }
        }
    }

    private void stopPlayAudio() {
        if (mPlayer != null) {
            mPlayer.stop();
            mPlayer.reset();
            mPlayer.release();
            mPlayer = null;
        }
    }

}
```

### 3. 播放 APK 中的音频文件

需要将音频文件放置在 res/raw 目录下。

#### 3.1 播放 raw 文件夹中的音频文件

##### 3.1.1 Kotlin

```kotlin
// 方法一
val mPlayer = MediaPlayer.create(this, R.raw.test)
// 无法在播放前调用 prepare()
mPlayer.start()

// 方法二
var mPlayer: MediaPlayer? = null
val fileDesc = resources.openRawResourceFd(R.raw.test)
fileDesc?.let { 
    mPlayer = MediaPlayer()
    try {
        mPlayer?.apply { 
            setDataSource(fileDesc.fileDescriptor, fileDesc.startOffset, fileDesc.length)
            it.close()
            prepare()
            start()
        }
    } catch (e : IOException) {
        Log.d(TAG, "error: ", e)
        mPlayer?.apply { 
            stop()
            reset()
            release()
        }
        mPlayer = null
    }
}
```

##### 3.1.2 Java

```java
// 方法一
MediaPlayer mPlayer = MediaPlayer.create(this, R.raw.test);
// calling prepare() is not required in this case
mPlayer.start();

// 方法二
MediaPlayer mPlayer = null;
AssetFileDescriptor fileDesc = getResources().openRawResourceFd(R.raw.test);
if (fileDesc != null) {
    mPlayer = new MediaPlayer();
    try {
        mPlayer.setDataSource(fileDesc.getFileDescriptor(), fileDesc.getStartOffset(), fileDesc.getLength());
        fileDesc.close();
        mPlayer.prepare();
        mPlayer.start();
    } catch (IOException e) {
        Log.d(TAG, "error: ", e);
        if (mPlayer != null) {
            mPlayer.stop();
            mPlayer.reset();
            mPlayer.release();
            mPlayer = null;
        }
    }
}
```

#### 3.2 播放 assets 文件夹中的音频文件

##### 3.2.1 Kotlin

```kotlin
var mPlayer: MediaPlayer? = null
val fileDesc = assets.openFd("test.mp3")
fileDesc?.let {
    mPlayer = MediaPlayer()
    try {
        mPlayer?.apply {
            setDataSource(fileDesc.fileDescriptor, fileDesc.startOffset, fileDesc.length)
            it.close()
            prepare()
            start()
        }
    } catch (e : IOException) {
        Log.d(TAG, "error: ", e)
        mPlayer?.apply {
            stop()
            reset()
            release()
        }
        mPlayer = null
    }
}
```

##### 3.2.2 Java

```java
MediaPlayer mPlayer = null;
AssetFileDescriptor fileDesc = getAssets().openFd("test.mp3");
if (fileDesc != null) {
    mPlayer = new MediaPlayer();
    try {
        mPlayer.setDataSource(fileDesc.getFileDescriptor(), fileDesc.getStartOffset(), fileDesc.getLength());
        fileDesc.close();
        mPlayer.prepare();
        mPlayer.start();
    } catch (IOException e) {
        Log.d(TAG, "error: ", e);
        if (mPlayer != null) {
            mPlayer.stop();
            mPlayer.reset();
            mPlayer.release();
            mPlayer = null;
        }
    }
}
```

### 4. 播放 SD 卡中的音频文件

#### 4.1 Kotlin

```kotlin
import android.os.Environment
import java.io.File

val dir = Environment.getExternalStorageDirectory()
Log.d(TAG, "dir: $dir")
val file = File(dir, "左宏元 张慧清 - 渡情.mp3")
if (file.exists() && file.isFile) {
    mPlayer = MediaPlayer()
    try {
        mPlayer?.apply {
            setDataSource(file.absolutePath)
            prepare()
            start()
        }
    } catch (e : IOException) {
        Log.d(TAG, "error: ", e)
        mPlayer?.apply {
            stop()
            reset()
            release()
        }
        mPlayer = null
    }
}
```

#### 4.2 Java

```java
import android.os.Environment;
import java.io.File;

MediaPlayer mPlayer = null;
File dir = Environment.getExternalStorageDirectory();
File audioFile = new File(dir, "左宏元 张慧清 - 渡情.mp3");
if (audioFile.exists() && audioFile.isFile()) {
    mPlayer = new MediaPlayer();
    try {
        mPlayer.setDataSource(audioFile.getAbsolutePath());
        mPlayer.prepare();
        mPlayer.start();
    } catch (IOException e) {
        Log.d(TAG, "error: ", e);
        if (mPlayer != null) {
            mPlayer.stop();
            mPlayer.reset();
            mPlayer.release();
            mPlayer = null;
        }
    }
}
```

