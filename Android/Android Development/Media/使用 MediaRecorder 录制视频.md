[toc]

> 提示
>
> 录制视频需要如下权限：
>
> + android.permission.RECORD_AUDIO
> + android.permission.CAMERA
> + android.permission.WRITE_EXTERNAL_STORAGE

### 1. 创建相机预览

#### 1.1  创建 Camera 对象

##### 1.1.1 Kotlin

```kotlin
val videoView = findViewById<VideoView>(R.id.videoview)
var camera = Camera.open()
videoView.holder.addCallback(this)
```

##### 1.1.2 Java

```java
VideoView videoView = findViewById(R.id.videoview);
Camera camera = Camera.open();
SurfaceHolder holder = videoView.getHolder();
holder.addCallback(this);
```

#### 1.2 在 SurfaceHolder 的 surfaceCreated() 回调方法中设置相机预览

##### 1.2.1 Kotlin

```kotlin
override fun surfaceCreated(holder: SurfaceHolder) {
    Log.v(TAG, "in surfaceCreated")
    try {
        camera?.apply {
            setPreviewDisplay(mHolder)
            startPreview()
        }
    } catch (e : Exception) {
        Log.e(TAG, "Could not start the preview: ", e)
    }
}
```

##### 1.2.2 Java

```java
@Override
public void surfaceCreated(@NonNull SurfaceHolder holder) {
    Log.v(TAG, "in surfaceCreated");
    try {
        camera.setPreviewDisplay(mHolder);
        camera.startPreview();
    } catch (Exception e) {
        Log.e(TAG, "Could not start the preview: ", e);
    }
}
```

### 2. 录制视频

#### 2.1 创建 MediaRecorder 对象

在初始化 MediaRecorder 时，可以使用 CamcorderProfile 类配置视频参数，在再通过 MediaRecorder 的 setProfile() 方法传递给 MediaRecorder 对象。

##### 2.1.1 Kotlin

```kotlin
val fileName = Environment.getExternalStorageDirectory().absolutePath + "/videooutput.mp4"
val outFile = File(fileName)
if (outFile.exists()) {
    outFile.delete()
}

try {
    outFile.createNewFile()
    // 停止预览并解锁相机，允许 MediaRecorder 控制相机
    camera?.stopPreview()
    camera?.unlock()

   	var recorder = MediaRecorder()
    recorder?.apply {
        setCamera(camera)
        setAudioSource(MediaRecorder.AudioSource.CAMCORDER)
        setVideoSource(MediaRecorder.VideoSource.CAMERA)
        setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
        setVideoSize(176, 144)
        setVideoFrameRate(15)
        setVideoEncoder(MediaRecorder.VideoEncoder.MPEG_4_SP)
        setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB)
        setMaxDuration(7000)    // limit to 7 seconds
        setOutputFile(fileName)
        prepare()
    }
    Log.v(TAG, "MediaRecorder initialized")
} catch (e: Exception) {
    Log.e(TAG, "MediaRecorder failed to initialize: ", e)
}
```

##### 2.1.2 Java

```java
String fileName = Environment.getExternalStorageDirectory().getAbsolutePath() + "/videooutput.mp4";

File outFile = new File(fileName);
if (outFile.exists()) {
    outFile.delete();
}

try {
    outFile.createNewFile();
    // 停止预览并解锁相机，允许 MediaRecorder 控制相机
    camera.stopPreview();
    camera.unlock();
    MediaRecorder recorder = new MediaRecorder();
    recorder.setCamera(camera);

    recorder.setAudioSource(MediaRecorder.AudioSource.CAMCORDER);
    recorder.setVideoSource(MediaRecorder.VideoSource.CAMERA);
    recorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4);
    recorder.setVideoSize(176, 144);
    recorder.setVideoFrameRate(15);
    recorder.setVideoEncoder(MediaRecorder.VideoEncoder.MPEG_4_SP);
    recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
    recorder.setMaxDuration(7000); // limit to 7 seconds
    recorder.setOutputFile(fileName);

    recorder.prepare();
    Log.v(TAG, "MediaRecorder initialized");
} catch (Exception e) {
    Log.e(TAG, "MediaRecorder failed to initialize: ", e);
}
```

#### 2.2 开始录制

##### 2.2.1 Kotlin

