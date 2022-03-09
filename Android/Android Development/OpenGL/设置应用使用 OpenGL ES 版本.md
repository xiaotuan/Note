可以在 AndroidManifest.xml 文件中使用 `<uses-feature>` 设置应用需要的 OpenGL ES 版本，例如：

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.android.kotlintest">
    
    ...
    
    <uses-feature android:glEsVersion="0x00020000" />
    
    <application ...>
        ...
    </application>
    
</manifest>
```

