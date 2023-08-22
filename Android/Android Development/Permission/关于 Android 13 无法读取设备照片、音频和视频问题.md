在 `Android 13` 系统中，应用添加了读写外部存储权限后，在读取照片、音频和视频文件时还是报权限错误问题：

```xml
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

这是因为 `Android 13` 系统为读取照片、音频和视频文件单独提供了各种的权限：

```xml
<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
<uses-permission android:name="android.permission.READ_MEDIA_AUDIO" />
<uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />
```

并且在 `Android 13` 系统中，读写外部存储权限已经变成了默认赋予状态，因此在请求权限时，只需在 `AndroidManifest.xml` 文件中添加权限即可，不再需要在代码中使用 `requestPermissions()` 方法申请该权限了。