```kotlin
recorder?.apply {
    setOnInfoListener(this@MainActivity)
    setOnErrorListener(this@MainActivity)
    start()
}

// OnInfoListener
override fun onInfo(mr: MediaRecorder?, what: Int, extra: Int) {
    Log.i(TAG, "got a recording event")
    if (what == MediaRecorder.MEDIA_RECORDER_INFO_MAX_DURATION_REACHED) {
        Log.i(TAG, "...max duration reached")
        stopRecording()
        Toast.makeText(this, "Recording limit has been reached. Stopping the recording", Toast.LENGTH_SHORT).show()
    }
}

// OnErrorListener
override fun onError(mr: MediaRecorder?, what: Int, extra: Int) {
    Log.e(TAG, "got a recording error")
    stopRecording()
    Toast.makeText(this, "Recording error has occurred. Stopping the recording", Toast.LENGTH_SHORT).show()
}
```

##### 2.2.2 Java

```java
mRecorder.setOnInfoListener(this);
mRecorder.setOnErrorListener(this);
mRecorder.start();

// OnInfoListener
@Override
public void onInfo(MediaRecorder mr, int what, int extra) {
    Log.i(TAG, "got a recording event");
    if (what == MediaRecorder.MEDIA_RECORDER_INFO_MAX_DURATION_REACHED) {
        Log.i(TAG, "...max duration reached");
        stopRecording();
        Toast.makeText(this, "Recording limit has been reached. Stopping the recording", Toast.LENGTH_SHORT).show();
    }
}

// OnErrorListener
@Override
public void onError(MediaRecorder mr, int what, int extra) {
    Log.e(TAG, "got a recording error");
    stopRecording();
    Toast.makeText(this, "Recording error has occurred. Stopping the recording", Toast.LENGTH_SHORT).show();
}
```

#### 2.3 停止录制

##### 2.3.1 Kotlin

```kotlin
recorder?.apply {
    setOnErrorListener(null)
    setOnInfoListener(null)
    try {
        stop()
    } catch (e: IllegalStateException) {
        // This can happen if the recorder has already stopped.
        Log.e(TAG, "Got IllegalStateException in stopRecording")
    }
}
releaseRecorder()
releaseCamera()
```

##### 2.3.2 Java

```java
if (recorder != null) {
    recorder.setOnErrorListener(null);
    recorder.setOnInfoListener(null);
    try {
        recorder.stop();
    } catch (IllegalStateException e) {
        // This can happen if the recorder has already stopped.
        Log.e(TAG, "Got IllegalStateException in stopRecording");
    }
    releaseRecorder();
    releaseCamera();
}
```

### 3. 一个完整示例代码

#### 3.1 Kotlin

