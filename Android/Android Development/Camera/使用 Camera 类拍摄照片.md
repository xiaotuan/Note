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

### 3. 添加 SurfaceHolder 的 Callback

#### 3.1 Kotlin 版本

```kotlin
private lateinit var cameraView: SurfaceView

cameraView = findViewById(R.id.CameraView)
cameraView.holder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS)
cameraView.holder.addCallback(this)
```

#### 3.2 Java 版本

```java
cameraView = findViewById(R.id.CameraView);
surfaceHolder = cameraView.getHolder();
surfaceHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
surfaceHolder.addCallback(this);
```

### 4. 实现 SurfaceHolder 的 Callback 方法

在 `surfaceCreated()` 方法中初始化 `Camera` 对象，在 `surfaceChanged()` 方法中开始预览，在 `surfaceDestroyed()` 方法中停止预览，并释放 `Camera` 对象。

#### 4.1 Kotlin 版本

```kotlin
override fun surfaceCreated(holder: SurfaceHolder) {
    // 打开相机
    camera = Camera.open(0)
    Log.d(TAG, "surfaceCreated=>camera: $camera")
    camera?.let {
        Log.d(TAG, "surfaceCreated=>setPreviewDisplay")
        val parameters = it.parameters
        // 设置相机预览界面
        it.setPreviewDisplay(holder)
        var rotation = 0
        when (windowManager.defaultDisplay.rotation) {
            Surface.ROTATION_0 -> {
                rotation = 90
            }
            Surface.ROTATION_180 -> {
                rotation = 270
            }
            Surface.ROTATION_270 -> {
                rotation = 180
            }
            Surface.ROTATION_90 -> {
                rotation = 0
            }
        }
        // 设置相机方向
        parameters.set("rotation", rotation)
        parameters.setRotation(rotation)
        it.setDisplayOrientation(rotation)

        // 设置持续自动对焦
        parameters.focusMode = Camera.Parameters.FOCUS_MODE_CONTINUOUS_PICTURE

        // 设置相机参数
        it.parameters = parameters
    }
}

override fun surfaceChanged(holder: SurfaceHolder, format: Int, width: Int, height: Int) {
    Log.d(TAG, "surfaceChanged...")
    camera?.let {
        val parameters = it.parameters
        var rotation = 0
        when (windowManager.defaultDisplay.rotation) {
            Surface.ROTATION_0 -> {
                rotation = 90
            }
            Surface.ROTATION_180 -> {
                rotation = 270
            }
            Surface.ROTATION_270 -> {
                rotation = 180
            }
            Surface.ROTATION_90 -> {
                rotation = 0
            }
        }
        // 设置相机预览方向
        parameters.set("rotation", rotation)
        parameters.setRotation(rotation)
        it.setDisplayOrientation(rotation)
        it.parameters = parameters
        // 开始预览
        it.startPreview()
    }
}

override fun surfaceDestroyed(holder: SurfaceHolder) {
    Log.d(TAG, "surfaceDestroyed...")
    // 停止预览
    camera?.stopPreview()
    // 释放相机
    camera?.release()
    camera = null
}
```

#### 4.2 Java 版本

```java
@Override
public void surfaceCreated(@NonNull SurfaceHolder holder) {
    camera = Camera.open();
    try {
        camera.setPreviewDisplay(holder);
        Camera.Parameters parameters = camera.getParameters();
        int rotation = getWindowManager().getDefaultDisplay().getRotation();
        Log.d(TAG, "surfaceCreated=>rotation: " + rotation);
        switch (rotation) {
            case Surface.ROTATION_0:
                rotation = 90;
                break;

            case Surface.ROTATION_90:
                rotation = 0;
                break;

            case Surface.ROTATION_180:
                rotation = 270;
                break;

            case Surface.ROTATION_270:
                rotation = 180;
                break;
        }
        parameters.set("rotaion", rotation);
        parameters.setRotation(rotation);
        camera.setDisplayOrientation(rotation);
        parameters.setFocusMode(Camera.Parameters.FOCUS_MODE_CONTINUOUS_PICTURE);

        camera.setParameters(parameters);
    } catch (IOException e) {
        Log.d(TAG, "surfaceCreated=>error: ", e);
        if (camera != null) {
            camera.release();
        }
    }
}

@Override
public void surfaceChanged(@NonNull SurfaceHolder holder, int format, int width, int height) {
    if (camera == null) {
        return;
    }
    Camera.Parameters parameters = camera.getParameters();
    int rotation = getWindowManager().getDefaultDisplay().getRotation();
    Log.d(TAG, "surfaceCreated=>rotation: " + rotation);
    switch (rotation) {
        case Surface.ROTATION_0:
            rotation = 90;
            break;

        case Surface.ROTATION_90:
            rotation = 0;
            break;

        case Surface.ROTATION_180:
            rotation = 270;
            break;

        case Surface.ROTATION_270:
            rotation = 180;
            break;
    }
    parameters.set("rotaion", rotation);
    parameters.setRotation(rotation);
    camera.setDisplayOrientation(rotation);
    camera.setParameters(parameters);
    camera.startPreview();
}

@Override
public void surfaceDestroyed(@NonNull SurfaceHolder holder) {
    if (camera != null) {
        camera.stopPreview();
        camera.release();
        camera = null;
    }
}
```

