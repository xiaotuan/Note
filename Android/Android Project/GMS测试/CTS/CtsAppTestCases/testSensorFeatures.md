[toc]

### 1. 测试命令

```shell
$ run cts -t CtsAppTestCases -m android.app.cts.SystemFeaturesTest#testSensorFeatures
```

### 2 错误列表

#### 2.1 没有指南针传感器功能

1. 报错信息

   ```
   java.lang.AssertionError: PackageManager#hasSystemFeature(android.hardware.sensor.compass) returns true but SensorManager#getSensorList(2) shows sensors [] expected:&lt;true&gt; but was:&lt;false&gt;
   ```

2. 错误分析

   通过 `PackageManager#hasSystemFeature(android.hardware.sensor.compass)` 方法返回系统支持指南针传感器，但是 `SensorManager#getSensorList(2)` 返回传感器列表没有指南针。

3. 解决办法

   **3.1 MTK8766、Android O**

   设备不支持指南针传感器，去掉指南针传感器即可。如果是 GO 版本，修改 `frameworks/native/data/etc/go_handheld_core_hardware.xml` 文件，否则修改 `frameworks/native/data/etc/handheld_core_hardware.xml` 文件。去掉文件中如下内容：

   ```xml
   <feature name="android.hardware.sensor.compass" />
   ```

   