```kotlin
import android.hardware.Camera
import android.media.MediaPlayer
import android.media.MediaRecorder
import android.os.Bundle
import android.os.Environment
import android.util.Log
import android.view.SurfaceHolder
import android.view.View
import android.widget.*

import androidx.appcompat.app.AppCompatActivity
import java.io.File
import java.lang.IllegalStateException
import kotlin.Exception

class MainActivity : AppCompatActivity(), SurfaceHolder.Callback, MediaRecorder.OnInfoListener,
    MediaRecorder.OnErrorListener {

    private lateinit var mVideoView: VideoView
    private lateinit var mInitBtn: Button
    private lateinit var mStartBtn: Button
    private lateinit var mStopBtn: Button
    private lateinit var mPlayBtn: Button
    private lateinit var mStopPlayBtn: Button
    private lateinit var mRecordingMsg: TextView

    private var mRecorder: MediaRecorder? = null
    private var mOutputFileName: String? = null
    private var mHolder: SurfaceHolder? = null
    private var mCamera: Camera? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.v(TAG, "in onCreate")

        mInitBtn = findViewById(R.id.initBtn)
        mStartBtn = findViewById(R.id.beginBtn)
        mStopBtn = findViewById(R.id.stopBtn)
        mPlayBtn = findViewById(R.id.playRecordingBtn)
        mStopPlayBtn = findViewById(R.id.stopPlayingRecordingBtn)
        mRecordingMsg = findViewById(R.id.recording)
        mVideoView = findViewById(R.id.videoView)
    }

    override fun onResume() {
        super.onResume()
        Log.v(TAG, "in onResume")
        mInitBtn.isEnabled = false
        mStartBtn.isEnabled = false
        mStopBtn.isEnabled = false
        mPlayBtn.isEnabled = false
        mStopPlayBtn.isEnabled = false
        if (!initCamera()) {
            finish()
        }
    }

    override fun onPause() {
        super.onPause()
        Log.v(TAG, "in onPause")
        releaseRecorder()
        releaseCamera()
    }

    private fun initCamera(): Boolean {
        try {
            mCamera = Camera.open()
            mCamera?.apply {
//                val camParam = parameters
                lock()
//                setDisplayOrientation(90)
                // Could also set other parameters here and apply using:
//                parameters = camParam

                mHolder = mVideoView.holder
                mHolder?.addCallback(this@MainActivity)
                mHolder?.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS)
            }
        } catch (e : Exception) {
            Log.e(TAG, "Could not initialize the Camera: ", e)
            return false
        }
        return true
    }

    override fun surfaceCreated(holder: SurfaceHolder) {
        Log.v(TAG, "in surfaceCreated")
        try {
            mCamera?.apply {
                setPreviewDisplay(mHolder)
                startPreview()
            }
        } catch (e : Exception) {
            Log.e(TAG, "Could not start the preview: ", e)
        }
        mInitBtn.isEnabled = true
    }

    override fun surfaceChanged(holder: SurfaceHolder, format: Int, width: Int, height: Int) {
        Log.v(TAG, "surfaceChanged: Width x Height = " + width + "x" + height)
    }

    override fun surfaceDestroyed(holder: SurfaceHolder) {
        Log.v(TAG, "in surfaceDestroyed")
    }

    private fun releaseRecorder() {
        mRecorder?.release()
        mRecorder = null
    }

    private fun releaseCamera() {
        try {
            mCamera?.reconnect()
        } catch (e: Exception) {
            Log.e(TAG, "releaseCamera=>error: ", e)
        }
        mCamera?.release()
        mCamera = null
    }

    public fun doClick(view: View) {
        when (view.id) {
            R.id.initBtn -> initRecorder()
            R.id.beginBtn -> beginRecording()
            R.id.stopBtn -> stopRecording()
            R.id.playRecordingBtn -> playRecording()
            R.id.stopPlayingRecordingBtn -> stopPlayingRecording()
        }
    }

    private fun initRecorder() {
        if (mRecorder != null) return

        mOutputFileName = Environment.getExternalStorageDirectory().absolutePath + "/videooutput.mp4"
        val outFile = File(mOutputFileName)
        if (outFile.exists()) {
            outFile.delete()
        }

        try {
            outFile.createNewFile()
            mCamera?.stopPreview()
            mCamera?.unlock()

            mRecorder = MediaRecorder()
            mRecorder?.apply {
                setCamera(mCamera)
                setAudioSource(MediaRecorder.AudioSource.CAMCORDER)
                setVideoSource(MediaRecorder.VideoSource.CAMERA)
                setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
                setVideoSize(176, 144)
                setVideoFrameRate(15)
                setVideoEncoder(MediaRecorder.VideoEncoder.MPEG_4_SP)
                setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB)
                setMaxDuration(7000)    // limit to 7 seconds
                setOutputFile(mOutputFileName)
                prepare()
            }
            Log.v(TAG, "MediaRecorder initialized")
            mInitBtn.isEnabled = false
            mStartBtn.isEnabled = true
        } catch (e: Exception) {
            Log.e(TAG, "MediaRecorder failed to initialize: ", e)
        }
    }

    private fun beginRecording() {
        mRecorder?.apply {
            setOnInfoListener(this@MainActivity)
            setOnErrorListener(this@MainActivity)
            start()
        }
        mRecordingMsg.text = "RECORDING"
        mStartBtn.isEnabled = false
        mStopBtn.isEnabled = true
    }

    private fun stopRecording() {
        mRecorder?.apply {
            setOnErrorListener(null)
            setOnInfoListener(null)
            try {
                stop()
            } catch (e: IllegalStateException) {
                // This can happen if the recorder has already stopped.
                Log.e(TAG, "Got IllegalStateException in stopRecording")
            }
        }
        releaseRecorder()
        mRecordingMsg.text = ""
        releaseCamera()
        mStartBtn.isEnabled = false
        mStopBtn.isEnabled = false
        mPlayBtn.isEnabled = true
    }

    private fun playRecording() {
        val mc = MediaController(this)
        mVideoView.setMediaController(mc)
        mVideoView.setVideoPath(mOutputFileName)
        mVideoView.setOnCompletionListener(object: MediaPlayer.OnCompletionListener {
            override fun onCompletion(mp: MediaPlayer?) {
                mPlayBtn.isEnabled = true
                mStopPlayBtn.isEnabled = false
            }
        })
        mVideoView.start()
        mPlayBtn.isEnabled = false
        mStopPlayBtn.isEnabled = true
    }

    override fun onInfo(mr: MediaRecorder?, what: Int, extra: Int) {
        Log.i(TAG, "got a recording event")
        if (what == MediaRecorder.MEDIA_RECORDER_INFO_MAX_DURATION_REACHED) {
            Log.i(TAG, "...max duration reached")
            stopRecording()
            Toast.makeText(this, "Recording limit has been reached. Stopping the recording", Toast.LENGTH_SHORT).show()
        }
    }

    override fun onError(mr: MediaRecorder?, what: Int, extra: Int) {
        Log.e(TAG, "got a recording error")
        stopRecording()
        Toast.makeText(this, "Recording error has occurred. Stopping the recording", Toast.LENGTH_SHORT).show()
    }

    private fun stopPlayingRecording() {
        mVideoView.stopPlayback()
        mPlayBtn.isEnabled = true
        mStopPlayBtn.isEnabled = false
    }

    companion object {
        const val TAG = "qty"
    }
}
```

