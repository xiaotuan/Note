在 Android SDK 大于或等于 24 时，使用如下代码封装 Uri 对象并使用该对象：

```java
Uri imageFileUri = Uri.fromFile(new File(picturePath));
Intent i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
i.putExtra(MediaStore.EXTRA_OUTPUT, imageFileUri);
startActivityForResult(i, CAMERA_RESULT);
```

时会报如下错误：

```
android.os.FileUriExposedException: file:///storage/emulated/0/Android/data/com.apress.proandroidmedia.ch1.fileprovidercameraintent/files/Pictures/test.jpg exposed beyond app through ClipData.Item.getUri()
```

解决方法如下所示：

参照 《[FileProvider 使用说明](./FileProvider 使用说明.md)》说明封装 Uri。

