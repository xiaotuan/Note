[toc]

> 提示：示例代码请查阅 <https://gitee.com/qtyresources/ProAndroidMedia>  中的 FileProviderCameraIntent示例程序。

### 1. 在 `res/xml` 中创建 FileProvider 的文件路径配置文件

**file_paths.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <files-path
        name="files"
        path="/" />
    <cache-path
        name="cache"
        path="/" />
    <external-cache-path
        name="external_cache"
        path="/" />
    <external-files-path
        name="external_files"
        path="/" />
    <external-media-path
        name="external_media"
        path="/" />
    <external-path
        name="external"
        path="/" />
</paths>
```

这里主要对几个路径做个概括：

+ **root-path**：`root-path` 对应 `device_root` , 也就是 `File file = new File("/")`，即根目录,一般不需要配置。
+ **files-path**：对应 `content.getFileDir()` 获取到的目录。
+ **cache-path**：对应 `content.getCacheDir()` 获取到的目录
+ **external-path**：对应 `Environment.getExternalStorageDirectory()` 指向的目录。
+ **external-files-path**：对应 `ContextCompat.getExternalFilesDirs()` 获取到的目录。
+ **external-cache-path**：对应 `ContextCompat.getExternalCacheDirs()` 获取到的目录。

对应关系如下表：

| TAG | Value | Path |
| :- | :- | :- |
| TAG_ROOT_PATH | root-path | / |
|TAG_FILES_PATH | files-path | /data/data/\<包名\>/files |
| TAG_CACHE_PATH | cache-path | /data/data/\<包名\>/cache |
| TAG_EXTERNAL | external-path | /storage/emulate/0 |
| TAG_EXTERNAL_FILES | external-files-path | /storage/emulate/0/Android/data/\<包名\>/files |
| TAG_EXTERNAL_CACHE | external-cache-path | /storage/emulate/0/Android/data/\<包名\>/cache |

### 2. 在 AndroidManifest.xml 中添加 FileProvider 声明

在 `application` 节点中添加如下声明：

```xml
<provider
          android:authorities="com.apress.proandroidmedia.ch1.fileprovidercameraintent.FileProvider"
          android:name="androidx.core.content.FileProvider"
          android:exported="false"
          android:grantUriPermissions="true">
    <meta-data
               android:name="android.support.FILE_PROVIDER_PATHS"
               android:resource="@xml/file_paths" />
</provider>
```

