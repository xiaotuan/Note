[toc]

### 1. 测试命令

```shell
$ run cts -t CtsAppTestCases -m ndroid.app.cts.SystemFeaturesTest#testCameraFeatures
```

### 2. 错误列表

#### 2.1 相机不支持自动对焦功能

1. 报错信息

   ```
   java.lang.AssertionError: PackageManager#hasSystemFeature should return true for android.hardware.camera.autofocus
   ```

2. 问题分析

   设备相机不支持自动对焦功能，需要去掉自动对焦功能。

3. 解决方法

   **3.1 MTK8766、Android O**

   去掉自动对焦功能，修改 `device/mediateksample/m863u_bsp_64/android.hardware.camera.xml` 文件，去掉文件中的如下内容：

   ```xml
   <feature name="android.hardware.camera.autofocus" />
   ```

   