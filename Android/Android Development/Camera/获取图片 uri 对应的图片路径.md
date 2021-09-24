[toc]

当应用通过如下方法获取图片：

**Kotlin 版本**

```kotlin
```

**Java 版本**

```java
Intent choosePictureIntent = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
startActivityForResult(choosePictureIntent, 0);
```

系统将会通过 `URI` 的方式返回用户选择的图片，这时可以同如下方法获取这个 `URI` 对应的文件路径：

### 1. Kotlin 版本

```kotlin
```

### 2. Java 版本

```java
private String getPicturePath(Uri pictureUri) {
    String path = null;
    Cursor c = getContentResolver().query(pictureUri, new String[]{MediaStore.Images.Media.DATA }, null, null, null);
    if (c.moveToFirst()) {
        path = c.getString(c.getColumnIndexOrThrow(MediaStore.Images.Media.DATA));
    }
    return path;
}
```



