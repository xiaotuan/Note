[toc]

> 提示：示例代码请查阅 <https://gitee.com/qtyresources/ProAndroidMedia>  中的 SnapShot 示例程序。

### 1. 添加权限

拍照需要如下权限：

```
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

### 2. 定义用于相机预览的控件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <SurfaceView
        android:id="@+id/CameraView"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

### 3. 实现代码

#### 3.1 Kotlin 版本

```kotlin
package com.apress.proandroidmedia.ch2.snapshot

import android.content.ContentValues
import android.content.res.Configuration
import android.hardware.Camera
import android.net.Uri
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.util.Log
import android.view.SurfaceHolder
import android.view.SurfaceView
import android.view.View

class SnapShot : AppCompatActivity(), SurfaceHolder.Callback, View.OnClickListener,
    Camera.PictureCallback {

    private lateinit var cameraView: SurfaceView
    private lateinit var  surfaceHolder: SurfaceHolder
    private var camera: Camera? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        cameraView = findViewById(R.id.CameraView)
        surfaceHolder = cameraView.holder
        surfaceHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS)
        surfaceHolder.addCallback(this)

        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) {
            cameraView.isFocusable = true
        } else {
            cameraView.focusable = View.FOCUSABLE
        }
        cameraView.isFocusableInTouchMode = true
        cameraView.isClickable = true

        cameraView.setOnClickListener(this)
    }

    override fun surfaceCreated(holder: SurfaceHolder) {
        camera = Camera.open(0)
        Log.d(TAG, "surfaceCreated=>camera: $camera")
        camera?.let {
            Log.d(TAG, "surfaceCreated=>setPreviewDisplay")
            val parameters = it.parameters
            it.setPreviewDisplay(holder)
            if (resources.configuration.orientation != Configuration.ORIENTATION_LANDSCAPE) {
                parameters["orientation"] = "portrait"

                // For Android Version 2.2 and above
                it.setDisplayOrientation(90)

                // For Android Version 2.0 and above
                parameters.setRotation(90)
            }

            // Effects are for Android Version 2.0 and higher
            val colorEffects = parameters.supportedColorEffects
            val iterable = colorEffects.iterator()
            while (iterable.hasNext()) {
                val currentEffect = iterable.next()
                if (currentEffect.equals(Camera.Parameters.EFFECT_SOLARIZE)) {
                    parameters.colorEffect = Camera.Parameters.EFFECT_SOLARIZE
                    break
                }
            }
            // End Effects for Android Version 2.0 and highter

            it.parameters = parameters
        }
    }

    override fun surfaceChanged(holder: SurfaceHolder, format: Int, width: Int, height: Int) {
        Log.d(TAG, "surfaceChanged...")
        camera?.startPreview()
    }

    override fun surfaceDestroyed(holder: SurfaceHolder) {
        Log.d(TAG, "surfaceDestroyed...")
        camera?.stopPreview()
        camera?.release()
    }

    override fun onClick(v: View?) {
        camera?.autoFocus(Camera.AutoFocusCallback() {
            success: Boolean, camera: Camera? ->
            if (success) {
                camera?.takePicture(null, null, this)
            }
        })
    }

    override fun onPictureTaken(data: ByteArray?, camera: Camera?) {
        data?.let {
            val imageFileUri = contentResolver.insert(
                MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
                ContentValues()
            )

            imageFileUri?.let { uri ->
                val imageFileOS = contentResolver.openOutputStream(uri)
                imageFileOS?.let {  os ->
                    os.write(it)
                    os.flush()
                    os.close()
                }
            }
        }
        camera?.startPreview()
    }

    companion object {
        const val TAG = "SnapShot"
    }
}
```

#### 3.2 Java 版本

```java
package com.apress.proandroidmedia.ch2.snapshot;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.res.Configuration;
import android.hardware.Camera;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.widget.Toast;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Iterator;
import java.util.List;

public class SnapShot extends AppCompatActivity implements SurfaceHolder.Callback, View.OnClickListener, Camera.PictureCallback {

    private static final String TAG = "SnapShot";

    private SurfaceView cameraView;
    private SurfaceHolder surfaceHolder;
    private Camera camera;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cameraView = findViewById(R.id.CameraView);
        surfaceHolder = cameraView.getHolder();
        surfaceHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
        surfaceHolder.addCallback(this);

        cameraView.setFocusable(true);
        cameraView.setFocusableInTouchMode(true);
        cameraView.setClickable(true);

        cameraView.setOnClickListener(this);
    }

    @Override
    public void surfaceCreated(@NonNull SurfaceHolder holder) {
        camera = Camera.open();
        try {
            camera.setPreviewDisplay(holder);
            Camera.Parameters parameters = camera.getParameters();
            if (getResources().getConfiguration().orientation != Configuration.ORIENTATION_LANDSCAPE) {
                parameters.set("orientation", "portrait");

                // For Android Version 2.2 and above
                camera.setDisplayOrientation(90);

                // For Android Version 2.0 and above
                parameters.setRotation(90);
            }

            // Effects are for Android Version 2.0 and higher
            List<String> colorEffects = parameters.getSupportedColorEffects();
            Iterator<String> cei = colorEffects.iterator();
            while (cei.hasNext()) {
                String currentEffect =cei.next();
                if (currentEffect.equals(Camera.Parameters.EFFECT_SOLARIZE)) {
                    parameters.setColorEffect(Camera.Parameters.EFFECT_SOLARIZE);
                    break;
                }
            }
            // End Effects for Android Version 2.0 and higher

            camera.setParameters(parameters);
        } catch (IOException e) {
            Log.d(TAG, "surfaceCreated=>error: ", e);
            camera.release();
        }
    }

    @Override
    public void surfaceChanged(@NonNull SurfaceHolder holder, int format, int width, int height) {
        camera.startPreview();
    }

    @Override
    public void surfaceDestroyed(@NonNull SurfaceHolder holder) {
        camera.stopPreview();
        camera.release();
    }

    @Override
    public void onClick(View v) {
        camera.autoFocus(new Camera.AutoFocusCallback() {
            @Override
            public void onAutoFocus(boolean success, Camera camera) {
                if (success) {
                    camera.takePicture(null, null, SnapShot.this);
                }
            }
        });
    }

    @Override
    public void onPictureTaken(byte[] data, Camera camera) {
        Uri imageFileUri = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, new ContentValues());
        try {
            OutputStream imageFileOS = getContentResolver().openOutputStream(imageFileUri);
            imageFileOS.write(data);
            imageFileOS.flush();
            imageFileOS.close();
        } catch (FileNotFoundException e) {
            Toast.makeText(this, e.getMessage(), Toast.LENGTH_SHORT).show();
        } catch (IOException e) {
            Toast.makeText(this, e.getMessage(), Toast.LENGTH_SHORT).show();
        }
        camera.startPreview();
    }
}
```

### 4. 注意

+ `SurfaceHolder` 类的 `setType()` 方法已经过时，新版本的 `SurfaceHolder` 类已经自动管理缓冲区了。
