在拍摄照片后，大多数时候图片的方向都是不正确的，可以通过将图片的方向信息写入图片文件中来解决，下面就是将图片方向写入图片的 EXFI 信息中，代码如下所示：

### 1. Kotlin 版本

```kotlin
```

### 2. Java 版本

```java
private void setExifOrientation(String path, int orientation) {
    try {
        ExifInterface exif = new ExifInterface(path);
        exif.setAttribute(ExifInterface.TAG_ORIENTATION, orientation + "");
        exif.saveAttributes();
    } catch (IOException e) {
        Log.e(TAG, "setExifOrientation=>error: ", e);
    }
}
```

