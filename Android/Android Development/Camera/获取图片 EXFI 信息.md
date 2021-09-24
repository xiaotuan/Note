[toc]

下面以获取图片方向为例，代码如下所示：

### 1. Kotlin 版本

```kotlin
```

### 2. Java 版本

```java
private int getExifOrientation(String path) {
    int degree = 0;

    try {
        ExifInterface exif = new ExifInterface(path);
        int orientation = exif.getAttributeInt(ExifInterface.TAG_ORIENTATION, -1);
        switch (orientation) {
            case ExifInterface.ORIENTATION_ROTATE_90:
                degree = 90;
                break;

            case ExifInterface.ORIENTATION_ROTATE_180:
                degree = 180;
                break;

            case ExifInterface.ORIENTATION_ROTATE_270:
                degree = 270;
                break;
        }
    } catch (IOException e) {
        Log.d(TAG, "getExifOrientation=>error: ", e);
    }

    return degree;
}
```

