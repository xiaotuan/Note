[toc]

> 摘自：<https://blog.csdn.net/chenxue843400447/article/details/86689583>

调用系统相机时,系统会抛出 `FileUriExposedException` 这个错误.具体堆栈信息如下:

```
2021-09-07 10:25:45.457 7425-7425/com.qty.androidtest E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.qty.androidtest, PID: 7425
    android.os.FileUriExposedException: file:///storage/emulated/0/Android/data/com.qty.androidtest/files/DCIM/test.jpg exposed beyond app through ClipData.Item.getUri()
        at android.os.StrictMode.onFileUriExposed(StrictMode.java:2141)
        at android.net.Uri.checkFileUriExposed(Uri.java:2391)
        at android.content.ClipData.prepareToLeaveProcess(ClipData.java:964)
        at android.content.Intent.prepareToLeaveProcess(Intent.java:11130)
        at android.content.Intent.prepareToLeaveProcess(Intent.java:11115)
        at android.app.Instrumentation.execStartActivity(Instrumentation.java:1722)
        at android.app.Activity.startActivityForResult(Activity.java:5383)
        at androidx.fragment.app.FragmentActivity.startActivityForResult(FragmentActivity.java:676)
        at android.app.Activity.startActivityForResult(Activity.java:5341)
        at androidx.fragment.app.FragmentActivity.startActivityForResult(FragmentActivity.java:663)
        at com.qty.androidtest.MainActivity$1.onClick(MainActivity.java:45)
        at android.view.View.performClick(View.java:7503)
        at com.google.android.material.button.MaterialButton.performClick(MaterialButton.java:992)
        at android.view.View.performClickInternal(View.java:7480)
        at android.view.View.access$3600(View.java:813)
        at android.view.View$PerformClick.run(View.java:28445)
        at android.os.Handler.handleCallback(Handler.java:938)
        at android.os.Handler.dispatchMessage(Handler.java:99)
        at android.os.Looper.loop(Looper.java:223)
        at android.app.ActivityThread.main(ActivityThread.java:7943)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:603)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:947)
```

### 7.0之前

```java
Uri pothoUri = Uri.fromFile(getSavePhotoPath());

private File getSavePhotoPath() {
        String photoFile = getExternalFilesDir(Environment.DIRECTORY_PICTURES)+ "/camera" + System.currentTimeMillis() + ".jpg";
        File file = new File(photoFile);
        if(!file.getParentFile().exists()){
            file.getParentFile().mkdirs();
        }
        return file;
    }
```

### 7.0之后

如果继续这样使用就会报 `android.os.FileUriExposedException` 错误，`Android` 不再允许在 `app` 中把 `file://Uri` 暴露给其他 app，包括但不局限于通过 `Intent` 或 `ClipData` 等方法。

原因在于使用 `file://Uri` 会有一些风险，比如：

文件是私有的，接收 `file://Uri` 的 app 无法访问该文件。
在 `Android6.0` 之后引入运行时权限，如果接收 `file://Uri` 的 app 没有申请`READ_EXTERNAL_STORAGE` 权限，在读取文件时会引发崩溃。
因此，google 提供了 `FileProvider`，使用它可以生成 `content://Uri` 来替代 `file://Uri` 。 

其中 education_system 可自己随意，但保证唯一。需要与AndroidManifest.xml中的provider  authorities保持一样：

```java
Uri pothoUri = FileProvider.getUriForFile(this,"education_system",getSavePhotoPath());
```

在 `AndroidManifest.xml` 添加 provider ：

```xml
<provider
            android:authorities="education_system"
            android:name="android.support.v4.content.FileProvider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/provider_paths"/>
        </provider>
```

+ `android:authorities`：用来标识 provider
+ `android:exported` : 是否支持其它应用调用当前组件。 默认为 false
+ `android:grantUriPermissions` ： 用来控制共享文件的访问权限，也可以在 java 代码中设置。

需要在 `res`下建立 `xml/provider_path.xml`

**provider_paths.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <external-path name="external_files" path="."/>
</paths>
```

`<paths>` 中可以定义以下节点:

| 子节点 | 对应路径 |
| :- | :- |
| files-path | Context.getFilesDir() |
| cache-path | Context.getCacheDir() |
| external-cache-path | Context.getExternalCacheDir() |
| external-files-path | Context.getExternalFilesDir(null) |
| external-path | Environment.getExternalStorageDirectory() |

### `file://` 到 `content://` 的转换规则

+ 替换前缀：把 `file://` 替换成 `content://${android:authorities}`。
+ 匹配和替换
	+ 遍历 `<paths>` 的子节点，找到最大能匹配上文件路径前缀的那个子节点。
	+ 用 path 的值替换掉文件路径里所匹配的内容。
+ 文件路径剩余的部分保持不变。