### 5. 实现拍照回调

#### 5.1 Kotlin 版本

```kotlin
override fun onPictureTaken(data: ByteArray?, camera: Camera?) {
    data?.let { d ->
               // 获取保存图片的 Uri
               val imageFileUri = contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, ContentValues())
               // 通过 uri 获取输出流
               val imageFileOS = imageFileUri?.let { contentResolver.openOutputStream(it) }
               // 以照片数据构建 Bitmap 对象
               var bmp = BitmapFactory.decodeByteArray(d, 0, d.size)
               // 创建变形对象
               val matrix = Matrix()
               // 设置旋转角度
               matrix.setRotate(rotation.toFloat())
               // 应用变形
               bmp = Bitmap.createBitmap(bmp, 0, 0, bmp.width, bmp.height, matrix, true)
               // 将 Bitmap 对象写入输出流
               bmp.compress(Bitmap.CompressFormat.JPEG, 100, imageFileOS)
               imageFileOS?.flush()
               imageFileOS?.close()
               Toast.makeText(this, "Saved JPEG!", Toast.LENGTH_SHORT).show()
              }
    camera?.startPreview()
}
```

#### 5.2 Java 版本

```java
@Override
public void onPictureTaken(byte[] data, Camera camera) {
    Uri imageFileUri = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, new ContentValues());

    try {
        OutputStream imageFileOS = getContentResolver().openOutputStream(imageFileUri);
        Bitmap bmp = BitmapFactory.decodeByteArray(data, 0, data.length);
        Matrix matrix = new Matrix();
        matrix.setRotate(rotation);
        bmp = Bitmap.createBitmap(bmp, 0, 0, bmp.getWidth(), bmp.getHeight(), matrix, true);
        bmp.compress(Bitmap.CompressFormat.JPEG, 100, imageFileOS);
        imageFileOS.flush();
        imageFileOS.close();

        Toast.makeText(this, "Saved JPEG!", Toast.LENGTH_SHORT).show();
    } catch (FileNotFoundException e) {
        Log.e(TAG, "onPictureTaken=>File not found.", e);
    } catch (IOException e) {
        Log.e(TAG, "onPictureTaken=>Write data error.", e);
    }

    if (camera != null) {
        camera.startPreview();
    }
}
```

### 6. 拍照

#### 6.1 Kotlin 版本

```kotlin
camera?.let {
    // 获取照片方向，用于在保存图片时，旋转图片
    when (windowManager.defaultDisplay.rotation) {
        Surface.ROTATION_0 -> {
            rotation = 90
        }
        Surface.ROTATION_180 -> {
            rotation = 270
        }
        Surface.ROTATION_270 -> {
            rotation = 180
        }
        Surface.ROTATION_90 -> {
            rotation = 0
        }
    }
    // 拍照
    it.takePicture(null, null, null, this)
}
```

#### 6.2 Java 版本

```java
if (camera != null) {
    rotation = getWindowManager().getDefaultDisplay().getRotation();
    Log.d(TAG, "onClick=>rotation: " + rotation);
    switch (rotation) {
        case Surface.ROTATION_0:
            rotation = 90;
            break;

        case Surface.ROTATION_90:
            rotation = 0;
            break;

        case Surface.ROTATION_180:
            rotation = 270;
            break;

        case Surface.ROTATION_270:
            rotation = 180;
            break;
    }
    camera.takePicture(null, null, null, this);
}
```