#### 3.2 Java

```java
import android.hardware.Camera;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.SurfaceHolder;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.VideoView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import java.io.File;

public class MainActivity extends AppCompatActivity implements SurfaceHolder.Callback, MediaRecorder.OnInfoListener, MediaRecorder.OnErrorListener {

    private static final String TAG = "qty";

    private MediaRecorder mRecorder;
    private String mOutputFileName;
    private VideoView mVideoView;
    private SurfaceHolder mHolder;
    private Button mInitBtn;
    private Button mStartBtn;
    private Button mStopBtn;
    private Button mPlayBtn;
    private Button mStopPlayBtn;
    private Camera mCamera;
    private TextView mRecordingMsg = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.v(TAG, "in onCreate");
        setContentView(R.layout.activity_main);

        mInitBtn = findViewById(R.id.initBtn);
        mStartBtn = findViewById(R.id.beginBtn);
        mStopBtn = findViewById(R.id.stopBtn);
        mPlayBtn = findViewById(R.id.playRecordingBtn);
        mStopPlayBtn = findViewById(R.id.stopPlayingRecordingBtn);
        mRecordingMsg = findViewById(R.id.recording);
        mVideoView = findViewById(R.id.videoView);
    }

    @Override
    protected void onResume() {
        Log.v(TAG, "in onResume");
        super.onResume();
        mInitBtn.setEnabled(false);
        mStartBtn.setEnabled(false);
        mStopBtn.setEnabled(false);
        mPlayBtn.setEnabled(false);
        mStopPlayBtn.setEnabled(false);
        if (!initCamera()) {
            finish();
        }
    }

    @Override
    protected void onPause() {
        Log.v(TAG, "in onPause");
        super.onPause();
        releaseRecorder();
        releaseCamera();
    }

    private boolean initCamera() {
        try {
            mCamera = Camera.open();
            Camera.Parameters camParams = mCamera.getParameters();
            mCamera.lock();
//            mCamera.setDisplayOrientation(90);
            // Could also set other parameters here and apply using:
//            mCamera.setParameters(camParams);

            mHolder = mVideoView.getHolder();
            mHolder.addCallback(this);
            mHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
        } catch (Exception e) {
            Log.e(TAG, "Could not initialize the Camera: ", e);
            return false;
        }
        return true;
    }

    @Override
    public void surfaceCreated(@NonNull SurfaceHolder holder) {
        Log.v(TAG, "in surfaceCreated");
        try {
            mCamera.setPreviewDisplay(mHolder);
            mCamera.startPreview();
        } catch (Exception e) {
            Log.e(TAG, "Could not start the preview: ", e);
        }
        mInitBtn.setEnabled(true);
    }

    @Override
    public void surfaceChanged(@NonNull SurfaceHolder holder, int format, int width, int height) {
        Log.v(TAG, "surfaceChanged: Width x Height = " + width + "x" + height);
    }

    @Override
    public void surfaceDestroyed(@NonNull SurfaceHolder holder) {
        Log.v(TAG, "in surfaceDestroyed");
    }

    private void releaseRecorder() {
        if (mRecorder != null) {
            mRecorder.release();
            mRecorder = null;
        }
    }

    private void releaseCamera() {
        if (mCamera != null) {
            try {
                mCamera.reconnect();
            } catch (Exception e) {
                Log.e(TAG, "releaseCamera=>error: ", e);
            }
            mCamera.release();
            mCamera = null;
        }
    }

    public void doClick(View view) {
        switch (view.getId()) {
            case R.id.initBtn:
                initRecorder();
                break;

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
    }

    private void initRecorder() {
        if (mRecorder != null) return;

        mOutputFileName = Environment.getExternalStorageDirectory().getAbsolutePath() + "/videooutput.mp4";

        File outFile = new File(mOutputFileName);
        if (outFile.exists()) {
            outFile.delete();
        }

        try {
            outFile.createNewFile();
            mCamera.stopPreview();
            mCamera.unlock();
            mRecorder = new MediaRecorder();
            mRecorder.setCamera(mCamera);

            mRecorder.setAudioSource(MediaRecorder.AudioSource.CAMCORDER);
            mRecorder.setVideoSource(MediaRecorder.VideoSource.CAMERA);
            mRecorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4);
            mRecorder.setVideoSize(176, 144);
            mRecorder.setVideoFrameRate(15);
            mRecorder.setVideoEncoder(MediaRecorder.VideoEncoder.MPEG_4_SP);
            mRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
            mRecorder.setMaxDuration(7000); // limit to 7 seconds
            mRecorder.setOutputFile(mOutputFileName);

            mRecorder.prepare();
            Log.v(TAG, "MediaRecorder initialized");
            mInitBtn.setEnabled(false);
            mStartBtn.setEnabled(true);
        } catch (Exception e) {
            Log.e(TAG, "MediaRecorder failed to initialize: ", e);
        }
    }

    private void beginRecording() {
        mRecorder.setOnInfoListener(this);
        mRecorder.setOnErrorListener(this);
        mRecorder.start();
        mRecordingMsg.setText("RECORDING");
        mStartBtn.setEnabled(false);
        mStopBtn.setEnabled(true);
    }

    private void stopRecording() {
        if (mRecorder != null) {
            mRecorder.setOnErrorListener(null);
            mRecorder.setOnInfoListener(null);
            try {
                mRecorder.stop();
            } catch (IllegalStateException e) {
                // This can happen if the recorder has already stopped.
                Log.e(TAG, "Got IllegalStateException in stopRecording");
            }
            releaseRecorder();
            mRecordingMsg.setText("");
            releaseCamera();
            mStartBtn.setEnabled(false);
            mStopBtn.setEnabled(false);
            mPlayBtn.setEnabled(true);
        }
    }

    private void playRecording() {
        MediaController mc = new MediaController(this);
        mVideoView.setMediaController(mc);
        mVideoView.setVideoPath(mOutputFileName);
        mVideoView.setOnCompletionListener((mp) -> {
            mPlayBtn.setEnabled(true);
            mStopPlayBtn.setEnabled(false);
        });
        mVideoView.start();
        mPlayBtn.setEnabled(false);
        mStopPlayBtn.setEnabled(true);
    }

    private void stopPlayingRecording() {
        mVideoView.stopPlayback();
        mPlayBtn.setEnabled(true);
        mStopPlayBtn.setEnabled(false);
    }

    @Override
    public void onInfo(MediaRecorder mr, int what, int extra) {
        Log.i(TAG, "got a recording event");
        if (what == MediaRecorder.MEDIA_RECORDER_INFO_MAX_DURATION_REACHED) {
            Log.i(TAG, "...max duration reached");
            stopRecording();
            Toast.makeText(this, "Recording limit has been reached. Stopping the recording", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onError(MediaRecorder mr, int what, int extra) {
        Log.e(TAG, "got a recording error");
        stopRecording();
        Toast.makeText(this, "Recording error has occurred. Stopping the recording", Toast.LENGTH_SHORT).show();
    }
}
```

#### 3.3 Layout

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <Button
            android:id="@+id/initBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Initialize Recorder"
            android:onClick="doClick"
            android:enabled="false" />

        <Button
            android:id="@+id/beginBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Begin Recording"
            android:onClick="doClick"
            android:enabled="false" />

        <Button
            android:id="@+id/stopBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Stop Recording"
            android:onClick="doClick" />

        <Button
            android:id="@+id/playRecordingBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Play Recording"
            android:onClick="doClick" />

        <Button
            android:id="@+id/stopPlayingRecordingBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Stop Playing"
            android:onClick="doClick" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <TextView
            android:id="@+id/recording"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textColor="#FF0000"
            android:text=" " />

        <VideoView
            android:id="@+id/videoView"
            android:layout_width="250dip"
            android:layout_height="200dip" />
    </LinearLayout>

</LinearLayout>
```

